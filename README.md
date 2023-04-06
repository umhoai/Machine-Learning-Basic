# Define function to parse JSON and flatten it into a string
def parse_json(json_str):
    # Convert JSON string to Python object
    json_obj = json.loads(json_str)
    # Initialize empty string to hold flattened JSON
    result = ""
    # Iterate through keys and values of the dictionary
    for key, value in json_obj.items():
        # If the value is another dictionary, recursively call the function on that value
        if isinstance(value, dict):
            result += f"{key}: {parse_json(json.dumps(value))}, "
        # If the value is a list, iterate through the list and call the function on each item
        elif isinstance(value, list):
            for item in value:
                result += f"{key}: {parse_json(json.dumps(item))}, "
        # If the value is neither a dictionary nor a list, append it to the result string
        else:
            result += f"{key}: {value}, "
    # Return the flattened string, with the last two characters removed (which will be a trailing comma and space)
    return result[:-2]

# Parse the input JSON and remove the "city" key and its value
