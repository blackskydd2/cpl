def equalize_expenses(n, expenses):
    total_expenses = sum(expenses)
    average_expense = total_expenses / n
    exchange = 0
    for expense in expenses:
        if expense < average_expense:
            exchange += average_expense - expense
    return "${:.2f}".format(exchange)

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        expenses = [float(input()) for _ in range(n)]
        result = equalize_expenses(n, expenses)
        print(result)

if __name__ == "__main__":
    main()
