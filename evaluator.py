import pytest
import pandas as pd
import os



def compare_dataframes(df1, df2):
    """
    Compare two dataframes are exactly the same
    """
    df = pd.concat([df1, df2]).drop_duplicates(keep=False)
    assert df1.columns.tolist() == df2.columns.tolist()
    assert df1.shape == df2.shape
    assert df.empty


def evaluate_result(path_to_csv, path_to_expected_csv):
    """
    Compare the result of the query with the expected result
    """
    if not os.path.exists(path_to_csv):
        assert False
    df = pd.read_csv(path_to_csv)
    df_expected = pd.read_csv(path_to_expected_csv)
    compare_dataframes(df, df_expected)


def test_ex_2():
    evaluate_result("results/result_2.csv", "result/ex_2.csv")


def test_ex_3():
    evaluate_result("results/result_3.csv", "result/ex_3.csv")


def test_ex_4():
    evaluate_result("results/result_4.csv", "result/ex_4.csv")


def test_ex_5():
    evaluate_result("results/result_5.csv", "result/ex_5.csv")


def test_ex_6():
    evaluate_result("results/result_6.csv", "result/ex_6.csv")


def test_ex_7():
    evaluate_result("results/result_7.csv", "result/ex_7.csv")


def test_ex_8():
    evaluate_result("results/result_8.csv", "result/ex_8.csv")


def test_ex_9():
    evaluate_result("results/result_9.csv", "result/ex_9.csv")


def test_ex_10():
    evaluate_result("results/result_10.csv", "result/ex_10.csv")
