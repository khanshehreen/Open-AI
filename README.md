# 🧠 Open-AI Text Summarizer

A Python project to extract and summarize insights from a PDF manuscript using OpenAI's GPT models.  
This tool reads a PDF, applies custom prompts, and generates concise topic-based summaries.

---

## 🚀 Features

- Extracts text from a PDF (`naval.pdf`) within a defined page range  
- Uses modular prompts from `prompts.py` to guide summarization  
- Generates summaries focused on a given topic (default: `life`)  
- Outputs clear, concise summaries to the console  

---

# 🧠 Open-AI Text Summarizer
 ```bash
Open-AI/
│
├── main.py        # Main script to generate summary
├── prompts.py     # Custom prompt definitions
├── naval.pdf      # PDF manuscript for summarization
├── .env           # Environment file for OpenAI API key (not uploaded)
└── README.md
```
---

## 📁 Dependencies

Install required libraries:

pip install openai PyPDF2 python-dotenv

---

**⚙️ Configuration**

Create a .env file in the root directory and add your OpenAI API key:

**OPENAI_API_KEY=your_openai_api_key_here
**

Ensure naval.pdf is placed in the root directory (or update the file_path in main.py).

---

🧩 **Usage**

Run the main script: python main.py

The script will:

- Extract text from the PDF

- Generate a prompt based on prompts.py

- Use OpenAI API to summarize content

- Print the summary in your terminal

---

🎨 **Customization**

**Topic**: Change the topic variable in main.py to target a different theme

**Page Range:** Adjust start_page and end_page in main.py

**Model Settings**: Modify temperature or max_tokens for different output styles

---

🎨 **Notes**

- Do not commit .env or any API keys.

- Keep PDFs private if this repo is public.

- Works with any GPT-compatible model (e.g., GPT-3.5, GPT-4).
  

**⭐ Tip: Feel free to fork this repo and modify prompts to build your own document summarizer!**
