from telethon.sync import TelegramClient
import pandas as pd

def scrape_telegram(api_keys, channel_name, limit=100):
    # Authenticate using Telethon
    client = TelegramClient('session_name', api_keys['api_id'], api_keys['api_hash'])
    client.start()
    
    messages = client.get_messages(channel_name, limit=limit)
    message_data = [
        {
            'message': msg.text,
            'created_at': msg.date,
            'sender': msg.sender_id
        } for msg in messages
    ]
    
    # Save to CSV
    df = pd.DataFrame(message_data)
    df.to_csv('../data/telegram_data.csv', index=False)
    print("Telegram data saved to `data/telegram_data.csv`")

# Replace with your API keys
api_keys = {
    'api_id': 'YOUR_API_ID',
    'api_hash': 'YOUR_API_HASH'
}

scrape_telegram(api_keys, channel_name="stock_predictions_channel", limit=100)
