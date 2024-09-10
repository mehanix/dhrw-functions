from pydantic import BaseModel
import pandas as pd
import json

class Input(BaseModel):
    dataframe: dict

class Output(BaseModel):
    summary_statistics: str 

def get_summary_statistics(input: Input) -> Output:
    df = pd.DataFrame(input.dataframe)
    city = df['Address'][2]
    stats = "Mesaj schimbat:" + city + " " + df.describe().to_string()
    return Output(summary_statistics=stats)
