import pandas as pd
import numpy as np

csv_path = "heatmap_new(1).csv"

def clean_text(value):
    return (
        str(value)
        .strip()
        .replace("+AC0-", "-")
        .replace("+AF8-", "_")
    )

def compute_metric_averages(csv_path):
    raw = pd.read_csv(csv_path, header=None, dtype=str, keep_default_na=False)

    results = []
    current_iteration = None

    i = 0
    while i < len(raw):
        row = [clean_text(x) for x in raw.iloc[i].tolist()]

        non_empty = [x for x in row if x]

        # Detect iteration title
        if non_empty and any("iteration" in x.lower() for x in non_empty):
            current_iteration = next(x for x in non_empty if "iteration" in x.lower())

        # Detect row with r1, r2, r3, r4, r5 headers
        if i + 1 < len(raw):
            next_row = [clean_text(x) for x in raw.iloc[i + 1].tolist()]
            r1_cols = [
                col for col, value in enumerate(next_row)
                if value.lower().endswith("r1")
            ]

            if r1_cols:
                for start_col in r1_cols:
                    cols = list(range(start_col, start_col + 5))

                    # Scenario name, for example:
                    # Deliver Goods / Equipment ZS-Persona-cot
                    scenario_candidates = [
                        row[c] for c in cols
                        if c < len(row) and row[c]
                    ]

                    scenario = (
                        scenario_candidates[0]
                        if scenario_candidates
                        else f"scenario_cols_{start_col}_{start_col + 4}"
                    )

                    # Data rows start two rows after scenario row
                    j = i + 2

                    while j < len(raw):
                        metric = clean_text(raw.iat[j, 0])

                        # Stop when block ends
                        if not metric:
                            break

                        values = []

                        for c in cols:
                            value = clean_text(raw.iat[j, c])

                            if value == "-":
                                value = 0

                            values.append(pd.to_numeric(value, errors="coerce"))

                        average = np.nansum(values) / 5

                        results.append({
                            "iteration": current_iteration,
                            "scenario": scenario,
                            "metric": metric,
                            "average": average
                        })

                        j += 1

                i = j
                continue

        i += 1

    return pd.DataFrame(results)


averages = compute_metric_averages(csv_path)

print(averages)

# Optional: save result to CSV
averages.to_csv("metric_averages.csv", index=False)