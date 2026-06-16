from pathlib import Path

import pandas as pd
import yfinance as yf


def main() -> None:
    project_dir = Path(__file__).resolve().parents[1]
    data_dir = project_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    ticker = "SPY"
    start = "2020-01-01"
    end = "2024-01-01"

    data = yf.download(
        tickers=ticker,
        start=start,
        end=end,
        interval="1d",
        auto_adjust=True,
        progress=False,
    )

    if data.empty:
        raise ValueError("No data downloaded.")

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()
    data = data[["Date", "Open", "High", "Low", "Close", "Volume"]]

    output_file = data_dir / f"{ticker}_daily_{start}_{end}.csv"
    data.to_csv(output_file, index=False)

    print(f"Data saved to: {output_file}")


if __name__ == "__main__":
    main()