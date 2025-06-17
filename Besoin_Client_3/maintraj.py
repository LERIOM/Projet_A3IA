import joblib
import pandas as pd
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "trajectoire.pkl")

model = joblib.load(model_path)
print("Modèle chargé.")

# ----------------------------
# Définir ton état actuel + delta_seconds désiré
# Exemple : tu peux remplacer ces valeurs par un input utilisateur ou un fichier
# ----------------------------
example_input = {
    "sog": 12.5,         # vitesse en noeuds
    "cog": 275.0,        # cap en degrés
    "heading": 270.0,    # orientation en degrés
    "length": 150.0,     # longueur en mètres
    "draft": 7.0,        # tirant d'eau en mètres
    "delta_seconds": 300  # temps futur désiré en SECONDES (ex: 300 s = 5 min)
}

# ----------------------------
# Convertir en DataFrame pour prédire
# ----------------------------
X_new = pd.DataFrame([example_input])

# ----------------------------
# Prédire la position future
# ----------------------------
predicted_position = model.predict(X_new)

# ----------------------------
# Afficher le résultat
# ----------------------------
print("\n📍 Position future estimée pour delta_seconds =", example_input["delta_seconds"], "secondes :")
print("Latitude :", predicted_position[0][0])
print("Longitude:", predicted_position[0][1])