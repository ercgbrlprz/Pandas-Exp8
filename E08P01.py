import pandas as pd

cars = pd.read_csv('cars.csv')
firstFive = cars.head()
lastFive = cars.tail()