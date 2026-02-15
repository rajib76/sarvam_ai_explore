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
You are an expert tour guide and you are going to help me plan a tour to {destination} based on my 
budget and the number of days I want to spend on the tour.

Here is my destination: {destination}
Here is my budget: {budget}
Here is the number of days I want to spend on the tour: {days}

Please provide a detailed day-by-day itinerary including:
- Destinations to visit
- Accommodation recommendations with estimated costs
- Transportation options and costs
- Must-see attractions and experiences
- Food recommendations
- Cost breakdown for each day
- Total estimated cost

"""

console = Console()

console.print("\n[bold cyan]🌏 AI Tour Planner[/bold cyan]\n")
console.print("[dim]Plan your perfect trip to any destination![/dim]\n")

destination = input("Enter your destination: ")
budget = input("Enter your budget (with currency): ")
days = input("Enter the number of days you want to spend: ")

console.print("\n[yellow]Planning your perfect tour...[/yellow]\n")

response = client.chat.completions(
    messages=[
        {"role": "user", "content": PROMPT.format(destination=destination, budget=budget, days=days)}
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
