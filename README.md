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

---

## Projects

### Week 1 — SMA Crossover Strategy
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

**Metrics used:** Sharpe Ratio, Equity Curve, Signal Returns

---

## Concepts Covered So Far

- Daily returns & pct_change()
- Rolling averages (SMA)
- Annualised volatility
- Sharpe ratio
- Equity curves & cumprod()
- Lookahead bias & shift(1)
- Buy & hold benchmarking
- Golden cross / death cross
- Signal generation with np.where()

---

## Honest Approach

Every strategy in this repo is tested properly:
- No curve fitting or parameter tweaking until results look good
- Failed hypotheses are documented alongside successful ones
- Conclusions reflect what the data actually shows

---

## Roadmap

- [x] SMA crossover strategy
- [ ] Mean reversion strategy
- [ ] Multi-stock comparison
- [ ] Maximum drawdown metric
- [ ] Portfolio of strategies
- [ ] Walk-forward validation

---

## Resources

- *Quantitative Trading* — Ernest Chan
- *Inside the Black Box* — Rishi Narang
- [SSRN](https://ssrn.com) — academic strategy papers
- [Patrick Boyle](https://www.youtube.com/@PBoyle) — YouTube
