from flask import Blueprint, jsonify

insurance_bp = Blueprint("insurance", __name__)

# Sample insurance data
INSURANCE_POLICIES = [
    {"id": 1, "name": "Basic Health Plan", "coverage": "$10,000", "premium": "$50/month"},
    {"id": 2, "name": "Comprehensive Health Plan", "coverage": "$50,000", "premium": "$150/month"},
    {"id": 3, "name": "Family Health Plan", "coverage": "$100,000", "premium": "$250/month"},
]

@insurance_bp.route("/policies", methods=["GET"])
def get_policies():
    return jsonify({"policies": INSURANCE_POLICIES})

@insurance_bp.route("/policy/<int:policy_id>", methods=["GET"])
def get_policy(policy_id):
    policy = next((p for p in INSURANCE_POLICIES if p["id"] == policy_id), None)
    if not policy:
        return jsonify({"error": "Policy not found"}), 404
    return jsonify({"policy": policy})
