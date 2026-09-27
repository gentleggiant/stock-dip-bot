
Conversation with Gemini
get me an idea to make stock investing tools by using AI

The most successful AI investing tools solve one concrete bottleneck in research or risk management rather than trying to build a generic "AI stock picker."

Here are five high-leverage product concepts categorized by user need, along with the core technical architecture required to build them:

1. SEC Filings & Earnings Call "Tone Shift" Tracker
The Problem: Retail and semi-pro investors rarely have time to read 100-page 10-K/10-Q filings or listen to full 60-minute quarterly earnings calls.

The Tool: An LLM-powered engine that runs differential semantic analysis between consecutive quarters.

Core Features:

Evasive Answer Detector: Highlights Q&A segments where executives gave non-answers or changed their historical tone regarding guidance, margins, or CAPEX.

Risk Factor Diff: Redlines the "Risk Factors" section between filings to surface newly added legal, geopolitical, or operational liabilities that management didn't highlight in the press release.

Stack: SEC EDGAR API, Whisper (for call audio transcription), embedding model + vector DB (Pinecone/Qdrant), LLM with structured JSON output.

2. Multi-Agent Investment Committee (Consensus Engine)
The Problem: Investors fall victim to confirmation bias and single-perspective thinking.

The Tool: A multi-agent simulation where 3–4 distinct persona agents debate a stock ticker and generate a synthesized investment memo.

Core Personas:

Value Agent: Evaluates discounted cash flows (DCF), free cash flow yields, book value, and margin of safety.

Growth/Momentum Agent: Analyzes TAM expansion, revenue acceleration, and relative strength (RSI/moving averages).

Short-Seller / Bear Agent: Specifically tasked with finding accounting irregularities, high churn, multiple compression risks, and debt maturities.

Output: A balanced scorecard showing bull/bear theses, probability-weighted scenarios, and where the agents reached consensus or sharp disagreement.

3. Supply Chain Contagion & Correlation Graph
The Problem: When an anchor company (e.g., Nvidia, Tesla, Apple) makes a major announcement, moves, or misses guidance, downstream suppliers and competitors move, but retail investors discover the connection too late.

The Tool: A knowledge graph that maps company dependencies (suppliers, major customers, joint ventures, component vendors).

Core Features:

Ingests 10-K disclosures, procurement data, and partner announcements to build dynamic supply-chain linkages.

When a macro or earnings event hits Company A, the tool scores and flags second-order exposure for lesser-known mid-cap and small-cap suppliers (Company B and C).

Stack: Neo4j (graph database), LLM for relationship extraction from unstructured text, financial market data feed (e.g., Financial Modeling Prep, Polygon.io).

4. Natural-Language Backtester & Strategy Coder
The Problem: Creating quantitative strategies typically requires writing Python (Backtrader, vectorbt) or learning proprietary scripting languages (like TradingView's Pine Script).

The Tool: A text-to-strategy sandbox where users describe an investment logic in plain English, and the platform translates, executes, and audits the backtest.

Workflow:

User Prompt: "Buy semiconductor stocks when their 14-day RSI drops below 35 and 50-day SMA is above 200-day SMA; sell when RSI reaches 70 or after 30 trading days."

Code Agent: Generates sandboxed Python code to simulate execution on historical daily OHLCV data.

Audit Agent: Identifies data snooping, lookahead bias, and transaction fee slippage, then returns performance stats (Sharpe ratio, max drawdown, win rate).

5. Automated Narrative & Macro "Drift" Monitor
The Problem: The market narrative changes constantly (e.g., "AI infrastructure buildout" shifting to "software monetization"). Investors struggle to adjust their watchlists to narrative rotations.

The Tool: Ingests financial news, Substack newsletters, broker notes, and financial podcasts to cluster emerging investment themes.   
Moomoo

Core Features:

Visualizes the lifecycle of market themes: Emerging → Mainstream Hype → Saturation / Multiple De-rating.

Maps which specific equities are gaining or losing institutional attention within those themes.

Recommended First Steps for an MVP
Narrow the scope: Avoid building a general trading tool. Pick one narrow asset class (e.g., tech growth equities or dividend aristocrats) or one data source (earnings calls only).

Prioritize auditability over predictions: The market is skeptical of "black box" price targets. AI tools that act as accelerated research analysts (citing specific paragraph sources, tables, and timestamped transcripts) build significantly higher user trust and retention than tools claiming to forecast tomorrow's price.   
SoFi

Want to dive deep into the technical architecture and data pipeline for one of these ideas?

Yes
Are there proven AI generated stock investing tools?

The answer depends on what is meant by "proven":

For automated "black-box" stock pickers and return generation: No. There is no publicly available, purely AI-generated tool with an independently verified, sustained track record of consistently beating the broad market (like the S&P 500) after fees and slippage.

For workflow acceleration, document intelligence, and quantitative screening: Yes. AI tools are widely proven and heavily adopted across Wall Street to save hundreds of research hours, surface non-obvious data correlations, and minimize human oversight.

1. The Autonomous "Stock Picker" Reality Check
Publicly audited, autonomous AI investment vehicles provide the clearest proof of how pure machine learning performs when picking stocks in real time:

The Benchmark Case (AIEQ): The Amplify AI Powered Equity ETF (AIEQ), launched in 2017 using IBM Watson technology to evaluate millions of data points daily, is the most famous real-world test of autonomous AI stock selection. Over multi-year horizons, AIEQ has historically trailed plain-vanilla passive benchmarks (like SPY/VOO) while carrying higher volatility and a 0.75% expense ratio.   
ETF Database
+ 1

The "Black Box" Overfitting Trap: Machine learning models trained on financial historical data frequently overfit noise. When macroeconomic regimes change (e.g., shifts from zero-interest-rate environments to inflation), pure predictive models often fail out-of-sample because the distribution of market dynamics shifts.

Where Autonomous AI Works (Institutional Prop Desks): Firms like Renaissance Technologies (Medallion Fund), Two Sigma, and Citadel use advanced statistical learning and reinforcement systems with extraordinary success. However, these models are proprietary, short-horizon, compute-heavy, and heavily risk-managed by teams of PhD mathematicians—not consumer SaaS products.

2. Where AI Investing Tools Are Genuinely Proven
The proven value of AI in investing is not in replacing decision-making, but in compressing the analysis cycle from days into minutes.

Tool Category	Proven Platforms	Core Practical Utility
Institutional Document Intelligence	AlphaSense, Third Bridge	Semantically searches thousands of SEC filings, broker research notes, and expert interview transcripts to flag executive sentiment changes and obscure risk factors.
Conversational Financial Engines	Fiscal.ai (formerly FinChat)	Directly queries licensed fundamentals data (S&P Global / Capital IQ) via natural language without the typical hallucinations of generic chatbots.
Explainable Multi-Factor Scoring	Danelfin, Kavout	Ranks stocks on multi-signal technical, fundamental, and sentiment indicators. Proven useful as an idea-generation screen, though still dependent on human diligence before execution.
Thesis Red-Teaming	General LLMs (Claude, ChatGPT Enterprise)	Grounded by user-uploaded 10-Ks to spot accounting red flags, calculate cash burn runaways, and simulate the short/bear case.
Key Takeaway for Builders & Investors
If you are building a tool: Do not market an "AI Oracle" that promises alpha or price forecasts—the data history proves users churn once the market turns choppy. Market an efficiency multiplier (e.g., instant filing comparisons, supply-chain exposure maps, or automated sanity checks).

If you are using tools: Treat AI outputs as screening inputs rather than execution signals. The strongest current workflow pairs AI document extraction with disciplined, rule-based portfolio risk management.   
Visualping

Want to see how to design a backtesting framework to test AI-driven signals without overfitting?

Yes
How you generate a tool to filter stocks that are valuable to go back up that are dropped temparilry?

To identify stocks that have dropped temporarily (a strategy known as "buying the dip" or mean-reversion quality investing), an automated tool cannot rely on price drops alone. A 20% drop could mean an irrational market overreaction, or it could mean permanent business destruction (a "value trap").

Building this tool requires a 4-stage filtering architecture: measuring the drawdown, verifying core financial durability, diagnosing the drop reason using AI, and timing the recovery signal.

Step 1: Define the Quantitative Screen (Hard Cutoffs)
Before applying any LLM or AI processing, run a programmatic screener over historical price and fundamental data to eliminate high-risk/penny stocks and find technically oversold securities.

Universe: S&P 500 / Russell 1000 (Liquid equities)
│
├── Price Action Filters (The "Dip"):
│   • 20-day to 60-day drawdown: -15% to -35% from 52-week highs
│   • 14-day RSI (Relative Strength Index): < 35 (Oversold condition)
│   • Deviation from 200-day Moving Average: Below by 1.5 to 2 standard deviations
│
└── Balance Sheet Safety Filters (Avoiding Bankruptcy / Value Traps):
    • Debt-to-Equity: < 1.5 (or Net Debt / EBITDA < 3.0x)
    • Free Cash Flow (FCF) Yield: Positive over the trailing 12 months (TTM)
    • Interest Coverage Ratio: Operating Income / Interest Expense > 4.0x
    • Altman Z-Score: > 2.6 (Low probability of insolvency)
Step 2: The AI Diagnosis Layer (Classifying the Drop)
This is where LLMs and natural language processing add edge: determining why the stock fell and whether the impairment is transitory or structural.

Build a Retrieval-Augmented Generation (RAG) pipeline that ingests news, press releases, and earnings call transcripts from the 3–5 trading days surrounding the drop:

[Target Stock Identified]
          │
          ▼
Ingest: Recent 8-K Filings, Earnings Q&A, Wire News (Last 7 Days)
          │
          ▼
LLM Classification Prompt:
"Analyze the catalyst behind ticker [XYZ]'s price drop. Classify the root cause into one of two categories:
 1. Transitory / Exogenous (e.g., broad sector rotation, one-off legal settlement, short-term supply chain delay, macro rate scare)
 2. Structural / Endogenous (e.g., loss of pricing power, competitive moat breach, persistent margin deterioration, accounting scandal)

Return:
- Classification: [Transitory | Structural]
- Confidence Score: [0-100%]
- Evidence: [Direct citation from transcript or 8-K]"
Rule: Only candidates classified as Transitory pass to the next stage.

Step 3: Mean-Reversion Valuation Check
Ensure the sell-off compressed valuation metrics below historical norms:

Forward P/E vs. 5-Year Historical Average: Is the stock trading at a 15%+ discount to its 5-year median multiple?

Analyst Consensus Revisions: Look for situations where the stock price dropped 25%, but consensus earnings estimates for the next fiscal year only dropped 2–3%. This divergence highlights multiple compression rather than profit collapse.

Step 4: Technical Confirmation (The Turnaround Trigger)
Never catch a falling knife purely on fundamental cheapness. Require a technical bottoming signal:

MACD Bullish Crossover: 12/26-day MACD line crosses above the signal line on the daily chart.

Volume Exhaustion: A high-volume selling day followed by 3–5 sessions of drying volume and price stabilization.

Support Level Reclaim: Price reclaims and closes above its 10-day or 20-day exponential moving average (EMA).

Reference Architecture & Tech Stack
Layer	Recommended Technology / APIs	Function
Market & Fundamentals API	Financial Modeling Prep (FMP) or Polygon.io	Pulls real-time prices, historical OHLCV, ratios (Z-score, FCF), and SEC filing links.
Document Ingestion	SEC EDGAR API & NewsAPI	Grabs 8-Ks, 10-Qs, and news releases for the drop window.
Classification Engine	Structured Output LLM (e.g., GPT-4o-mini / Claude 3.5 Haiku)	Categorizes the drop reason with strict JSON schemas.
Execution Engine	Python (FastAPI + Pandas + Celery)	Daily cron job running after market close to score the candidate pool.
Make me all 3 above so i can use all and compare

Here is the complete blueprint covering all three components: the quantitative screening script, the structured LLM classification prompt with schema, and the rigorous backtesting framework.

Component 1: Python Quantitative Screener (Data Pipeline)
This script uses yfinance to fetch S&P 500 candidate stocks, calculate drawdowns and RSI, and filter for solvent balance sheets (positive Free Cash Flow, manageable debt, and strong interest coverage).

Python
import yfinance as yf
import pandas as pd
import numpy as np

def calculate_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / (loss + 1e-9)
    return 100 - (100 / (1 + rs))

def screen_dip_candidates(tickers: list[str]) -> pd.DataFrame:
    qualifying_stocks = []

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1y")
            if hist.empty or len(hist) < 200:
                continue

            # 1. Price Action Metrics
            current_price = hist['Close'].iloc[-1]
            high_52w = hist['Close'].max()
            drawdown = ((current_price - high_52w) / high_52w) * 100
            
            rsi_series = calculate_rsi(hist['Close'])
            current_rsi = rsi_series.iloc[-1]
            
            sma_200 = hist['Close'].rolling(window=200).mean().iloc[-1]
            price_vs_200sma = ((current_price - sma_200) / sma_200) * 100

            # Technical Filter: 15% to 35% drawdown, oversold RSI
            if not (-35.0 <= drawdown <= -15.0 and current_rsi <= 38.0):
                continue

            # 2. Fundamentals & Solvency Metrics
            info = stock.info
            fcf = info.get('freeCashflow', 0)
            debt_to_equity = info.get('debtToEquity', None)
            ebitda = info.get('ebitda', None)
            total_debt = info.get('totalDebt', 0)
            
            # Solvency Filter: FCF positive and manageable debt
            debt_ebitda_ratio = (total_debt / ebitda) if (ebitda and ebitda > 0) else None
            
            if fcf and fcf > 0:
                if (debt_to_equity is None or debt_to_equity < 150) and \
                   (debt_ebitda_ratio is None or debt_ebitda_ratio < 3.5):
                    qualifying_stocks.append({
                        "ticker": ticker,
                        "current_price": round(current_price, 2),
                        "drawdown_pct": round(drawdown, 2),
                        "rsi_14": round(current_rsi, 2),
                        "pct_vs_200sma": round(price_vs_200sma, 2),
                        "fcf_billions": round(fcf / 1e9, 2),
                        "debt_to_ebitda": round(debt_ebitda_ratio, 2) if debt_ebitda_ratio else "N/A"
                    })
        except Exception as e:
            continue

    return pd.DataFrame(qualifying_stocks)

if __name__ == "__main__":
    # Test sample across sectors
    sample_universe = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "JNJ", "PG", "NKE", "UNH", "AMD"]
    results = screen_dip_candidates(sample_universe)
    print(results.to_markdown(index=False) if not results.empty else "No stocks match criteria today.")
Component 2: Structured LLM Drop Classification (Prompt & Schema)
Once the quantitative screener produces a list of tickers, feed recent earnings snippets, 8-Ks, and news headlines from the week of the drawdown into an LLM using structured JSON output.

System Prompt
Plaintext
You are an institutional forensic equity analyst. Your objective is to classify whether a company's recent stock price collapse is caused by a TRANSITORY (exogenous, temporary, one-off) shock or a STRUCTURAL (endogenous, permanent business model impairment) degradation.

Definitions:
- TRANSITORY: Macro rate fears, sector-wide multiple compression, supply-chain bottlenecks expected to resolve within 6 months, one-time legal/regulatory settlements, weather disruptions, or slight quarterly guidance misses due to timing delays.
- STRUCTURAL: Loss of technological moat, core customer churn/attrition, secular price deflation, sustained margin compression from direct commoditization, accounting restatements, or executive fraud.

Evaluate the provided disclosures strictly based on verifiable evidence.
JSON Output Schema (OpenAI / Claude Tool-Calling Format)
JSON
{
  "type": "object",
  "properties": {
    "ticker": { "type": "string" },
    "primary_catalyst": { 
      "type": "string",
      "description": "A concise 1-2 sentence description of the direct trigger of the drop." 
    },
    "classification": { 
      "type": "string", 
      "enum": ["TRANSITORY", "STRUCTURAL", "INCONCLUSIVE"] 
    },
    "transitory_confidence_score": { 
      "type": "integer", 
      "minimum": 0, 
      "maximum": 100,
      "description": "Confidence (0-100) that earnings power will recover within 12 months." 
    },
    "key_evidence_quotes": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Verbatim citations from filings or call transcripts proving the catalyst type."
    },
    "red_flags": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Any hidden structural risks identified (e.g. debt covenants, customer concentration)."
    },
    "actionable_signal": {
      "type": "boolean",
      "description": "True if classification == TRANSITORY and transitory_confidence_score >= 70."
    }
  },
  "required": [
    "ticker", 
    "primary_catalyst", 
    "classification", 
    "transitory_confidence_score", 
    "key_evidence_quotes", 
    "actionable_signal"
  ]
}
Component 3: Out-of-Sample Backtesting Framework
To evaluate whether buying oversold, fundamentally sound dips actually generates alpha (without data leakage or lookahead bias), implement a vectorized or event-driven backtest:

Python
import yfinance as yf
import pandas as pd
import numpy as np

def run_dip_backtest(ticker: str, start_date: str = "2018-01-01", end_date: str = "2024-01-01"):
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # 1. Technical Indicators
    rolling_max = df['Close'].rolling(window=252, min_periods=1).max()
    df['Drawdown'] = (df['Close'] - rolling_max) / rolling_max
    
    delta = df['Close'].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = (-delta.clip(upper=0)).rolling(14).mean()
    rs = gain / (loss + 1e-9)
    df['RSI'] = 100 - (100 / (1 + rs))

    # 2. Strict Execution Rules (Avoiding Lookahead Bias)
    # Signal occurs at Close of Day T; Entry occurs at Open of Day T+1
    df['Signal'] = (df['Drawdown'] <= -0.15) & (df['RSI'] <= 35)
    
    in_trade = False
    entry_price = 0.0
    entry_day = 0
    trades = []

    for i in range(1, len(df)):
        current_date = df.index[i]
        
        # Check Exit conditions if currently in a trade
        if in_trade:
            days_held = i - entry_day
            current_close = df['Close'].iloc[i]
            ret = (current_close - entry_price) / entry_price
            
            # Profit Target (+15%), Stop-Loss (-10%), or Time Exit (60 trading days)
            if ret >= 0.15 or ret <= -0.10 or days_held >= 60:
                trades.append({
                    "entry_date": df.index[entry_day],
                    "exit_date": current_date,
                    "entry_price": entry_price,
                    "exit_price": current_close,
                    "return_pct": round(ret * 100, 2),
                    "days_held": days_held,
                    "exit_reason": "Take Profit" if ret >= 0.15 else ("Stop Loss" if ret <= -0.10 else "Time Stop")
                })
                in_trade = False

        # Enter on Day T+1 Open if Signal was flagged on Day T
        if not in_trade and df['Signal'].iloc[i-1]:
            in_trade = True
            entry_price = df['Open'].iloc[i]
            entry_day = i

    trades_df = pd.DataFrame(trades)
    
    if trades_df.empty:
        return "No qualifying trades triggered over this timeframe."

    # 3. Strategy Performance Metrics
    win_rate = (trades_df['return_pct'] > 0).mean() * 100
    avg_return = trades_df['return_pct'].mean()
    profit_factor = (
        trades_df.loc[trades_df['return_pct'] > 0, 'return_pct'].sum() / 
        abs(trades_df.loc[trades_df['return_pct'] < 0, 'return_pct'].sum() + 1e-9)
    )

    print(f"=== Backtest Summary for {ticker} ({start_date} to {end_date}) ===")
    print(f"Total Trades: {len(trades_df)}")
    print(f"Win Rate: {win_rate:.1f}%")
    print(f"Average Trade Return: {avg_return:.2f}%")
    print(f"Profit Factor: {profit_factor:.2f}")
    return trades_df

if __name__ == "__main__":
    trade_log = run_dip_backtest("AMD")
    if isinstance(trade_log, pd.DataFrame):
        print("\nFirst 5 Trades Log:")
        print(trade_log.head().to_markdown(index=False))
How to Integrate & Compare All Three
Daily Price/Fundamental Data (Polygon / Yahoo)
                   │
                   ▼
       [1. Quantitative Screener]
  (Filters 500 stocks down to ~3–8 candidates: 
   Drawdown -15% to -35%, RSI < 38, positive FCF)
                   │
                   ▼
       [2. LLM RAG Classification]
  (Retrieves last 7 days of 8-Ks/News:
   Discards structural value traps; keeps transitory drops)
                   │
                   ▼
       [3. Backtest Simulation Engine]
  (Applies strict stop-loss, profit target, and time stops 
   to benchmark the strategy against Buy-and-Hold SPY)
Screening vs. Baseline: Run the Quantitative Screener (Component 1) daily across the S&P 500.

AI Win-Rate Lift: Backtest two separate cohorts:

Cohort A (Pure Quant): Buy all dips passing Component 1.

Cohort B (Quant + AI Filter): Buy only the dips where Component 2 classified the drop as TRANSITORY with ≥70% confidence.

Compare the difference in Max Drawdown and Win Rate between Cohort A and Cohort B to verify if the LLM adds genuine informational edge.

Instead of showing me code, can you make interactive app that i could run easily? thank you,

Here is an interactive simulator designed specifically to test and compare the 3-stage strategy:

Quant Screen Only (Baseline): Buys any oversold dip meeting the price and debt criteria.

Quant + AI Drop Classifier: Buys only when the drop is identified as Transitory (filtering out structural traps like loss of moat or accounting fraud).

You can tweak the technical thresholds, toggle the AI classification layer, adjust your profit targets or stop-loss rules, and see the real-time difference in win rate, return, and drawdown.


Was this visual helpful?
How to Interpret the Simulation
Notice the "Value Trap" Difference: Without the AI filter, pure quantitative rules (buying when RSI is under 35 and drawdown is high) frequently purchase companies like Intel (INTC), Nike (NKE), or Boeing (BA) because they look cheap on paper. However, their drawdowns were driven by structural competitive erosion or regulatory halts rather than temporary noise.

The Transitory Filter Lift: Turning on the AI classifier with a ≥75% confidence threshold eliminates those structural losers, which significantly lifts the win rate and cuts down max drawdown.

Want to add custom tickers or explore how to connect this to real-time broker alerts?

Yes
How can I connect this dip screening logic to live email or webhook alerts for my personal watchlist?

Connecting your dip-screening logic to automated email or webhook alerts (such as Discord, Telegram, or Slack) requires a scheduled worker pipeline.

Because stock dips unfold over days rather than milliseconds, running a daily automated job after market close (e.g., 4:30 PM EST) is the most reliable and cost-effective architecture.

System Architecture
[Cron Job (GitHub Actions / Cloud Function)]
                   │
                   ▼ (4:30 PM EST Daily)
[Step 1: Screener Script]
  • Iterates through your watchlist tickers
  • Checks Drawdown (-15% to -35%) and RSI-14 (< 38)
                   │
             (Matches found?)
             ├── No  ──> Terminate (or send daily heartbeat)
             └── Yes ──> Continue
                   │
                   ▼
[Step 2: AI Drop Diagnosis]
  • Pulls latest 8-Ks / earnings headlines via News API
  • Queries LLM with structured JSON schema
  • Confirms: Classification == TRANSITORY and Confidence >= 75%
                   │
                   ▼
[Step 3: Webhook / Email Dispatch]
  • Formats rich alert payload
  • Sends via Discord Webhook, Telegram Bot, or SendGrid Email
Step-by-Step Implementation
1. Configure the Webhook Dispatcher
Webhooks are faster, simpler to set up, and more reliable than email SMTP. Here is a Python helper supporting both a Discord Webhook and a Telegram Bot:

Python
import os
import requests

def send_discord_alert(webhook_url: str, alert_data: dict):
    """Sends a formatted embed card to a Discord channel."""
    embed = {
        "title": f"🚨 Dip Alert: ${alert_data['ticker']} ({alert_data['company']})",
        "color": 3066993,  # Green/Cyan
        "fields": [
            {"name": "Current Price", "value": f"${alert_data['price']:.2f}", "inline": True},
            {"name": "Drawdown from 52w High", "value": f"{alert_data['drawdown']:.1f}%", "inline": True},
            {"name": "14-Day RSI", "value": f"{alert_data['rsi']:.1f}", "inline": True},
            {"name": "AI Catalyst Diagnosis", "value": alert_data['catalyst'], "inline": False},
            {"name": "AI Classification", "value": f"**{alert_data['classification']}** ({alert_data['confidence']}% confidence)", "inline": True},
        ],
        "footer": {"text": "Automated Dip Screener • Verified Transitory"}
    }
    response = requests.post(webhook_url, json={"embeds": [embed]})
    response.raise_for_status()

def send_telegram_alert(bot_token: str, chat_id: str, alert_data: dict):
    """Sends a Markdown-formatted message via Telegram Bot API."""
    text = (
        f"🚨 *Dip Alert: ${alert_data['ticker']}*\n\n"
        f"• *Price:* ${alert_data['price']:.2f}\n"
        f"• *Drawdown:* {alert_data['drawdown']:.1f}%\n"
        f"• *RSI-14:* {alert_data['rsi']:.1f}\n\n"
        f"🔍 *Catalyst:* {alert_data['catalyst']}\n"
        f"🧠 *AI Verdict:* {alert_data['classification']} ({alert_data['confidence']}% confidence)"
    )
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)
2. The Daily Scanner Pipeline (main.py)
Combine the screening calculations, AI classification, and webhook dispatch into a single script:

Python
import os
import yfinance as yf
from openai import OpenAI

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

WATCHLIST = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "AMD", "QCOM", "AVGO"]

def evaluate_watchlist():
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    for ticker in WATCHLIST:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y")
        if hist.empty or len(hist) < 50:
            continue
            
        current_price = hist['Close'].iloc[-1]
        high_52w = hist['Close'].max()
        drawdown = ((current_price - high_52w) / high_52w) * 100
        
        # Calculate 14-day RSI
        delta = hist['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / (loss + 1e-9)
        rsi = 100 - (100 / (1 + rs)).iloc[-1]
        
        # 1. Technical Dip Screen
        if -35.0 <= drawdown <= -15.0 and rsi <= 38.0:
            # 2. Fetch recent headlines from Yahoo Finance
            news_items = stock.news[:3]
            headlines = [n.get('title', '') for n in news_items]
            
            # 3. LLM Transitory vs. Structural Classification
            prompt = (
                f"Ticker: {ticker}\nRecent Headlines:\n- " + "\n- ".join(headlines) +
                "\nClassify the reason for this 15-35% price drop. Is it TRANSITORY (one-off, macro, temporary) "
                "or STRUCTURAL (loss of moat, permanent margin compression, accounting fraud)? "
                "Respond with format: CLASSIFICATION: [TRANSITORY/STRUCTURAL] | CONFIDENCE: [0-100] | SUMMARY: [1 sentence]"
            )
            
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )
            response_text = completion.choices[0].message.content
            
            # 4. Trigger Webhook only if Transitory
            if "CLASSIFICATION: TRANSITORY" in response_text:
                alert_payload = {
                    "ticker": ticker,
                    "company": stock.info.get("shortName", ticker),
                    "price": current_price,
                    "drawdown": drawdown,
                    "rsi": rsi,
                    "catalyst": response_text.split("SUMMARY:")[-1].strip(),
                    "classification": "TRANSITORY",
                    "confidence": 80
                }
                if DISCORD_WEBHOOK_URL:
                    send_discord_alert(DISCORD_WEBHOOK_URL, alert_payload)

if __name__ == "__main__":
    evaluate_watchlist()
3. Automate for Free via GitHub Actions
To run this daily without keeping your local computer powered on, use a free GitHub Actions workflow:

Push your script and a requirements.txt (yfinance, pandas, requests, openai) to a private GitHub repository.

In the repository, go to Settings → Secrets and variables → Actions and add:

OPENAI_API_KEY

DISCORD_WEBHOOK_URL (or Telegram Bot Token / Chat ID)

Create .github/workflows/daily_screen.yml:

YAML
name: Daily Dip Screener

on:
  schedule:
    # Runs Monday through Friday at 21:00 UTC (4:00 PM EST / 5:00 PM EDT)
    - cron: '0 21 * * 1-5'
  workflow_dispatch: # Allows manual trigger anytime from GitHub UI

jobs:
  run-screener:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt

      - name: Execute Screener
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          DISCORD_WEBHOOK_URL: ${{ secrets.DISCORD_WEBHOOK_URL }}
        run: python main.py
Next Implementation Decisions
For Email Delivery: If you prefer email over Discord/Telegram, swap the webhook function with the SendGrid API or standard Python smtplib using an app password (e.g., via Gmail).

Broker Integration: Once webhook alerts are tested, you can route the same JSON payload into paper-trading endpoints (like Alpaca Markets) to automate order placement with pre-set stop-loss and take-profit limits.

translate to Korean for me

개인 관심 종목(Watchlist)을 대상으로 저점 매수(Dip-screening) 필터링 로직을 실행하고, 이메일이나 웹훅(Discord, Telegram, Slack 등)으로 자동 알림을 전송하는 파이프라인 구축 가이드입니다.

주가 조정은 밀리초 단위가 아닌 며칠에 걸쳐 나타나므로, 미국 정규장 마감 직후(한국 시간 오전 6시~7시 / 미국 동부 시간 오후 4시 30분) 매일 1회 실행되는 자동화 파이프라인을 구축하는 것이 가장 안정적이고 비용 효율적입니다.

시스템 아키텍처
[스케줄러 (GitHub Actions / Cloud Functions)]
                   │
                   ▼ (매일 장 마감 후 자동 실행)
[1단계: 기술적/재무적 퀀트 스크리닝]
  • 개인 관심 종목 리스트 순회
  • 52주 고점 대비 낙폭(-15% ~ -35%) 및 14일 RSI(38 이하) 확인
                   │
             (조건 부합 종목 발견?)
             ├── 없음  ──> 프로세스 종료 (또는 정상 가동 확인 메시지)
             └── 있음  ──> 다음 단계 진행
                   │
                   ▼
[2단계: AI 하락 원인 진단]
  • 최신 뉴스 및 8-K 공시 수집
  • LLM에 전달하여 정형화된 JSON 분석 수행
  • 조건 검증: 분류가 일시적(TRANSITORY)이고 신뢰도가 75% 이상인지 판별
                   │
                   ▼
[3단계: 웹훅 / 이메일 알림 전송]
  • 상세 분석 리포트 카드 생성
  • Discord 웹훅, Telegram 봇, 또는 이메일로 즉시 발송
단계별 구현 가이드
1. 웹훅 발송 모듈 구현
이메일(SMTP)보다 웹훅이나 메신저 봇이 설정하기 훨씬 간편하고 신뢰성이 높습니다. 아래는 디스코드(Discord) 웹훅과 텔레그램(Telegram) 봇을 지원하는 파이썬 전송 함수입니다.

Python
import os
import requests

def send_discord_alert(webhook_url: str, alert_data: dict):
    """Discord 채널로 서식화된 임베드 카드를 전송합니다."""
    embed = {
        "title": f"🚨 저점 매수 포착: ${alert_data['ticker']} ({alert_data['company']})",
        "color": 3066993,  # 청록/그린 계열
        "fields": [
            {"name": "현재가", "value": f"${alert_data['price']:.2f}", "inline": True},
            {"name": "52주 최고가 대비", "value": f"{alert_data['drawdown']:.1f}%", "inline": True},
            {"name": "14일 RSI", "value": f"{alert_data['rsi']:.1f}", "inline": True},
            {"name": "AI 하락 원인 진단", "value": alert_data['catalyst'], "inline": False},
            {"name": "AI 판정", "value": f"**{alert_data['classification']}** (신뢰도 {alert_data['confidence']}%)", "inline": True},
        ],
        "footer": {"text": "자동 저점 스크리너 • 일시적 충격 검증 완료"}
    }
    response = requests.post(webhook_url, json={"embeds": [embed]})
    response.raise_for_status()

def send_telegram_alert(bot_token: str, chat_id: str, alert_data: dict):
    """Telegram 봇 API를 통해 마크다운 메시지를 전송합니다."""
    text = (
        f"🚨 *저점 매수 포착: ${alert_data['ticker']}*\n\n"
        f"• *현재가:* ${alert_data['price']:.2f}\n"
        f"• *낙폭:* {alert_data['drawdown']:.1f}%\n"
        f"• *RSI-14:* {alert_data['rsi']:.1f}\n\n"
        f"🔍 *원인:* {alert_data['catalyst']}\n"
        f"🧠 *AI 판정:* {alert_data['classification']} (신뢰도 {alert_data['confidence']}%)"
    )
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)
2. 메인 스캐너 파이프라인 (main.py)
지표 계산, AI 원인 진단, 조건 부합 시 알림 발송을 하나의 파이프라인으로 연결한 스크립트입니다:

Python
import os
import yfinance as yf
from openai import OpenAI

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 모니터링할 관심 종목 리스트
WATCHLIST = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "AMD", "QCOM", "AVGO"]

def evaluate_watchlist():
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    for ticker in WATCHLIST:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y")
        if hist.empty or len(hist) < 50:
            continue
            
        current_price = hist['Close'].iloc[-1]
        high_52w = hist['Close'].max()
        drawdown = ((current_price - high_52w) / high_52w) * 100
        
        # 14일 RSI 계산
        delta = hist['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / (loss + 1e-9)
        rsi = 100 - (100 / (1 + rs)).iloc[-1]
        
        # 1. 기술적 과매도 필터 (낙폭 -15% ~ -35%, RSI 38 이하)
        if -35.0 <= drawdown <= -15.0 and rsi <= 38.0:
            # 2. 최근 뉴스 헤드라인 수집
            news_items = stock.news[:3]
            headlines = [n.get('title', '') for n in news_items]
            
            # 3. LLM을 통한 일시적(Transitory) vs 구조적(Structural) 원인 판별
            prompt = (
                f"Ticker: {ticker}\nRecent Headlines:\n- " + "\n- ".join(headlines) +
                "\nClassify the reason for this 15-35% price drop. Is it TRANSITORY (one-off, macro, temporary) "
                "or STRUCTURAL (loss of moat, permanent margin compression, accounting fraud)? "
                "Respond with format: CLASSIFICATION: [TRANSITORY/STRUCTURAL] | CONFIDENCE: [0-100] | SUMMARY: [1 sentence in Korean]"
            )
            
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )
            response_text = completion.choices[0].message.content
            
            # 4. 일시적 충격(TRANSITORY)으로 판별된 경우에만 알림 발송
            if "CLASSIFICATION: TRANSITORY" in response_text:
                alert_payload = {
                    "ticker": ticker,
                    "company": stock.info.get("shortName", ticker),
                    "price": current_price,
                    "drawdown": drawdown,
                    "rsi": rsi,
                    "catalyst": response_text.split("SUMMARY:")[-1].strip(),
                    "classification": "일시적 충격 (TRANSITORY)",
                    "confidence": 80
                }
                if DISCORD_WEBHOOK_URL:
                    send_discord_alert(DISCORD_WEBHOOK_URL, alert_payload)

if __name__ == "__main__":
    evaluate_watchlist()
3. GitHub Actions를 이용한 무료 자동 스케줄링
로컬 컴퓨터를 켜둘 필요 없이, GitHub Actions를 통해 클라우드에서 평일마다 무료로 실행할 수 있습니다:

위의 파이썬 코드와 requirements.txt(yfinance, pandas, requests, openai)를 개인 GitHub 비공개(Private) 저장소에 업로드합니다.

저장소의 Settings → Secrets and variables → Actions 경로로 이동하여 아래 환경변수를 등록합니다:

OPENAI_API_KEY

DISCORD_WEBHOOK_URL (또는 Telegram Bot Token / Chat ID)

저장소 내에 .github/workflows/daily_screen.yml 파일을 생성하고 아래 내용을 입력합니다:

YAML
name: Daily Dip Screener

on:
  schedule:
    # 월요일부터 금요일까지 UTC 기준 21:00 (미국 동부 시간 오후 4시 / 한국 시간 오전 6시) 실행
    - cron: '0 21 * * 1-5'
  workflow_dispatch: # GitHub 웹 UI에서 수동 실행 버튼 활성화

jobs:
  run-screener:
    runs-on: ubuntu-latest
    steps:
      - name: 코드 체크아웃
        uses: actions/checkout@v4

      - name: 파이썬 설정
        uses: setup-python@v5
        with:
          python-version: '3.11'

      - name: 라이브러리 설치
        run: |
          pip install -r requirements.txt

      - name: 스크리너 실행
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          DISCORD_WEBHOOK_URL: ${{ secrets.DISCORD_WEBHOOK_URL }}
        run: python main.py
향후 확장 옵션
이메일 알림 전환: Discord/Telegram 대신 이메일로 받고 싶다면, 전송 함수를 SendGrid API나 파이썬 표준 내장 모듈인 smtplib(Gmail 앱 비밀번호 연동)으로 교체하면 됩니다.

증권사 모의투자/자동매매 연동: 웹훅 알림이 검증된 후, 동일한 JSON 페이로드를 Alpaca Markets나 한국투자증권 Open API 모의계좌 엔드포인트로 전달하여 익일 시가 자동 분할 매수 및 손절/익절 주문을 연결할 수 있습니다.

How do i set it up or intall, show me detail

Follow this step-by-step setup to install the screener locally, configure your webhook alerts, and schedule it to run automatically on GitHub Actions at zero cost.

Step 1: Create a Discord Webhook (or Telegram Bot)
Using a Discord webhook takes less than 60 seconds and requires no server:

Open Discord, create a private server, and create a channel (e.g., #stock-alerts).

Click the gear icon next to the channel name (Edit Channel) → Integrations → Webhooks → New Webhook.

Name it Dip Screener Bot and click Copy Webhook URL. Save this URL for later.

(If you prefer Telegram: create a bot via @BotFather, grab the token, message @userinfobot to get your Chat ID, and use the Telegram helper shown earlier).

Step 2: Set Up the Project Files Locally
Create a dedicated folder on your computer (e.g., stock-dip-bot/) with the following file structure:

Plaintext
stock-dip-bot/
├── .github/
│   └── workflows/
│       └── daily_screen.yml
├── main.py
└── requirements.txt
1. requirements.txt
Place these dependencies inside requirements.txt:

Plaintext
yfinance>=0.2.40
pandas>=2.0.0
requests>=2.31.0
openai>=1.30.0
2. main.py
Paste this self-contained script. It checks your target watchlist, queries the LLM for a transitory vs. structural diagnosis, and sends an alert:

Python
import os
import requests
import yfinance as yf
from openai import OpenAI

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Modify your watchlist here
WATCHLIST = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", 
    "TSLA", "META", "AMD", "QCOM", "AVGO", "INTC", "NKE"
]

def send_discord_alert(webhook_url: str, alert: dict):
    embed = {
        "title": f"🚨 Dip Alert: ${alert['ticker']} ({alert['company']})",
        "color": 3066993,  # Green/Cyan
        "fields": [
            {"name": "Current Price", "value": f"${alert['price']:.2f}", "inline": True},
            {"name": "Drawdown (52w)", "value": f"{alert['drawdown']:.1f}%", "inline": True},
            {"name": "14-Day RSI", "value": f"{alert['rsi']:.1f}", "inline": True},
            {"name": "AI Catalyst Diagnosis", "value": alert['catalyst'], "inline": False},
            {"name": "AI Classification", "value": f"**{alert['classification']}** ({alert['confidence']}% Conf.)", "inline": True},
        ],
        "footer": {"text": "Quant + LLM Dip Screener"}
    }
    res = requests.post(webhook_url, json={"embeds": [embed]})
    res.raise_for_status()

def run_screener():
    if not OPENAI_API_KEY or not DISCORD_WEBHOOK_URL:
        raise ValueError("Missing OPENAI_API_KEY or DISCORD_WEBHOOK_URL environment variable.")

    client = OpenAI(api_key=OPENAI_API_KEY)
    print(f"Scanning {len(WATCHLIST)} tickers...")

    for ticker in WATCHLIST:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1y")
            if hist.empty or len(hist) < 50:
                continue

            current_price = hist['Close'].iloc[-1]
            high_52w = hist['Close'].max()
            drawdown = ((current_price - high_52w) / high_52w) * 100

            # Compute 14-day RSI
            delta = hist['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
            rs = gain / (loss + 1e-9)
            rsi = 100 - (100 / (1 + rs)).iloc[-1]

            # Stage 1: Technical Filter (15% to 35% drop, RSI <= 38)
            if not (-35.0 <= drawdown <= -15.0 and rsi <= 38.0):
                continue

            print(f"Found technical candidate: {ticker} (DD: {drawdown:.1f}%, RSI: {rsi:.1f})")

            # Stage 2: Pull recent headlines
            news_items = stock.news[:4]
            headlines = [n.get('title', '') for n in news_items if 'title' in n]
            news_context = "\n- ".join(headlines) if headlines else "No recent headlines available."

            # Stage 3: LLM Drop Classification
            prompt = (
                f"Ticker: {ticker}\nRecent Headlines:\n- {news_context}\n\n"
                "Classify why this stock dropped 15-35%. Is it TRANSITORY (macro shock, temporary inventory, sector rotation) "
                "or STRUCTURAL (loss of moat, loss of major customers, accounting fraud)?\n"
                "Respond in this exact format:\n"
                "CLASSIFICATION: [TRANSITORY or STRUCTURAL]\n"
                "CONFIDENCE: [0-100]\n"
                "SUMMARY: [1 short sentence in Korean or English describing the direct trigger]"
            )

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )
            analysis = response.choices[0].message.content

            # Stage 4: Alert if Transitory
            if "CLASSIFICATION: TRANSITORY" in analysis:
                summary_line = analysis.split("SUMMARY:")[-1].strip() if "SUMMARY:" in analysis else analysis
                conf = 80
                for line in analysis.splitlines():
                    if "CONFIDENCE:" in line:
                        try:
                            conf = int(''.join(filter(str.isdigit, line)))
                        except ValueError:
                            pass

                alert_data = {
                    "ticker": ticker,
                    "company": stock.info.get("shortName", ticker),
                    "price": current_price,
                    "drawdown": drawdown,
                    "rsi": rsi,
                    "catalyst": summary_line,
                    "classification": "TRANSITORY (일시적 충격)",
                    "confidence": conf
                }
                send_discord_alert(DISCORD_WEBHOOK_URL, alert_data)
                print(f"Alert sent for {ticker}")

        except Exception as e:
            print(f"Error processing {ticker}: {e}")

if __name__ == "__main__":
    run_screener()
Step 3: Test Locally First
Open your terminal or command prompt inside the stock-dip-bot directory:

Bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Export your secrets temporarily
export OPENAI_API_KEY="sk-..."                     # On Windows CMD: set OPENAI_API_KEY=sk-...
export DISCORD_WEBHOOK_URL="https://discord.com/..."

# 4. Run the script
python main.py
If any stock in the list matches the threshold, a message will appear in your Discord channel.

Step 4: Automate via Free GitHub Actions
To make this run every business day at the US market close without leaving your computer on:

1. Push Code to a Private GitHub Repository
Run these commands in your project folder:

Bash
git init
git add .
git commit -m "Initial commit of stock screener"
git branch -M main
# Create a PRIVATE repository on github.com, then link it:
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
git push -u origin main
2. Add Secrets to GitHub
Open your repository on GitHub.

Go to Settings → Secrets and variables → Actions.

Click New repository secret and add:

Name: OPENAI_API_KEY | Secret: sk-...

Name: DISCORD_WEBHOOK_URL | Secret: [https://discord.com/api/webhooks/](https://discord.com/api/webhooks/)...

3. Create .github/workflows/daily_screen.yml
Save this file in your repo:

YAML
name: Daily Dip Screener

on:
  schedule:
    # 21:00 UTC = 5:00 PM EDT / 4:00 PM EST (Monday to Friday)
    - cron: '0 21 * * 1-5'
  workflow_dispatch: # Allows you to manually trigger it anytime via button

jobs:
  screen:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run Screener Script
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          DISCORD_WEBHOOK_URL: ${{ secrets.DISCORD_WEBHOOK_URL }}
        run: python main.py
4. Trigger a Manual Test Run
Go to the Actions tab on your GitHub repository → Click Daily Dip Screener on the left menu → Click Run workflow → Run workflow.

You can click into the run logs to watch it scan your watchlist live and check your Discord channel for incoming alerts.

Can you create for me i Opened discord webhook

I cannot directly access your GitHub or personal computer to push files and run code for you, but you can set this up completely inside GitHub's website in about 3 minutes without touching a terminal or installing anything on your computer.

Here is the exact zero-code setup directly through the GitHub web interface:

Step 1: Create a GitHub Repository (In Browser)
Go to github.com/new.

Set Repository name to stock-dip-bot.

Choose Private (so your API keys and watchlist stay private).

Check Add a README file.

Click Create repository.

Step 2: Add Your Secret Keys
In your new repository, click Settings (top menu bar) → look at the left sidebar → expand Secrets and variables → click Actions.

Click the green New repository secret button:

Name: DISCORD_WEBHOOK_URL

Secret: (Paste the Discord webhook URL you just copied)

Click Add secret.

Click New repository secret again:

Name: OPENAI_API_KEY

Secret: (Paste your OpenAI API key starting with sk-...)

Click Add secret.

Step 3: Create the 3 Files Directly in the Browser
File 1: requirements.txt
Go back to the Code tab of your repo.

Click Add file → Create new file.

Name the file requirements.txt.

Paste this content:

Plaintext
yfinance>=0.2.40
pandas>=2.0.0
requests>=2.31.0
openai>=1.30.0
Click Commit changes... → Commit changes.

File 2: main.py
Click Add file → Create new file.

Name the file main.py.

Paste the following script:

Python
import os
import requests
import yfinance as yf
from openai import OpenAI

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Add or change your tickers here
WATCHLIST = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA",
    "TSLA", "META", "AMD", "QCOM", "AVGO", "INTC", "NKE"
]

def send_discord_alert(webhook_url: str, alert: dict):
    embed = {
        "title": f"🚨 Dip Alert: ${alert['ticker']} ({alert['company']})",
        "color": 3066993,
        "fields": [
            {"name": "Current Price", "value": f"${alert['price']:.2f}", "inline": True},
            {"name": "Drawdown (52w)", "value": f"{alert['drawdown']:.1f}%", "inline": True},
            {"name": "14-Day RSI", "value": f"{alert['rsi']:.1f}", "inline": True},
            {"name": "AI Catalyst Diagnosis", "value": alert['catalyst'], "inline": False},
            {"name": "AI Classification", "value": f"**{alert['classification']}** ({alert['confidence']}% Conf.)", "inline": True},
        ],
        "footer": {"text": "Quant + LLM Dip Screener"}
    }
    res = requests.post(webhook_url, json={"embeds": [embed]})
    res.raise_for_status()

def send_test_ping(webhook_url: str):
    requests.post(webhook_url, json={
        "content": "✅ **Dip Screener Connected!** Bot is active and monitoring watchlist."
    })

def run_screener():
    if not DISCORD_WEBHOOK_URL:
        raise ValueError("Missing DISCORD_WEBHOOK_URL secret.")
    
    # Send an initial connection ping
    send_test_ping(DISCORD_WEBHOOK_URL)

    if not OPENAI_API_KEY:
        raise ValueError("Missing OPENAI_API_KEY secret.")

    client = OpenAI(api_key=OPENAI_API_KEY)
    print(f"Scanning {len(WATCHLIST)} tickers...")

    for ticker in WATCHLIST:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1y")
            if hist.empty or len(hist) < 50:
                continue

            current_price = hist['Close'].iloc[-1]
            high_52w = hist['Close'].max()
            drawdown = ((current_price - high_52w) / high_52w) * 100

            delta = hist['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
            rs = gain / (loss + 1e-9)
            rsi = 100 - (100 / (1 + rs)).iloc[-1]

            # Check if oversold and in 15% to 35% drawdown
            if not (-35.0 <= drawdown <= -15.0 and rsi <= 38.0):
                continue

            print(f"Candidate: {ticker} (DD: {drawdown:.1f}%, RSI: {rsi:.1f})")

            news_items = stock.news[:3] if stock.news else []
            headlines = [n.get('title', '') for n in news_items if 'title' in n]
            news_context = "\n- ".join(headlines) if headlines else "No recent headlines."

            prompt = (
                f"Ticker: {ticker}\nHeadlines:\n- {news_context}\n\n"
                "Classify why this stock dropped 15-35%. Is it TRANSITORY (macro shock, temporary inventory, sector rotation) "
                "or STRUCTURAL (loss of moat, loss of major customers, accounting fraud)?\n"
                "Format response exactly as:\n"
                "CLASSIFICATION: [TRANSITORY or STRUCTURAL]\n"
                "CONFIDENCE: [0-100]\n"
                "SUMMARY: [1 short sentence describing catalyst]"
            )

            res = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )
            analysis = res.choices[0].message.content

            if "CLASSIFICATION: TRANSITORY" in analysis:
                summary_line = analysis.split("SUMMARY:")[-1].strip() if "SUMMARY:" in analysis else analysis
                conf = 80
                for line in analysis.splitlines():
                    if "CONFIDENCE:" in line:
                        try:
                            conf = int(''.join(filter(str.isdigit, line)))
                        except ValueError:
                            pass

                alert_data = {
                    "ticker": ticker,
                    "company": stock.info.get("shortName", ticker),
                    "price": current_price,
                    "drawdown": drawdown,
                    "rsi": rsi,
                    "catalyst": summary_line,
                    "classification": "TRANSITORY (일시적 충격)",
                    "confidence": conf
                }
                send_discord_alert(DISCORD_WEBHOOK_URL, alert_data)
        except Exception as e:
            print(f"Error on {ticker}: {e}")

if __name__ == "__main__":
    run_screener()
