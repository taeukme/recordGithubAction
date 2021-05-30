import json

def write_json(json_data, filepath):
    with open(filepath, 'w', encoding='UTF-8-sig') as f_write:
        json.dump(json_data, f_write, ensure_ascii=False, indent=4)