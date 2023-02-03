import csv
import sys
import datetime


def spend_points(transactions, spend_amount):
    payer_points = {}
    transactions = sorted(transactions, key=lambda x: x[2])

    for transaction in transactions:
        payer, points, timestamp = transaction
        if payer not in payer_points:
            payer_points[payer] = 0
        if(points < 0):
            spend_amount += -(points)

    for transaction in transactions:
        payer, points, timestamp = transaction

        if (points < 0):
            points = 0
        else:
            if (spend_amount >= points):
                spend_amount -= points
                points = 0
            else:
                points -= spend_amount
                spend_amount = 0
        payer_points[payer] += points
    return payer_points


def main(spend_amount):
    transactions = []
    try:
        with open('transactions.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                payer = row[0]
                points = int(row[1])
                timestamp = datetime.datetime.strptime(row[2], "%Y-%m-%dT%H:%M:%SZ")
                transactions.append((payer, points, timestamp))
    except FileNotFoundError:
        print("Error: The file 'transactions.csv' could not be found.")
        return
    except csv.Error:
        print("Error: There was an error reading the CSV file.")
        return
    except ValueError:
        print("Error: Incorrect format for timestamp in the CSV file.")
        return
    except Exception as e:
        print("Error: An unexpected error occurred:", str(e))
        return

    try:
        result = spend_points(transactions, spend_amount)
    except Exception as e:
        print("Error: An unexpected error occurred:", str(e))
        sys.exit()
    print(result)


if __name__ == '__main__':
    try:
        spend_amount = int(sys.argv[1])
    except IndexError:
        print("Error: The spend amount is not provided as the command-line argument.")
        sys.exit()
    except ValueError:
        print("Error: The spend amount should be an integer.")
        sys.exit()
    except Exception as e:
        print("Error: An unexpected error occurred:", str(e))
        sys.exit()

    main(spend_amount)
