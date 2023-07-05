transactions_in_cents = [1000, -450, 7500, -3475, 13000, -8150, 25000, -850, 0, -1125, -600, 102550, -25025, 6500, -3850, -2500, 1875, 4000]

print("Transactions (cents):")
print(transactions_in_cents)

transactions = [transaction / 100 for transaction in transactions_in_cents]
print("Transaction (dollars):")
print(transactions)

transactions.sort()
print(transactions)

deposits = [transaction for transaction in transactions if transaction >= 0]
withdrawals = [transaction for transaction in transactions if transaction < 0]

print("Deposits:")
print(deposits)
print("Withdrawals:")
print(withdrawals)

def invert_negative_num(negative_num):
  positive_num = negative_num * -1
  return positive_num

withdrawals = [invert_negative_num(withdrawal) for withdrawal in withdrawals]

print("Withdrawals (positive values):")
print(withdrawals)

largest_withdrawals = withdrawals[0:5]
print("Largest Withdrawals:")
print(largest_withdrawals)

average_deposit = sum(deposits) / len(deposits)
average_withdrawal = sum(withdrawals) / len(withdrawals)

average_deposit = int(average_deposit)
average_withdrawal = int(average_withdrawal)

print("Average Deposit (int):")
print(average_deposit)
print("Average Withdrawal (int):")
print(average_withdrawal)

balance = sum(transactions)

print("Balance:")
print(balance)