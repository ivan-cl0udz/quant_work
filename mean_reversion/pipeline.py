


def sharpe(returns):
    return (returns.mean() / returns.std()) * (255 ** 0.5)

def backtest_mean_reversion(data, window=20, z_entry=-1, z_exit=1):
    df = data.copy()
    df['Rolling_Mean'] = df['Close'].rolling(window=window).mean()
    df['Rolling_Std'] = df['Close'].rolling(window=window).std()

    df['Z_Score'] = (df['Close'] - df['Rolling_Mean']) / df['Rolling_Std']

    df['Returns'] = df['Close'].pct_change()

    df['Signal'] = 0
    df.loc[df['Z_Score'] < z_entry, 'Signal'] = 1
    df.loc[df['Z_Score'] > z_exit,'Signal'] = 0

    df['Strategy_Returns'] = df['Signal'].shift(1) * df['Returns']

    df['Equity_Curve'] = (1 + df['Strategy_Returns']).cumprod()
    df['Buy_Hold'] = (1 + df['Returns']).cumprod()

    sharpe_mr = sharpe(df['Strategy_Returns'])
    sharpe_bh = sharpe(df['Returns'])

    print(f'Mean Reversion Strategy Sharpe Ratio: {sharpe_mr:.2f}')
    print(f'Buy and Hold Sharpe Ratio: {sharpe_bh:.2f}')

    return df 


