from src.translator import translate_content
from openai import AzureOpenAI
import os 

client = AzureOpenAI(
    api_key=os.getenv("API_KEY"),  
    api_version="2024-02-15-preview",
    azure_endpoint="https://team-turtles-ai.openai.azure.com/"  
)
#Assertion Tests
def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content.strip().lower() == "this is a chinese message."

def test_llm_normal_response():
    is_english, translated_content = translate_content("Bonjour tout le monde")
    assert is_english == False
    assert translated_content.strip().lower() == "hello everyone"

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("asdkjasld1239adk")
    assert is_english == False
    assert translated_content == "Not Translatable"

def test_spanish_with_punctuation():
    is_english, translated_content = translate_content("¡Buenos días!")
    assert is_english == False
    assert translated_content.strip().lower() == "good morning!"

def test_non_english_with_numbers():
    is_english, translated_content = translate_content("Esto es una prueba 1234")
    assert is_english == False
    assert translated_content.strip().lower() == "this is a test 1234"

def test_badly_formatted():
    is_english, translated_content = translate_content("   Hola    Mundo  ")
    assert is_english == False
    assert translated_content.strip().lower() == "hello world"

def test_emojis():
    is_english, translated_content = translate_content("こんにちは 🌸")
    assert is_english == False
    assert translated_content.strip().lower() == "hello 🌸"

def test_english():
    is_english, translated_content = translate_content("this is english")
    assert is_english == True
    assert translated_content.strip().lower() == "this is english"


#Mock Test

from mock import patch
from unittest.mock import MagicMock

@patch('src.translator.client.chat.completions.create')
def test_unexpected_language(mocker):
  mocker.return_value.choices[0].message.content = "I don't understand your request"
  assert translate_content("Hier ist dein erstes Beispiel.")

@patch('src.translator.client.chat.completions.create')
def test_returning_not_a_language(mocker):
    mocker.return_value.choices[0].message.content = "string, not a tuple"
    response = translate_content("Summarize this text.")
    assert response  == (False, "")

@patch('src.translator.client.chat.completions.create')
def test_correct_translation(mocker):
    mocker.return_value.choices[0].message.content = "English"
    response = translate_content("Provide a list of AI tools.")
    assert response == (True, "Provide a list of AI tools.")

@patch('src.translator.client.chat.completions.create')
def test_empty_response(mocker):
    mocker.return_value.choices = [MagicMock(message=MagicMock(content=""))]
    response = translate_content("Provide a list of AI tools.")
    assert response == (False, "")
