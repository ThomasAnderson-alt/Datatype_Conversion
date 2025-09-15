# Datatype Conversion 🛠️

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white&style=flat-square)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?logo=javascript&logoColor=white&style=flat-square)
![JSON](https://img.shields.io/badge/JSON-Supported-brightgreen?logo=json&logoColor=white&style=flat-square)

---

## 🚀 Project Overview

**Datatype Conversion** is a Python-based utility for converting deeply nested, hierarchical JavaScript data structures into a clean, grouped CSV format. This is especially useful for flattening medical or survey data for analysis, reporting, or further processing.

---

## 📁 Project Structure

| File                 | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| `Data_Conversion.py` | Python script for converting JS data to grouped CSV.                         |
| `data.js`            | Example input: hierarchical data in JavaScript object notation.              |
| `Data_Conversion.md` | Step-by-step, detailed explanation of the conversion logic and script usage. |
| `README.md`          | Project documentation and usage guide (this file).                           |

---

## ⚙️ How to Use

1. **Prepare Data**: Place your hierarchical data in `data.js` as an array of objects with `name` and (optionally) `childrenList` properties.
2. **Run Conversion**:

   ```bash
   python Data_Conversion.py
   ```

3. **Get Results**: The output CSV (`medical_data.csv`) will be generated in the same directory, with grouped formatting for easy reading.

---

## 📝 Documentation

- For a **detailed explanation** of the conversion logic, see [`Data_Conversion.md`](./Data_Conversion.md).
- Example input data is provided in [`data.js`](./data.js).

---

## 💡 Features

- Converts deeply nested JS data to flat, grouped CSV
- Handles arbitrary hierarchy depth
- No external dependencies required
- Output is ready for Excel, data analysis, or reporting

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/ThomasAnderson-alt/Datatype_Conversion/issues).

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
