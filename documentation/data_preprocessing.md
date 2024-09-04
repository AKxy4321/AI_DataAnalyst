### Data Processing Module Documentation

This module provides essential functions for loading, cleaning, and normalizing datasets. It supports multiple file formats and handles common data cleaning tasks like filling missing values, removing duplicates, and normalizing numeric columns.

---

#### Functions:

1. **`load_data(file_path: str) -> pd.DataFrame`**
   - **Description**: 
     This function loads data from a file into a pandas DataFrame. The function supports CSV, JSON, and Excel file formats.
   - **Parameters**:
     - `file_path (str)`: The path to the file to be loaded. The file extension must be `.csv`, `.json`, or `.xlsx`.
   - **Returns**:
     - `pd.DataFrame`: A DataFrame containing the loaded data.
   - **Raises**:
     - `ValueError`: If the file format is unsupported.

   - **Usage Example**:
     ```python
     df = load_data("data.csv")
     ```

2. **`clean_data(file_path: str, normalise: bool = False) -> pd.DataFrame`**
   - **Description**: 
     This function cleans the data by handling missing values, removing duplicates, and optionally normalizing numeric columns. It first loads the data using the `load_data` function.
   - **Parameters**:
     - `file_path (str)`: The path to the data file that needs to be cleaned.
     - `normalise (bool, optional)`: If `True`, numeric columns are normalized to a range between 0 and 1. Default is `False`.
   - **Returns**:
     - `pd.DataFrame`: A cleaned DataFrame with missing values handled, duplicates removed, and optionally normalized numeric columns.
     
   - **Data Cleaning Steps**:
     1. **Handle Missing Numeric Values**:
        - Numeric columns' missing values are filled with the mean of the respective column.
     2. **Remove Duplicates**:
        - Duplicate rows are identified and removed from the DataFrame.
     3. **Normalize Numeric Columns (Optional)**:
        - If `normalise=True`, numeric columns are scaled to a range of 0 to 1 using min-max normalization.
     4. **Handle Missing String Values**:
        - String columns' missing values are filled with the mode (most frequent value) of the respective column.
     
   - **Usage Example**:
     ```python
     # Clean data without normalization
     df = clean_data("data.csv")

     # Clean data with normalization
     df = clean_data("data.csv", normalise=True)
     ```

---

### Module Workflow:

1. **Loading Data**: The `load_data` function detects the file format from the file extension and loads the data into a pandas DataFrame.
   
2. **Cleaning Data**:
   - Numeric columns are cleaned by filling missing values with their respective means.
   - Duplicate rows are removed.
   - String columns are cleaned by filling missing values with the mode.
   - If normalization is enabled, numeric columns are scaled to a range of 0 to 1.

### Error Handling:

- The `load_data` function raises a `ValueError` if the file format is unsupported, ensuring that only `.csv`, `.json`, and `.xlsx` files are processed.

### Notes:

- **Normalization**: When normalizing, the min-max scaling technique is used, which scales the values to the range [0, 1].
- **Performance Considerations**: The module handles missing data efficiently but assumes the dataset can fit in memory. For larger datasets, consider chunking or using a data processing framework that supports out-of-core computation.

This documentation should help you understand and effectively use the data processing module in your projects.