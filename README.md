# 📊 YouTube Trending Videos — India vs US

A complete Exploratory Data Analysis (EDA) comparing YouTube trending behaviour between **India (IN)** and the **United States (US)**, built entirely with Python using pandas, NumPy, and Matplotlib.

---

## 📌 Project Overview

YouTube's trending list reflects what millions of people are watching — but what trends in India is very different from what trends in the US. This project investigates those differences across engagement, content, language, timing, and platform dynamics.

The dataset contains daily snapshots of trending YouTube videos from 113 countries. This analysis filters to India and the US and asks:

- Do Indian audiences engage more actively than US audiences relative to views?
- How quickly do videos trend after being published — and does it differ by country?
- Which languages, channels, and content types dominate each market?
- How long do videos stay on the trending list — are they one-day spikes or sustained presences?
- How do these patterns change over time?

---

## 📁 Repository Structure

```
youtube-trending-analysis/
│
├── data/
│   ├── sample/
│   │   └── sample_youtube_data.csv     # small dataset for testing
│   └── README.md                      # explains data handling
│
├── notebook/
│   └── eda.ipynb                      # full EDA pipeline
│
├── src/
│   └── sample.py                      # script to generate sample dataset
│
├── .gitignore
├── LICENSE
├── README.md
```

---

## 📦 Dataset

**Source:** [Trending YouTube Videos — 113 Countries](https://www.kaggle.com/datasets/asaniczka/trending-youtube-videos-113-countries) (Kaggle)

The raw CSV is not included in this repository due to file size. Download it from Kaggle and place it at:
```
data/raw/trending_yt_videos_113_countries.csv
```

**Key columns in the raw data:**

| Column | Description |
|---|---|
| `title` | Video title |
| `channel_name` | Uploading channel |
| `daily_rank` | Position on trending list (1 = top) |
| `daily_movement` | Rank change since yesterday |
| `weekly_movement` | Rank change over 7 days |
| `snapshot_date` | Date the trending data was captured |
| `country` | Country code (e.g. IN, US) |
| `view_count` | Total views on snapshot date |
| `like_count` | Total likes on snapshot date |
| `comment_count` | Total comments on snapshot date |
| `publish_date` | Date the video was originally uploaded |
| `language` | Detected video language |

---

## 🛠️ Technical Implementation

### Libraries
| Library | Use |
|---|---|
| `pandas` | Data loading, filtering, grouping, feature engineering |
| `numpy` | Log transforms, matrix operations |
| `matplotlib.pyplot` | All visualisations — no seaborn |
| `os` | Cross-platform file path handling |

### Pipeline

**1. Memory-Safe Data Loading**
The full dataset is too large to load into RAM at once. Solved using chunked reading — processing 50,000 rows at a time and concatenating only India and US rows:
```python
chunks = []
for chunk in pd.read_csv(FILE_PATH, chunksize=50_000, low_memory=True):
    filtered = chunk[chunk['country'].isin(['IN', 'US'])]
    if not filtered.empty:
        chunks.append(filtered)
df = pd.concat(chunks, ignore_index=True)
```

**2. Feature Engineering**
9 derived columns created from raw data:

| Feature | Formula |
|---|---|
| `days_to_trend` | `(snapshot_date - publish_date).days` |
| `engagement_rate` | `(likes + comments) / views` |
| `likes_ratio` | `likes / views` |
| `momentum_score` | `daily_movement + weekly_movement` |
| `engagement_per_rank` | `engagement_rate / daily_rank` |
| `video_age` | `(snapshot_date - publish_date).days + 1` |
| `views_per_day` | `view_count / video_age` |
| `publish_day` | Day of week from `publish_date` |
| `publish_month` | Month number from `publish_date` |

**3. Outlier Treatment — Winsorisation**
- Rows with `engagement_rate > 1` or `likes_ratio > 1` dropped as physically impossible
- IQR-based capping at 1st–99th percentile applied to all skewed numerical columns
- Viral videos preserved but capped — they don't distort charts or correlations

**4. Analysis Layers**

| Layer | What was done |
|---|---|
| Univariate | 18 columns — histograms, boxplots, log transforms, value counts |
| Bivariate | IN vs US — engagement, trending speed, rank, timing, language, channels, scatter plots |
| Multivariate | Engagement × country × language, trending speed × country × publish day, heatmaps |
| Time Series | View count, engagement rate, days to trend tracked over snapshot dates |
| Repeat Analysis | Video stickiness — classified as one-day, 2–5 days, or sustained (6+ days) |

**5. Correlation Heatmap — Pure Matplotlib**
Built without seaborn using `ax.imshow()` with manual cell annotation across 13 numerical features.

---

## 📈 Key Findings

> These are observations built into the notebook as templated placeholders. Fill them in after running the notebook with your actual output values.

### Engagement
- US videos have higher absolute view and like counts due to a larger English-speaking base
- India shows higher engagement rates relative to views — suggesting more active, community-driven viewership
- `views_per_day` (age-normalised) is the fairest popularity comparison between the two markets

### Trending Speed
- Most videos in both countries trend within a few days of publishing
- Videos published on certain days trend faster — day-of-week patterns differ between India and the US

### Content Patterns
- India's trending list is more linguistically diverse — Hindi and regional languages appear alongside English
- Top channels in India skew toward music, cricket, and devotional content; US toward news, late-night TV, and major music labels
- Seasonal spikes differ by market — India aligns with cricket seasons and Diwali; the US with NFL and the holiday season

### Stickiness
- A large proportion of trending videos in both countries appear for only one day — trending lists refresh quickly
- The US trending list tends to be slightly stickier — videos linger longer on average

---

## 🚀 How to Run

1. Clone the repository
```bash
git clone https://github.com/your-username/youtube-global-vs-india.git
cd youtube-global-vs-india
```

2. Install dependencies
```bash
pip install pandas numpy matplotlib
```

3. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/asaniczka/trending-youtube-videos-113-countries) and place it at `data/raw/trending_yt_videos_113_countries.csv`

4. Open and run the notebook
```bash
jupyter notebook eda_final.ipynb
```

Run all cells from top to bottom. The cleaned dataset will be saved automatically to `data/cleaned/youtube_cleaned.csv`.

---

## 🔮 Next Steps

- **NLP on titles and tags** — topic modelling to identify content categories driving trending in each market
- **Predictive modelling** — classify whether a video will trend in India or the US based on EDA features
- **Dashboard** — interactive visualisation of IN vs US comparisons using Plotly or Streamlit

---

## 👤 Author

**Vishesh**
Feel free to connect or raise an issue if you have questions about the analysis.
