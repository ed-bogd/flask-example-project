'''
Detecting emotion in text
'''
# Import required libraries
import json
import requests

# Define sentiment analysis function
def emotion_analyzer(text_to_analyze):
    ''' Analyze sentiment function'''
    # Define constant values
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Build request JSON
    text_to_analyze_str = str(text_to_analyze)
    request_json = { "raw_document": { "text":  text_to_analyze_str} }
    # Send request
    result = requests.post(url, json = request_json, headers=headers, timeout=3)
    # Get response
    response = result.text
    # Format as JSON
    formatted_response = json.loads(response)
    # Condition if status code is 400 - Bad request
    if result.status_code == 400:
        # Return if code is defined
        return bad_request()
    # Else return emotions
    output_json = formatted_response['emotionPredictions'][0]['emotion']
    # Find dominant value
    dominant_emotion = max(output_json.values())
    # Add dominant emotion to dict by it's value
    output_json['dominant_emotion'] = list(output_json.keys())[list(output_json.values()).index(dominant_emotion)]
    return output_json

# Define bad request output function
def bad_request():
    ''' 
        Return Bad request output with the same structure 
        as it would be with successful request
    '''
    # Same structure as with successful request
    bad_request_output = {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None
        }
    return bad_request_output
