
import pandas as pd
import pytest

from src.main import analyze_sales


def test_sales_summary():
    data = pd.DataFrame({
        "product": ["Laptop", "Mobile", "Tablet"],
        "sales": [50000, 20000, 10000]
    })

    result = analyze_sales(data)

    assert result["total_sales"] == 80000
    assert result["average_sales"] == pytest.approx(26666.67, rel=1e-4)
    assert result["highest_sales"] == 50000
    assert result["lowest_sales"] == 10000
    assert result["total_records"] == 3


def test_missing_column():
    data = pd.DataFrame({
        "product": ["Laptop"]
    })

    with pytest.raises(ValueError):
        analyze_sales(data)


def test_empty_dataset():
    data = pd.DataFrame(columns=["product", "sales"])

    with pytest.raises(ValueError):
        analyze_sales(data)


def test_missing_sales():
    data = pd.DataFrame({
        "product": ["Laptop", "Mobile"],
        "sales": [50000, None]
    })

    with pytest.raises(ValueError):
        analyze_sales(data)


def test_non_numeric_sales():
    data = pd.DataFrame({
        "product": ["Laptop", "Mobile"],
        "sales": ["high", "low"]
    })

    with pytest.raises(ValueError):
        analyze_sales(data)
