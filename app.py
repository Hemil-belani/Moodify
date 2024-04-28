import base64
from flask import Flask, render_template, request, jsonify, redirect, url_for
import cv2
import numpy as np
import webbrowser
from inference import perform_inference

app = Flask(__name__)

# Route for serving the landing page
@app.route('/')
def landing_page():
    return render_template('land.html')

# Route for serving the inference page
@app.route('/inference')
def inference_page():
    return render_template('inference.html')

# Route for capturing the face and performing inference
@app.route('/capture-face', methods=['POST'])
def capture_face():
    # Assuming the image data is sent as a base64-encoded string in the request body
    image_data = request.json['image_data']
    
    # Convert base64 image data to OpenCV image
    nparr = np.frombuffer(base64.b64decode(image_data.split(',')[1]), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Perform inference to detect emotion
    emotion_prediction = perform_inference(image)
    
    # Redirect to Spotify based on the detected emotion
    return redirect(url_for('recommend_songs', emotion=emotion_prediction))

# Route for recommending songs based on detected emotion
#@app.route('/recommend-songs/<emotion>', methods=['GET'])
#def recommend_songs(emotion):
    # Redirect to Spotify search page with the detected emotion as a query parameter
    # Replace the URL with the appropriate Spotify search endpoint URL
    #spotify_url = f"https://open.spotify.com/search/{emotion}"
    #webbrowser.open_new_tab(spotify_url)
   # return redirect(url_for('landing_page'))  # Redirect back to the landing page
   # Route for recommending songs based on detected emotion
@app.route('/recommend-songs/<emotion>', methods=['GET'])
def recommend_songs(emotion):
    # Dictionary mapping emotions to Spotify playlist URLs
    playlist_urls = {
        'happy': 'https://open.spotify.com/playlist/4l7S8jYce53k5qriDma6Ha?si=8b0334225ade4ca8',
        'sad': 'https://open.spotify.com/playlist/06UM7loEdJCss4orDOb4XJ?si=acc8328860534a5b',
        'energetic': 'https://open.spotify.com/playlist/your_energetic_playlist_url',
        # Add more emotions and corresponding playlist URLs as needed
    }
    
    # Check if the detected emotion has a corresponding playlist URL
    if emotion.lower() in playlist_urls:
        # Redirect to the corresponding playlist URL
        webbrowser.open_new_tab(playlist_urls[emotion.lower()])
    else:
        # If no specific playlist URL is found, redirect to the landing page
        return redirect(url_for('landing_page'))


if __name__ == '__main__':
    app.run(debug=True)
