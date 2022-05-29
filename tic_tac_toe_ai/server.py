from flask import Flask
# import dbconnect

app = Flask(__name__)


@app.route("/TicTacToeFlaskReact")
def game():
    return {1: [1, 1, 1, 1, 0], 2: [1, 1, 1, 1, 0], 3: [1, 1, 1, 1, 0], 4: [1, 1, 1, 1, 0], 5: [1, 1, 1, 1, 0]}


if __name__ == "__main__":
    # This file runs all the logic
    # flow = dbconnect.build_flow()
    # flow.run(parameters={
    #     "path": "/sds/sds/dad.csv"
    # })
    app.run(debug=True)