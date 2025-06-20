# 🐍 Utilisation d’un fichier `.pkl` dans un projet Python

Ce projet montre comment utiliser un fichier `.pkl`, un format de sérialisation d’objets Python. Cela permet de sauvegarder un objet complexe (modèle entraîné, dictionnaire, etc.) dans un fichier, et de le recharger plus tard sans avoir à le recalculer.

---

## 📁 Contenu du projet

- `main.py` : script Python qui charge et utilise un objet stocké dans un fichier `.pkl`.
- `mon_objet.pkl` : fichier contenant l’objet Python correspondant au modèle.

---

## 🚀 Comment utiliser ce projet

- Charger le modèle en `.pkl` en créant un objet python : 
    `mon_objet = pickle.load(f)`
- Donner les données que vous voulez afin de prédire le type de bateau : 
        `new_data = pd.DataFrame({
            'sog': [12.0],
            'cog': [180.0],
            'heading': [190.0],
            'length': [150.0],
            'width': [30.0],
            'draft': [8.0]
        })`
- Utiliser le modèle directement pour faire une prédiction :
    `prediction = model_random_forest.predict(new_data)`
- Afficher le résultat : 
    `print("Prédiction :", prediction)`