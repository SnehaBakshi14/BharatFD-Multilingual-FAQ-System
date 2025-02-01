from googletrans import Translator

translator = Translator()

def translate_text(text: str, target_lang: str) -> str:
    """Translate text to target language using Google Translate."""
    try:
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Fallback to original text