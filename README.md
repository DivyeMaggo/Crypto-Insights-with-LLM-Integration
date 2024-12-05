# Crypto Insights and Trends Analyzer with LLM Integration

A terminal-based web app that provides cryptocurrency insights, featuring real-time data from CoinCAP API, AI-generated summaries via Google GEMINI, and interactive trend analysis with yearly price visualizations. This project supports 1,000 cryptocurrencies and 2,000 responses per page upon requests.

## Features

- Real-time cryptocurrency data from the CoinCAP API.
- Fetch data for up to 1,000 cryptocurrencies.
- Handles up to 2,000 responses per page upon requests.
- AI-generated summaries using OpenAI's language model.
- Interactive trend analysis with yearly price visualizations.
- Easy to use from the terminal by running `python main.py`.

## Installation

### Prerequisites

Before running the project, ensure that you have the following installed:

- Python 3.11

### Installing

1. Clone the repository:
    ```bash
    git clone https://github.com/DivyeMaggo/Crypto-Insights-with-LLM-Integration
    ```

2. Navigate to the project directory:
    ```bash
    cd crypto-insights-analyzer
    ```

3. No dependencies required.


4. Ensure you have a valid API key for GEMINI_API_KEY and CoinCAP API if needed. Add them to your environment variables or include them in the configuration file as described in the next section.

## Configuration

1. Create your own GEMINI api key and add in the `.env` file in the root of the project to store your API keys:
    ```
    GEMINI_API_KEY=your-openai-api-key
    ```


## Usage

To run the application, enter the directory and simply execute the following command in your terminal:

```bash
python main.py
```
