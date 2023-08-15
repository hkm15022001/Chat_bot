import json
import random
import pickle
from .training_LogisticRegression import file_name, all_words, tags, bag_of_words, token
import numpy as np
import os


parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(parent_directory, "data", "content.json")

with open(file_path, "r", encoding="utf-8") as json_data:
    contents = json.load(json_data)
with open(file_name, "rb") as file:
    loaded_model = pickle.load(file)


def chat_bot_LR(sentence):
    sentence = token(sentence)
    X = bag_of_words(sentence, all_words)
    X = np.asarray(X)
    X = np.reshape(X, (1, X.shape[0]))
    output = loaded_model.predict_proba(X)
    predict = np.argmax(output, axis=1)
    tag = tags[predict.item()]
    for content in contents["intents"]:
        if tag == content["tag"]:
            if "!" in tag:
                string = "Một vài gợi ý dành cho bạn:\n"
                answer = "\n".join(content["responses"])
                return string + answer
            else:
                answer = random.choice(content["responses"])
                return answer
