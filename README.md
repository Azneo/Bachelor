# Sentiment Analysis and Stock Market Comparison

## Overview

This project performs sentiment analysis on tweets published by a company and compares the resulting sentiment trends with stock market data. The main objectives are to process multiple tweets per day, handle missing data for days without tweets, and visualize sentiment trends over time in comparison with stock market movements.

## Steps

### 1. **Daily Average Calculation**
- Often, a company posts multiple tweets throughout the day. To simplify the analysis, we calculate the **average polarity** and **subjectivity** for each day, ensuring that only a single sentiment value is recorded per day.

### 2. **Filling Missing Days**
- There are certain days without any tweets. For these days, we estimate sentiment values by calculating the difference in sentiment between the two nearest tweets (before and after the missing day). This difference is divided by the number of days between the two tweets, and the value is then distributed evenly across the missing days to create a continuous sentiment trend.

### 3. **Graph Construction**
- Once the daily average sentiment values are calculated and missing data is filled, we construct a **line graph** displaying the sentiment trends over time. Additionally, we overlay this sentiment graph with **stock market data**, allowing us to visually compare sentiment fluctuations with market movements.

## Usage

To get started with the project, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/Azneo/sentiment-analysis-stock-comparison.git
    ```

2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the sentiment analysis script:
    ```bash
    python sentiment_analysis.py
    ```

4. View the graph comparing sentiment trends with stock market data.

## Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `vaderSentiment` (for sentiment analysis)
  - `yfinance` (for stock data)

The list of required libraries can be found in the `requirements.txt` file.

## Author

- **Aziz Ishan-Khojaev** - [Your GitHub Profile](https://github.com/Azneo)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
