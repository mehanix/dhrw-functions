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

def get_summary_statistics(input: Input) -> Output:
    df = pd.DataFrame(input.dataframe)
    city = df['Address'][2]
    stats = "Summary statistics for:" + city + " " + df.describe().to_string()
    return Output(summary_statistics=stats)
