import pytest

from src import pd_to_dict


def test_pd_to_dict_function_raises_error_if_not_dataframe_or_series_is_provided():
    # GIVEN
    wrong_parameter = list()

    # WHEN & THEN
    with pytest.raises(AttributeError):
        pd_to_dict(df=wrong_parameter)


def test_pd_to_dict_function_raises_error_if_empty_col_string_is_provided(
    sample_singleindexed_dataframe,
):
    # GIVEN
    wrong_col_label = ""

    # WHEN & THEN
    with pytest.raises(AttributeError):
        pd_to_dict(
            df=sample_singleindexed_dataframe,
            col_label=wrong_col_label,
        )


def test_pd_to_dict_function_raises_error_if_dataframe_without_index_names_is_provided(
    sample_singleindexed_dataframe,
):
    # GIVEN
    sample_singleindexed_dataframe.index.name = None

    # WHEN & THEN
    with pytest.raises(ValueError):
        pd_to_dict(df=sample_singleindexed_dataframe)


def test_pd_to_dict_function_raises_error_if_nonexisting_orient_paramter_is_provided(
    sample_singleindexed_dataframe,
):
    # GIVEN
    wrong_orient = "tuple"

    # WHEN & THEN
    with pytest.raises(AttributeError):
        pd_to_dict(df=sample_singleindexed_dataframe, orient=wrong_orient)


def test_pd_to_dict_function_works_properly_for_single_indexed_dataframe_dict_orient(
    sample_singleindexed_dataframe,
):
    # GIVEN
    expected_result = {
        "classification": {
            "first": {"values": {"a": 1, "b": 2}},
            "second": {"values": {"a": 3, "b": 4}},
        }
    }

    # WHEN
    result = pd_to_dict(df=sample_singleindexed_dataframe, orient="dict")

    # WHEN & THEN
    assert result == expected_result


def test_pd_to_dict_function_works_properly_for_single_indexed_dataframe_list_orient(
    sample_singleindexed_dataframe,
):
    # GIVEN
    expected_result = {
        "classification": [
            {"name": "first", "values": {"a": 1, "b": 2}},
            {"name": "second", "values": {"a": 3, "b": 4}},
        ]
    }

    # WHEN
    result = pd_to_dict(df=sample_singleindexed_dataframe, orient="list")

    # THEN
    assert result == expected_result


def test_pd_to_dict_function_works_properly_for_multi_indexed_dataframe_dict_orient(
    sample_mulitindexed_dataframe,
):
    # GIVEN
    expected_result = {
        "race": {
            "0": {
                "lap": {
                    "0": {"values": {"James": 1, "John": 2, "Albert": 4, "Michael": 3}},
                    "1": {"values": {"James": 2, "John": 3, "Albert": 1, "Michael": 4}},
                }
            },
            "1": {
                "lap": {
                    "0": {"values": {"James": 4, "John": 3, "Albert": 1, "Michael": 2}},
                    "1": {"values": {"James": 2, "John": 3, "Albert": 1, "Michael": 4}},
                }
            },
        }
    }
    # WHEN
    result = pd_to_dict(df=sample_mulitindexed_dataframe, orient="dict")

    # THEN
    assert result == expected_result


def test_pd_to_dict_function_works_properly_for_multi_indexed_dataframe_list_orient(
    sample_mulitindexed_dataframe,
):
    # GIVEN
    expected_result = {
        "race": [
            {
                "name": 0,
                "lap": [
                    {"name": 0, "values": {"James": 1, "John": 2, "Albert": 4, "Michael": 3}},
                    {"name": 1, "values": {"James": 2, "John": 3, "Albert": 1, "Michael": 4}},
                ],
            },
            {
                "name": 1,
                "lap": [
                    {"name": 0, "values": {"James": 4, "John": 3, "Albert": 1, "Michael": 2}},
                    {"name": 1, "values": {"James": 2, "John": 3, "Albert": 1, "Michael": 4}},
                ],
            },
        ]
    }
    result = pd_to_dict(df=sample_mulitindexed_dataframe, orient="list")

    # THEN
    assert result == expected_result
