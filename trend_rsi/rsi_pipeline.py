

def sharpe_ratio(returns):
    return (returns.mean() / returns.std()) * (252 ** 0.5)  # Annualized Sharpe ratio

def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def perform_rsi_analysis(data, window=14):
    df = data.copy()  # ✅ never modify original
    df.columns = df.columns.get_level_values(0)
    df['Returns'] = df['Close'].pct_change()
    df['SMA_50'] = df['Close'].rolling(50).mean()
    df['RSI'] = calculate_rsi(df, window)
    df = df.dropna()  # ✅ not inplace, just reassign
    
    df['Signal'] = 0
    df.loc[df['RSI'] < 30, 'Signal'] = 1
    df.loc[df['RSI'] > 70, 'Signal'] = 0
    
    df['Strategy_Returns'] = df['Signal'].shift(1) * df['Returns']
    df = df.dropna()
    df['Equity_Curve'] = (1 + df['Strategy_Returns']).cumprod()
    df['Buy_and_Hold'] = (1 + df['Returns']).cumprod()
    
    strat_sharpe = sharpe_ratio(df['Strategy_Returns'])
    bh_sharpe = sharpe_ratio(df['Returns'])
    
    print(f"Strategy Sharpe Ratio: {strat_sharpe:.2f}")
    print(f"Buy and Hold Sharpe Ratio: {bh_sharpe:.2f}")
    
    return df