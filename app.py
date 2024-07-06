from flask import Flask, render_template, send_from_directory
import os

# Initialize Flask app
app = Flask(__name__, template_folder='.', static_folder='')

# Route for the home page
@app.route("/")
def home():
    return render_template('index2.html')

# Route to serve styles2.css
@app.route('/styles2.css')
def styles():
    return send_from_directory(app.root_path, 'styles2.css')

# Route to serve images from the images folder
@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(os.path.join(app.root_path, 'images'), filename)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
