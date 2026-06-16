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

    data = data.dropna(subset=volatility_cols).copy()

    low_threshold = data["cc_volatility"].quantile(0.25)
    high_threshold = data["cc_volatility"].quantile(0.75)

    data["regime"] = "normal"
    data.loc[data["cc_volatility"] <= low_threshold, "regime"] = "low_volatility"
    data.loc[data["cc_volatility"] >= high_threshold, "regime"] = "high_volatility"

    regime_summary = data.groupby("regime")[volatility_cols].mean()

    regime_summary = regime_summary.rename(
        columns={
            "cc_volatility": "Close-to-close",
            "parkinson_volatility": "Parkinson",
            "garman_klass_volatility": "Garman-Klass",
            "rogers_satchell_volatility": "Rogers-Satchell",
        }
    )

    high_vol_days = data.sort_values("cc_volatility", ascending=False).head(20)

    high_vol_days = high_vol_days[
        [
            "Date",
            "Open",
            "High",
            "Low",
            "Close",
            "cc_volatility",
            "parkinson_volatility",
            "garman_klass_volatility",
            "rogers_satchell_volatility",
        ]
    ]

    regime_output = output_dir / "regime_summary.csv"
    high_vol_output = output_dir / "top_high_volatility_days.csv"

    regime_summary.to_csv(regime_output)
    high_vol_days.to_csv(high_vol_output, index=False)

    print("Regime summary")
    print(regime_summary)
    print()
    print("Top high volatility days")
    print(high_vol_days.head(10))
    print()
    print(f"Regime summary saved to: {regime_output}")
    print(f"Top high volatility days saved to: {high_vol_output}")


if __name__ == "__main__":
    main()