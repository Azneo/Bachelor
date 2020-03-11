from pandas import (
    read_csv,
    to_datetime,
    date_range,
    DatetimeIndex,
    )

class PreparePriceData:
    def __init__(self, data):
        self.data = data

    def rebuild_time_series(self, column):
        idx = date_range(self.data[column].min(), self.data[column].max(), name=column)
        self.data[column] = DatetimeIndex(self.data[column])
        self.data = self.data.set_index(column).reindex(idx).reset_index()
        return self

    def get_full_data(self):
        return self.data
    
    def get_columns(self, *args):
        self.data = self.data.filter(list(args))
        return self
    
    def interpolate(self):
        self.data = self.data.interpolate(method='linear', limit_direction='forward', axis=0)
        return self
    
    def group_by_time(self, column='date', freq='D'):
        self.data[column] = to_datetime(self.data[column])
        result=self.data.resample(freq, on=column).mean().reset_index()
        return result