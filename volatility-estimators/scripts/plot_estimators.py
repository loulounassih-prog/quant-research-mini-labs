from pathlib import Path

import matplotlib.pyplot as plt
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

    labels = {
        "cc_volatility": "Close-to-close",
        "parkinson_volatility": "Parkinson",
        "garman_klass_volatility": "Garman-Klass",
        "rogers_satchell_volatility": "Rogers-Satchell",
    }

    plt.figure(figsize=(12, 6))

    for col in volatility_cols:
        plt.plot(data["Date"], data[col], label=labels[col])

    plt.title("Rolling Annualized Volatility Estimators")
    plt.xlabel("Date")
    plt.ylabel("Annualized volatility")
    plt.legend()
    plt.grid(True)

    output_file = output_dir / "volatility_comparison.png"
    plt.savefig(output_file, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"Figure saved to: {output_file}")


if __name__ == "__main__":
    main()