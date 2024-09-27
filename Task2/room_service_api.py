import json
import os
from flask import Flask, request, jsonify
from threading import Lock
from uuid import uuid4
from functools import wraps

app = Flask(__name__)
DATA_FILE = 'requests.json'
file_lock = Lock()

def error_handler(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except FileNotFoundError:
            return jsonify({'error': 'Data file not found'}), 500
        except json.JSONDecodeError:
            return jsonify({'error': 'Invalid JSON data'}), 500
        except KeyError as e:
            return jsonify({'error': f'Missing required field: {str(e)}'}), 400
        except Exception as e:
            return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500
    return decorated_function

def read_requests():
    with file_lock:
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, 'r') as f:
            return json.load(f)

def write_requests(requests):
    with file_lock:
        with open(DATA_FILE, 'w') as f:
            json.dump(requests, f, indent=2)

@app.route('/requests', methods=['POST'])
@error_handler
def create_request():
    data = request.json
    new_request = {
        'id': str(uuid4()),
        'guestName': data['guestName'],
        'roomNumber': data['roomNumber'],
        'requestDetails': data['requestDetails'],
        'priority': data['priority'],
        'status': 'received'
    }
    requests = read_requests()
    requests.append(new_request)
    write_requests(requests)
    return jsonify(new_request), 201


# Sorting data based on priority first and then on status !
@app.route('/requests', methods=['GET'])
@error_handler
def get_all_requests():
    requests = read_requests()

    status_order = {
        'received': 0,
        'in progress': 1,
        'awaiting confirmation': 2,
        'completed': 3,
        'canceled': 4
    }

    def sort_key(x):
        status = x.get('status', 'unknown')
        priority = x.get('priority', 'unknown')
        return (status_order.get(status, 999), status_order.get(priority, 999))

    sorted_requests = sorted(requests, key=sort_key)
    return jsonify(sorted_requests)


@app.route('/requests/<string:request_id>', methods=['GET'])
@error_handler
def get_request(request_id):
    requests = read_requests()
    request = next((req for req in requests if req['id'] == request_id), None)
    if request:
        return jsonify(request)
    return jsonify({'error': 'Request not found'}), 404

@app.route('/requests/<string:request_id>', methods=['PUT'])
@error_handler
def update_request(request_id):
    data = request.json
    requests = read_requests()
    for req in requests:
        if req['id'] == request_id:
            req.update(data)
            write_requests(requests)
            return jsonify(req)
    return jsonify({'error': 'Request not found'}), 404

@app.route('/requests/<string:request_id>', methods=['DELETE'])
@error_handler
def delete_request(request_id):
    requests = read_requests()
    requests = [req for req in requests if req['id'] != request_id]
    write_requests(requests)
    return 'Deleted successfully !', 200

@app.route('/requests/<string:request_id>/complete', methods=['POST'])
@error_handler
def complete_request(request_id):
    requests = read_requests()
    for req in requests:
        if req['id'] == request_id:
            req['status'] = 'completed'
            write_requests(requests)
            return jsonify(req)
    return jsonify({'error': 'Request not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
