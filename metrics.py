def sharpe(returns):
    return (returns.mean() / returns.std()) * (252 ** 0.5)  # Annualized Sharpe ratio

def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def calc_max_drawdown(equity_curve):
    rolling_max = equity_curve.cummax()

    drawdown = (equity_curve - rolling_max) / rolling_max
    return drawdown.min()


def calc_win_rate(strategy_returns):
    active = strategy_returns[strategy_returns != 0]
    wins = (active > 0).sum()
    total = len(active)
    return wins / total if total > 0 else 0


def calc_ann_returns(equity_curve, trading_days=252):
    clean_curve = equity_curve.dropna()
    if len(clean_curve) < 2:
        return float("nan")

    total_returns = clean_curve.iloc[-1] / clean_curve.iloc[0]
    n_years = (len(clean_curve) - 1) / trading_days
    return total_returns ** (1 / n_years) - 1


def print_metrics_summary(name, returns, equity_curve):
    metrics = {
        "Sharpe": sharpe(returns),
        "Max Drawdown": calc_max_drawdown(equity_curve),
        "Win Rate": calc_win_rate(returns),
        "Annualised Return": calc_ann_returns(equity_curve),
    }

    print(f"\n{name} Metrics")
    print(f"Sharpe: {metrics['Sharpe']:.2f}")
    print(f"Max Drawdown: {metrics['Max Drawdown']:.2%}")
    print(f"Win Rate: {metrics['Win Rate']:.2%}")
    print(f"Annualised Return: {metrics['Annualised Return']:.2%}")
    return metrics
