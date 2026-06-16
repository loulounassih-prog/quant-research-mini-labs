# Volatility Estimators

This mini-project compares several realized volatility estimators on daily SPY OHLCV data.

The goal is not to build a trading strategy. The goal is to study how different volatility estimators behave across market regimes, especially during periods of market stress.

## Research Question

How do close-to-close and range-based volatility estimators compare on SPY daily data?

In particular:

* Do the estimators move together?
* Do range-based estimators provide different information from close-to-close volatility?
* How do the estimators behave in low-volatility and high-volatility regimes?

## Dataset

The project uses daily SPY OHLCV data downloaded from Yahoo Finance.

Current experiment:

* Asset: SPY
* Frequency: daily
* Period: 2020-01-01 to 2024-01-01
* Prices: adjusted prices from Yahoo Finance

## Estimators

The project compares four volatility estimators.

### Close-to-close volatility

This estimator uses only consecutive closing prices.

```text
r_t = log(Close_t / Close_{t-1})
```

The daily variance estimate is:

```text
cc_variance = r_t^2
```

This is the simplest estimator, but it ignores intraday information contained in the daily high and low.

### Parkinson volatility

The Parkinson estimator uses the daily high-low range.

```text
parkinson_variance = (1 / (4 log(2))) * (log(High / Low))^2
```

It uses more information than close-to-close volatility because it captures the intraday trading range.

### Garman-Klass volatility

The Garman-Klass estimator uses open, high, low, and close prices.

```text
garman_klass_variance =
0.5 * (log(High / Low))^2
- (2 log(2) - 1) * (log(Close / Open))^2
```

It combines range information with the open-to-close move.

### Rogers-Satchell volatility

The Rogers-Satchell estimator also uses open, high, low, and close prices.

```text
rogers_satchell_variance =
log(High / Close) * log(High / Open)
+ log(Low / Close) * log(Low / Open)
```

It is designed to handle drift more robustly than some other range-based estimators.

## Methodology

The project computes daily variance estimates, then converts them into rolling annualized volatility estimates.

The rolling window is:

```text
20 trading days
```

The annualization factor is:

```text
252 trading days per year
```

The transformation is:

```text
annualized_volatility =
sqrt(rolling_mean(daily_variance, 20) * 252)
```

## Outputs

The scripts generate several files in the `reports/` directory.

```text
reports/
├── volatility_estimators.csv
├── volatility_comparison.png
├── summary_metrics.csv
├── correlation_matrix.csv
├── regime_summary.csv
└── top_high_volatility_days.csv
```

## Results

The volatility estimators are strongly related and move together across market regimes.

Average rolling annualized volatility by regime:

```text
Regime              Close-to-close   Parkinson   Garman-Klass   Rogers-Satchell
high_volatility     0.338            0.243       0.245          0.249
normal              0.163            0.135       0.135          0.136
low_volatility      0.098            0.086       0.087          0.088
```

All estimators increase substantially in high-volatility regimes.

However, on this SPY daily sample, the range-based estimators produce lower volatility levels than close-to-close volatility, especially during high-volatility periods.

## Interpretation

The results suggest that all four estimators capture similar volatility regimes.

The range-based estimators use more intraday information because they include the daily high-low range. However, in this experiment, they are less extreme than close-to-close volatility during stressed periods.

This does not mean that range-based estimators are useless. It means that, on this specific SPY daily sample, they provide a smoother view of realized volatility than close-to-close volatility.

## Conclusion

This mini-project shows that volatility estimation is sensitive to the choice of estimator.

The close-to-close estimator is simple and reactive, but it ignores intraday price ranges.

The Parkinson, Garman-Klass, and Rogers-Satchell estimators use more OHLC information and produce smoother volatility estimates on this dataset.

The main conclusion is that range-based volatility estimators capture the same broad volatility regimes as close-to-close volatility, but with lower and smoother estimated volatility levels on SPY daily data from 2020 to 2024.

## How to Run

From the root of the repository:

```powershell
python volatility-estimators/scripts/download_data.py
python volatility-estimators/scripts/compute_estimators.py
python volatility-estimators/scripts/plot_estimators.py
python volatility-estimators/scripts/summarize_estimators.py
python volatility-estimators/scripts/analyze_regimes.py
```

## Possible Extensions

Possible extensions include:

* testing more assets
* comparing equity indices, single stocks, bonds, commodities, and FX
* using intraday data
* comparing estimators during crisis periods
* adding realized volatility from high-frequency returns
* studying estimator bias under different simulated price processes
