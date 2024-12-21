from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Exemplo de dados
texts = ["I love sunny days", "Rainy days make me sad", "I am happy", "I am feeling blue"]
labels = [1, 0, 1, 0]  # 1 = positivo, 0 = negativo

# Vetorização e treinamento do modelo
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

# Salvar o modelo e o vetor de características
joblib.dump(model, 'tools/model.pkl')
joblib.dump(vectorizer, 'tools/vectorizer.pkl')
