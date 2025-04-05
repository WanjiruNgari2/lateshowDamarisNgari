from flask import Blueprint, request, jsonify
from .models import db, Episode, Guest, Appearance

main = Blueprint('main', __name__)

@main.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([ep.to_dict() for ep in episodes]), 200

@main.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    ep = Episode.query.get(id)
    if not ep:
        return jsonify({"error": "Episode not found"}), 404

    data = ep.to_dict()
    data["appearances"] = [a.to_dict() for a in ep.appearances]
    return jsonify(data), 200

@main.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests]), 200

@main.route('/appearances', methods=['POST'])
def post_appearance():
    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
    errors = appearance.validate()

    if errors:
        return jsonify({"errors": errors}), 400

    db.session.add(appearance)
    db.session.commit()

    return jsonify(appearance.to_dict()), 201
