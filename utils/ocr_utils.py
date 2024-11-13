
import easyocr
import os
import logging


LANGUAGE_COMBINATIONS = {
    'en': ['en'],
    'hi': ['hi', 'en'],
    'mr': ['mr', 'en'],
    'kn': ['kn', 'en'],
    'te': ['te', 'en'],
    'ta': ['ta', 'en'],
}


READERS = {}
for lang_code, lang_list in LANGUAGE_COMBINATIONS.items():
    try:
        logging.info(f'Initializing EasyOCR reader for languages: {lang_list}')
        READERS[lang_code] = easyocr.Reader(lang_list, gpu=False)
    except Exception as e:
        logging.error(f'Error initializing reader for {lang_code}: {e}')
        READERS[lang_code] = None

def extract_text(image_path, lang='en'):
    """
    Extract text from an image using EasyOCR.
    """
    logging.info(f'Extracting text from image: {image_path} with language: {lang}')
    try:
    
        reader = READERS.get(lang)
        if reader is None:
            logging.error(f'No EasyOCR reader available for language: {lang}')
            return f"Error: OCR language '{lang}' is not supported."
        results = reader.readtext(image_path, detail=0, paragraph=True)
        text = '\n'.join(results)
        logging.debug(f'Extracted text: {text[:100]}...')
        return text.strip()
    except Exception as e:
        logging.error(f'Error extracting text: {e}')
        return f"Error extracting text: {e}"
