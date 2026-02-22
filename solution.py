import operator
import pandas as pd

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}

def valid_df(df: pd.DataFrame):
    if df is None:
        raise ValueError("df is None")
    if df.empty:
        raise ValueError("df is empty")
    non_numeric = df.select_dtypes(exclude="number").columns
    if len(non_numeric) > 0:
        raise ValueError(f"Non-numeric columns found: {list(non_numeric)}")


def valid_label(lable: str) -> bool:
    return lable.replace("_", "").isalpha()


def valid_table(df: pd.DataFrame, eqt_col: str, sum_col: str):
    operators = ["+", "-", "*"]
    found_ops = [op for op in operators if op in eqt_col]

    if len(found_ops) != 1:
        return False

    if not valid_label(sum_col):
        return False

    op = found_ops[0]
    str1, str2 = map(str.strip, eqt_col.split(op))

    if not (valid_label(str1) and valid_label(str2)):
        return False

    if list(df.columns[:2]) != [str1, str2]:
        return False

    return op, str1, str2


def add_virtual_column(df: pd.DataFrame,
                       eqt_col: str,
                       sum_col: str
                       ) -> pd.DataFrame:
    valid_df(df)
    result = valid_table(df, eqt_col, sum_col)
    if not result:
        return pd.DataFrame()
    else:
        op, col_1, col_2 = result

    df = df.copy()
    df[sum_col] = OPS[op](df[col_1], df[col_2])
    return df
