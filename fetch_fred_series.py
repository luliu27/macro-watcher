import os
import pandas as pd
from dotenv import load_dotenv
from fredapi import Fred
from typing import Optional

class FredClient:
    def __init__(self, api_key=None):
        # Load environment variables if api_key is not provided
        if api_key is None:
            load_dotenv()
            api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            raise ValueError("FRED_API_KEY is not set in the environment.")
        self.api_key = api_key
        self.fred = Fred(api_key=self.api_key)

    def get_series_data(self, series_id, start_date: Optional[str] = None, end_date: Optional[str] = None) -> pd.DataFrame:
        """
        Fetch the specified FRED series and return a pandas DataFrame.
        """
        try :
            series = self.fred.get_series(series_id, observation_start=start_date, observation_end=end_date)
            if series.empty:
                raise ValueError(f"No data found for series ID: {series_id}")
            return series
        except Exception as e:
            raise RuntimeError(f"Error fetching data for series ID {series_id}: {e}")

if __name__ == "__main__":
    # Example usage: Fetch and display the M2 money stock data (M2SL)
    client = FredClient()
    series_id = "M2REAL"
    start_date = "2018-01-01"
    data = client.get_series_data(series_id, start_date)
    print(data.head())
    print(data.tail())