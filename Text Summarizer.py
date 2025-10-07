"""
Text Summarizer (extractive, frequency-based)

Functions:
- tokenize_sentences(text): splits text into sentences
- tokenize_words(text): returns cleaned word tokens
- build_word_frequencies(words, stopwords): dictionary of word -> normalized frequency
- score_sentences(sentences, word_freq): sentence -> score
- summarize(text, max_sentences=3): returns the top-N sentence summary (in original order)

No external libraries required.
"""

import re
from math import sqrt
from collections import Counter, defaultdict

# Minimal stopwords list (expand if needed)
STOPWORDS = {
    "a","an","the","and","or","but","if","while","of","at","by","for","with","about",
    "against","between","into","through","during","before","after","above","below","to",
    "from","up","down","in","out","on","off","over","under","again","further","then",
    "once","here","there","when","where","why","how","all","any","both","each","few",
    "more","most","other","some","such","no","nor","not","only","own","same","so",
    "than","too","very","can","will","just","don't","should","now","is","are","was",
    "were","be","been","being","have","has","had","do","does","did","i","you","he",
    "she","it","we","they","me","him","her","them","my","your","his","their","our"
}

_SENT_END_RE = re.compile(r'(?<=[.!?])\s+')

def tokenize_sentences(text):
    """Split text into sentences. Keeps punctuation at sentence end."""
    # Clean repeated whitespace
    text = re.sub(r'\s+', ' ', text.strip())
    if not text:
        return []
    sentences = _SENT_END_RE.split(text)
    # remove empty sentences
    return [s.strip() for s in sentences if s.strip()]

def tokenize_words(text):
    """Lowercase, remove non-alphanumeric (keep apostrophes removed), return list of words."""
    text = text.lower()
    # replace non-alphanumeric with spaces
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    words = [w for w in text.split() if w]
    return words

def build_word_frequencies(words, stopwords=STOPWORDS):
    """Return normalized frequency dict for words (excluding stopwords)."""
    counts = Counter(w for w in words if w not in stopwords)
    if not counts:
        return {}
    max_freq = max(counts.values())
    # normalize by max frequency
    freq = {w: count/max_freq for w, count in counts.items()}
    return freq

def score_sentences(sentences, word_freq):
    """Score each sentence by summing word frequencies (longer sentences get proportionally higher score).
       Returns dict: index -> score
    """
    scores = {}
    for idx, sent in enumerate(sentences):
        words = tokenize_words(sent)
        if not words:
            scores[idx] = 0.0
            continue
        # sum frequencies; can normalize by sqrt(len) to avoid bias toward very long sentences
        raw = sum(word_freq.get(w, 0.0) for w in words)
        norm = raw / sqrt(len(words))  # mild length normalization
        scores[idx] = norm
    return scores

def summarize(text, max_sentences=3):
    """
    Summarize the given text and return the summary as a string.
    - max_sentences: number of sentences in the summary (default 3)
    """
    sentences = tokenize_sentences(text)
    if not sentences:
        return ""
    words = tokenize_words(text)
    word_freq = build_word_frequencies(words)
    sent_scores = score_sentences(sentences, word_freq)
    # pick top indices by score
    top_n = sorted(sent_scores.items(), key=lambda x: x[1], reverse=True)[:max_sentences]
    top_indices = set(idx for idx, _ in top_n)
    # return sentences in original order
    summary_sentences = [sentences[i] for i in range(len(sentences)) if i in top_indices]
    return " ".join(summary_sentences)

# --- Example usage ---
if __name__ == "__main__":
    sample_text = (
        "Artificial Intelligence (AI) is transforming many industries. "
        "From healthcare to finance, AI systems are used to make decisions, "
        "automate tasks, and generate insights. The rapid growth of AI has "
        "raised ethical and regulatory challenges that need careful consideration. "
        "Researchers are working on solutions for fairness, transparency, and robustness. "
        "Education will need to adapt so learners can thrive in an AI-enabled world."
    )
    print("Original text:\n", sample_text, "\n")
    print("Summary (2 sentences):\n", summarize(sample_text, max_sentences=2))
