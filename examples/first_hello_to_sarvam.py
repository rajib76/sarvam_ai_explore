from sarvamai import SarvamAI
from dotenv import load_dotenv
import os

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY"),
)

PROMPT = """
you are an expert tour guide and you are going to help me plan a tour in Northern India based on my 
budget and the number of days I want to spend in the tour.

Here is my budget: {budget}
Here is the number of days I want to spend in the tour: {days}

"""

budget= input("Enter your budget: ")
days= input("Enter the number of days you want to spend in the tour: ")


response = client.chat.completions(
    messages=[
        {"role": "user", "content": PROMPT.format(budget=budget, days=days)}
    ],
    temperature=0.5,
    top_p=1,
    max_tokens=1000,
)
print(response)
