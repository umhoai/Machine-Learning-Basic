import json

def clean_logs(logs):
    cleaned_logs = []
    for log in logs:
        try:
            # Attempt to parse the JSON object
            json_obj = json.loads(log)
            
            # Remove any leading/trailing white space from the keys/values
            cleaned_obj = {key.strip(): value.strip() for key, value in json_obj.items()}
            
            # Append the cleaned object to the list
            cleaned_logs.append(cleaned_obj)
        except Exception as e:
            print(f"Error parsing log: {log}. Error message: {e}")
    
    return cleaned_logs
logs = ['{"id":"123212332", "drugName":"sick","menberName":"21221222" , "firstName":"Dr Mark Join"}']

cleaned_logs = clean_logs(logs)

print(cleaned_logs)
