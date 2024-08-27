# Stock-market-Efficiency-Streamlining-MicroServered-Pipeline-with-SQS-Powered-Data-Flow
The project centers around developing a REST API that fetches stock data from the "Rapid API" website 
After we hit the api link every 1 min with the Python script and send the data to AWS SQS
Once 10 records accumulate in the SQS queue, a separate AWS Lambda function named "Processor" is triggered to process this data. 
The processed data, containing information about stock price, then inserted into a dynamo db database.
