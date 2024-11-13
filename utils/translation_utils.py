

import logging
from google.cloud import translate_v2 as translate

def translate_text(text, target_language):
    """
    Translate text into the target language.
    """
    logging.info(f'Translating text to {target_language}')
    try:
      
        client = translate.Client()
        result = client.translate(text, target_language=target_language)
        translated_text = result['translatedText']
        logging.debug(f'Translated text: {translated_text[:100]}...')
        return translated_text, None
    except Exception as e:
        logging.error(f'Error translating text: {e}')
        return None, f"Error translating text: {e}"
