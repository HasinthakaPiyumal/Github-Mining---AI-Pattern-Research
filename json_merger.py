import json
import glob

# Folder where your JSON files are stored
folder_path = "/home/hasinthaka/Documents/Projects/AI/AI Pattern Mining/Github Mining/results/"   # change this to your folder

# Get all JSON files in the folder
json_files = glob.glob(folder_path + "*.json")

merged_data = []

for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        if isinstance(data, list):   # make sure it's a list
            merged_data.extend(data)
        else:
            print(f"⚠️ {file} does not contain a list, skipping.")

# Save merged data into one JSON file
with open("merged.json", "w", encoding="utf-8") as f:
    json.dump(merged_data, f, indent=2, ensure_ascii=False)

print(f"✅ Merged {len(json_files)} files into merged.json with {len(merged_data)} items.")
