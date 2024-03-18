from arneso_pypitemplate_instance2.functions import append_to_list
from arneso_pypitemplate_instance2.functions import example_function


def test_example_function() -> None:
    assert example_function(1, 2) == "1 is less than 2"
    assert example_function(1, 0) == "1 is greater than or equal to 0"


def test_append_to_list() -> None:
    result1 = append_to_list(12)
    result2 = append_to_list(101, [1, 2, 3])
    result3 = append_to_list(102)
    # The result3 is [12, 102], because of mutable default value
