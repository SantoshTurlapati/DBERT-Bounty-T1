
import pandas as pd


def analyze_sales(data: pd.DataFrame) -> dict:
    required_columns = {"product", "sales"}

    if not required_columns.issubset(data.columns):
        raise ValueError("Missing required columns")

    if data.empty:
        raise ValueError("Dataset cannot be empty")

    if data["sales"].isna().any():
        raise ValueError("Sales column contains missing values")

    if not pd.api.types.is_numeric_dtype(data["sales"]):
        raise ValueError("Sales must contain numeric values")

    return {
        "total_sales": float(data["sales"].sum()),
        "average_sales": float(data["sales"].mean()),
        "highest_sales": float(data["sales"].max()),
        "lowest_sales": float(data["sales"].min()),
        "total_records": int(len(data))
    }


if __name__ == "__main__":
    sample_data = pd.DataFrame({
        "product": ["Laptop", "Mobile", "Tablet", "Keyboard"],
        "sales": [50000, 20000, 15000, 3000]
    })

    result = analyze_sales(sample_data)

    print("\nSales Analysis Report")
    print("---------------------")

    for key, value in result.items():
        print(f"{key}: {value}")
