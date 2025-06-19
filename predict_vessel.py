{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fedced66",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "usage: ipykernel_launcher.py [-h] --sog SOG --cog COG --heading HEADING\n",
      "                             --length LENGTH --width WIDTH --draft DRAFT\n",
      "ipykernel_launcher.py: error: the following arguments are required: --sog, --cog, --heading, --length, --width, --draft\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\lucav\\AppData\\Roaming\\Python\\Python39\\site-packages\\IPython\\core\\interactiveshell.py:3558: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "import argparse\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Charger le modèle entraîné\n",
    "model = joblib.load(\"model_vessel_type_one_line_per_mmsi.pkl\")\n",
    "\n",
    "# Définir les arguments de la ligne de commande\n",
    "parser = argparse.ArgumentParser(description=\"Prédire le type de navire\")\n",
    "parser.add_argument('--sog', type=float, required=True, help=\"Speed Over Ground\")\n",
    "parser.add_argument('--cog', type=float, required=True, help=\"Course Over Ground\")\n",
    "parser.add_argument('--heading', type=float, required=True, help=\"Heading\")\n",
    "parser.add_argument('--length', type=float, required=True, help=\"Length of the vessel\")\n",
    "parser.add_argument('--width', type=float, required=True, help=\"Width of the vessel\")\n",
    "parser.add_argument('--draft', type=float, required=True, help=\"Draft of the vessel\")\n",
    "\n",
    "args = parser.parse_args()\n",
    "\n",
    "# Créer un tableau numpy avec les valeurs d'entrée\n",
    "input_data = np.array([[args.sog, args.cog, args.heading, args.length, args.width, args.draft]])\n",
    "\n",
    "# Faire la prédiction\n",
    "predicted_class = model.predict(input_data)[0]\n",
    "\n",
    "# Afficher le résultat\n",
    "print(f\"👉 Type de navire prédit : {predicted_class}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
