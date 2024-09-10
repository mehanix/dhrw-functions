# Function Repository

This is the repository used by the project for hosting the function collection.

To create a new function for your computation graph, create a new file using this template:

```
from pydantic import BaseModel

class Input(BaseModel):
    # add your input parameters here, with types

class Output(BaseModel):
    # add your output parameters here, with types

def function_name(input:Input) -> Output:
    # add your function logic here
```
And complete it with your own code. Use it by referencing `filename`, as well as `function_name` when adding the new function to the platform.
