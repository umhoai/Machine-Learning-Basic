def parse_json(json_str):
    json_obj = json.loads(json_str)
    result = ""
    for key, value in json_obj.items():
        if isinstance(value, dict):
            result += f"{key}: {parse_json(json.dumps(value))}\n"
        elif isinstance(value, list):
            for item in value:
                result += f"{key}: {parse_json(json.dumps(item))}\n"
        else:
            result += f"{key}: {value}\n"
    return result

text = parse_json(json_str)
print(text)
