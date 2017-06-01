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

Make sure to run the python files from the project root directory. Althoug the API is meant to be run under a NGROK tunneler, you can also host it locally by running the api.py file. 

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
