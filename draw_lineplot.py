import json
from enum import Enum
from typing import Annotated, List

from pydantic import BaseModel, Field, StrictInt
from pydantic.config import ConfigDict
import pandas as pd

class Input(BaseModel):
    x_axis: List[str]
    y_axis: List[int]

class Output(BaseModel):
    image_bytes: str

def csv_to_int_arr(input: Input) -> Output:
   
    res = []
    df = pd.DataFrame({
        'x': input.x_axis,
        'y':input.y_axis
    })

    df.plot(x='x', y='y')
    return Output(data=res)
