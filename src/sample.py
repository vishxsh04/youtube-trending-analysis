import os
import pandas as pd

def generate_sample(input_path, output_path, n=50):
    """
    Generate a sample dataset from a large CSV file.
    """
    df = pd.read_csv(input_path)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    sample_df = df.sample(n=n, random_state=42)
    sample_df.to_csv(output_path, index=False)
    
    print(f"Sample dataset saved to: {output_path}")


if __name__ == "__main__":
    generate_sample(
        input_path=r"C:\Users\vishe\youtube-global-vs-india\data\raw\trending_yt_videos_113_countries.csv",  
        output_path=r"C:\Users\vishe\youtube-global-vs-india\data\sample\sample_trending_yt_videos_113_countries.csv",
        n=50
    )