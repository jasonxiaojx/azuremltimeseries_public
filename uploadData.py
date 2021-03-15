# Data Pipeline
import os
import uuid
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import pandas as pd


load_dotenv()
BLOB_CONN_STR = "USE OWN CONNECTION STRING"

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONN_STR)
print("AUTHENTICATION SUCCESS")
# Create a unique name for the container
container_name = "stockpricetest"

# Create the container
# container_client = blob_service_client.create_container(container_name)


# Call AlphaVantage API and then funnel data into CSV.
# ticker = "NIO"
print("Please enter a stock ticker: ")
ticker = input()
API_KEY = os.getenv("API_KEY")

ts = TimeSeries(key = API_KEY, output_format = "pandas")
# data, meta_data = ts.get_intraday(symbol='MSFT',interval='60min', outputsize='full')
data, meta_data = ts.get_daily(symbol = ticker, outputsize = 'full')
print(type(data))


# Rename columns and lag data here.
data = data.rename({"date": "date", "4. close": "close", "3. low": "low", "2. high": "high", "1. open": "open", "5. volume": "volume"}, axis = 1)

# Create a file in local data directory to upload and download
local_path = "./"
local_file_name = ticker + ".csv"
upload_file_path = os.path.join(local_path, local_file_name)

# Write stockprice to the TICKER.csv
data.to_csv(local_file_name, sep= ",")

# Keep track of lagged data here.
forecast_data = pd.DataFrame(data.iloc[:30])
test_data = data.iloc[30:60]
# Write stockprice forecast and test to TICKER_forecast.csv, TICKER_test.csv, TICKER_train.csv
local_file_name_forecast = ticker + "_forecast.csv"
local_file_name_test = ticker + "_test.csv"
local_file_name_train = ticker + "_train.csv"
upload_file_path_forecast = os.path.join(local_path, local_file_name_forecast)
upload_file_path_train = os.path.join(local_path, local_file_name_train)
upload_file_path_test = os.path.join(local_path, local_file_name_test)

# Write forecast shell
forecast_data.to_csv(local_file_name_forecast, sep = ",")
test_data.to_csv(local_file_name_test, sep = ",")

# Shift
data["close"] = data['close'].shift(30)
data = data.dropna()
train_data = data.iloc[30:]
train_data.to_csv(local_file_name_train, sep = ",")



# Create a blob client using the local file name as the name for the blob
# blob_client = blob_service_client.get_blob_client(c=container_name, blob=local_file_name)
blob_client_train = BlobClient(account_url = "REPLACE" , container_name = container_name, blob_name = local_file_name_train, credential= "REPLACE")
blob_client_forecast = BlobClient(account_url = "REPLACE" , container_name = container_name, blob_name = local_file_name_forecast, credential= "REPLACE")
blob_client_test = BlobClient(account_url = "REPLACE" , container_name = container_name, blob_name = local_file_name_test, credential= "REPLACE")

# Upload the created file
with open(upload_file_path_train, "rb") as data:
    blob_client_train.upload_blob(data, overwrite = True)
    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name_train)
    # blob_client_meta.upload_blob(meta_data, overwrite = True)
    # print("\nUploading to Azure Storage as blob:\n\t" + local_file_name_meta)

with open(upload_file_path_forecast, "rb") as data:
    blob_client_forecast.upload_blob(data, overwrite = True)
    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name_forecast)


with open(upload_file_path_test, "rb") as data:
    blob_client_test.upload_blob(data, overwrite = True)
    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name_test)



# Add section for deletion here.
