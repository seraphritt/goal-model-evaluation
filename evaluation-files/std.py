import csv
import re
from pathlib import Path

import numpy as np
import pandas as pd

# std formula: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html
# normalized with N-1 by default.

INPUT_FILE = Path("files/first-and-second-it-results.csv")
OUTPUT_CSV = Path("summary_by_condition.csv")
OUTPUT_LATEX = Path("summary_by_condition.tex")

METRIC_ORDER = [
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

ITERATION_ORDER = [
    "1st iteration",
    "2nd iteration",
]

MISSION_ORDER = [
    "Deliver Goods / Equipment",
    "Food Logistics",
]

TECHNIQUE_ORDER = [
    "ZS",
    "FS",
]


def parse_results(path: Path) -> pd.DataFrame:
    """Parse the two-block CSV structure into tidy, long-form data."""

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        rows = list(csv.reader(file))

    records = []
    current_iteration = None
    current_blocks = []

    for row in rows:
        # Guarantee enough columns for the two groups of five runs.
        row = row + [""] * max(0, 11 - len(row))
        first_cell = row[0].strip()

        # Detect a new experimental condition.
        if first_cell in ITERATION_ORDER:
            current_iteration = first_cell
            current_blocks = []

            # Find mission/technique headers dynamically.
            for start_column, cell in enumerate(row[1:], start=1):
                header = cell.strip()

                if not header:
                    continue

                match = re.fullmatch(
                    r"(.+?)\s+(ZS|FS)-Persona-cot",
                    header,
                    flags=re.IGNORECASE,
                )

                if match:
                    mission = match.group(1).strip()
                    technique = match.group(2).upper()

                    current_blocks.append(
                        {
                            "start_column": start_column,
                            "mission": mission,
                            "technique": technique,
                        }
                    )

            continue

        # Ignore blank rows, run-header rows, and unrelated rows.
        if first_cell not in METRIC_ORDER or current_iteration is None:
            continue

        metric = first_cell

        # Read the five runs for each mission block.
        for block in current_blocks:
            start_column = block["start_column"]

            for offset in range(5):
                column = start_column + offset
                raw_value = row[column].strip() if column < len(row) else ""

                # "-" represents a missing observation, not zero.
                if raw_value in {"", "-"}:
                    value = np.nan
                else:
                    value = float(raw_value)

                records.append(
                    {
                        "Iteration": current_iteration,
                        "Mission": block["mission"],
                        "Technique": block["technique"],
                        "Run": f"r{offset + 1}",
                        "Metric": metric,
                        "Value": value,
                    }
                )

    data = pd.DataFrame(records)

    if data.empty:
        raise ValueError(
            "No observations were found. Check the input CSV structure."
        )

    return data


def calculate_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """Calculate statistics without pooling missions or techniques."""

    summary = (
        data.groupby(
            ["Iteration", "Mission", "Technique", "Metric"],
            observed=True,
            sort=False,
        )["Value"]
        .agg(
            Mean="mean",
            Standard_deviation="std",
            N="count",
        )
        .reset_index()
    )

    # Apply the desired ordering.
    summary["Iteration"] = pd.Categorical(
        summary["Iteration"],
        categories=ITERATION_ORDER,
        ordered=True,
    )

    summary["Mission"] = pd.Categorical(
        summary["Mission"],
        categories=MISSION_ORDER,
        ordered=True,
    )

    summary["Technique"] = pd.Categorical(
        summary["Technique"],
        categories=TECHNIQUE_ORDER,
        ordered=True,
    )

    summary["Metric"] = pd.Categorical(
        summary["Metric"],
        categories=METRIC_ORDER,
        ordered=True,
    )

    summary = summary.sort_values(
        ["Iteration", "Mission", "Technique", "Metric"]
    ).reset_index(drop=True)

    summary["Mean"] = summary["Mean"].round(2)
    summary["Standard_deviation"] = (
        summary["Standard_deviation"].round(2)
    )

    # Combine the mean and standard deviation using the requested notation.
    summary["Estimate"] = summary.apply(
        lambda row: (
            rf"${row['Mean']:.2f} \pm "
            rf"{row['Standard_deviation']:.2f}$"
        ),
        axis=1,
    )

    return summary


def export_results(summary: pd.DataFrame) -> None:
    """Export the numerical results and a LaTeX longtable."""

    # Keep separate numerical columns in the CSV for later analysis.
    summary.to_csv(OUTPUT_CSV, index=False)

    latex_table = summary[
        [
            "Iteration",
            "Mission",
            "Technique",
            "Metric",
            "Estimate",
            "N",
        ]
    ].copy()

    latex_table.columns = [
        "Prompt iteration",
        "Mission",
        "Prompting technique",
        "Metric",
        r"$\hat{x} \pm s$",
        "N",
    ]

    latex_code = latex_table.to_latex(
        index=False,
        escape=False,
        longtable=True,
        column_format="llllcr",
        caption=(
            "Descriptive statistics separated by prompt iteration, "
            "robotic mission, and prompting technique."
        ),
        label="tab:descriptive-statistics-by-condition",
        na_rep="--",
    )

    OUTPUT_LATEX.write_text(latex_code, encoding="utf-8")


def main() -> None:
    data = parse_results(INPUT_FILE)
    summary = calculate_statistics(data)

    # There should be:
    # 2 iterations × 2 missions × 2 techniques × 9 metrics = 72 rows.
    expected_rows = 2 * 2 * 2 * len(METRIC_ORDER)

    if len(summary) != expected_rows:
        print(
            f"Warning: expected {expected_rows} summary rows, "
            f"but obtained {len(summary)}."
        )

    print(
        summary[
            [
                "Iteration",
                "Mission",
                "Technique",
                "Metric",
                "Estimate",
                "N",
            ]
        ].to_string(index=False)
    )

    export_results(summary)

    print(f"\nCSV saved to: {OUTPUT_CSV}")
    print(f"LaTeX table saved to: {OUTPUT_LATEX}")


if __name__ == "__main__":
    main()
