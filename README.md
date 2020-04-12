## Trading bot

### Description
Bot generate trading operations based on MACD, using historical data. By default bot use [Finnhub](https://finnhub.io/) API.

### How to start
1. Clone repo
2. pip install -r requirements.txt
3. Run ```python3 trading_bot.py```

### Instruction:
1. Register on the site [Finnhub](https://finnhub.io/) and get API key
2. Put key into variable API_KEY located on /src/settings.py
3. You can change resource querying by api (for more information [read docs](https://finnhub.io/docs/api))
4. Flags:
    * -t - Stock ticker (for example APPL).
    * -s - Start date. Set up by default as 2018-01-01.
    * -e - End date. Set up by default as today.
5. Script generate file with transactions. File located on the root folder.
    
Command example: ```python3 trading_bot.py -t APPl -s 2018-01-01 -e 2018-03-1```   
