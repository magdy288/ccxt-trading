from data import DataFrameC

import pandas_ta as ta
import pandas as pd

df = DataFrameC.get_data()



atr = ta.atr(df['high'], df['low'], df['close'], length=5)



# very valid
def aroon_signal(df):
    aroon = ta.aroon(df['high'], df['low'])
    signal = []
    for i in range(len(df)):
        if aroon['AROONU_14'][i] >= 70 and aroon['AROOND_14'][i] <= 30:
            signal.append(1)
        elif aroon['AROONU_14'][i] <= 30 and aroon['AROOND_14'][i] >= 70:
            signal.append(-1)
        else:
            signal.append(0)
            
    return pd.Series(signal).astype(int)

# very valid
def ebws_signal(df):
    ebsw = ta.ebsw(df['close'])
    signal = []
    
    for i in range(len(df)):
        if ebsw.iloc[i] > 0:
            signal.append(1)
        elif ebsw.iloc[i] < 0:
            signal.append(-1)
        else:
            signal.append(0)
    return pd.Series(signal).astype(int)




def eom_signal(df):
    eom = ta.eom(df['close'], df['low'], df['high'], df['volume'])
    signal = []
    
    for i in range(len(df)):
        if eom.iloc[i] > 0:
            signal.append(1)
        elif eom.iloc[i] < 0:
            signal.append(-1)
        else:
            signal.append(0)
            
    return pd.Series(signal).astype(int)

def cti_signal(df):
    cti = ta.cti(df['close'])
    signal = []
    
    for i in range(len(df)):
        if cti.iloc[i] > 0:
            signal.append(1)
        elif cti.iloc[i] < 0:
            signal.append(-1)
        else:
            signal.append(0)
    return pd.Series(signal)


cti = cti_signal(df)
ebws = ebws_signal(df)
aroon = aroon_signal(df)
eom = eom_signal(df)
signals = pd.concat(objs=[ebws, eom, cti, aroon], axis=1, keys=['ebws', 'eom', 'cti', 'aroon'])


def sig(signals):
    signal = []

    for i in range(0, len(signals)):
        if signals['ebws'].iloc[i] and signals['eom'].iloc[i] and signals['cti'].iloc[i] or signals['aroon'].iloc[i] == 1:
            signal.append(int(1))
                
            
        elif signals['ebws'].iloc[i] and signals['eom'].iloc[i] and signals['cti'].iloc[i] or signals['aroon'].iloc[i] == -1:
            signal.append(int(-1))

            
        else:
            signal.append(0)
        
    return pd.Series(signal)

sign = sig(signals)


 