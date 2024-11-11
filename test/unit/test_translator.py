from src.translator import translate_content
from unittest.mock import patch
import src.translator

###################
# UNIT TEST CASES #
###################

def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_french():
    is_english, translated_content = translate_content("Ceci est un message en français")
    assert is_english == False
    assert translated_content == "This is a French message"

def test_spanish():
    is_english, translated_content = translate_content("Esta es un mensaje en español")
    assert is_english == False
    assert translated_content == "This is a Spanish message"
def test_portuguese():
    is_english, translated_content = translate_content("Esta é uma mensagem em português")
    assert is_english == False
    assert translated_content == "This is a Portuguese message"

def test_japanese():
    is_english, translated_content = translate_content("これは日本語のメッセージです")
    assert is_english == False
    assert translated_content == "This is a Japanese message"

def test_korean():
    is_english, translated_content = translate_content("이것은 한국어 메시지입니다")
    assert is_english == False
    assert translated_content == "This is a Korean message"

def test_german():
    is_english, translated_content = translate_content("Dies ist eine Nachricht auf Deutsch")
    assert is_english == False
    assert translated_content == "This is a German message"

def test_italian():
    is_english, translated_content = translate_content("Questo è un messaggio in italiano")
    assert is_english == False
    assert translated_content == "This is an Italian message"

def test_russian():
    is_english, translated_content = translate_content("Это сообщение на русском")
    assert is_english == False
    assert translated_content == "This is a Russian message"

def test_arabic():
    is_english, translated_content = translate_content("هذه رسالة باللغة العربية")
    assert is_english == False
    assert translated_content == "This is an Arabic message"

def test_hindi():
    is_english, translated_content = translate_content("यह हिंदी में संदेश है")
    assert is_english == False
    assert translated_content == "This is a Hindi message"

def test_thai():
    is_english, translated_content = translate_content("นี่คือข้อความภาษาไทย")
    assert is_english == False
    assert translated_content == "This is a Thai message"

def test_turkish():
    is_english, translated_content = translate_content("Bu bir Türkçe mesajdır")
    assert is_english == False
    assert translated_content == "This is a Turkish message"

def test_vietnamese():
    is_english, translated_content = translate_content("Đây là một tin nhắn bằng tiếng Việt")
    assert is_english == False
    assert translated_content == "This is a Vietnamese message"

def test_catalan():
    is_english, translated_content = translate_content("Esto es un mensaje en catalán")
    assert is_english == False
    assert translated_content == "This is a Catalan message"

# Test for English (should return True)
def test_english():
    is_english, translated_content = translate_content("This is an English message")
    assert is_english == True
    assert translated_content == "This is an English message"


###################
# MOCK TEST CASES #
###################

@patch('src.translator.dummy_translate')
def test_llm_mandarin_text(mock_dummy_translate):
    mandarin_text = "这是一条中文消息"
    mock_dummy_translate.return_value = "This is a Chinese message"

    is_english, translated_content = translate_content(mandarin_text)
    assert is_english == False, "Expected the content to be recognized as non-English"
    assert translated_content == "This is a Chinese message", f"Expected translation to be 'This is a Chinese message', got '{translated_content}'"

@patch('src.translator.dummy_translate')
def test_llm_thai_text(mock_dummy_translate):
    thai_text = "นี่คือข้อความภาษาไทย"
    mock_dummy_translate.return_value = "This is a Thai message"

    is_english, translated_content = translate_content(thai_text)
    assert is_english == False, "Expected the content to be recognized as non-English"
    assert translated_content == "This is a Thai message", f"Expected translation to be 'This is a Thai message', got '{translated_content}'"


@patch('src.translator.dummy_translate')
def test_llm_numeric_input(mock_dummy_translate):
    mock_dummy_translate.return_value = "12345"

    is_english, translated_content = translate_content("12345")
    assert is_english == True, "Expected numeric input to be recognized as English"
    assert translated_content == "12345", f"Expected translation to be '12345', got '{translated_content}'"


@patch('src.translator.dummy_translate')
def test_llm_empty_string(mock_dummy_translate):
    mock_dummy_translate.return_value = ""

    is_english, translated_content = translate_content("")
    assert is_english == True, "Expected empty input to be recognized as English"
    assert translated_content == "", f"Expected translation to be '', got '{translated_content}'"


@patch('src.translator.dummy_translate')
def test_llm_special_characters(mock_dummy_translate):
    special_characters = "!@#$%^&*()_+"
    mock_dummy_translate.return_value = "!@#gibberish)_+"

    is_english, translated_content = translate_content(special_characters)
    assert is_english == True, "Expected special characters to be recognized as English"
    assert translated_content == "!@#$%^&*()_+", f"Expected translation to be '{special_characters}', got '{translated_content}'"


@patch('src.translator.dummy_translate')
def test_llm_none_return(mock_dummy_translate):
    mock_dummy_translate.return_value = None

    is_english, translated_content = translate_content("Bonjour")
    assert is_english == True, "Expected None return from dummy_translate to default to English"
    assert translated_content == "Bonjour", f"Expected translation to be 'Bonjour', got '{translated_content}'"

@patch('src.translator.dummy_translate')
def test_llm_gibberish(mock_dummy_translate):
    mock_dummy_translate.return_value = "askdlf; jsadfewio"

    is_english, translated_content = translate_content("Hello")
    assert is_english == True, "Expected the content to be recognized as English"
    assert translated_content == "Hello", f"Expected translation to be 'Hello', got '{translated_content}'"
