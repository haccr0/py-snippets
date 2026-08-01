import os
import json

current_dir = os.getcwd()
print(current_dir)

data = { "name": "John",
          "age": 30,
         "city": "New York"
        }

json_string = json.dumps(data)
print(json_string)