# Data_Conversion.py Detailed Explanation

This document provides a step-by-step explanation of the `Data_Conversion.py` script, which converts a JavaScript data structure into a grouped CSV format.

## Overview

The script reads a JavaScript file (`data.js`), cleans and parses its content into JSON, flattens any hierarchical data, and writes the result to a CSV file (`medical_data.csv`).

---

## Step-by-Step Explanation

### 1. Importing Required Modules

```python
import json
import re
import csv
```

- **json**: For parsing JSON data.
- **re**: For regular expressions to clean/modify the JS file.
- **csv**: For writing the output in CSV format.

---

### 2. Defining the Conversion Function

```python
def js_to_csv():
    ...
```

All logic is encapsulated in the `js_to_csv` function for clarity and reusability.

---

### 3. Reading and Cleaning the JS File

```python
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.strip().rstrip(';')
content = re.sub(r'(\w+):', r'"\1":', content)
data = json.loads(content)
```

- Reads the contents of `data.js`.
- Removes any trailing semicolon (common in JS files).
- Uses regex to add quotes around property names (converts JS object notation to valid JSON).
- Parses the cleaned string into a Python object (`data`).

---

### 4. Flattening the Hierarchical Data

```python
rows = []
def flatten(item, path=[]):
    current = path + [item['name']]
    if not item.get('childrenList'):
        rows.append(current)
    else:
        for child in item['childrenList']:
            flatten(child, current)

for item in data:
    flatten(item)
```

- Defines a recursive `flatten` function to traverse the hierarchy.
- Builds a list (`rows`) where each entry is a path from the root to a leaf node.
- If an item has no `childrenList`, it is a leaf and its path is added to `rows`.
- Otherwise, recursively processes each child.

---

### 5. Writing the Grouped CSV Output

```python
with open('medical_data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    prev_row = []
    for row in rows:
        output_row = []
        for i, value in enumerate(row):
            if i < len(prev_row) and value == prev_row[i]:
                output_row.append('')
            else:
                output_row.append(value)
                prev_row = prev_row[:i+1]
        writer.writerow(output_row)
        prev_row = row.copy()
```

- Opens `medical_data.csv` for writing with UTF-8 BOM for compatibility.
- For each row, compares with the previous row:
  - If a value is repeated in the same column, writes an empty cell for grouping.
  - Otherwise, writes the value and resets subsequent previous values.
- This results in a grouped, easy-to-read CSV.

---

### 6. Running the Conversion

```python
js_to_csv()
```

- Calls the function to execute the conversion process.

---

## Summary

- **Goal**: Convert a hierarchical JS data structure to a grouped CSV.
- **Approach**: Clean JS, parse to JSON, flatten hierarchy, write grouped CSV.
- **Result**: `medical_data.csv` with grouped, non-redundant rows for each leaf node.

---

**Note:**

- The script assumes the JS file is an array of objects with `name` and optional `childrenList` properties.
- The output CSV will have as many columns as the maximum depth of the hierarchy.
