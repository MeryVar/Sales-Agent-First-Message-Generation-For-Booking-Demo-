"""
Mock data scenarios for testing all variations of the sales agent system.
This file contains comprehensive test cases covering:
- Basic scenarios (email/SMS with/without sender)
- Edge cases (empty data, invalid links, special characters)
- Industry-specific scenarios
- Contact name variations
- Knowledge base variations
- Chat history variations
- Extreme edge cases
"""

MOCK_DATA = {
"scenario": {
    "global_context": "EngageBot helps local service businesses improve appointment booking through conversational AI and automated reminders.",
    "company_info": "EngageBot - AI appointment assistant. Founded 2021. 300+ local businesses onboarded. Based in Denver.",
    "knowledge_base": "Case study: DentalPlus reduced no-shows by 45% and increased bookings by 60% using our AI bot. Integrates with Google Calendar, Calendly, SMS/Email. Starting at $79/month.",  # None
    "contact_info": "Dr. Élodie McAllister, Founder at WellnessCare Group. Phone: +1-555-2345. Email: elodie@wellnesscare.com. Boutique wellness clinic in San Diego.",
    "chat_history": "No contact history. Reached via industry mailing list.",
    "calendly_link": "https://calendly.com/engagebot-demo",
    "sender_info": "Michael Thompson",
    "channel": "sms" # "email"
}
}