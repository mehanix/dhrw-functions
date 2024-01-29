import json
from enum import Enum

from typing import Annotated, List

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class Input(BaseModel):
    array: List[str | int | None]

class Output(BaseModel):
    array: List[int]

def cleanup(arr:Input) -> Output:
    res = Output(array=[])

    for val in arr:
        if isinstance(val, int):
            res.array.append(val)
    
    return res

# main_model_schema = Input.model_json_schema()  # (1)!
# print(json.dumps(main_model_schema, indent=2))  # (2)!
