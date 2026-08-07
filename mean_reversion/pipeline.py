
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from metrics import print_metrics_summary

def backtest_mean_reversion(data, window=20, z_entry=-1, z_exit=1, label="Mean Reversion"):
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

    print_metrics_summary(f'{label} Strategy', df['Strategy_Returns'], df['Equity_Curve'])
    print_metrics_summary(f'{label} Buy & Hold', df['Returns'], df['Buy_Hold'])

    return df 
