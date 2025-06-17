import joblib
import pandas as pd
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "trajectoire.pkl")

model = joblib.load(model_path)
print("Modèle chargé.")


# Définir ton état actuel + delta_seconds désiré
# Exemple : tu peux remplacer ces valeurs par un input utilisateur ou un fichier

input = {
    "lat": 29.123,      # Position actuelle en latitude
    "lon": -90.123,     # Position actuelle en longitude
    "sog": 12.5,        # Vitesse
    "cog": 275.0,       # Cap
    "heading": 270.0,   # Orientation
    "length": 150.0,    # Longueur navire
    "draft": 7.0,       # Tirant d'eau
    "delta_seconds": 300  # Durée désirée en SECONDES
}

# Convertir en DataFrame 
X_new = pd.DataFrame([input])

# Prédire la position future
predicted_position = model.predict(X_new)


# Afficher le résultat
print("\n📍 Position future estimée pour delta_seconds =", input["delta_seconds"], "secondes :")
print("Latitude :", predicted_position[0][0])
print("Longitude:", predicted_position[0][1])