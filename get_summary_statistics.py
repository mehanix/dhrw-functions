import json
from enum import Enum
from typing import Annotated, List

from pydantic import BaseModel, Field, StrictInt
from pydantic.config import ConfigDict

import random
import dill
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd


class Input(BaseModel):
    dataframe: dict

class Output(BaseModel):
    summary_statistics: str 

def gen_summary_statistics(input: Input) -> Output:
    # create dataframe and get year
    df = pd.DataFrame(input.dataframe)
    stats = df.describe().to_string()
    print("Stats ", stats)
    return Output(summary_statistics=stats)
