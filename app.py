from flask import Flask, request, jsonify
import pprint

from nlp.parser import process_parse

app = Flask(__name__)


@app.route("/api/test", methods=["POST"])
def exstract_test():
    data = request.json
    message = str(data.get("message"))
    parsed_message_dict = process_parse(message)
    return jsonify(vars(parsed_message_dict))


if __name__ == "__main__":
    app.run(debug=True)
