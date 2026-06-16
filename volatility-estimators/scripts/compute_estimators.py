from pathlib import Path

import numpy as np
import pandas as pd


def add_volatility_estimators(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()

    log_open = np.log(data["Open"])
    log_high = np.log(data["High"])
    log_low = np.log(data["Low"])
    log_close = np.log(data["Close"])
    log_close_prev = log_close.shift(1)

    data["cc_variance"] = (log_close - log_close_prev) ** 2

    data["parkinson_variance"] = (
        (1 / (4 * np.log(2))) * (log_high - log_low) ** 2
    )

    data["garman_klass_variance"] = (
        0.5 * (log_high - log_low) ** 2
        - (2 * np.log(2) - 1) * (log_close - log_open) ** 2
    )

    data["rogers_satchell_variance"] = (
        (log_high - log_close) * (log_high - log_open)
        + (log_low - log_close) * (log_low - log_open)
    )

    return data

def add_rolling_annualized_volatility(
    data: pd.DataFrame,
    window: int = 20,
    periods_per_year: int = 252,
) -> pd.DataFrame:
    data = data.copy()

    variance_cols = [
        "cc_variance",
        "parkinson_variance",
        "garman_klass_variance",
        "rogers_satchell_variance",
    ]

    for col in variance_cols:
        vol_col = col.replace("_variance", "_volatility")
        data[vol_col] = np.sqrt(
            data[col].rolling(window=window).mean() * periods_per_year
        )

    return data

def main() -> None:
    project_dir = Path(__file__).resolve().parents[1]
    input_file = project_dir / "data" / "SPY_daily_2020-01-01_2024-01-01.csv"
    output_dir = project_dir / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    data = pd.read_csv(input_file)
    data["Date"] = pd.to_datetime(data["Date"])

    data = add_volatility_estimators(data)
    data = add_rolling_annualized_volatility(data, window=20)

    output_file = output_dir / "volatility_estimators.csv"
    data.to_csv(output_file, index=False)

    print(data.head())
    print()
    print(data[
        [
            "cc_variance",
            "parkinson_variance",
            "garman_klass_variance",
            "rogers_satchell_variance",
        ]
    ].describe())

    print()
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()