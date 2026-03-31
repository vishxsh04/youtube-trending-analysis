## Data

This directory manages all dataset-related components for the YouTube Trending Analysis project.

### What’s included

* `sample/`
  A lightweight sample dataset (`sample_trending_yt_videos_113_countries.csv`) is provided to help quickly understand the schema and test the analysis without requiring the full dataset.

---

### What’s not included

The complete dataset is intentionally excluded due to size constraints and repository best practices.

You can download it from:

* `https://www.kaggle.com/datasets/asaniczka/trending-youtube-videos-113-countries`

---

### Why this approach?

In real-world data workflows, large datasets are not stored in version control systems like GitHub. Instead, repositories focus on:

* Reproducible code
* Clear data transformations
* Documented analysis

This project follows the same principle.

---

### Recreating the sample

If you have the full dataset locally, you can regenerate the sample using:

```bash
python src/sample.py
```

---

### Summary

* Full dataset → external
* Sample dataset → included
* Analysis → fully reproducible

---
