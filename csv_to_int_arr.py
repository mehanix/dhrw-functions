import json
from enum import Enum
from typing import Annotated, List

from pydantic import BaseModel, Field, StrictInt
from pydantic.config import ConfigDict


class Input(BaseModel):
    array: str

class Output(BaseModel):
    ans: List[int]

def csv_to_int_arr(input: Input) -> Output:
    print(input.array)
    line = input.array.split('\\n')[1]
    tokens = [int(x.strip()) for x in lines.split(',')]
    return Output(ans=tokens)
