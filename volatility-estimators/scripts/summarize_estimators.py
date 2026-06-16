from pathlib import Path

import pandas as pd


def main() -> None:
    project_dir = Path(__file__).resolve().parents[1]

    input_file = project_dir / "reports" / "volatility_estimators.csv"
    output_dir = project_dir / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    data = pd.read_csv(input_file)
    data["Date"] = pd.to_datetime(data["Date"])

    volatility_cols = [
        "cc_volatility",
        "parkinson_volatility",
        "garman_klass_volatility",
        "rogers_satchell_volatility",
    ]

    summary = data[volatility_cols].describe().T

    summary = summary[
        [
            "mean",
            "std",
            "min",
            "25%",
            "50%",
            "75%",
            "max",
        ]
    ]

    summary = summary.rename(
        index={
            "cc_volatility": "Close-to-close",
            "parkinson_volatility": "Parkinson",
            "garman_klass_volatility": "Garman-Klass",
            "rogers_satchell_volatility": "Rogers-Satchell",
        }
    )

    correlation = data[volatility_cols].corr()

    output_summary = output_dir / "summary_metrics.csv"
    output_correlation = output_dir / "correlation_matrix.csv"

    summary.to_csv(output_summary)
    correlation.to_csv(output_correlation)

    print("Summary metrics")
    print(summary)
    print()
    print("Correlation matrix")
    print(correlation)
    print()
    print(f"Summary saved to: {output_summary}")
    print(f"Correlation matrix saved to: {output_correlation}")


if __name__ == "__main__":
    main()