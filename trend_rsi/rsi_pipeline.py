import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from metrics import calculate_rsi, print_metrics_summary


def perform_rsi_analysis(data, window=14, label="RSI"):
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
    
    print_metrics_summary(f'{label} Strategy', df['Strategy_Returns'], df['Equity_Curve'])
    print_metrics_summary(f'{label} Buy & Hold', df['Returns'], df['Buy_and_Hold'])
    
    return df
