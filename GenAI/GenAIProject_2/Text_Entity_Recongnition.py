import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from nltk.corpus import stopwords, wordnet
from nltk.tree import Tree
import string
from collections import defaultdict
import Config

# Download resources (only needed once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')

# POS tag converter (WordNet)
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default fallback

def perform_ner(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)

    # Filter tokens: remove stopwords and punctuation
    tokens_filtered = [
        token for token in tokens
        if token.lower() not in stop_words and token not in string.punctuation
    ]

    # POS tagging
    tagged = pos_tag(tokens)

    # Named Entity Recognition on filtered/tagged tokens
    ner_tree = ne_chunk(tagged)

    # POS tags in full words
    tokens_filtered = [t for t in tokens if t.lower() not in stopwords.words('english') and t not in string.punctuation]
    tagged_filtered = pos_tag(tokens_filtered)
    tagged_full = [(word, Config.get_full_pos(tag)) for word, tag in tagged_filtered]

    # Group words by POS tags
    pos_groups = defaultdict(list)
    for word, pos in tagged_full:
        pos_groups[pos].append(word)

    # Display tokens
    print("\nTokens:")
    print(tokens)

    # Display the groups
    print("\nGrouped by POS tags:")
    for pos, words in pos_groups.items():
        print(f"{pos}: {', '.join(words)}")

    #Display NER
    print("\nNamed Entities:")
    print(ner_tree)

    # Return tokens, POS groups, and NER groups
    return tokens, pos_groups, ner_tree
