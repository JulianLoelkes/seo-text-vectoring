# Install necessary libraries (optimized for Colab)
!pip install -q --upgrade --no-deps sentence-transformers openpyxl

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from google.colab import files


def load_input_excel(expected_columns=('ID', 'Text')):
    uploaded = files.upload()
    filepath = next(iter(uploaded))
    df = pd.read_excel(filepath)
    missing = [col for col in expected_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")
    return df


def compute_embeddings(texts, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    return model.encode(texts, batch_size=32, show_progress_bar=True)


def export_embeddings(df, embeddings, filename="text_vectors_with_ids.xlsx"):
    embedding_cols = [f'vec_{i}' for i in range(len(embeddings[0]))]
    df_vectors = pd.DataFrame(embeddings, columns=embedding_cols)
    df_out = pd.concat([df[['ID', 'Text']], df_vectors], axis=1)
    df_out.to_excel(filename, index=False)
    files.download(filename)


def recommend_internal_links(embeddings, ids, texts, top_n=3, min_score=0.0):
    similarity_matrix = cosine_similarity(embeddings)
    np.fill_diagonal(similarity_matrix, 0)
    recommendations = []

    for idx, text in enumerate(texts):
        similar_indices = similarity_matrix[idx].argsort()[::-1]
        filtered = [(i, similarity_matrix[idx][i]) for i in similar_indices if similarity_matrix[idx][i] >= min_score][:top_n]
        recommendations.append({
            'ID': ids[idx],
            'Text': text,
            'Recommended_Link_IDs': [ids[i] for i, _ in filtered],
            'Similarity_Scores': [round(score, 4) for _, score in filtered]
        })

    return pd.DataFrame(recommendations)


def export_recommendations(df, filename="internal_linking_recommendations.xlsx"):
    df.to_excel(filename, index=False)
    files.download(filename)


def main():
    df = load_input_excel()
    texts = df['Text'].tolist()
    ids = df['ID'].tolist()
    embeddings = compute_embeddings(texts)

    export_embeddings(df, embeddings)
    recommendations = recommend_internal_links(embeddings, ids, texts)
    export_recommendations(recommendations)


main()
