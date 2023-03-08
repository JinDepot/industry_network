# Industry Network

This project builds an industry network of S&P500 stocks using various sources of data
- DEPENDENCY CHECK: runs on python 3.9.13
---

## Preprocessing
- Runs minimal preprocessing in prior to leaning firm embedding vectors, such as:
    - removing ewline markers, like "\n"
    - removing redundant, non-informative words such as "Overview", "Table of Contents", "Description of Major Subsidiaries"
    - removing the word "General" if it appears at the beginning of the document
    - replacing running whitespaces with a single space

- **Execution**: On terminal, run the following
```python
 python preprocessing.py
 ```

---

## Embedding Learner 
- Learns firm embedding vectors
