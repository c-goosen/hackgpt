import typer
from rich import print
from dotenv import load_dotenv
import openai
import os

load_dotenv()
# openai.id
openai.api_key = os.getenv("OPENAI_API_KEY", "")

app = typer.Typer()

@app.command()
def main():
    print("[bold green]Welcome to hackegpt! hackgpt is your pentesting/hacking butler[/bold green] :boom:")

    # print("Welcome to hackedgpt")

@app.command()
def init():
    openapi_org_id = typer.prompt("Add a openapi Org ID to your config:")
    openapi_key = typer.prompt("Add a openapi API key to your config:")
    print(f"Org ID: {openapi_org_id}")
    print(f"Org API Key: xxxxx")

@app.command()
def generatePrompt():
    prompt_context="Write a prompt for openAI with the following input:\n"
    prompt_input = typer.prompt("Ask a question:")
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=str(prompt_context+prompt_input),
    temperature=0,
    max_tokens=os.getenv("OPENAI_MAX_TOKENS",200)
    )
    choices = response.get('choices')
    print("0 -> Skip sending back to openAI")
    for x in range(0, len(choices)):
        print(f"{x+1} -> {choices[x].get('text').strip()}")
    continue_options = typer.prompt("Ask openAI with this prompt Y/N:")
    if (continue_options !="0"):
        complete_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=str(choices[int(continue_options)-1]),
        temperature=0,
        max_tokens=os.getenv("OPENAI_MAX_TOKENS",200)
        )
        complete_choices = complete_response.get('choices')
        for x in range(0, len(complete_choices)):
            print(f"{complete_choices[x].get('text').strip()}")

        
if __name__ == "__main__":
    app()
    # typer.run(main)
