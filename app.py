# Import the Flask module
from flask import Flask, Response, request,render_template

# Import the subprocess module
import subprocess

# Import the time module
import time

# Create a Flask app
app = Flask(__name__)

# Define a function to run the command for object detection and tracking
#---------------------------------------------------------------------
def run_command():
    """
    Run the command for object detection and tracking using the YOLOv7 model
    and source 1 (webcam).

    Returns:
        str: The output or error message from the subprocess.
    """
    # Define the command to run
    command = "python detect_and_track.py --weights yolov7.pt --source 1"

    # Create a subprocess to run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    # Get the output and error from the subprocess
    output, error = process.communicate()

    # Check if there was an error
    if error:
        # Return the error as a string
        return str(error)
    else:
        # Return the output as a string
        return output.decode()

# Define a route for the home page
#---------------------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Handle GET and POST requests for the home page.

    Returns:
        str or render_template: The response to send to the client.
    """
    # Check if the request method is POST
    if request.method == 'POST':
        # Check if the start button was clicked
        if request.form.get('start'):
            # Create a global variable for the subprocess
            global process

            # Define the command to run
            command = "python detect_and_track.py --weights yolov7.pt --source 1"

            # Create a subprocess to run the command
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

            # Return a message indicating that tracking has started
            return "Tracking started"

        # Check if the stop button was clicked
        elif request.form.get('stop'):
            # Terminate the subprocess
            process.terminate()

            # Return a message indicating that tracking has stopped
            return "Tracking stopped"

    # Render the index.html template
    return render_template('index.html')
# Create a Flask app
# Define a function to run the command for object detection and tracking
#---------------------------------------------------------------------
def run_command():
    """
    Run the command for object detection and tracking using the YOLOv7 model
    and source 1 (webcam).

    Returns:
        str: The output or error message from the subprocess.
    """
    # Define the command to run
    command = "python detect_and_track.py --weights yolov7.pt --source 1"

    # Create a subprocess to run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

    # Get the output and error from the subprocess
    output, error = process.communicate()

    # Check if there was an error
    if error:
        # Return the error as a string
        return str(error)
    else:
        # Return the output as a string
        return output.decode()

# Define a route for the home page
#---------------------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Handle GET and POST requests for the home page.

    Returns:
        str or render_template: The response to send to the client.
    """
    # Check if the request method is POST
    if request.method == 'POST':
        # Check if the start button was clicked
        if request.form.get('start'):
            # Create a global variable for the subprocess
            global process

            # Define the command to run
            command = "python detect_and_track.py --weights yolov7.pt --source 1"

            # Create a subprocess to run the command
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

            # Return a message indicating that tracking has started
            return "Tracking started"

        # Check if the stop button was clicked
        elif request.form.get('stop'):
            # Terminate the subprocess
            process.terminate()

            # Return a message indicating that tracking has stopped
            return "Tracking stopped"

    # Render the index.html template
    return render_template('index.html')

# Define the main block to run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')