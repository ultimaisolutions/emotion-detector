"""
Server module for Emotion Detection application.
Provides Flask routes for emotion analysis functionality.
"""
from flask import Flask, render_template, request
from emotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route('/')
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_analysis_function():
    """
    Analyze emotion from text input.
    Returns formatted emotion analysis results.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid Text, try again!"

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again"
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is: {response['dominant_emotion']}"
    )

    return formatted_response
    