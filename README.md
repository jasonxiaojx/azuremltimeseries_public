# Stock Price Forecasting via AlphaVantage and AzureML

## Objective: 
* Compare AzureML forecasting models with other forecasting models for prediction accuracy of stock prices under both high and low volatility time segments. Also assess the two model’s capability in making profitable trading decisions. (MAYBE)

## Success Metrics:
* Extract real market data and locate high and low volatility segments for a selective amount of stocks from different sectors (tech, pharmaceuticals, consumer goods, etc)
* Generate stock price predictions/forecasts using AzureML forecasting tools and other forecasting models on historical stock prices in both high and low volatility time segments.
* Generate stock price predictions/forecasts using AzureML forecasting tools and other forecasting models on live-intraday market data.
* Compare accuracy metrics of part 2 and part 3, analyze pros and cons of AzureML forecasting vs other models, and implicit human workload associated with each model.
* Compare profitability of decisions based on the forecasts of the two models. (MAYBE)

## Data Access and Description:
This project will utilize the AlphaVantage API which is capable of extracting live-intraday market data as well as historical market data. 


## Modeling Technique and Architecture:
* AlphaVantage -> VM -> Azure Blob -> AzureML -> Visualization 

![](https://github.com/jasonxiaojx/azuremltimeseries/blob/master/arch_ts.jpeg)
 
## Description:
* Will pull data daily from AlphaVantage using a constantly running script on VM with sleep function.
* Load data into csv and upload to blob.
* Load data out of blob to analyze using AzureML or other frameworks on VM.
* Visualize forecast and classification of “winner/loser” stock.
## Execution Stages:
* Provision resources required, Azure VM, Azure Blob, Azure ML.
* Setup data access on VM, connect to alpha vantage and check upstream to azure blob, historical and live.
* Load data into blob and split into tables of different stocks and different volatility ranges.
* Conduct time series analysis on data pulled from Azure Blob storage using Azure ML and other frameworks.
* Classify stocks as winners or losers and check for accuracy. Define winner as an overall growing stock.

## Software Frameworks:
* Sklearn
* Python Prophet
* Azure AutoML
* Personal Algorithms (MAYBE)

