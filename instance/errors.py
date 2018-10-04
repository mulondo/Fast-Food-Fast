class Errors_msg:

    def not_found():
        result = {
        "message": "The requested resource is not found"
        }
        return jsonify(result), 404
    def bad_request():
        result = {
        "message": "Incorrect request, please check your inputs"
        }
        return jsonify(result), 400
    def internal_server_error():
        result = {
        "message": "Unable to process your request"
        }
        return jsonify(result),500

    def method_not_allowed():
        result = {"message":"Rejected request"}
        return jsonify(result), 405

