# AlgoBot 

AlgoBot is an algorithmic trading robot written in Python. It currently analyzes patterns in the stock market to automate or suggest trades, using strategies such as mean reversion or trend following. 

**Disclaimer:** This program is not a platform for guaranteed success. AlgoBot is not responsible for any financial losses that may occur.



## Installation and Usage

**Requirements:**

 - Python 3.5+
 - Numpy 
 - Pandas
 - Matplotlib
 - Flask (API only)
 - Sqlalchemy (API only)
 
In addition to the dependencies listed above, you will need an internet connection to receive data from Google Finance, unless the most recent data is already cached offline in your computer.
 
**Usage:**

Both the backtest.py in the strategies mean reversion and trend following test the algorithm on historical data. The user can specify the amount of historical days used by modifying the constant **time_span** found in the source code. In mean reversion, the user can also specify the Bollinger band constant, which is represented by the constant **k**. However, the default Bollinger band constant of 1.20 is recommended. Modifying this constant in the trend following algorithm will have no effect.

