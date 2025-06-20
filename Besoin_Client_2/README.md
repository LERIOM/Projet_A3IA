# 🐍 Utilisation d’un fichier `.pkl` dans un projet Python

Ce projet montre comment utiliser un fichier `.pkl`, un format de sérialisation d’objets Python. Cela permet de sauvegarder un objet complexe (modèle entraîné, dictionnaire, etc.) dans un fichier, et de le recharger plus tard sans avoir à le recalculer.

---

## 📁 Contenu du projet

- `prediction.ipynb` : fichier qui crée, entraine et teste les modèles 
- `predict_vessel.py` : script Python qui charge et utilise un objet stocké dans un fichier `.pkl`.
- `mon_objet.pkl` : fichier contenant l’objet Python correspondant au modèle.

---

## 🚀 Comment utiliser ce projet

Executer la ligne suivante dans le terminal : `python predict_vessel.py --sog 12.5 --cog 180.0 --heading 175 --length 100 --width 20 --draft 6.5`
Pour choisir le modèle il suffit de changer le nom du .pkl dans le fichier predict_vessel.pkl : `model = joblib.load("model_vessel_type_one_line_per_mmsi.pkl")`