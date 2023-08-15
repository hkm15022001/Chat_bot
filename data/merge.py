import json
import os
# Thư mục chứa các file .json
folder_path = "chu_de"

# Đối tượng Python để lưu trữ dữ liệu gộp từ các file .json
merged_data = {"intents": []}

# Lặp qua tất cả các file .json trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            for i, element in enumerate(data["intents"]):
                if len(element["patterns"]) == 0:
                    data["intents"].remove(element)
                if '!' in element["tag"]:
                    sub_file_path = os.path.join(folder_path,(element["tag"]+'.json').replace('!', ''))
                    with open(sub_file_path, "r", encoding="utf-8") as sub_file:
                        sub_data = json.load(sub_file)
                        for j, v in enumerate(sub_data["intents"]):
                            if '?' in v["tag"]:
                                data["intents"][i]["responses"].append(v["patterns"][0])
            merged_data["intents"] += data["intents"]


# Ghi dữ liệu gộp vào file .json mới
output_file = "content.json"
with open(output_file, "w", encoding="utf-8") as outfile:
    json.dump(merged_data, outfile, ensure_ascii=False, indent=4)