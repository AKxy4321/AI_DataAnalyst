# Project Summary

## Overview

This project comprises several modules designed for data analysis, processing, and reporting. The modules integrate functionalities for clustering, computing correlation matrices, generating descriptive statistics, and visualizing data. Additionally, the project incorporates AI interaction for advanced insights and report generation.

## Modules

### 1. **Analysis Engine Module**

This module provides functionality for analyzing datasets through:
- **Clustering**: Performs KMeans clustering on numeric columns.
- **Correlation Matrix**: Computes relationships between variables.
- **Descriptive Statistics**: Generates key statistics for each column.

**Key Functions**:
- `perform_clustering(df: pd.DataFrame) -> tuple`
- `compute_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame`
- `compute_descriptive_statistics(df: pd.DataFrame) -> pd.DataFrame`
- `analyse(df: pd.DataFrame) -> dict`

### 2. **Data Processing Module**

This module handles data loading, cleaning, and normalization:
- **Loading Data**: Supports CSV, JSON, and Excel formats.
- **Cleaning Data**: Fills missing values, removes duplicates, and normalizes numeric columns if specified.

**Key Functions**:
- `load_data(file_path: str) -> pd.DataFrame`
- `clean_data(file_path: str, normalise: bool = False) -> pd.DataFrame`

### 3. **Main Application Module**

Integrates the data processing, analysis, and reporting functionalities, and interacts with a generative AI model:
- **Data Loading and Cleaning**: Uses user input to load and clean data.
- **Data Analysis**: Performs clustering, correlation, and descriptive statistics.
- **Report Generation**: Creates visualizations of the analysis results.
- **Generative AI Interaction**: Generates textual summaries and handles user prompts.

**Key Workflow**:
1. Load and clean data.
2. Analyze data.
3. Generate and visualize reports.
4. Interact with AI for additional insights.

### 4. **Report Generation Module**

Generates visual reports based on analysis results:
- **Scatter Plot**: Visualizes clustering results.
- **Heatmap**: Shows correlation matrix.
- **Bar Chart**: Displays descriptive statistics.

**Key Function**:
- `report(analysis_results: dict, original_data: pd.DataFrame)`

## Getting Started

1. **Installation**: Ensure you have the required libraries (`pandas`, `matplotlib`, `seaborn`, `sklearn`, `google-generativeai`, `dotenv`).
2. **Setup**: Configure environment variables for API keys and other settings.
3. **Usage**: Run the main script, provide data file paths, and follow prompts for data cleaning, analysis, and reporting.

## Notes

- Ensure data files are in supported formats (.csv, .json, .xlsx).
- For large datasets, consider performance optimizations.
- AI-generated summaries are based on analysis results and user prompts.


Feel free to adjust any sections according to your specific needs or project details!