import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('seaborn')

## Load in the car data csv file
data = pd.read_csv('auto-mpg.csv')

## Take a look at the dataframe
#print(data.head(19))
#print(data.info())

#describe the dataframe

#print(data.describe())

## Getting the headers
headers = data.columns
#print(headers)


### Data cleaning ###

#checking for null values
#getting value options for every column using value_counts
for column in data.columns:
    #print(column)
    #print(data[column].value_counts())
    pass

missing_values = data.isna()

for val in missing_values.columns.values.tolist():
    #print(val)
    #print(missing_values[val].value_counts())
    pass



#getting the mean of horsepower
avg_HP = data['horsepower'].mean()
#print(avg_HP)

## replacing null values with the mean(average)
#data['horsepower'].replace(null, avg_HP, inplace=True)

#replacing null values that are not numbers
'''
    this can be done by find the maximum used value
'''
#getting the most used value
avg_carName = data['car_name'].value_counts()
avg_carName_id = avg_carName.idxmax()

#replacing
#data['car_name'].replace(null, avg_carName_id, inplace=True)

## Adding more columns to dataframe
#converting mpg to L/100km (divde 235 by mpg)
data['L/100km'] = 235/data['mpg']
#print(data.head(19))

#Binning
data['horsepower'] = data['horsepower'].astype(int, copy=True)
bins = np.linspace(min(data['horsepower']), max(data['horsepower']), 4)
groups = ['Low', 'Medium', 'High']
data['HP range'] = pd.cut(data['horsepower'], bins, labels=groups, include_lowest=True)
#print(data[['horsepower', 'HP range']].head(35))
#print(data['HP range'].value_counts())



### Working with the dataframe

##Q1 which cars has the highest horsepower(the fastest)
hp_max_val = data['horsepower'].values.max()
#print(hp_max_val)
cars_maxHP = data.loc[data['horsepower']==hp_max_val]
#print(cars_maxHP.head())
'''
    Plotting the fastest cars
'''
f_cars = data.loc[data['HP range'] == 'High']
f_cars = f_cars.reset_index(drop=True)
#print(f_cars)
f_cars1 = f_cars.drop_duplicates(subset=['car_name'])
#print(f_cars1)

# Rearanging the columns and saving
cols = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
       'acceleration', 'model_year', 'origin', 'car_name', 'L/100km',
       'HP range']
f_cars1 = f_cars1[[cols[8]] + cols[6:8] + cols[0:6] + cols[9:11]]    
# print(f_cars1)
# f_cars1.to_excel('Cars with the most HP.xlsx', index=False)


# plt.bar(f_cars1['car_name'], f_cars1['horsepower'])
# plt.xticks(f_cars1['car_name'], rotation='vertical', size=8)
# plt.title('Cars with their HP')
# plt.xlabel('Car Names')
# plt.ylabel('Horse Power', rotation='vertical')
# plt.grid(True, color='black')
# plt.show()



## Q2 which cars has the most breaking (smallest displacement)455+68

# break_max_val = data['displacement'].min()
# print(break_max_val)
# print(data.describe())
# break_max = data.loc[data['displacement']==break_max_val]
# print(break_max.head())

# break_range = data.loc[data['displacement'] <= data['displacement'].mean()]
# print(break_range.drop_duplicates(subset=['car_name']))

'''
    Plotting the fastest breaking
'''
#re_data = data[::-1]#To reverse the dataframe
#carName2 = f_cars1['car_name'].unique()

# plt.bar(break_range['car_name'], break_range['displacement'])
# plt.xticks(break_range['car_name'], rotation='vertical', size=8)
# plt.title('Cars with most breaking')
# plt.xlabel('Car Names')
# plt.ylabel('Displacement', rotation='vertical')
# plt.grid(True, color='black')
# plt.show()



##Q3 which car has the highest acceleration
accel_max_val = data['acceleration'].max()
# print(accel_max_val)

accel_max = data.loc[data['acceleration']==accel_max_val]
# print(accel_max.head())

acc_range = data.loc[data['acceleration']>=17]
# print(acc_range)

a_cars = acc_range.drop_duplicates(subset=['acceleration'])
a_cars.reset_index(drop=True, inplace=True)
# print(a_cars.columns)

# Rearanging the columns and saving
cols = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
       'acceleration', 'model_year', 'origin', 'car_name', 'L/100km',
       'HP range']
a_cars = a_cars[[cols[8]] + cols[6:8] + cols[0:6] + cols[9:11]]    
# print(a_cars)
# a_cars.to_excel('Cars with the most acceleration.xlsx', index=False)

'''
    Plotting the fastest acceleration
'''
# plt.bar(a_cars['car_name'], a_cars['acceleration'])
# plt.xticks(a_cars['car_name'], rotation='vertical', size=8)
# plt.title('Cars with the most Acceleration')
# plt.xlabel('Car Names')
# plt.ylabel('Acceleration', rotation='vertical')
# plt.grid(True, color='black')
# plt.show()


##Q4 which car has the most weight
car_weightMax = data['weight'].max() 
print(car_weightMax)
# print( data['weight'].describe() )
car_weight = data.loc[data['weight'] >= 4614 ] # added 1000 to the 75% 
car_weight.reset_index(drop=True, inplace=True)
# print(car_weight)

# Rearanging the columns and saving
cols = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
       'acceleration', 'model_year', 'origin', 'car_name', 'L/100km',
       'HP range']
car_weight = car_weight[[cols[8]] + cols[6:8] + cols[:6] + cols[9:11]]
  
# car_weight.to_excel('Car with the most weight.xlsx', index=False)

'''
    Plotting the most weight
'''
# plt.bar(car_weight['car_name'], car_weight['weight'])
# plt.xticks(car_weight['car_name'], rotation='vertical', size=8)
# plt.title('Cars with the most Weight')
# plt.xlabel('Car Names')
# plt.ylabel('Weight', rotation='vertical')
# plt.grid(True, color='black')
# plt.show()


##Q5 which car has the best fuel comsumption(mpg or L/100km)
b_fuel = data['mpg'].max()
print(b_fuel)

##Q6a which hp range has the most number of cars
''' To get the number of cars in each hp range, state the range and the count for each '''
range_ = ['Low', 'Medium', 'High']
# plt.bar(range_, data['HP range'].value_counts())
# plt.title('Horsepower Range')
# plt.xlabel('Range')
# plt.ylabel('Number of cars')
# plt.grid(True, color='black')
#plt.show()


##Q6b which HP has the most number of cars
''' Using the  HP values '''
# plt.hist(data['horsepower'], bins=5)
# plt.title('Horsepower Range Defined')
# plt.xlabel('Horse Power')
# plt.ylabel('Number of cars')
# plt.grid(True, color='black')
# plt.show()



##Q7 what is the relationship b/w the cylinders and the horsepower, the displacement and the acceleration
rel_cyl_hp = data[['cylinders', 'horsepower']].corr()
print(rel_cyl_hp)

rel_dis_acc = data[['displacement', 'acceleration']].corr()
print(rel_dis_acc)

rel_hp_acc = data[['horsepower', 'acceleration']].corr()
print(rel_hp_acc)


