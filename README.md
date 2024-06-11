## Instructions
Run this command in the project directory, the output files for each deliverable will be `legislators-support-oppose-count.csv` and `bills-support-oppose-count.csv`
```bash
python app.py
```

## [Answers] - Writeup questions
1. The time complexity for the solution would be O(B+L+V+VR), where each letter consists of the datasets provided by the challenge. We can break down our solution in 3 parts:
    - Reading each dataset has a O(n) time complexity, where n is the length of each dataset
    - Each `for loop` has a O(VR) time complexity, where VR is the length of the `vote_results` dataset since everything will use the features of a hashmap in Python dictionaries, making search operations become O(1).
    - Each export operations iterates over the whole dataset provided in the data parameter, so it has a O(n) time complexity, where n is the length of the data provided

    The main tradeoff of my current solution would be the lack of flexibility for drastic changes in the datasets, since I tailor-made it to this particular problem, transforming the `list of dictionaries` to `dictionaries`, because they are more performant for searching.
2. I will assume "Bill Voted On Date" is a column added to `votes.csv` and "Co-Sponsors" is a new table column added to `bills.csv` . In this case, I can just modify the input data by inserting new keys into my dictionaries and proceed with other analyses. 
3. The initial part of my solution already transforms the csv data into a list of dictionaries, so my solution would be simpler, with no csv read, since I already have the list of each entry as input.
4. I took a little bit more than 1 hour to work on the implementation.