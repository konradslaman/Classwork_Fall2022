from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


@app.route("/info", methods=["GET"])
def information():
    x = "This webstite will calculate blood cholesterol levels. \n"
    x += "It is written by Konrad Slaman."
    return x


@app.route("/hdl_check", methods=["POST"])
def hdl_check():
    """
        incoming_json =  {"name": <name_str>,
                          "hdl_value": <hdl_value_int>}
    """
    from blood_calculator import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    answer = check_HDL(hdl_value)
    return answer


@app.route("/add_numbers", methods=["POST"])
def add_numbers():
    in_data = request.get_json()
    try:
        firstNum = float(in_data['a'])
        secondNum = float(in_data['b'])
    except TypeError:
        return jsonify("Not a valid pair of numbers")
    else:
        added = firstNum + secondNum
        return jsonify(added)


if __name__ == '__main__':
    app.run()
