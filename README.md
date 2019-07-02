# Chatbot for Stock Information Queries
In this project, a basic chatbot for stock information queries was built by using the AI (Artificial Intelligence), NLP (Natural Language Processing) knowledge. The program were firstly constructed and run using python on JupyterLab during to its aesthetic and interactivity, then it was completed, perfected on Spyder and the final step was to test its performance on Wechat. Several methods and algorithms including those obtained from extension python modules were used to build the main framework.

## Demonstration GIF
![image](https://github.com/FredZCY/MIT-NLP-Chatbot-for-Stock-Information-Queries/blob/master/Final_Project/Wechat%20Demo%20GIF.gif)
## Packages Installation
### [Rasa NLU]
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
Please click on https://rasa.com/docs/rasa/user-guide/installation/ 



### [iexfinance]
The iexfinance is a Python module help you get data for Stocks, ETFs, Mutual Funds, Forex/Currencies, Options, Commodities, Bonds, and Cryptocurrencies from IEX Cloud and IEX API:
- Real-time and delayed quotes
- Historical data (daily and minutely)
- Financial statements (Balance Sheet, Income Statement, Cash Flow)
- End of Day Options Prices
- Institutional and Fund ownership
- Analyst estimates, Price targets
- Corporate actions (Dividends, Splits)
- Sector performance
- Market analysis (gainers, losers, volume, etc.)
- IEX market data & statistics (IEX supported/listed symbols, volume, etc)
- Social Sentiment and CEO Compensation

Using pip to install iexfinance via Python Library From pypi (latest stable release): 
```
pip3 install iexfinance
```

An IEX Cloud account is required to acecss the IEX Cloud API. Various plans are availalbe, free, paid, and pay-as-you-go.  
Your IEX Cloud (secret) authentication token can be passed to any function or at the instantiation of a `Stock` object. The easiest way to store a token is in the `IEX_TOKEN` environment variable.  

***Real-time Quotes***  
To obtain real-time quotes for one or more symbols, use the `get_price` method of the `Stock` object:  
```
from iexfinance.stocks import Stock  
tsla = Stock('TSLA')  
tsla.get_price()  
```
***Historical Data***  
It’s possible to obtain historical data using `get_historical_data` and `get_historical_intraday`.

**For more installation information of iexfinance**  
Please click on https://github.com/addisonlynch/iexfinance  

**For more information about iexfinance**  
Please click on https://pypi.org/project/iexfinance/  



### [wxpy]  
The wxpy is a python module and it was a updated version of itchat. By installing it, many functions related to Wechat APP such as sending messages or pictures, automatically replying messages of various types can be achieved.  

Using pip to install wxpy via Python Library From pypi (latest stable release): 
```
pip install -U wxpy
```
**For more information about wxpy**  
Please click on https://github.com/youfou/wxpy to visit its official Github webpage

## Instruction  
To run the program on wechat, please follow the following instructions:
1. Downdoal all the files in the `Final_Project`
2. Run the `Chatbot_for_stockmarket (Final).py` on any python IDE  

*`Spyder` is recommended, or you can use `Jupyter` to test the program in seperate blocks*  

3. Part of codes about `wechat friend searching` may need to be specified by yourself  
```python
# Search the specified Wechat account
my_friend = bot.friends().search('Stockbot Coco')[0]
```
4. Scan the generated QR code and start to chat with the Chatbot:relaxed:  

## Contact the Author  

***Special thanks*** :pray: to the instruction and advice from  

*[Dr. Fan Zhang (张帆)](http://www.mit.edu/~f_zhang/) (Watson Core Platform Service IBM Massachusetts Labratory)*  


If you got any enquiries or suggestions, I'm all ears :sunglasses:  

- **Institution:**  Xiamen University Malaysia  :mortar_board: Sophomore  
- **Personal E-mail:** zhangchenyu555@gmail.com   
- **Academic E-mail:** CST1709482@xmu.edu.my  
- **Insterested Area:**

  - [ ] Artificial Intelligence  
  - [ ] Machine Learning  
  - [ ] Computer Vision  
  - [ ] Natural Language Processing  
  - [ ] Data Analysis
