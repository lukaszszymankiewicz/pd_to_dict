import pandas as pd


def _convert_pd_dict_orient(df: pd.DataFrame, col_label: str) -> dict:
    if type(df) == pd.Series:
        return {col_label: df.to_dict()}
    else:
        current_level = df.index.names[0]

        return {
            current_level: {
                str(value): _convert_pd_dict_orient(df.xs(value), col_label)
                for value in df.index.unique(current_level)
            }
        }


def _convert_pd_list_orient(df: pd.DataFrame, col_label: str) -> dict:
    if type(df) == pd.Series:
        return {col_label: df.to_dict()}
    else:
        current_level = df.index.names[0]

        return {
            current_level: [
                {"name": value, **_convert_pd_list_orient(df.xs(value), col_label)}
                for value in df.index.unique(current_level)
            ]
        }


def pd_to_dict(df: pd.DataFrame, orient: str = "dict", col_label: str = "values") -> dict:
    """
    Recursively converting DataFrame going down by its MultiIndex level. If function ends up on
    DataFrame with single-level index or Series, then its values is resulted as a dict.

    """
    if not isinstance(df, (pd.DataFrame, pd.Series)):
        raise AttributeError("Only DataFrame (or Series) instance can be converted!")

    if not col_label:
        raise AttributeError("col_label attribute can not be empty!")

    if None in df.index.names:
        raise ValueError("Only DataFrame with index names provided can be converted!")

    if orient == "dict":
        return _convert_pd_dict_orient(df, col_label)
    elif orient == "list":
        return _convert_pd_list_orient(df, col_label)
    else:
        raise AttributeError("Unknown orient attribute provided!")
