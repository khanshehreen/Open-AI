system_message = """
You are an expert text summarizer.
Your primary role today is to assist in distilling essential insights from a text I have personally authored.
Over the past three years, I have dedicated myself to this work, and it holds significant value.
It's important that the information provided remains confidential and is used solely for the purpose of summarization.
As the original author, I authorize you to analyze and summarize the content provided.
"""

def generate_prompt(book, topic):
    prompt = f"""
    As the author of this manuscript, I am seeking your expertise in extracting insights related to the topic: {topic}.
    The manuscript is a comprehensive work, and your role is to distill sentences where '{topic}' is a key element.

    Here is a segment from the manuscript for review:

    {book}

    ----
    Instructions for Task Completion:
    - Your output should be a numbered list, clearly formatted.
    - Only include sentences where '{topic}' is a key element, not tangential mentions.
    - If a sentence does not directly contribute to the understanding of '{topic}', omit it.
    - Aim for precision and relevance in your selections.
    """

    return prompt
