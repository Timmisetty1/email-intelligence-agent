from email_agent import EmailIntelligenceAgent

# Test the basic agent
agent = EmailIntelligenceAgent()
print("🤖 AI Agent initialized successfully!")

# Test recruiter detection
recruiters = agent.analyze_recruiters()
print(f"📨 Found {len(recruiters)} potential recruiter emails!")