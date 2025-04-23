from datasets import load_dataset
import pickle
import sys
import io

# Forcer l'encodage en UTF-8 pour stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Charger le dataset
# ds = load_dataset("TEAMREBOOTT-AI/SciCap-MLBCAP")

# Sauvegarder le dataset dans un fichier pickle
# with open("dataset.pkl", "wb") as f:
#     pickle.dump(ds, f)
# Une fois cela fait, on ne travaille qu'à partir du dataset directement importé
with open("dataset.pkl", "rb") as f:
    ds = pickle.load(f)
#  Intéreserrons nous premièrement au train
train_dataset = ds["train"] 
figure_type = list(set(train_dataset["figure_type"]))
dict_fig_type = dict()
for fig_type in figure_type:
    dict_fig_type[fig_type] = 0
for elt in train_dataset["figure_type"]:
    dict_fig_type[elt] += 1
print(dict_fig_type)
# Methode pour décoder les caractères spéciaux.
desc_0 = train_dataset[0]["paragraph"]
# print(desc_0.encode().decode('unicode_escape'))


features = ['image', 'id', 'figure_type', 'ocr', 'paragraph', 
            'mention', 'figure_description', 'mlbcap_long', 
            'mlbcap_short', 'categories']
for feature in features :
    print('-'*10 + feature + '\n')
    print(train_dataset[0][feature]) # .encode().decode('unicode_escape')


