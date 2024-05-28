from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image
import io
import base64
import numpy as np

app = Flask(__name__)

# Load the YOLOv8n model
model = YOLO('model/best.pt')

@app.route('/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    image = Image.open(file.stream)

    # Convert image to numpy array
    image = np.array(image)

    # Perform object detection
    results = model(image)
    print(results)

    # Convert detection results to JSON format
    detections = []
    for result in results:
        for box in result.boxes:
            detections.append({
                'class': result.names[box.cls.item()],
                'confidence': float(box.conf),
                'bbox': box.xyxy.tolist()  # [x1, y1, x2, y2]
            })

    return jsonify(detections)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <title>YOLOv8 Object Detection</title>
    <h1>Upload an Image for Object Detection</h1>
    <form method="POST" action="/detect" enctype="multipart/form-data">
      <input type="file" name="image">
      <input type="submit" value="Upload">
    </form>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
