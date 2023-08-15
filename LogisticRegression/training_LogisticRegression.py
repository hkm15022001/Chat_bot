import json
from .nltk_utils import token, bag_of_words
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)

file_path1 = os.path.join(parent_directory, "data", "content.json")
print(file_path1)
file_path2 = os.path.join(parent_directory, "data", "test_content.json")

with open(file_path1, "r", encoding="utf-8") as c:
    contents = json.load(c)

with open(file_path2, "r", encoding="utf-8") as t:
    test_contents = json.load(t)

all_words = []
tags = []
xy = []
xy_test = []
punctuation = ["?", ".", ",", "!", ":", "/"]
for content in contents["intents"]:
    tag = content["tag"]
    tags.append(tag)
    for pattern in content["patterns"]:
        w = token(pattern)
        all_words.extend(w)
        xy.append((w, tag))
for test_content in test_contents["intents"]:
    tag = test_content["tag"]
    for test_pattern in test_content["patterns"]:
        t_w = token(test_pattern)
        xy_test.append((t_w, tag))

all_words = sorted(set([w.lower() for w in all_words if w not in punctuation]))
tags = sorted(set(tags))
X_train = []
y_train = []
X_test = []
y_test = []

for pattern_sentence, tag in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    label = tags.index(tag)
    X_train.append(bag)
    y_train.append(label)
for pattern_test, tag in xy_test:
    bag = bag_of_words(pattern_test, all_words)
    label = tags.index(tag)
    X_test.append(bag)
    y_test.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)
# Model:
model = LogisticRegression(multi_class="multinomial")

# Training:
model.fit(X_train, y_train)

# Saving model:
file_name = os.path.join(current_directory, "LogisticRegression_weight.pkl")
with open(file_name, "wb") as file:
    pickle.dump(model, file)

# Testing:
prediction = model.predict(X_test)
correct = 0
for i in range(len(prediction)):
    if prediction[i] == y_test[i]:
        correct += 1
