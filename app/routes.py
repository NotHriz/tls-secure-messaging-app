# app/routes.py
from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('main', __name__)

messages = []  # in‑memory message list (no database)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    if data and 'text' in data:
        messages.append(data['text'])
        return jsonify({'status': 'ok'}), 200
    return jsonify({'status': 'error'}), 400

@bp.route('/messages')
def get_messages():
    return jsonify(messages)