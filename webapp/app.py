from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Endpoint 1: /ping returns pong
@app.route('/ping', methods=['GET'])
def ping():
    """Returns 'pong' to check if the service is running."""
    return "pong"

# Endpoint 2: /system-info returns content of /etc/os-release
@app.route('/system-info', methods=['GET'])
def system_info():
    """Returns the content of the /etc/os-release file."""
    try:
        with open('/etc/os-release', 'r') as f:
            content = f.read()
        return jsonify({"os-release": content})
    except FileNotFoundError:
        return jsonify({"error": "/etc/os-release not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint 3: /home returns content of the user's home directory
@app.route('/home', methods=['GET'])
def home_directory():
    """Returns a list of files and directories in the user's home directory."""
    try:
        # Get the path to the current user's home directory
        home_dir = os.path.expanduser('~')
        items = os.listdir(home_dir)
        
        # You might want to filter or format the list for security/readability
        return jsonify({"home_directory_contents": items})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


