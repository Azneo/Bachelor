import re
from textblob import TextBlob
from pandas import (
    read_csv,
    to_datetime,
    date_range,
    DatetimeIndex,
    )

class SentimentAnalysis:
    def __init__(self, data):
        self.data = data
    """
    method ochistki teksta ot musora
    """
    def _clean_text(self, text):
        PATTERNS = [
            '@[A-Za-z0–9]+',
            '#',
            'RT[\s]+',
            'https?:\/\/\S+'
        ]
        for pattern in PATTERNS:
            text = re.sub(pattern, '', text)
        return text
        
    def _get_subjectivity(self, text):
        return TextBlob(text).sentiment.subjectivity
    
    def _get_polarity(self, text):
        return TextBlob(text).sentiment.polarity

    def set_time_format(self, column='date', format='%Y-%m-%d'):
        """
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
        """
        self.data[column] = to_datetime(self.data[column]).dt.strftime(format)
        return self

    def count_subjectivity(self, column):
        """
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
        ko vsem zapisjam v kolonke primenjaem funkciju rascheta "subjectivity" resultaty sohranajem v novoj kolonke "subjectivity"
        """
        self.data['subjectivity'] = self.data[column].apply(self._get_subjectivity)
        return self
    
    def count_polarity(self, column):
        self.data['polarity'] = self.data[column].apply(self._get_polarity)
        return self
    
    def clean_text(self, column):
        self.data[column] = self.data[column].apply(self._clean_text)
        return self
    
    def get_full_data(self):
        return self.data

    def rebuild_time_series(self, column='date'):
        """
        1. grupperuem po date v dannom sluchae
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
        2. raschitivaem granizi vremynogo ryada
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html
        3. pereindeksiruem
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reindex.html
        """
        self.data = self.data.groupby([column], as_index=False).mean()
        idx = date_range(self.data[column].min(), self.data[column].max(), name=column)
        self.data[column] = DatetimeIndex(self.data[column])
        self.data = self.data.set_index(column).reindex(idx).reset_index()
        return self

    def interpolate(self, method='linear'):
        """
        zapolnjaem propuski vo vremznom rjadu
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.interpolate.html
        """
        self.data = self.data.interpolate(method)
        return self

    def group_by_time(self, column='date', freq='D'):
        """
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html
        """
        self.data[column] = to_datetime(self.data[column])
        return self.data.resample(freq, on=column).mean().reset_index()