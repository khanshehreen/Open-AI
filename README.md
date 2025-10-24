🧠 Open-AI Text Summarizer

A Python project to extract and summarize insights from a PDF manuscript using OpenAI's GPT models.  
This tool reads a PDF, applies custom prompts, and generates concise topic-based summaries.

---
🚀 Features

- Extracts text from a PDF (`naval.pdf`) within a defined page range  
- Uses modular prompts from `prompts.py` to guide summarization  
- Generates summaries focused on a given topic (default: `life`)  
- Outputs clear, concise summaries to the console  

---

Project Structure

Open-AI/
│
├── main.py        # Main script to generate summary
├── prompts.py     # Custom prompt definitions
├── naval.pdf      # PDF manuscript for summarization
├── .env           # Environment file for OpenAI API key (not uploaded)
└── README.md

Dependencies
