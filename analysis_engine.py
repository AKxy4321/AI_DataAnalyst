
#################################################################################
############## Analysis Engine Module ###########################################
#################################################################################

from sklearn.cluster import KMeans
import pandas as pd


def perform_clustering(df, n_clusters=3):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    if n_clusters < len(df.columns) // 2:
        n_clusters = len(df.columns) // 2
    if n_clusters % 2 == 0:
        n_clusters -= 1
    model = KMeans(n_clusters=n_clusters)
    model.fit(numeric_df)

    return model.labels_, model.cluster_centers_

def compute_correlation_matrix(df):
    # Ensure all columns are numeric for this analysis
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    # Compute correlation matrix
    correlation_matrix = numeric_df.corr()
    
    return correlation_matrix


def compute_descriptive_statistics(df):
    return df.describe()

def analyse(df) -> dict:
    # Perform clustering
    labels, centers = perform_clustering(df)
        
    # Compute correlation matrix
    correlation_matrix = compute_correlation_matrix(df)
    
    # Compute descriptive statistics
    descriptive_stats = compute_descriptive_statistics(df)
    if 'count' in descriptive_stats.index:
        descriptive_stats = descriptive_stats.drop('count')

    # Organize the results into a dictionary
    analysis_results = {
        "Clustering Labels": labels.tolist(), 
        "Cluster Centers": centers.tolist(),  
        "Correlation Matrix": correlation_matrix.to_dict(),  
        "Descriptive Statistics": descriptive_stats
    }
    
    return analysis_results
