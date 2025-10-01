import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from test_gmail import test_gmail_connection

# Load environment variables
load_dotenv()

class EmailIntelligenceAgent:
    def __init__(self):
        print("🧠 Starting Email Intelligence Agent...")
        
        # Connect to Gmail
        self.service = test_gmail_connection()
        
        # Setup AI brain with OpenRouter - WORKING CONFIG
        self.llm = ChatOpenAI(
            model="google/gemini-2.5-flash-lite-preview-09-2025",
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1",
            max_tokens=1000,
        )
        
        print("✅ Agent ready!")
    
    def test_ai(self):
        """Test that the AI is working"""
        print("🧪 Testing AI connection...")
        try:
            response = self.llm.invoke("Say 'AI is working' in one word.")
            print(f"✅ AI Response: {response.content}")
            return True
        except Exception as e:
            print(f"❌ AI Error: {e}")
            return False
    
    def search_emails(self, query):
        """Search emails using Gmail API"""
        try:
            results = self.service.users().messages().list(
                userId='me', 
                q=query,
                maxResults=10
            ).execute()
            return results.get('messages', [])
        except Exception as e:
            return f"Error searching emails: {e}"
    
    def analyze_recruiters(self):
        """Look for recruiter emails"""
        print("🔍 Analyzing emails for recruiters...")
        
        queries = [
            "recruiter",
            "hiring", 
            "interview",
            "job opportunity",
            "careers",
            "talent acquisition"
        ]
        
        recruiter_emails = []
        for query in queries:
            emails = self.search_emails(query)
            if isinstance(emails, list):
                recruiter_emails.extend(emails)
        
        return recruiter_emails

# Simple test
if __name__ == '__main__':
    agent = EmailIntelligenceAgent()
    
    # Test AI first
    if agent.test_ai():
        recruiters = agent.analyze_recruiters()
        print(f"📨 Found {len(recruiters)} potential recruiter emails!")
        
        # Ask AI about the findings
        if recruiters:
            response = agent.llm.invoke(f"I found {len(recruiters)} potential recruiter emails. Give me a brief analysis of my job search status.")
            print(f"🤖 AI Analysis: {response.content}")
    else:
        print("AI test failed - but Gmail is working!")