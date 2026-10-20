# Quant Trading — Learning Repository

A self-directed quant trading research project built from scratch.
All strategies are backtested on real market data using Python.

---

## About

I'm 16, teaching myself quantitative trading and systematic strategy
development. This repository documents my learning journey —
hypothesis formation, backtesting, analysis, and honest conclusions
including failed strategies.

---

## Tech Stack

- Python 3.14
- Pandas & NumPy — data manipulation
- yFinance — market data
- Plotly — interactive visualisations
- Jupyter Notebooks — research and documentation
- Modular pipeline architecture (metrics.py, strategy pipelines)

---

## Projects

### Project 1 — SMA Crossover Strategy
**Hypothesis:** SMA crossover strategies perform differently
depending on market conditions.

**Stocks tested:** AAPL (2025–2026), INTC (2022–2026)

**Strategies tested:**
- SMA 20/50 crossover
- SMA 10/30 crossover
- Buy & Hold benchmark

**Key findings:**
- SMA crossover underperforms buy & hold in strong uptrends (AAPL)
- SMA crossover provides meaningful downside protection in choppy/
  declining markets (INTC) — avoided ~60% drawdown
- Faster crossover (10/30) produced more signals but lower
  Sharpe ratio than slower (20/50)
- Buy & hold is a deceptively strong benchmark to beat

**Metrics used:** Sharpe Ratio, Equity Curve, Max Drawdown

---

### Project 2 — Mean Reversion Strategy (Z-Score)
**Hypothesis:** Stocks that deviate significantly from their
rolling mean tend to revert — this can be exploited systematically.

**Stocks tested:** INTC (2022–2026), KO (2020–2026)

**Key findings:**
- Mean reversion strategy avoided the majority of INTC's
  2022–2024 decline by sitting in cash during extended downtrends
- KO's steady uptrend meant the strategy rarely triggered —
  buy & hold captured far more upside
- Consistent pattern: active strategies protect capital in choppy
  markets but miss gains in trending ones

**Metrics used:** Sharpe Ratio, Equity Curve, Max Drawdown, Z-Score signals

---

### Project 3 — RSI Strategy
**Hypothesis:** RSI oversold/overbought signals generate
positive returns across different market conditions.

**Stocks tested:** INTC, KO (2020–2026)

**Key findings:**
- RSI provides downside protection on volatile stocks (INTC)
  but misses gains on stable uptrending stocks (KO)
- KO rarely hit RSI extremes — strategy sat in cash too long
- Sharpe: INTC strategy 0.05 vs B&H 0.47 — lower but significantly
  smoother equity curve

**Metrics used:** Sharpe Ratio, Equity Curve, Max Drawdown, Win Rate

---

### Project 4 — Dual Momentum Strategy
**Hypothesis:** Combining relative momentum (SPY vs EFA) with
absolute momentum (winner vs cash) improves risk-adjusted returns
versus buy & hold.

**Assets tested:** SPY, EFA, BIL (2011–2025)

**Strategy logic:**
- Each month: pick the higher momentum asset between SPY and EFA
- If winner beats T-bills (BIL) → hold winner
- If winner underperforms T-bills → move to cash (BIL)
- Rebalance monthly

**Key findings:**
- Strategy returned 224% vs SPY's 593% over 2011–2025
- Max drawdown significantly lower: -19.48% vs -23.93%
- Underperformed in prolonged bull market — designed to shine
  during bear markets (2000–2002, 2008) not tested in this period
- Transaction costs minimal due to low monthly turnover

**Metrics used:** Sharpe Ratio, Equity Curve, Max Drawdown,
Annualised Return, Transaction Costs, Slippage

---

## Overarching Finding

Across all four strategies and multiple assets, one consistent
pattern emerged:

| Market Type | Best Approach |
|-------------|--------------|
| Strong uptrend | Buy & Hold |
| Choppy / volatile | Active strategy (RSI, Mean Reversion, SMA) |
| Bear market | Momentum rotation (Dual Momentum) |

**Strategy selection should be driven by market regime —
not applied blindly across all conditions.**

---

## Concepts Covered

**Strategy & Backtesting**
- Signal generation with np.where() and .loc[]
- Lookahead bias prevention with shift(1)
- Buy & hold benchmarking
- Walk-forward thinking
- Transaction costs and slippage modelling
- Monthly vs daily rebalancing

**Technical Indicators**
- SMA crossover (Golden cross / Death cross)
- RSI (Relative Strength Index)
- Z-score mean reversion
- Rolling volatility
- 12-month momentum

**Risk & Performance Metrics**
- Sharpe ratio (daily and monthly, annualised)
- Maximum drawdown
- Win rate
- Annualised return
- Equity curves & cumprod()
- Risk-free rate adjustment

**Data & Infrastructure**
- Modular pipeline architecture
- Shared metrics.py across all strategies
- Multi-asset portfolio construction
- yFinance data handling and MultiIndex flattening
- Survivorship bias awareness

---

## Honest Approach

Every strategy in this repo is tested properly:
- No curve fitting or parameter tweaking until results look good
- Failed hypotheses documented alongside successful ones
- Transaction costs and slippage included in final results
- Conclusions reflect what the data actually shows

---

## Roadmap

- [x] SMA crossover strategy
- [x] Mean reversion strategy (Z-score)
- [x] RSI strategy
- [x] Dual momentum (multi-asset rotation)
- [x] Shared metrics pipeline
- [x] Maximum drawdown metric
- [x] Transaction costs and slippage
- [ ] Bollinger Bands strategy
- [ ] Volume-filtered SMA
- [ ] Walk-forward validation
- [ ] Portfolio combining multiple strategies

---

## Resources

- *Quantitative Trading* — Ernest Chan
- *Inside the Black Box* — Rishi Narang
- [SSRN](https://ssrn.com) — academic strategy papers
- [Patrick Boyle](https://www.youtube.com/@PBoyle) — YouTube
- [Khan Academy Statistics & Probability](https://www.khanacademy.org/math/statistics-probability)
