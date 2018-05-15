# Points Table Predictor
A python script that helps to predict the chances of a team to qualify to next round in a tournament.
### How to use
```sh
$ python predict.py
```
### Requirements
1) pTable.csv   : It contains the current points table scenario in the tournament . 
2) fixtures.csv : It contains the remaining fixtures between teams left in the tournament.


This script assumes that there is no change in NRR in the course of the tournament which is not an ideal case.Can improve this code by analysing the change in NRR during wins and defeats of each team to estimate a tentative final NRR which can result in a more optimised prediction.
