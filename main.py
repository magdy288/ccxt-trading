import data
import indicator
import config

import ccxt
import time

class Strategy:
    def __init__(self):
        self.df = data.DataFrameC()

        self.signals = indicator.sign
        self.symbol = data.symbol
        self.amount = float(input('enter the Qty of coin: '))

        
        apiKey = config.apiKey
        secret = config.secret
        self.api = ccxt.phemex({
            'enableRateLimit': True,
            'apiKey': apiKey,
            'secret': secret
        })
        self.api.set_sandbox_mode(True)

        ob = self.api.fetch_order_book(self.symbol)
        self.bid = ob['bids'][0][0]
        self.ask = ob['asks'][0][0]

    def run(self):
        position = False

        while True:
            for i in range(len(self.signals)):
                
                if self.signals[i] == 1 and  position is False:
                    print(f'Buy {self.symbol} at {self.bid}')
                    print(self.signals.iloc[i])
                    position = True

                    order = self.api.create_limit_buy_order(self.symbol,self.amount,self.bid)  
                    print(order.id)
                            
                elif self.signals[i] == -1 and position is True:
                    print(f'Sell {self.symbol} at {self.ask}')
                    print(self.signals.iloc[i])
                    position = False

                    order = self.api.create_limit_sell_order(self.symbol,self.amount,self.ask)
                    print(order.id)  
                
                    
                elif self.signals[i] == 0:
                    print(f'no position taken at ${self.bid,self.ask}: for  {self.symbol}')
                    print(self.signals.iloc[i])
                time.sleep(60)
                
ss = Strategy()
ss.run()