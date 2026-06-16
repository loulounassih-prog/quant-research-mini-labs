# Quant Research Mini Labs

Collection of small quantitative research studies in Python.

The goal of this repository is to group short, focused projects on quantitative finance topics such as volatility estimation, risk analysis, event studies, factor analysis, and portfolio construction.

Each mini-lab is designed to answer a specific research question with a clean and reproducible workflow.

## Mini-Labs

### 1. Volatility Estimators

Folder:

```text
volatility-estimators/
```

This mini-lab compares several volatility estimators on daily SPY OHLCV data:

* close-to-close volatility
* Parkinson volatility
* Garman-Klass volatility
* Rogers-Satchell volatility

The objective is to study how different estimators behave across low-volatility, normal, and high-volatility regimes.

Main conclusion: range-based estimators capture similar volatility regimes as close-to-close volatility, but produce smoother and lower volatility estimates on SPY daily data from 2020 to 2024.

## Repository Structure

```text
quant-research-mini-labs/
│
├── README.md
├── requirements.txt
├── .gitignore
│
└── volatility-estimators/
    ├── README.md
    ├── data/
    ├── reports/
    └── scripts/
```

## Current Outputs

The `volatility-estimators` mini-lab generates:

```text
volatility-estimators/reports/
├── volatility_estimators.csv
├── volatility_comparison.png
├── summary_metrics.csv
├── correlation_matrix.csv
├── regime_summary.csv
└── top_high_volatility_days.csv
```

CSV files are ignored by Git because they are reproducible from the scripts.

The main plot is kept in the repository for quick visual inspection.

## Usage

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the volatility estimators mini-lab:

```powershell
python volatility-estimators/scripts/download_data.py
python volatility-estimators/scripts/compute_estimators.py
python volatility-estimators/scripts/plot_estimators.py
python volatility-estimators/scripts/summarize_estimators.py
python volatility-estimators/scripts/analyze_regimes.py
```

## Planned Mini-Labs

Possible future mini-labs include:

* event study analysis
* factor return analysis
* portfolio risk decomposition
* volatility regime detection
* drawdown and tail-risk analysis
* simple portfolio construction methods

## Purpose

This repository is not meant to present trading strategies.

It is meant to demonstrate clean quantitative research workflows on small, well-scoped finance problems.
