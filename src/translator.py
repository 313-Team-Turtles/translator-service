from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("API_KEY"),  
    api_version="2024-02-15-preview",
    azure_endpoint="https://team-turtles-ai.openai.azure.com/"  
)


def get_translation(post: str) -> str:
    context = "Translate the following text to English. Keep all appropriate punctuation. If it does not have translatable meaning, return \"Not Translatable\" "
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Or "gpt-4" if using the main gpt-4 model, depending on API availability
        messages=[
            {"role": "system",
             "content": context},
            {"role": "user",
             "content": post}
        ]
    )

    # Extract and return the translation from the response
    translation = response.choices[0].message.content
    return translation

def get_language(post: str) -> str:
    context = "Determine if the following text is written in English or not. Respond with 'English' or 'Non-English' only."
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Or "gpt-4" if using the main gpt-4 model, depending on API availability
        messages=[
            {"role": "system",
             "content": context},
            {"role": "user",
             "content": post}
        ]
    )
    return response.choices[0].message.content

def translate_content(content: str) -> tuple[bool, str]:
    language = get_language(content).strip()
    print(language)
    try:
        if language == "English":
            return (True, content)
        elif language == "Non-English":
            translation = get_translation(content).strip()
            return (False, translation)
        else:
            return (False, "")
    except Exception as e:
        return (False, "A general error occured")