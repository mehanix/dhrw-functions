import json
from enum import Enum
from typing import Annotated, List

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class Input(BaseModel):
    arr: List[str | int | None]

class Output(BaseModel):
    res: int

def sum_array_int(input: Input) -> Output:
    return Output(res=sum(input.arr))
