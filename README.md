# 🔍 Smart Query

**Smart Query** is a full-stack data analytics project built around the **Chinook** digital media store database. It combines four complementary tools into one suite: an **AI agent** for asking questions in plain English, an interactive **Power BI dashboard** for visual exploration, a **Python notebook** for exploratory data analysis, and a **SQLite database** as the clean relational source of truth underneath it all.

### 🔗 [Live Website](https://smartquery-22ix.onrender.com/)

---

## ⚒️ Project Created By: Pranav Choubey

**LinkedIn -** [Click Here](https://www.linkedin.com/in/pranavchoubey89/)
**GitHub -** [Click Here](https://github.com/PRANAV4248)

*Your feedback & LinkedIn DMs are much appreciated!* 😊

---

## 🧱 The Four Pillars of Smart Query

This project analyses the same Chinook database from four complementary angles — each stack plays to its own strengths:

| Stack                              | Role                     | What it's good for                                     |
| ---------------------------------- | ------------------------ | ------------------------------------------------------ |
| 🤖**AI (Smart Query Agent)** | Conversational interface | Instant, plain-English answers — no code required     |
| 📊**Power BI**               | Interactive dashboard    | Visual, drill-down exploration for business users      |
| 🐍**Python (EDA)**           | Notebook-based analysis  | Deeper statistical exploration & custom visualizations |
| 🗄️**SQL (SQLite)**         | Data layer               | The single source of truth all three tools query       |

---

## 🤷 1. AI — The Smart Query Agent

Imagine you have a music store database (`Chinook`) with thousands of records about artists, albums, invoices, and customers. Instead of writing code, you just **ask**.

Smart Query acts as a bridge 🌉 between you and your data. You ask a question, and the AI:

1. **Understands** what you are looking for. 💭
2. **Writes** the safe SQL to find it. ⌨️
3. **Explains** the answer back to you clearly. 🗣️

<img width="800" alt="Smart Query chat interface" src="images\Website Preview.png" />

### ✨ Why You'll Love It

* 🗣️ **Just Ask**: "Who bought the most rock music?" is all you need to say.
* 🛡️ **Safe & Secure**: The AI is strictly **read-only**. It can *look* at data, but it can never *delete* or *change* it.
* ⚡ **Instant Insights**: Get answers in seconds, not hours.
* 💬 **Chat Naturally**: It remembers context! Ask "Who is the top artist?" and then follow up with "What are their top 3 songs?"

### 🎮 How to Use It

Once the app is running in your browser, you'll see a clean chat interface. Click one of the **Quick Starters** to jump right in:

* *🔍 Tell me about the database*
* *📋 List Tables*
* *🎸 Playlists*
* *🛒 Top customer*

Or type your own questions:

**🎵 For Music Analysis:**

* *"Show me the top 5 selling tracks of all time."*
* *"List all albums by AC/DC."*
* *"Which genre has the most tracks?"*

**🌍 For Customer Insights:**

* *"Which countries have the most invoices?"*
* *"Who is the top customer by total spending?"*
* *"How many customers are from Brazil?"*

All the SQL writing and execution happens in the background 🕵️‍♂️ — you just get the answer.

---

## 📊 2. Power BI — Interactive Dashboard

For anyone who wants to explore the numbers visually, the project includes a 4-page Power BI dashboard built on top of the same Chinook data.

### 🏠 Overview

Headline KPIs at a glance — total sales, total orders, total customers, average order value, and countries served — plus a world map showing where sales are coming from.

<img width="800" alt="Overview page" src="images\Overview.png" />

### 💰 Sales Analysis

Breaks down total sales by genre, by employee, and over time (by year and by month) to spot seasonality and top-performing categories/staff.

<img width="800" alt="Sales Analysis page" src="images\Sales analysis.png" />

### 🙋 Customer Insights

Surfaces the highest-spending customers, average spend per customer, and how top customers' spending trends across years.

<img width="800" alt="Customer Insights page" src="images\Customer insights.png" />

### 🌍 Country Analysis

Total sales by country and genre, a choropleth map of sales by country, and a gauge comparing average sales per country against target.

<img width="800" alt="Country Analysis page" src="images\Country analysis.png" />

**Highlights across the dashboard:**

- 💵 **$2.33K** total sales across **412 orders** from **59 customers** in **24 countries**
- 🇺🇸 USA is the highest-selling country; Argentina the lowest
- 🎸 Rock is the best-selling genre by a wide margin
- 👤 Helena Holý is the top customer by total spend ($49.62)

---

## 🐍 3. Python — Exploratory Data Analysis (EDA)

A companion Jupyter notebook (`EDA.ipynb`) explores the Chinook database directly with **pandas**, **matplotlib**, and **seaborn** — useful for anyone who wants to see the raw analytical process behind the dashboard, or extend it further.

**What it covers:**

- Connecting to the SQLite database and loading every table into pandas DataFrames
- Table-by-table previews, schema info (`.info()`), and summary statistics (`.describe()`)
- Total store revenue
- Number of customers by country
- Revenue by country (bar chart + pie chart revenue share)
- Revenue by media type
- Monthly revenue trend over time
- Revenue by genre and country, visualized as a heatmap

This notebook is a good starting point if you want to prototype a new metric before adding it to the Power BI dashboard or teaching the AI agent about it.

---

## 🗄️ 4. SQL — The Data Layer (SQLite)

All three tools above read from the same **Chinook SQLite database** (`Chinook.db`), which models a digital media store with the following core tables and relationships:

- `Artist` → `Album` → `Track` (music catalog)
- `Genre` and `MediaType` (track classification)
- `Customer` → `Invoice` → `InvoiceLine` (purchases)
- `Employee` (sales staff, linked to customers)
- `Playlist` → `PlaylistTrack` (playlists)

<img width="800" alt="Tables and Relationships" src="images\Tables Relationships.png" />

Keeping one clean relational schema at the center means the AI agent, the Power BI dashboard, and the Python notebook are all always answering questions from the **same ground truth**.

---

## 🛠️ Tech Stack Used

| Layer                        | Tools                                    |
| ---------------------------- | ---------------------------------------- |
| **AI / Agent**         | Python & LangChain 🦜, Groq (Kimi-k2) ⚡ |
| **Chat Interface**     | Chainlit ⛓️                            |
| **BI Dashboard**       | Power BI 📊                              |
| **EDA / Data Science** | Python 🐍, pandas, matplotlib, seaborn   |
| **Database**           | SQLite 🗄️                              |
| **Package Manager**    | UV 📦                                    |
| **Deployment**         | Render 🚀                                |

---

Made with 🖤 by **[Pranav Choubey](https://github.com/PRANAV4248)**
