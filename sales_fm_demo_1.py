import openai
import os
from typing import Dict, Any, Optional
import re
from mock_data_1 import MOCK_DATA

# =============================================================================
# CORE PROMPTS
# =============================================================================

SALES_AGENT_PROMPT = """
You are a professional sales representative focused on building relationships and delivering value.

## CORE OBJECTIVES
• Build Trust & Relationships: Establish genuine connections, understand customer needs, deliver personalized solutions
• Drive Value: Demonstrate product expertise, highlight unique benefits, address pain points, show clear ROI  
• Guide Sales Process: Qualify prospects, handle objections professionally, close deals naturally

## KEY RESPONSIBILITIES
• Product Knowledge: Only present factual information from approved sources
• Communication: Adapt style to audience needs without fabrication
• Problem-Solving: Identify and address customer challenges using available facts
• Objection Handling: Address concerns with empathy using factual information
• Process Management: Guide customers through sales journey based on factual information

## ESSENTIAL BEHAVIOR
• Maintain professional, human-like interaction
• Focus on customer needs over sales targets
• Build trust through transparency and factual information
• Only use information from approved sources - NO hallucinations
• Remember: You are a professional building relationships

## CONTEXT INFORMATION
Global Context: {global_context}
Company Information: {company_info}
Knowledge Base: {knowledge_base}
"""

PERSONALIZATION_PROMPT = """
## CONTACT PERSONALIZATION
Contact Details: {contact_info}
Conversation History: {chat_history}
Calendly Link: {calendly_link}
Sender Information: {sender_info}

## PERSONALIZATION INSTRUCTIONS
• Address the contact appropriately based on available information
• If contact name is provided, use it naturally (e.g., "Hi Sarah", "Hello Mike")
• If no contact name is available, use friendly alternatives like "Hi there", "Hello", or "Hi dear"
• For message signature: ONLY use sender name if provided in sender_info. If sender_info is empty, end with company name only
• NEVER EVER use placeholders like [YOUR NAME], [CONTACT NAME], [Your Actual Name], or any brackets with names
• Reference relevant conversation history for continuity
• Maintain professional tone while being personable
• Ensure all responses are relevant to contact's specific context
• ALWAYS include the provided Calendly link in every message
• NEVER mention discounts, percentages off, or specific promotional numbers
"""

FIRST_MESSAGE_EMAIL_PROMPT = """
## EMAIL OUTREACH TASK
Create a professional first outreach email following these guidelines:

**EMAIL STRUCTURE:**
• Subject Line: Concise, personalized, value-focused (under 50 characters)
• Greeting: Use recipient's name if available, otherwise use "Hi there" or "Hello"
• Opening: Brief, personalized introduction (1-2 sentences)
• Value Proposition: 1-2 sentences on how you can help their specific situation
• Social Proof: Brief relevant success mention from knowledge base (if available)
• Call to Action: Clear next step with meeting request
• Closing: "Best regards," or "Looking forward to connecting!"
• Signature: ONLY include sender name if provided in sender_info, otherwise just company name
• MUST Include: The exact Calendly link provided

**SIGNATURE RULES:**
• If sender_info contains a name: "Best regards,\nJohn Smith\nCompany Name"
• If sender_info is empty: "Best regards,\nCompany Name"
• NEVER use [YOUR NAME] or any placeholder names

**CRITICAL REQUIREMENTS:**
• Keep entire email under 150 words
• Use clear, direct language
• Address recipient directly - NO placeholders of any kind
• Reference specific pain points relevant to their industry/role
• Avoid spam trigger words
• Professional tone throughout
• NEVER mention discounts, percentages off, or promotional pricing
• ALWAYS include the provided Calendly link
• NO name placeholders anywhere in the message

**OUTPUT FORMAT:**
Subject: [Subject line]
---
[Email body]
"""

FIRST_MESSAGE_SMS_PROMPT = """
## SMS OUTREACH TASK
Create a professional first outreach SMS following these guidelines:

**SMS STRUCTURE:**
• Greeting with contact name if available, otherwise "Hi there" or "Hello"
• Brief introduction: "This is [sender name] from [company]" OR "This is [company]" if no sender name
• Clear value proposition (1 sentence)
• Call to action with meeting request
• MUST Include: The exact Calendly link provided

**INTRODUCTION RULES:**
• If sender_info contains name: "Hi Mike, this is John from CloudSync Pro"
• If sender_info is empty: "Hi Mike, this is CloudSync Pro"
• NEVER use [YOUR NAME] or any placeholder names

**CRITICAL REQUIREMENTS:**
• Keep under 160 characters total
• Direct and concise language
• Address recipient appropriately - NO placeholders of any kind
• One clear call-to-action
• Professional but friendly tone
• ALWAYS include the provided Calendly link
• NEVER mention discounts, percentages off, or promotional pricing
• NO name placeholders anywhere in the message

**OUTPUT FORMAT:**
[SMS message - single paragraph, under 160 characters]
"""

HALLUCINATION_PROMPT = """
## CRITICAL CONSTRAINT: ZERO HALLUCINATIONS

You MUST NOT invent, assume, or imagine ANY information not explicitly available in:
1. Chat History: {chat_history}
2. Knowledge Base: {knowledge_base}  
3. Global Context: {global_context}
4. Company Information: {company_info}
5. Contact Information: {contact_info}
6. Calendly Link: {calendly_link}
7. Sender Information: {sender_info}

**STRICT RULES:**
• 0% hallucination tolerance - no guesses, assumptions, or creative additions
• If information is NOT in provided sources, respond: "I don't have that information available, but I can verify and follow up with you."
• Only use factual information from approved sources
• Do not speculate or fill gaps with assumptions
• NEVER EVER use placeholders like [YOUR NAME], [CONTACT NAME], [Your Actual Name], or any name placeholders
• If sender name is not provided in sender_info, simply omit it from signature or use company name only
• ALWAYS include the provided Calendly link
• NEVER mention discounts or promotional pricing not explicitly mentioned in sources

**CRITIQUE TASK:**
Review this initial response for any information not found in the provided sources:

**INITIAL RESPONSE:**
{initial_answer}

**CRITIQUE INSTRUCTIONS:**
1. Identify any claims not supported by provided sources
2. Flag potential hallucinations or assumptions
3. Check for ANY placeholder names (including [YOUR NAME], [Your Actual Name], [NAME], etc.)
4. Verify no unauthorized discounts or promotional pricing mentioned
5. Ensure Calendly link is included correctly
6. If sender name is not provided in sender_info, ensure no name placeholders are used anywhere
7. Provide a corrected version that only uses verified information
8. Maintain the same format and effectiveness while ensuring 100% accuracy
9. Remove ALL placeholder names and brackets with names

**OUTPUT FORMAT:**
CRITIQUE: [List any issues found]
---
CORRECTED VERSION: [Improved message using only verified information with NO placeholders]
"""

# =============================================================================
# COMPOSITE PROMPTS
# =============================================================================

FULL_SALES_PROMPT_FOR_DEMO = """
{sales_agent_prompt}

{personalization_prompt}

{outreach_prompt}

Based on all the above context and guidelines, generate the appropriate first outreach message.
"""

CRITIQUE_PROMPT = """
{sales_agent_prompt}

{personalization_prompt}

{hallucination_prompt}
"""


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def extract_contact_name(contact_info: str) -> str:
    """Extract and format contact name from contact info, return appropriate greeting if no name found."""
    if not contact_info:
        return "Hi there"

    # Look for common name patterns
    name_patterns = [
        r'([A-Z][a-z]+\s+[A-Z][a-z]+)',  # First Last
        r'([A-Z][a-z]+)\s+[A-Z]\.',  # First M.
        r'([A-Z][a-z]+)',  # Just first name
    ]

    for pattern in name_patterns:
        match = re.search(pattern, contact_info)
        if match:
            full_name = match.group(1)
            first_name = full_name.split()[0]
            return f"Hi {first_name}"

    # If no name found, use friendly alternative
    return "Hi there"


def validate_calendly_link(calendly_link: str) -> str:
    """Validate and return the Calendly link."""
    if not calendly_link or not calendly_link.startswith('http'):
        return "https://calendly.com/demo-booking"  # Default fallback
    return calendly_link


# =============================================================================
# FORMATTING FUNCTIONS
# =============================================================================

def format_sales_prompt(global_context="", company_info="", knowledge_base=""):
    """Format the core sales agent prompt with context information."""
    return SALES_AGENT_PROMPT.format(
        global_context=global_context,
        company_info=company_info,
        knowledge_base=knowledge_base
    )


def format_personalization_prompt(contact_info="", chat_history="", calendly_link="", sender_info=""):
    """Format the personalization prompt with contact and conversation details."""
    validated_link = validate_calendly_link(calendly_link)
    return PERSONALIZATION_PROMPT.format(
        contact_info=contact_info,
        chat_history=chat_history,
        calendly_link=validated_link,
        sender_info=sender_info
    )


def format_outreach_prompt(channel="email"):
    """Format the appropriate outreach prompt based on channel."""
    if channel.lower() == "sms":
        return FIRST_MESSAGE_SMS_PROMPT
    else:
        return FIRST_MESSAGE_EMAIL_PROMPT


def format_full_sales_prompt(global_context="", company_info="", knowledge_base="",
                             contact_info="", chat_history="", calendly_link="", sender_info="", channel="email"):
    """Format the complete sales prompt for demo purposes."""
    sales_prompt = format_sales_prompt(global_context, company_info, knowledge_base)
    personalization_prompt = format_personalization_prompt(contact_info, chat_history, calendly_link, sender_info)
    outreach_prompt = format_outreach_prompt(channel)

    return FULL_SALES_PROMPT_FOR_DEMO.format(
        sales_agent_prompt=sales_prompt,
        personalization_prompt=personalization_prompt,
        outreach_prompt=outreach_prompt
    )


def format_critique_prompt(global_context="", company_info="", knowledge_base="",
                           contact_info="", chat_history="", calendly_link="", sender_info="", initial_answer=""):
    """Format the critique prompt to review and improve initial responses."""
    sales_prompt = format_sales_prompt(global_context, company_info, knowledge_base)
    personalization_prompt = format_personalization_prompt(contact_info, chat_history, calendly_link, sender_info)
    validated_link = validate_calendly_link(calendly_link)

    hallucination_prompt = HALLUCINATION_PROMPT.format(
        chat_history=chat_history,
        knowledge_base=knowledge_base,
        global_context=global_context,
        company_info=company_info,
        contact_info=contact_info,
        calendly_link=validated_link,
        sender_info=sender_info,
        initial_answer=initial_answer
    )

    return CRITIQUE_PROMPT.format(
        sales_agent_prompt=sales_prompt,
        personalization_prompt=personalization_prompt,
        hallucination_prompt=hallucination_prompt
    )


# =============================================================================
# OPENAI CLIENT WRAPPER
# =============================================================================

class OpenAIClient:
    """OpenAI API client wrapper for sales agent pipeline."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize OpenAI client with API key."""
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass it directly.")

        openai.api_key = self.api_key

    def count_tokens(self, text: str) -> int:
        """Count tokens in a text string using tiktoken."""
        try:
            import tiktoken
            encoding = tiktoken.encoding_for_model("gpt-4o")
            return len(encoding.encode(text))
        except ImportError:
            # Fallback method if tiktoken is not installed
            # This is a rough estimate (1 token ≈ 4 chars)
            return len(text) // 4
        except Exception as e:
            print(f"Token counting error: {e}")
            return len(text) // 4  # Fallback to rough estimate

    def generate(self, prompt: str, model: str = "gpt-4o", temperature: float = 0.7, max_tokens: int = 500) -> dict:
        """Generate response using OpenAI API. Returns response text and token counts."""
        try:
            # Count prompt tokens
            prompt_tokens = self.count_tokens(prompt)

            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a professional sales representative."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )

            response_text = response.choices[0].message.content.strip()

            # Get completion tokens from API response if available, otherwise count
            if hasattr(response, 'usage') and hasattr(response.usage, 'completion_tokens'):
                completion_tokens = response.usage.completion_tokens
            else:
                completion_tokens = self.count_tokens(response_text)

            # Get total tokens from API response if available
            if hasattr(response, 'usage') and hasattr(response.usage, 'total_tokens'):
                total_tokens = response.usage.total_tokens
            else:
                total_tokens = prompt_tokens + completion_tokens

            return {
                "text": response_text,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens
            }
        except Exception as e:
            print(f"OpenAI API Error: {e}")
            error_msg = f"Error generating response: {e}"
            return {
                "text": error_msg,
                "prompt_tokens": self.count_tokens(prompt),
                "completion_tokens": 0,
                "total_tokens": self.count_tokens(prompt)
            }


# =============================================================================
# LLM CHAIN PIPELINE
# =============================================================================

class SalesAgentPipeline:
    """Pipeline for generating and critiquing sales messages using OpenAI."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize with OpenAI client."""
        self.openai_client = OpenAIClient(api_key)

    def generate_sales_message(self, scenario_data: Dict[str, Any]) -> dict:
        """Generate initial sales message using FULL_SALES_PROMPT_FOR_DEMO."""
        prompt = format_full_sales_prompt(**scenario_data)

        print("Generating initial sales message...")
        print("Using FULL_SALES_PROMPT_FOR_DEMO chain")

        response = self.openai_client.generate(
            prompt=prompt,
            temperature=0.7,
            max_tokens=400 if scenario_data.get('channel') == 'email' else 150
        )
        return response

    def critique_and_improve(self, initial_answer: str, scenario_data: Dict[str, Any]) -> dict:
        """Critique initial response using CRITIQUE_PROMPT and provide improved version."""
        critique_prompt = format_critique_prompt(
            global_context=scenario_data.get('global_context', ''),
            company_info=scenario_data.get('company_info', ''),
            knowledge_base=scenario_data.get('knowledge_base', ''),
            contact_info=scenario_data.get('contact_info', ''),
            chat_history=scenario_data.get('chat_history', ''),
            calendly_link=scenario_data.get('calendly_link', ''),
            sender_info=scenario_data.get('sender_info', ''),
            initial_answer=initial_answer
        )

        print("Critiquing and improving message...")
        print("Using CRITIQUE_PROMPT chain")

        response = self.openai_client.generate(
            prompt=critique_prompt,
            temperature=0.3,  # Lower temperature for critique to be more analytical
            max_tokens=600
        )
        return response

    def run_full_pipeline(self, scenario_name: str = "basic_email_no_sender") -> Dict[str, Any]:
        """Run complete pipeline: FULL_SALES_PROMPT_FOR_DEMO → CRITIQUE_PROMPT."""

        if scenario_name not in MOCK_DATA:
            raise ValueError(f"Scenario '{scenario_name}' not found. Available: {list(MOCK_DATA.keys())}")

        scenario_data = MOCK_DATA[scenario_name]
        channel = scenario_data.get('channel', 'email')

        print(f" Starting Sales Agent Pipeline for {scenario_name}")
        print(f" Channel: {channel.upper()}")
        print(f" Calendly Link: {scenario_data.get('calendly_link', 'Not provided')}")
        print(f" Sender: {scenario_data.get('sender_info', 'Not provided - will use company only')}")
        print("=" * 60)

        # Step 1: Generate initial sales message using FULL_SALES_PROMPT_FOR_DEMO
        initial_response = self.generate_sales_message(scenario_data)
        initial_message = initial_response["text"]
        initial_tokens = initial_response["total_tokens"]
        initial_prompt_tokens = initial_response["prompt_tokens"]
        initial_completion_tokens = initial_response["completion_tokens"]

        print("\n✅ Initial message generated!")
        print(f" Tokens: {initial_completion_tokens} (completion) / {initial_prompt_tokens} (prompt) / {initial_tokens} (total)")
        print("-" * 40)

        # Step 2: Critique and improve using CRITIQUE_PROMPT
        final_response = self.critique_and_improve(initial_message, scenario_data)
        final_message = final_response["text"]
        final_tokens = final_response["total_tokens"]
        final_prompt_tokens = final_response["prompt_tokens"]
        final_completion_tokens = final_response["completion_tokens"]

        print("\n✅ Message critiqued and improved!")
        print(f" Tokens: {final_completion_tokens} (completion) / {final_prompt_tokens} (prompt) / {final_tokens} (total)")
        print("=" * 60)

        # Calculate total tokens for the entire pipeline
        total_pipeline_tokens = initial_tokens + final_tokens

        return {
            "scenario": scenario_name,
            "channel": channel,
            "contact": scenario_data.get('contact_info', ''),
            "calendly_link": scenario_data.get('calendly_link', ''),
            "sender": scenario_data.get('sender_info', ''),
            "initial_message": initial_message,
            "critique_and_final": final_message,
            "token_counts": {
                "initial_message": {
                    "prompt": initial_prompt_tokens,
                    "completion": initial_completion_tokens,
                    "total": initial_tokens
                },
                "critique_and_final": {
                    "prompt": final_prompt_tokens,
                    "completion": final_completion_tokens,
                    "total": final_tokens
                },
                "pipeline_total": total_pipeline_tokens
            },
            "pipeline_steps": [
                "1. FULL_SALES_PROMPT_FOR_DEMO → Generated initial message",
                "2. CRITIQUE_PROMPT → Reviewed and improved message"
            ]
        }


# =============================================================================
# DEMO FUNCTIONS
# =============================================================================

def run_demo_scenario(scenario_name: str, api_key: Optional[str] = None):
    """Run a specific demo scenario."""
    try:
        pipeline = SalesAgentPipeline(api_key)
        result = pipeline.run_full_pipeline(scenario_name)

        print(f"\n RESULTS for {scenario_name}:")
        print(f" Channel: {result['channel'].upper()}")
        print(f" Contact: {result['contact']}")
        print(f" Calendly Link: {result['calendly_link']}")
        print(f" Sender: {result['sender'] if result['sender'] else 'Company only'}")

        print(f"\n INITIAL MESSAGE:")
        print("-" * 40)
        print(result['initial_message'])

        print(f"\n CRITIQUE & FINAL MESSAGE:")
        print("-" * 40)
        print(result['critique_and_final'])

        return result

    except Exception as e:
        print(f" Error running demo: {e}")
        return None


def run_all_scenarios(api_key: Optional[str] = None):
    """Run all available demo scenarios."""
    print("🚀 Running all demo scenarios...")

    results = {}
    for scenario_name in MOCK_DATA.keys():
        print(f"\n{'=' * 60}")
        print(f" RUNNING: {scenario_name}")
        print(f"{'=' * 60}")

        result = run_demo_scenario(scenario_name, api_key)
        if result:
            results[scenario_name] = result

        print(f"\n⏳ Waiting 2 seconds before next scenario...")
        import time
        time.sleep(2)

    return results


def show_available_scenarios():
    """Display all available mock scenarios."""
    print(" Available Demo Scenarios:")
    print("=" * 40)

    for name, data in MOCK_DATA.items():
        print(f"\n🔹 {name}:")
        print(f"    Channel: {data['channel'].upper()}")
        print(f"    Company: {data['company_info'].split('.')[0] if data.get('company_info') else 'Not provided'}")
        print(f"    Contact: {data['contact_info'].split('.')[0] if data.get('contact_info') else 'Not provided'}")
        print(f"    Calendly: {data['calendly_link'] if data.get('calendly_link') else 'Not provided'}")
        print(f"    Sender: {data['sender_info'] if data['sender_info'] else 'Company only'}")


def test_specific_scenarios(scenario_list: list, api_key: Optional[str] = None):
    """Test specific scenarios from a list."""
    print(f" Testing {len(scenario_list)} specific scenarios...")

    results = {}
    for scenario_name in scenario_list:
        if scenario_name not in MOCK_DATA:
            print(f"  Scenario '{scenario_name}' not found. Skipping...")
            continue

        print(f"\n{'=' * 60}")
        print(f" TESTING: {scenario_name}")
        print(f"{'=' * 60}")

        result = run_demo_scenario(scenario_name, api_key)
        if result:
            results[scenario_name] = result

        print(f"\n⏳ Waiting 1 second before next scenario...")
        import time
        time.sleep(1)

    return results


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🤖 Sales Agent Pipeline with OpenAI Integration")
    print("=" * 50)

    # Show available scenarios
    show_available_scenarios()

    print(f"\n{'=' * 50}")
    print("🚀 DEMO EXECUTION")
    print(f"{'=' * 50}")


    API_KEY = '...'

    try:
        # Test basic scenarios
        basic_scenarios = [
            "basic_email_no_sender",
            "basic_sms_with_sender",
            "basic_email_with_sender",
            "basic_sms_no_sender"
        ]

        print(" Testing basic scenarios...")
        basic_results = test_specific_scenarios(basic_scenarios, API_KEY)

        # Test edge cases
        print(f"\n{'=' * 60}")
        print(" Testing edge cases...")
        edge_cases = [
            "minimal_all_empty",
            "invalid_calendly_link",
            "no_contact_name_email",
            "special_characters_in_names"
        ]
        edge_results = test_specific_scenarios(edge_cases, API_KEY)

        # Uncomment to run ALL scenarios:
        # print(f"\n{'=' * 60}")
        # print("🚀 Running ALL scenarios...")
        # all_results = run_all_scenarios(API_KEY)

        print("\n✅ Demo completed successfully!")

    except Exception as e:
        print(f" Demo failed: {e}")
        print("\n Make sure to:")
        print("   • Set your OpenAI API key in the API_KEY variable")
        print("   • Or set environment variable: export OPENAI_API_KEY='your-key-here'")
        print("   • Ensure mock_data.py is in the same directory")