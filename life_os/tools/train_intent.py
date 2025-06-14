import spacy
import json
from spacy.training import Example


def train_intent_model():
    nlp = spacy.load("en_core_web_sm")
    if "textcat" not in nlp.pipe_names:
        textcat = nlp.add_pipe("textcat", last=True)
    else:
        textcat = nlp.get_pipe("textcat")

    with open("life_os/data/intents.json", "r") as f:
        intents = json.load(f)

    for intent in intents:
        textcat.add_label(intent)

    train_data = []
    for intent, texts in intents.items():
        for text in texts:
            doc = nlp.make_doc(text)
            cats = {
                label: 1.0 if label == intent else 0.0
                for label in intents
            }
            train_data.append(Example.from_dict(doc, {"cats": cats}))

    nlp.begin_training()
    for _ in range(10):
        for example in train_data:
            nlp.update([example])

    nlp.to_disk("life_os/models/intent_classifier")


if __name__ == "__main__":
    train_intent_model()
