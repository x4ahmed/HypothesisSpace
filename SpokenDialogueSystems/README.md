# Spoken Dialogue Systems - Theory & Explanations

This document contains structured explanations for theory questions from the SDS exercises.

---

## Table of Contents

- [Exercise 1: Word2Vec & Word Embeddings](#exercise-1-word2vec--word-embeddings)

---

## Exercise 1: Word2Vec & Word Embeddings

### Dataset: DSTC2

**DSTC2** (Dialog State Tracking Challenge 2) is a benchmark dataset of human-computer dialogues where users search for restaurants. It contains utterances with domain-specific vocabulary organized into clear semantic clusters:
- **Food types**: italian, indian, chinese
- **Locations**: north, south, east, west, centre
- **Price levels**: cheap, moderate, expensive

---

### Q1: Two Advantages of Dense Parameterized Word Representations vs One-Hot Vectors

**1. Captures Semantic Relationships**
- One-hot vectors treat all words as equally different (orthogonal)
- Dense embeddings place similar words close in vector space
- Enables vector arithmetic: `king - man + woman ≈ queen`

**2. Dimensionality Efficiency**
- One-hot: dimension = vocabulary size (10K-1M+)
- Dense: fixed low dimension (50-300)
- Dense vectors are more memory-efficient and computationally tractable

| Aspect | One-Hot | Dense Embeddings |
|--------|---------|------------------|
| Dimensionality | Vocabulary size (huge) | Fixed small size (50-300) |
| Semantic similarity | None (all orthogonal) | Captured via vector proximity |
| Generalization | None | Can infer similar words |
| Memory efficiency | Poor (sparse) | Good (dense) |

---

### Q2: Intuition Behind Word2Vec Training

**Core Principle: "You shall know a word by the company it keeps"**

Word2Vec is based on the **distributional hypothesis**: words appearing in similar contexts have similar meanings.

**Training Architectures:**

1. **Skip-gram**: Predict context words from target word
   - Input: Center word (e.g., "apple")
   - Output: Surrounding words (e.g., "tasty", "fruit")

2. **CBOW**: Predict target word from context words
   - Input: Surrounding words
   - Output: Center word

**Why It Works:**
Words like "apple" and "orange" both appear near "fruit", "eat", "tasty". The model learns to give them similar vectors to generate similar context predictions. Through gradient descent, words with interchangeable contexts cluster together in vector space.

---

### Q6: Issue Revealed by Similarity Examples

**The Problem: Polysemy (Words with Multiple Meanings)**

The word "apple" has two distinct meanings:
1. **The fruit** - related to "fruit", "tasty", "eat", "orange"
2. **The company** - related to "computer", "technology", "iPhone", "Mac"

**What Happens:**
- Word2Vec creates **a single vector** for "apple" that averages BOTH meanings
- When 'computer' is in the candidate list, it may score higher than 'fruit' because the training corpus contains many co-occurrences of "Apple" (company) with "computer"
- The embedding cannot distinguish which sense you intended

**The Core Issue: Word Embeddings Conflate Multiple Meanings**

| Aspect | Problem |
|--------|---------|
| **Single vector per word** | Cannot represent different senses separately |
| **Context-free** | Same vector regardless of usage context |
| **Frequency bias** | More common meaning dominates |

**Why This Matters:**
- Static embeddings (Word2Vec, GloVe) cannot handle polysemous words properly
- "Apple" ≈ "computer" and "Apple" ≈ "orange" simultaneously in the same vector space
- This leads to ambiguous similarity results depending on which other words are present

**Modern Solution:** Contextualized embeddings (BERT, GPT) generate different vectors based on surrounding context, solving this polysemy problem.

---

### Q8: Why Sentence Similarity Remains Close

**The Problem: Averaging Dilutes Semantic Signals**

When averaging word embeddings, generic function words ("is", "more", "than") pull the sentence vector toward a neutral center. The sentence becomes a "blurry" mix where:
- Specific words like "tasty" and "orange" suggest the fruit meaning of "apple"
- But the averaging with 3 generic words dilutes this signal
- Both "fruit" and "computer" end up with similar similarity scores because the sentence vector is too generic to strongly distinguish either

**Key Issue:** Averaging is a bag-of-words approach that loses word order and compositionality. "Apple is tasty" and "apple computer" have very different meanings, but word averaging cannot tell them apart.

**Better Approaches:** TF-IDF weighting, SIF (Smooth Inverse Frequency), or contextualized embeddings (BERT) that capture word order and context.

---

### Q9: Advantage of Embeddings for Neural Networks

*[To be added when discussed]*

---

### Word2Vec Hyperparameters Reference

| Parameter | Role | Effect |
|-----------|------|--------|
| **`vector_size`** | Embedding dimension | Higher = more expressive, slower (common: 50-300) |
| **`window`** | Context window size | Words within N distance considered neighbors |
| **`min_count`** | Min word frequency | Words appearing < N times are ignored (filters noise) |
| **`epochs`** | Training iterations | More passes = better convergence, longer training |
| **`sg`** | Algorithm choice | 1=Skip-gram (rare words), 0=CBOW (frequent words, faster) |
| **`negative`** | Negative samples | How many "wrong" words to contrast against |
| **`sample`** | Downsampling rate | Reduces frequent words ("the", "is") from training |

**Key Trade-offs:**
- **Higher `vector_size`**: Better quality, more memory/time
- **Larger `window`**: Captures broader context but dilutes local patterns
- **Skip-gram vs CBOW**: Skip-gram for small data/rare words, CBOW for large data/speed

---

### Q10: Problem with FastText for User Preference Detection

*[To be added when discussed]*

---

*Last updated: 2026-04-19*
