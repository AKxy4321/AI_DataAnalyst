import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def report(analysis_results: dict, original_data):
    labels = np.array(analysis_results["Clustering Labels"])
    centers = np.array(analysis_results["Cluster Centers"])
    correlation_matrix = pd.DataFrame(analysis_results["Correlation Matrix"])
    descriptive_stats = pd.DataFrame(analysis_results["Descriptive Statistics"])

    # Select the numeric columns for visualization (assuming 2D or 2 principal components)
    numeric_df = original_data.select_dtypes(include=['float64', 'int64'])

    if numeric_df.shape[1] > 2:
        # If more than 2 features, reduce dimensions using PCA for visualization
        from sklearn.decomposition import PCA
        pca = PCA(n_components=2)
        reduced_data = pca.fit_transform(numeric_df)
        reduced_centers = pca.transform(centers)
    else:
        reduced_data = numeric_df.values
        reduced_centers = centers

    # 1. Scatter plot of clustering labels with PCA-reduced data
    plt.figure(figsize=(8, 6))
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap='viridis', label='Data Points')
    plt.scatter(reduced_centers[:, 0], reduced_centers[:, 1], c='red', marker='x', s=200, label='Cluster Centers')
    plt.title("Clustering Labels and Centers (PCA-reduced)")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend()
    plt.show()

    # 2. Heatmap of the Correlation Matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.title("Correlation Matrix Heatmap")
    plt.show()

    # 3. Descriptive Statistics Visualization
    descriptive_stats.T.plot(kind='bar', figsize=(12, 8))
    plt.title("Descriptive Statistics")
    plt.xlabel("Metrics")
    plt.ylabel("Values")
    plt.xticks(rotation=45)
    plt.show()
