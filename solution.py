import pandas as pd
# import locale


def valid_df(df: pd.DataFrame):
    if df is None:
        raise ValueError("df is None")
    if df.empty:
        raise ValueError("df is empty")
    non_numeric = df.select_dtypes(exclude="number").columns
    if len(non_numeric) > 0:
        raise ValueError("")


def valid_eqt(df: pd.DataFrame,
              eqt_col: str):
    calc = eqt_col.count("+") + eqt_col.count("-") + eqt_col.count("*")
    if calc != 1:
        print("0")
    if eqt_col.find("+") > 0:
        cols = eqt_col.split("+")
        str1 = cols[0].strip()
        str2 = cols[1].strip()
        if df.columns[0] == str1:
            return "+", str1, str2
    elif eqt_col.find("*") > 0:
        cols = eqt_col.split("*")
        str1 = cols[0].strip()
        str2 = cols[1].strip()
        if df.columns[0] == str1 and df.columns[1] == str2:
            return "*", str1, str2
    elif eqt_col.find("-") > 0:
        cols = eqt_col.split("-")
        str1 = cols[0].strip()
        str2 = cols[1].strip()
        if df.columns[0] == str1 and df.columns[1] == str2:
            return "-", str1, str2
    else:
            return False


def add_virtual_column(df: pd.DataFrame,
                       eqt_col: str,
                       sum_col: str
                       ) -> pd.DataFrame:
    valid_df(df)
    if valid_eqt(df, eqt_col) == False:
        return pd.DataFrame()
    result = valid_eqt(df, eqt_col)
    eqt = result[0]
    col_1 = result[1]
    col_2 = result[2]
    if eqt[0] == "+":
        df[sum_col] = df[col_1] + df[col_2]
    elif eqt[0] == "*":
        df[sum_col] = df[col_1] * df[col_2]
    elif eqt[0] == "-":
        df[sum_col] = df[col_1] - df[col_2]
    return (df)
