# Chatbot for Stock Information Queries
In this project, a basic chatbot for stock information queries was built by using the AI (Artificial Intelligence), NLP (Natural Language Processing) knowledge. The program were firstly constructed and run using python on JupyterLab during to its aesthetic and interactivity, then it was completed, perfected on Spyder and the final step was to test its performance on Wechat. Several methods and algorithms including those obtained from extension python modules were used to build the main framework.
## Packages Installation
### Rasa NLU
Rasa is an open source machine learning framework to automate text-and voice-based conversations. With Rasa, you can build chatbots on:
- Facebook Messenger
- Slack
- Microsoft Bot Framework
- Rocket.Chat
- Mattermost
- Telegram
- Twilio
- Your own custom conversational channels  

And Rasa NLU (Natural Language Understanding) is a tool for understanding what is being said in short pieces of text.  
For example, taking a short message like:  
```
"I'm looking for a Mexican restaurant in the center of town"   
```
And returning structured data like:  
```
intent: search_restaurant  
entities:  
  - cuisine : Mexican  
  - location : center  
```

Using pip to install Rasa NLU via Python Library From pypi:  
```
pip install rasa_nlu
```
**For more installation information of Rasa NLU** 
Please click on https://rasa.com/docs/nlu/installation/  

### iexfinance
The iexfinance is a Python module help you get data for Stocks, ETFs, Mutual Funds, Forex/Currencies, Options, Commodities, Bonds, and Cryptocurrencies from IEX Cloud and IEX API:
Real-time and delayed quotes
Historical data (daily and minutely)
Financial statements (Balance Sheet, Income Statement, Cash Flow)
End of Day Options Prices
Institutional and Fund ownership
Analyst estimates, Price targets
Corporate actions (Dividends, Splits)
Sector performance
Market analysis (gainers, losers, volume, etc.)
IEX market data & statistics (IEX supported/listed symbols, volume, etc)
Social Sentiment and CEO Compensation
