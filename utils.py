import os
import requests

def fake_news_detection(text, api_key):
    # Define the model and the candidate labels for fake news detection
    model_name = "facebook/bart-large-mnli"  # Example model for classification
    candidate_labels = ["real", "fake"]  # These are the possible categories to classify the text into

    # Prepare the payload
    payload = {
        "inputs": text,
        "parameters": {
            "candidate_labels": candidate_labels
        }
    }
    
    url = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.post(url, headers=headers, json=payload)

    # Check the response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}


def topic_modulation(documents, api_key):
    model_name = "t5-base"  # You can use T5 for topic generation tasks
    payload = {"inputs": " ".join(documents), "parameters": {"max_length": 500}}
    url = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}
