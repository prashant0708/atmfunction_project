from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/pin_request", methods=["POST"])
def atmpin():
    user_pin = int(request.form["pin"])
    machine_pin = 2356
    if machine_pin == user_pin:
        return redirect(url_for("atmaction"))
    else:
        return "Wrong Pin"


@app.route("/atmaction", methods=["POST", "GET"])
def atmaction():
    if request.method == "POST":
        balance_check = request.form.get("balance_check", None)
        print(balance_check)
        money_withdraw = request.form.get("money_withdraw", None)
        money_deposit = request.form.get("money_deposit", None)
        return render_template(
            "ATM_function.html",
            balance_check=balance_check,
            money_withdraw=money_withdraw,
            money_deposit=money_deposit,
        )
    return render_template("ATM_function.html")


Bank_Balance = 55000


@app.route("/action/input", methods=["POST"])
def action():
    input1 = request.form.get("balance_check")

    input2 = request.form.get("money_deposit")
    input3 = request.form.get("money_withdraw")
    if input1:
        result = Bank_Balance
        return render_template("balance.html", result=result)
    elif input2:
        return redirect(url_for("moneydeposit"))

    elif input3:
        return redirect(url_for("moneywidrawl"))
    else:
        return f"Not going to the loop{input1}"


@app.route("/moneydeposit", methods=["POST", "GET"])
def moneydeposit():
    return render_template("money_deposit.html")


@app.route("/deposit", methods=["POST", "GET"])
def deposit():
    if request.method == "POST":
        amount = int(request.form["Amount"])
        total_amount = amount + Bank_Balance
        return render_template("balance.html", result=total_amount)
    else:
        return render_template("ATM_function.html")


@app.route("/moneywidrawl", methods=["POST", "GET"])
def moneywidrawl():
    return render_template("money_withdraw.html")


@app.route("/withdraw", methods=["POST", "GET"])
def withdraw():
    if request.method == "POST":
        amount = int(request.form["Amount"])
        total_amount = Bank_Balance - amount
        return render_template("balance copy.html", amount=amount, result=total_amount)
    else:
        return render_template("ATM_function.html")


if __name__ == "__main__":
    app.run(debug=True)
