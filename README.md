# Fetch-Assignment
Solution to the Assignment Problem

## Overview

This script reads transactions data from a CSV file (transactions.csv) and calculates point balance of each payer. The output is a dictionary with payer names as keys and their point balances as values.

## Requirements
Python 3

## Input

The input is a CSV file (transactions.csv) with three columns: payer, points, and timestamp.

payer: The name of the payer as a string.

points: The number of points spent or received as an integer.

timestamp: The date and time of the transaction in the format YYYY-MM-DDTHH:MM:SSZ.


## Usage

The script takes one command-line argument, the spend_amount, which is an integer representing the amount of points the user wants to spend.

```bash
python main.py {spend_amount}
```

## Output

The output is a dictionary with payer names as keys and their point balances as values.

![image](https://user-images.githubusercontent.com/31534762/216580895-1ef85804-f1d3-4274-b800-9fdad07f5db9.png)



## Note
The script assumes that the transactions.csv file is located in the same directory as the script.
