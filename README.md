# 📊 Datatype Conversion Project

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=for-the-badge&logo=javascript)
![JSON](https://img.shields.io/badge/JSON-Supported-brightgreen?style=for-the-badge&logo=json)

## 📖 About The Project

The **Datatype Conversion Project** is a Python-based utility designed to convert deeply nested, hierarchical JavaScript data structures into a clean, grouped CSV format. This tool is particularly useful for flattening medical or survey data for analysis, reporting, or further processing.

## 🚀 Getting Started

Follow these steps to set up and run the project.

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/ThomasAnderson-alt/Datatype_Conversion.git
   ```

2. **Navigate to the project directory**

   ```sh
   cd Data_Export_Project
   ```

3. **Run the script**

   ```sh
   python Data_Conversion.py
   ```

## ⚙️ Usage

1. **Prepare Data**: Place your hierarchical data in `data.js` as an array of objects with `name` and (optionally) `childrenList` properties.
2. **Run Conversion**:

   ```sh
   python Data_Conversion.py
   ```

3. **Get Results**: The output CSV (`medical_data.csv`) will be generated in the same directory, with grouped formatting for easy reading.

## 📂 Project Structure

```plaintext
Data_Export_Project/
├── Data_Conversion.md       # Detailed explanation of the conversion logic
├── Data_Conversion.py       # Python script for converting JS data to grouped CSV
├── data.js                  # Example input: hierarchical data in JavaScript object notation
├── README.md                # Project documentation
```

## 🏗️ System Structure

The **Datatype Conversion Project** follows a modular structure to ensure clarity and maintainability. Below is an overview of the system structure:

1. **Input Module**: Handles the ingestion of hierarchical JavaScript data from `data.js`.
2. **Processing Module**: Implements the logic to traverse and flatten the hierarchical data structure.
3. **Output Module**: Formats the processed data into a grouped CSV file and saves it as `medical_data.csv`.

This modular design allows for easy debugging, testing, and future enhancements.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

Project Link: [https://github.com/ThomasAnderson-alt/Datatype_Conversion](https://github.com/ThomasAnderson-alt/Datatype_Conversion)
