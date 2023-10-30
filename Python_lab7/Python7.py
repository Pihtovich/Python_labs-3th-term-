# Sample-JSON-file-with-multiple-records.json
import json

filename = input("Enter 'filename.json': ")
with open(filename, "r") as f:
    data = json.loads(f.read())

    new_data = dict()
    for key, value in data.items():
        if not isinstance(value, dict):
            new_data[key] = value
        else:
            for k, v in value.items():
                new_data[key + "_" + k] = v

    print("New dict:", new_data)

    csv_columns = new_data.keys()

    csv_data = ",".join(csv_columns) + "\n"
    new_row = list()
    for col in csv_columns:
        new_row.append(str(new_data[col]))
    csv_data += ",".join(new_row) + "\n"

    with open('output.scv', 'w') as j:
        j.write(csv_data)




