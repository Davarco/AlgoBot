# AlgoBot 

AlgoBot is an algorithmic trading robot written in Python. It currently analyzes patterns in the stock market to automate or suggest trades, using strategies such as mean reversion or trend following. 

**Disclaimer:** This program is not a platform for guaranteed success. AlgoBot is not responsible for any financial losses that may occur.



## Installation and Usage

**Requirements:**

 - Python 3.5+
 - Numpy 
 - Pandas
 - Requests
 - Matplotlib (not required for API)
 - Flask (API only)
 - Flask-RESTful (API only)
 
In addition to the dependencies listed above, you will need an internet connection to receive data from Google Finance, unless the most recent data is already cached offline in your computer.
 
**Usage:**

The backtest.py executables in both the mean reversion and trend following strategies test the respective algorithm on historical data. The user can specify the amount of historical days used by modifying the constant **time_span** found in the source code. In mean reversion, the user can also specify the Bollinger band constant, which is represented by the constant **k**. However, the default Bollinger band constant of 1.20 is recommended. Modifying this constant in the trend following algorithm will have no effect.

Make sure to run all Python executables from the project's **root** directory!

**API:**

The API is designed for optimal use through PyCharm and under an NGROK port tunnel. You can also host it locally by running the api.py file **under mean_reversion** (again, from the **root** directory!).

The API is hosted at http://apcsalgobot.herokuapp.com/ and provides the following methods:

 - /stocks/get/**ticker** - replace ticker with the symbol for any NASDAQ 100 stock. EX /stocks/get/GOOG
 - /stocks/buy - returns a JSON list of all NASDAQ 100 stocks sorted in order of difference between today's price and the general lower band. The topmost is most favorable to purchase today.
 - /stocks/sell - returns a JSON list of all NASDAQ 100 stocks sorted in order of difference between today's price and the general upper band. The topmost is most favorable to sell today.
 
Do keep in mind that, while we try our best, our API server is set up to sleep after 30 minutes of inactivity. So if it's taking you longer than usual to load results, just know that nothing is broken - it's just the API starting up again. We manually restart the API server once each day to fetch results relevant to today's data.

## License

    AlgoBot - An algorithmic trading bot written in Python

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
For more information, see [LICENSE.md](https://github.com/Davarco/AlgoBot/blob/master/LICENSE.md).
