
# Input filepath
inputFilePath = r"C:\Users\subin\OneDrive\Desktop\GenAI\Data\Output\output.md"

# NER label explanations
ner_explanations = {
    'PERSON': 'People, including fictional.',
    'NORP': 'Nationalities or religious/political groups.',
    'FAC': 'Buildings, airports, highways, bridges, etc.',
    'ORG': 'Companies, agencies, institutions, etc.',
    'GPE': 'Countries, cities, states.',
    'LOC': 'Non-GPE locations, mountain ranges, bodies of water.',
    'PRODUCT': 'Vehicles, weapons, foods, etc.',
    'EVENT': 'Named hurricanes, battles, wars, sports events, etc.',
    'WORK_OF_ART': 'Titles of books, songs, etc.',
    'LAW': 'Named documents made into laws.',
    'LANGUAGE': 'Any named language.',
    'DATE': 'Absolute or relative dates or periods.',
    'TIME': 'Times smaller than a day.',
    'PERCENT': 'Percentage, including "%".',
    'MONEY': 'Monetary values, including unit.',
    'QUANTITY': 'Measurements, as of weight or distance.',
    'ORDINAL': '“first”, “second”, etc.',
    'CARDINAL': 'Numerals that do not fall under another type.'
}

# POS tag converter to full word
def get_full_pos(treebank_tag):
    pos_map = {
        'CC': 'COORDINATING CONJUNCTION',
        'CD': 'CARDINAL NUMBER',
        'DT': 'DETERMINER',
        'EX': 'EXISTENTIAL THERE',
        'FW': 'FOREIGN WORD',
        'IN': 'PREPOSITION/CONJUNCTION',
        'JJ': 'ADJECTIVE',
        'JJR': 'ADJECTIVE, COMPARATIVE',
        'JJS': 'ADJECTIVE, SUPERLATIVE',
        'LS': 'LIST ITEM MARKER',
        'MD': 'MODAL',
        'NN': 'NOUN, SINGULAR',
        'NNS': 'NOUN, PLURAL',
        'NNP': 'PROPER NOUN, SINGULAR',
        'NNPS': 'PROPER NOUN, PLURAL',
        'PDT': 'PREDETERMINER',
        'POS': 'POSSESSIVE ENDING',
        'PRP': 'PRONOUN, PERSONAL',
        'PRP$': 'PRONOUN, POSSESSIVE',
        'RB': 'ADVERB',
        'RBR': 'ADVERB, COMPARATIVE',
        'RBS': 'ADVERB, SUPERLATIVE',
        'RP': 'PARTICLE',
        'SYM': 'SYMBOLE',
        'TO': 'TO',
        'UH': 'INTERJECTION',
        'VB': 'VERB, BASE FORM',
        'VBD': 'VERB, PAST TENSE',
        'VBG': 'VERB, GERUND/PARTICIPLE',
        'VBN': 'VERB, PAST PARTICIPLE',
        'VBP': 'VERB, NON-3RD PERSON SINGULAR PRESENT',
        'VBZ': 'VERB, 3RD PERSON SINGULAR PRESENT',
        'WDT': 'WH-DET',
        'WP': 'WH-PRONOUN',
        'WP$': 'POSSESSIVE WH-PRONOUN',
        'WRB': 'WH-ADVERB'
    }
    return pos_map.get(treebank_tag, 'UNKNOWN')