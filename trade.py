// using Twitch chat bot to re
import irc.bot
import requests
import yfinance as yf

# Twitch IRC details
username = 'your_username'  # Your Twitch username
token = 'your_oauth_token'  # Your OAuth token generated from https://twitchapps.com/tmi/
channel = '#channel_name'   # The channel you want to join, e.g., '#twitch'

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, username, token):
        self.token = token
        self.channel = channel
        self.irc_token = f"oauth:{token}"
        self.server = 'irc.chat.twitch.tv'
        self.port = 6667
        self.username = username

        # Connect to Twitch IRC
        server = irc.bot.ServerSpec(self.server, self.port, self.irc_token)
        super().__init__([server], self.username, self.username)

    def on_welcome(self, connection, event):
        # Join the specified channel
        connection.join(self.channel)
        print(f"Joined {self.channel}")

    def on_pubmsg(self, connection, event):
        # Display received messages
        message = event.arguments[0]
        username = event.source.split('!')[0]
        print(f"{username}: {message}")

if __name__ == "__main__":
    bot = TwitchBot(channel, username, token)
    bot.start()


def get_trading_symbols():
    # List of company tickers
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']  # Add more symbols as needed

    symbols = {}
    for ticker in tickers:
        try:
            company = yf.Ticker(ticker)
            name = company.info['longName']
            symbols[ticker] = name
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    
    return symbols

if __name__ == "__main__":
    trading_symbols = get_trading_symbols()
    for symbol, name in trading_symbols.items():
        print(f"Symbol: {symbol}, Name: {name}")
