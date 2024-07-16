# PyBank and PyPoll Analysis

This project contains two Python scripts designed to analyze financial records (PyBank) and election results (PyPoll) for a small U.S. town.

## PyBank
The PyBank script analyzes financial records to calculate the following:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

### PyBank Script Usage
To run the PyBank analysis:

1. Ensure the `PyBank/Resources/budget_data.csv` file is located in the `Resources` directory.
2. Run the `PyBank/main.py` script.
3. The results will be saved in `pybank_analysis.txt`.

## PyPoll
The PyPoll script analyzes election data to calculate the following:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

### PyPoll Script Usage
To run the PyPoll analysis:

Ensure the `PyPoll/Resources/election_data.csv` file is located in the `Resources` directory.
Run the `PyPoll/main.py` script.
