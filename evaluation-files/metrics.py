import re
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


CSV_PATH = Path("files/first-and-second-it-results.csv")
OUTPUT_DIR = Path("metric_plots")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

metric_order = [
    "T",
    "MAI",
    "GTC_A",
    "GTC_Q",
    "GTC_P",
    "IC",
    "NR",
    "DLC",
    "RAC",
]


red_green_cmap = LinearSegmentedColormap.from_list(
    "red_green_score",
    [
        (0.0, "red"),       # 0
        (0.5, "yellow"),    # 50
        (1.0, "green"),     # 100
    ],
)

# NaN / missing values will appear as light gray
red_green_cmap.set_bad(color="lightgray")


def clean_text(value):
    if pd.isna(value):
        return None

    value = str(value).strip()

    # Fix possible CSV encoding artifacts
    value = value.replace("+AC0-", "-")
    value = value.replace("+AF8-", "_")

    return value or None


def safe_filename(text):
    text = clean_text(text) or "unnamed"
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", text)
    return text.strip("_")


def parse_embedded_iteration_csv(csv_path):
    raw = pd.read_csv(csv_path, header=None, dtype=str)

    records = []

    i = 0
    while i < len(raw):
        row = raw.iloc[i]

        iteration = clean_text(row.iloc[0])

        # A valid block starts with 1st iteration or 2nd iteration
        if iteration not in {"1st iteration", "2nd iteration"}:
            i += 1
            continue

        # Detect scenario columns dynamically
        scenario_cols = []
        for col in range(raw.shape[1]):
            value = clean_text(row.iloc[col])

            if value is not None and "Persona-cot" in value:
                scenario_cols.append((col, value))

        if len(scenario_cols) < 2:
            i += 1
            continue

        runs_row_idx = i + 1
        metric_start_idx = i + 2

        j = metric_start_idx

        # Read metrics until the next empty row or next iteration block
        while j < len(raw):
            metric = clean_text(raw.iat[j, 0])

            if metric is None:
                break

            if metric in {"1st iteration", "2nd iteration"}:
                break

            for scenario_idx, start_info in enumerate(scenario_cols):
                start_col, scenario = start_info

                if scenario_idx + 1 < len(scenario_cols):
                    end_col = scenario_cols[scenario_idx + 1][0]
                else:
                    end_col = raw.shape[1]

                run_cols = list(range(start_col, end_col))

                for col in run_cols:
                    run = clean_text(raw.iat[runs_row_idx, col])
                    value = clean_text(raw.iat[j, col])

                    if run is None:
                        continue

                    records.append(
                        {
                            "iteration": iteration,
                            "scenario": scenario,
                            "metric": metric,
                            "run": run,
                            "score": pd.to_numeric(value, errors="coerce"),
                        }
                    )

            j += 1

        i = j + 1

    data = pd.DataFrame(records)

    if data.empty:
        raise ValueError(
            "No data was parsed. Check if the CSV has rows starting with "
            "'1st iteration' or '2nd iteration' and scenario names containing 'Persona-cot'."
        )

    data["metric"] = pd.Categorical(
        data["metric"],
        categories=metric_order,
        ordered=True,
    )

    data = data.sort_values(
        ["iteration", "scenario", "metric", "run"]
    )

    return data


long_df = parse_embedded_iteration_csv(CSV_PATH)

long_df.to_csv(
    OUTPUT_DIR / "parsed_long_format.csv",
    index=False,
)

metric_means = (
    long_df
    .groupby(
        ["iteration", "scenario", "metric"],
        observed=True,
        as_index=False,
    )["score"]
    .mean()
)

metric_means.to_csv(
    OUTPUT_DIR / "metric_means_by_iteration_scenario.csv",
    index=False,
)


plot_count = 0

for (iteration, scenario), block in long_df.groupby(
    ["iteration", "scenario"],
    sort=False,
):
    matrix = block.pivot_table(
        index="metric",
        columns="run",
        values="score",
        aggfunc="mean",
        observed=True,
    ).reindex(metric_order)

    matrix["Mean"] = matrix.mean(axis=1, skipna=True)

    fig, ax = plt.subplots(figsize=(8.5, 5.2))

    values = matrix.to_numpy(dtype=float)
    masked_values = np.ma.masked_invalid(values)

    image = ax.imshow(
        masked_values,
        cmap=red_green_cmap,
        vmin=0,
        vmax=100,
        aspect="auto",
    )

    cbar = fig.colorbar(image, ax=ax)
    cbar.set_label("Score")

    # ax.set_title(f"{iteration} - {scenario}")
    ax.set_xlabel("Runs + Mean")
    ax.set_ylabel("Metrics")

    ax.set_xticks(range(len(matrix.columns)))
    ax.set_xticklabels(matrix.columns, rotation=45, ha="right")

    ax.set_yticks(range(len(matrix.index)))
    ax.set_yticklabels(matrix.index)

    for y in range(values.shape[0]):
        for x in range(values.shape[1]):
            val = values[y, x]
            label = "-" if np.isnan(val) else f"{val:.1f}"

            ax.text(
                x,
                y,
                label,
                ha="center",
                va="center",
                fontsize=8,
                color="black",
            )

    fig.tight_layout()

    output_file = OUTPUT_DIR / (
        f"{safe_filename(iteration)}__{safe_filename(scenario)}.png"
    )

    fig.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close(fig)

    plot_count += 1


print(f"Created {plot_count} plots.")
print(f"Files saved in: {OUTPUT_DIR}")
print(f"Long-format CSV saved in: {OUTPUT_DIR / 'parsed_long_format.csv'}")
print(f"Means CSV saved in: {OUTPUT_DIR / 'metric_means_by_iteration_scenario.csv'}")
