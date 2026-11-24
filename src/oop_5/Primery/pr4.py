from typing import Union

def normalize(value: Union[int, float, str])->float:
    if isinstance(value, str):
        value = value.replace(',', '.')
        return float(value)
    return float(value)

def normalize_(value: int | float | str)->float:
    if isinstance(value, str):
        value = value.replace(',', '.')
        return float(value)
    return float(value)
