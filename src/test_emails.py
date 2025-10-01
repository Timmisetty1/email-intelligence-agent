from test_gmail import test_gmail_connection

def list_recent_emails():
    print("📨 Reading your recent emails...")
    
    # Get the Gmail service
    service = test_gmail_connection()
    
    # Get the latest 5 emails
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])
    
    if not messages:
        print("No messages found.")
        return
    
    print(f"\n📧 Found {len(messages)} recent emails:")
    
    for i, message in enumerate(messages, 1):
        # Get full message details
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        
        # Extract headers
        headers = msg['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown Sender')
        
        print(f"\n{i}. From: {sender}")
        print(f"   Subject: {subject}")

if __name__ == '__main__':
    list_recent_emails()