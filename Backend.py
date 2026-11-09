from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

transactions_db = []



@app.route("/")
@app.route("/Overview")
def overview():
    total_income = 0.0
    total_spending = 0.0

    for t in transactions_db:
        amount = float(t.get('amount', 0))

        if t.get("type") == "income":
            total_income += amount
        elif t.get("type") == "spending":
            total_spending += amount

    net_income = total_income - total_spending
    total_balance = net_income

    return render_template("Overview.html",
        transactions=transactions_db[::-1],
        total_balance=total_balance,
        total_income=total_income,
        total_spending=total_spending,
        net_income=net_income
    )
@app.route("/Transactions")
def transactions():
    return render_template("Transaction.html")

@app.route("/add_transactions", methods=["GET", "POST"])
def add_transactions():
    if request.method == "POST":
        t_type = request.form.get("type")
        amount = request.form.get("amount")
        date = request.form.get("date")
        description = request.form.get("description")
        category = request.form.get("category")
        account = request.form.get("account")


        transactions_db.append({
            "type": t_type,
            "amount": amount,
            "date": date,
            "description": description,
            "category": category,
            "account": account

        })
    
        print("Uus transaktsioon", transactions_db[-1])

        return redirect(url_for("overview"))
    
    return render_template("Transaction.html")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()