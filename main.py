import os
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import prompts
client = OpenAI()


api_key = os.getenv("OPENAI_API_KEY")

model = "gpt-3.5-turbo"
temperature = 0.3
max_tokens = 500
topic = "life"

book = ""
file_path = "naval.pdf"

#prompts
system_message = prompts.system_message
prompt = prompts.generate_prompt(book, topic)


with open(file_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    start_page = 23
    end_page = total_pages - 220

    for page_number in range(start_page, end_page):
        page = reader.pages[page_number]
        book += page.extract_text() + " "

print(book)


messages=[
    {"role": "system", "content": system_message},
    {"role": "user", "content": prompt}
]

def get_summary():
   completion = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=temperature,
    max_tokens=max_tokens
    )
   return completion.choices[0].message.content 

print(get_summary())


