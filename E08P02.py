import pandas as pd

cars = pd.read_csv('cars.csv')
QA = cars.loc[0:4, ['mpg','disp','drat','qsec','am'] ]
QB = cars[cars['Model'] == 'Mazda RX4']
QC = cars.loc[cars['Model'] == 'Camaro Z28' , ['cyl'] ]
QD = cars.loc[(cars['Model'] == 'Mazda RX4 Wag') | (cars['Model'] == 'Ford Pantera L') | 
        (cars['Model'] == 'Honda Civic'), ['cyl','gear'] ]