
# Goal Model Evaluation

A research artifact for evaluating **LLM-generated goal models for multi-robot system missions**.

This repository compares zero-shot and few-shot persona-based prompting across two hospital logistics missions and two prompt iterations. It preserves repeated model outputs, evaluation scores, generated figures, and Python scripts for producing heatmaps and descriptive statistics.

## Experimental Design

The first evaluation cycle compares three dimensions:

| Dimension          | Conditions                                 |
| ------------------ | ------------------------------------------ |
| Prompt iteration   | First iteration, second/improved iteration |
| Prompting strategy | ZS-Persona-CoT, FS-Persona-CoT             |
| Mission            | Food Logistics, Deliver Goods / Equipment  |

Each mission and prompting condition contains five generated outputs:

```text
result-1.txt
result-2.txt
result-3.txt
result-4.txt
result-5.txt
```

### Prompting strategies

* **ZS-Persona-CoT**: zero-shot prompting with a multi-robot mission-designer persona and structured reasoning instructions.
* **FS-Persona-CoT**: few-shot prompting that adds examples and more explicit justification requirements.

### Mission scenarios

The complete mission descriptions are available in [`mission_descriptions.md`](mission_descriptions.md).

## Repository Structure

```text
goal-model-evaluation/
├── README.md
├── mission_descriptions.md
│
├── first-cycle/
│   ├── first-iteration/
│   │   ├── fs-persona-cot.txt
│   │   ├── zs-persona-cot.txt
│   │   ├── fs-persona-cot/
│   │   │   ├── Deliver_Goods_Equipment/
│   │   │   └── Food_Logistics/
│   │   └── zs-persona-cot/
│   │       ├── Deliver_Goods_Equipment/
│   │       └── Food_Logistics/
│   │
│   └── second-iteration/
│       ├── fs-persona-cot-improved.txt
│       ├── zs-persona-cot-improved.txt
│       ├── fs-persona-cot/
│       │   ├── Deliver_Goods_Equipment/
│       │   └── Food_Logistics/
│       └── zs-persona-cot/
│           ├── Deliver_Goods_Equipment/
│           └── Food_Logistics/
│
├── second-cycle/
│   └── inital-prompt-exp1.txt
│
└── evaluation-files/
    ├── metric_plots/
    │   ├── *.png
    │   ├── metric_means_by_iteration_scenario.csv
    │   └── parsed_long_format.csv
    ├── first-and-second-it-results.csv
    ├── metrics.py
    ├── std.py
    └── summary_by_condition.csv
```

## Evaluation Data

The main evaluation dataset is:

```text
evaluation-files/files/first-and-second-it-results.csv
```

It contains five runs for every combination of:

* Two prompt iterations
* Two robotic missions
* Two prompting strategies
* Nine evaluation metrics

The metric labels preserved by the dataset are:

```text
T - Traceability
MAI - Mission Aspects Identification
GTC_A - Goal Type Correctness  - Achieve
GTC_Q - Goal Type Correctness - Query
GTC_P - Goal Type Correctness - Perform
IC - Intention Coverage
NR - Non-redundancy
DLC - Decomposition Link Correctness
RAC - Runtime Annotation Correctness
```

Scores are represented on a 0–100 scale. A hyphen (`-`) represents a missing observation rather than a score of zero.

## Quickstart

### Prerequisites

* Git
* A recent Python 3 installation
* `pip`

### 1. Clone the repository

```bash
git clone https://github.com/seraphritt/goal-model-evaluation.git
cd goal-model-evaluation
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install the analysis dependencies

The repository does not currently include a dependency file. Install the packages used by the scripts directly:

```bash
python -m pip install numpy pandas matplotlib jinja2
```

### 4. Run the analysis from the correct directory

The scripts use paths relative to `evaluation-files`, so change into that directory first:

```bash
cd evaluation-files
```

Generate parsed datasets, means, and heatmaps:

```bash
python metrics.py
```

Generate standard deviation + mean results:

```bash
python std.py
```
