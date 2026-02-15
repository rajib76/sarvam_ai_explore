from sarvamai import SarvamAI
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.markdown import Markdown

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

console = Console()

console.print("\n[bold cyan]🌏 Northern India Tour Planner[/bold cyan]\n")

budget = input("Enter your budget: ")
days = input("Enter the number of days you want to spend in the tour: ")

console.print("\n[yellow]Planning your perfect tour...[/yellow]\n")

response = client.chat.completions(
    messages=[
        {"role": "user", "content": PROMPT.format(budget=budget, days=days)}
    ],
    temperature=0.5,
    top_p=1,
    max_tokens=1000,
)

# Extract the content from the response
if hasattr(response, 'choices') and len(response.choices) > 0:
    content = response.choices[0].message.content
    
    # Render the markdown content beautifully
    markdown = Markdown(content)
    console.print(markdown)
else:
    console.print("[red]Error: Unable to get response from the AI[/red]")
    console.print(response)
