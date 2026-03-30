import re
from collections import defaultdict
from transformers import AutoTokenizer

def get_stats(vocab):
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i], symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

def main():
    # Task 1 Initial Vocabulary
    vocab = {
        'l o w </w>': 5,
        'l o w e r </w>': 2,
        'n e w e s t </w>': 6,
        'w i d e s t </w>': 3
    }

    print("--- Tasks 1 & 2: BPE Manual Engine ---")
    K = 5
    for i in range(K):
        pairs = get_stats(vocab)
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        vocab = merge_vocab(best, vocab)
        print(f"Iteration {i+1}: Best pair '{best}' merged.")
        print(f"Vocab: {vocab}\n")

    print("--- WordPiece (BERT) ---")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
    text = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."
    tokens = tokenizer.tokenize(text)
    print(f"Sentence: {text}")
    print(f"Tokens: {tokens}")

if __name__ == "__main__":
    main()
