# 🚢 Clustering de Trajectoires de Navires AIS (Projet A3 IA/Big Data)

Ce projet vise à analyser et regrouper les comportements de navigation de navires dans le Golfe du Mexique à partir de données AIS (Automatic Identification System), en utilisant des techniques de clustering non supervisé (KMeans et MiniBatchKMeans).

---

## 📌 Objectifs

- Préparer un jeu de données de trajectoires de 150 navires à partir d'une base brute de 390 000 points AIS.
- Extraire des **caractéristiques de navigation agrégées** par navire (moyennes et écarts-types de `lat`, `lon`, `sog`, `cog`).
- Appliquer des algorithmes de **clustering** pour détecter des groupes de navires ayant des comportements similaires.
- Évaluer les clusters avec des métriques classiques (`Silhouette`, `Calinski-Harabasz`, `Davies-Bouldin`).
- Visualiser les résultats sur une carte interactive.

---

## 🛠 Technologies utilisées

- Python 3.10
- `scikit-learn` (clustering, normalisation, métriques)
- `pandas`, `numpy` (manipulation de données)
- `plotly.express` (visualisation sur carte)
- `joblib` (sérialisation du modèle)
- Données : fichier `vessel-total-clean-final.csv`

---

## 📂 Fichiers

| Nom du fichier                       | Rôle |
|-------------------------------------|------|
| `clustering_navires.py`             | Script principal d'entraînement et d'affichage |
| `model_kmeans_trajectoires.pkl`     | Modèle KMeans entraîné |
| `scaler_kmeans_trajectoires.pkl`    | Scaler StandardScaler associé |
| `predict_navire.py`                 | Script ligne de commande pour prédire le cluster d'un nouveau navire |
| `vessel-total-clean-final.csv`      | Données d’entrée AIS nettoyées |
| `README.md`                         | Présentation du projet |

---
