# PySpark Learning Journey

A comprehensive guide to learning PySpark for Data Engineering, Data Analysis, and Machine Learning.

## Overview

This repository contains practical examples and projects covering:
- **DE (Data Engineering)**: ETL pipelines, data transformations, structured streaming
- **DA (Data Analysis)**: Data exploration, aggregations, analytics
- **ML (Machine Learning)**: Spark MLlib, supervised/unsupervised learning

## Prerequisites

- Java 8+ (OpenJDK 11 recommended)
- Python 3.8+
- Ubuntu/Linux or macOS

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/pyspark-learning.git
cd pyspark-learning
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
python3 test_setup.py
```

## Project Structure
```
pyspark-learning/
├── de/                    # Data Engineering examples
│   ├── 01_basic_etl.py
│   ├── 02_transformations.py
│   └── 03_streaming.py
├── da/                    # Data Analysis examples
│   ├── 01_exploratory_analysis.py
│   └── 02_aggregations.py
├── ml/                    # Machine Learning examples
│   ├── 01_classification.py
│   ├── 02_regression.py
│   └── 03_clustering.py
├── notebooks/             # Jupyter notebooks
│   └── 01_getting_started.ipynb
├── data/                  # Sample datasets
├── test_setup.py          # Setup verification script
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

## Getting Started

### Run Test Script
```bash
source venv/bin/activate
python3 test_setup.py
```

### Start Jupyter Notebook
```bash
source venv/bin/activate
jupyter notebook
```

### Run Individual Examples
```bash
source venv/bin/activate
python3 de/01_basic_etl.py
```

## Quick Tips

- Always activate venv before running scripts: `source venv/bin/activate`
- Use Jupyter for interactive learning
- Create sample datasets in the `data/` folder
- Check Spark logs in logs/ directory if issues occur

## Learning Resources

- [Apache Spark Documentation](https://spark.apache.org/docs/)
- [PySpark API Docs](https://spark.apache.org/docs/latest/api/python/)
- [Spark by Examples](https://sparkbyexamples.com/)

## License

This project is for educational purposes.
