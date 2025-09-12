# Datatype Conversion

This project provides a script to convert hierarchical JavaScript data into a grouped CSV format. It is useful for transforming nested data structures into flat, readable tables for analysis or reporting.

## Files

- `Data_Conversion.py`: Python script that performs the conversion from JS to CSV.
- `data.js`: Example input file containing hierarchical data in JavaScript object notation.
- `Data_Conversion.md`: Detailed step-by-step explanation of the Python script and its logic.

## Usage

1. Place your hierarchical data in `data.js` (as an array of objects with `name` and optional `childrenList` properties).
2. Run the Python script:

   ```bash
   python Data_Conversion.py
   ```

3. The output will be saved as `medical_data.csv` in the same directory.

## Requirements

- Python 3.x
- No external dependencies (uses only standard library modules: `json`, `re`, `csv`)

## Repository

[GitHub Repository](https://github.com/ThomasAnderson-alt/Datatype_Conversion.git)

---

For a detailed explanation of the code and its logic, see `Data_Conversion.md`.
