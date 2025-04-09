# 🧠 Semantic Internal Linking Recommender

This Google Colab-friendly script takes a list of texts (e.g. articles, pages, or product descriptions) from an Excel file, computes their semantic embeddings using a Sentence Transformer, and recommends internal links based on semantic similarity.

It’s ideal for content-heavy websites or blogs where meaningful internal linking is crucial for SEO and user experience.

---

## 🔧 Features

- 💬 Uses `sentence-transformers` for text embedding
- 📈 Computes pairwise cosine similarity between texts
- 🔗 Suggests top-N semantically related entries per text
- 📁 Exports:
  - Text vectors with IDs
  - Internal link recommendations

---

## 📥 Input Format

Upload an `.xlsx` Excel file with **two columns**:

| ID  | Text               |
|-----|--------------------|
| 1   | How to plant roses |
| 2   | Gardening basics   |

- `ID` must be unique, use slug for easy reading
- `Text` is the body of the content to be analyzed

---

## 🚀 How to Use (in Google Colab)

1. Open the notebook in Google Colab
2. Run all cells
3. Upload your Excel file when prompted
4. The script will:
   - Generate text embeddings
   - Export an Excel with those embeddings
   - Recommend internal links
   - Export the recommendations as another Excel

---

## 📦 Dependencies

These are automatically installed via the script in Colab:

- `sentence-transformers`
- `openpyxl`
- `scikit-learn`
- `pandas`
- `numpy`

---

## 🧪 Output Files

- `text_vectors_with_ids.xlsx`: Each text's vector representation
- `internal_linking_recommendations.xlsx`: Top-N internal link targets per text, with similarity scores

---

## 📌 Notes

- The script uses the model `all-MiniLM-L6-v2` by default for fast and effective embeddings.
- You can change the `top_n` or `min_score` parameters in `recommend_internal_links()` for different results.

---

## 🤖 Example Use Cases

- SEO internal linking strategy
- Content clustering
- Similar article suggestions
- Content deduplication checks

---

## 🔐 Author
Julian Lölkes

Made with ❤️ to automate smart internal linking with semantic similarity.
