import csv
import numpy as np
import argparse
import pandas as pd

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str)
    args = parser.parse_args()
    if args.command == "start":
        arr = np.array([[np.random.randint(1, 100) for _ in range(10)] for _ in range(300)])
        with open('nums.csv', 'w') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(arr)
    elif args.command == "evens":
        try:
            data = pd.read_csv("nums.csv", delimiter=";", header=None).to_numpy(dtype=int)
            for i in data.flat:
                if i % 2 == 0:
                    print(i, end=', ')
        except FileExistsError:
            print("Please run the command 'start' to generate a csv file")
    else:
        print("Please run the command 'start' to generate a csv file or the command 'evens' to print the even ones")
except:
    print("Please run the command 'start' to generate a csv file or the command 'evens' to print the even ones")