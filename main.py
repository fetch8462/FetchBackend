from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


transactions = []
balances = {}

@app.route('/add', methods=['POST'])
def add_points():
    transaction = request.get_json()

    payer = transaction.get('payer')
    points = transaction.get('points')
    timestamp = transaction.get('timestamp')
    
    transaction_datetime = datetime.fromisoformat(timestamp)
    
    index = 0
    for existing_transactions in transactions:
        existing_datetime = datetime.fromisoformat(existing_transactions['timestamp'])
        if transaction_datetime < existing_datetime:
            break
        index += 1

    transactions.insert(index, transaction)

    if payer in balances:
        balances[payer] += points
    else:
        balances[payer] = points

    return '', 200

@app.route('/spend', methods=['POST'])
def spend_points():
    data = request.get_json()
    cost = data.get('points')

    total_points = 0
    for points in balances.values():
        total_points += points
    
    if cost > total_points:
        return "This user does not have enough points!", 400
    

    response = []
    for transaction in transactions:    
        points = transaction.get('points')
        payer = transaction.get('payer')
        if points - cost < 0:
            balances[payer] = balances[payer] - points
            cost = cost - points
            
            exists = False
            for i, subtractions in enumerate(response):
                if subtractions.get("payer") == payer:
                    response[i]['points'] = response[i]['points'] - points
                    exists = True
                    break
            
            if not exists:
                response.append({"payer": payer, "points": -points})
    
        else:
            balances[transaction.get('payer')] = balances[transaction.get('payer')] - cost
            exists = False
            for i, subtractions in enumerate(response):
                if subtractions.get("payer") == payer:
                    response[i]['points'] = response[i]['points'] - cost

                    exists = True
                    break
            
            if not exists:
                response.append({"payer": payer, "points": -cost})

            break
    return jsonify(response), 200


@app.route('/balance')
def current_balance():
    return jsonify(balances), 200

if __name__ == "__main__":
    app.run(debug=True, port = 8000)
