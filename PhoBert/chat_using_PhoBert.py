import json
import torch
import random
from transformers import AutoModel, AutoTokenizer
from .phobert_finetuned import PhoBERT_finetuned
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(parent_directory, "data", "content.json")
with open(file_path, "r", encoding="utf-8") as c:
    contents = json.load(c)

# Process the train dataset and get unique tags
tags = []
for content in contents["intents"]:
    tag = content["tag"]
    tags.append(tag)
tags_set = sorted(set(tags))


# Load pre-trained model PhoBERT and its tokenizer
model_name = "vinai/phobert-base"
phobert = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
num_class = len(tags_set)
hidden_size = 512
model = PhoBERT_finetuned(phobert, hidden_size=hidden_size, num_class=num_class)

path = os.path.join(current_directory, "PhoBert_weight.pth")
model.load_state_dict(torch.load(path, map_location=torch.device(device)))


def chat_bot_PhoBERT(sentence):
    token = tokenizer(sentence, max_length=13, padding="max_length", truncation=True)
    X_mask = torch.tensor([token["attention_mask"]])
    X = torch.tensor([token["input_ids"]])
    with torch.no_grad():
        preds = model(X, X_mask)
    preds = torch.argmax(preds, dim=1)
    tag = tags_set[preds.item()]
    for content in contents["intents"]:
        if tag == content["tag"]:
            if "!" in tag:
                string = "Một vài gợi ý dành cho bạn:\n"
                answer='\n'.join(content["responses"])
                return string+answer
            else:
                answer = random.choice(content["responses"])
                return answer
