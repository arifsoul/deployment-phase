from flask import Flask, request, jsonify, render_template
import torch
import torchvision.transforms as transforms
from PIL import Image
import psycopg2


conn = psycopg2.connect(
    host="localhost",  # ganti dengan nama host PostgreSQL
    database="ai_dev",  # ganti dengan nama database PostgreSQL
    user="postgres",  # ganti dengan nama user PostgreSQL
    password="superuserpwd"  # ganti dengan password user PostgreSQL
)


# Load model
model = torch.load('model/model.pt')

# Define Flask app
app = Flask(__name__)

# Define class names
class_names = [
    'airplane',
    'automobile',
    'bird',
    'cat',
    'deer',
    'dog',
    'frog',
    'horse',
    'ship',
    'truck'
]

# Define image transforms
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

# Define route for home page


@app.route('/')
def home():
    return render_template('index.html')

# Define route for image upload


@app.route('/predict', methods=['POST'])
def predict():
    # Get uploaded image
    file = request.files['image']
    img = Image.open(file.stream)

    # Apply transforms to image
    img = transform(img)

    # Add batch dimension to image
    img = img.unsqueeze(0)

    # Disable gradients
    with torch.no_grad():
        # Predict class probabilities
        output = model(img)
        probs = torch.nn.functional.softmax(output, dim=1)[0]

        # Get predicted class index
        pred_class_idx = torch.argmax(output).item()

        # Get predicted class name
        pred_class_name = class_names[pred_class_idx]

    # Create dictionary of results
    dict_prob = {class_names[i]: round(float(probs[i]), 4)
                 for i in range(len(probs))}
    results = {
        'class_name': pred_class_name,
        'class_probs': dict_prob
    }

    # Save prediction to database
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO predictions (class_name, class_probs)
        VALUES (%s, %s)
        """, (pred_class_name, str(results['class_probs'])))
    conn.commit()

    # Return results as JSON
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
    conn.close()
