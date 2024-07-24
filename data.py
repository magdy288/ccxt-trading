import config

import ccxt
import pandas as pd

apiKey = config.apiKey
secret = config.secret
api = ccxt.phemex({
    'enableRateLimit': True,
    'apiKey': apiKey,
    'secret': secret
})
api.set_sandbox_mode(True)


symbol = str(input('enter the symbol: '))
tf = str(input('timeframe: '))
limit = int(input('enter limit candels: '))


class DataFrameC:

    def get_data():
    
        can = api.fetch_ohlcv(symbol,tf,limit)
        df = pd.DataFrame(can, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
        df['time'] = pd.to_datetime(df['time'], unit='ms')

        return df

