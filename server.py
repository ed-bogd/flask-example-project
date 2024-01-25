''' Flask app for emotion detection in a string '''
# Importing Flask libraries
from flask import Flask, request, render_template
# Importing Emotion Detection package
from EmotionDetection.emotion_detection import emotion_analyzer

# Define app
app = Flask("Emotion Detection")
app.debug = True

@app.route("/emotionDetector")
def emotion_detector():
    ''' Main emotion analyzer function'''
    # Get request argument
    text_to_analyze = request.args.get('textToAnalyze')
    # Run emotion analysis
    res = emotion_analyzer(text_to_analyze)
    # Prepare response
    dominant_emotion = res['dominant_emotion'] # set dominant emotion
    del res['dominant_emotion'] # remove from the dict
    res = str(res)[1:-1] # remove brackets { }
    # Prepare the output string
    res_1 = f"For the given statement, the system response is {res}. "
    res_2 = f"The dominant emotion is {dominant_emotion}."
    res = res_1 + res_2
    # Handle response in case of Bad request - 400 => no dominant emotion
    if dominant_emotion is None:
        return "Invalid text! Please try again!", 400
    # Return sentiment if request is OK - 200
    return res

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main page'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
