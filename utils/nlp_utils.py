

import logging
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

try:
    logging.info('Loading Hugging Face NER model: dslim/bert-base-NER')
    tokenizer = AutoTokenizer.from_pretrained('dslim/bert-base-NER')
    model = AutoModelForTokenClassification.from_pretrained('dslim/bert-base-NER')
    nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    logging.info('Hugging Face NER model loaded successfully')
except Exception as e:
    logging.error(f'Error loading NER model: {e}')
    nlp = None

def perform_ner(text):
    """
    Perform Named Entity Recognition on the given text using Hugging Face Transformers.
    """
    logging.info('Performing NER on text using Hugging Face Transformers')
    if nlp is None:
        logging.error('NER model is not loaded')
        return {'entities': [], 'error': 'NER model is not available'}

    if not text or not isinstance(text, str):
        logging.error('Input text for NER is empty or invalid')
        return {'entities': [], 'error': 'Input text is empty or invalid for NER'}

    try:
        ner_results = nlp(text)
        entities = []
        for entity in ner_results:
            entities.append({
                'label': entity['entity_group'],
                'text': entity['word'],
                'score': entity['score'],
                'start': entity['start'],
                'end': entity['end']
            })
        return {'entities': entities, 'error': None}
    except Exception as e:
        logging.error(f'Error performing NER: {e}')
        return {'entities': [], 'error': f"Error performing NER: {e}"}



# The dslim/bert-base-NER model is trained on English data. For texts in other languages, consider using multilingual models like xlm-roberta-base fine-tuned for NER

# utils/nlp_utils.py
"""
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

try:
    logging.info('Loading Hugging Face Multilingual NER model: Davlan/xlm-roberta-base-ner-hrl')
    tokenizer = AutoTokenizer.from_pretrained('Davlan/xlm-roberta-base-ner-hrl')
    model = AutoModelForTokenClassification.from_pretrained('Davlan/xlm-roberta-base-ner-hrl')
    nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    logging.info('Hugging Face Multilingual NER model loaded successfully')
except Exception as e:
    logging.error(f'Error loading NER model: {e}')
    nlp = None
"""