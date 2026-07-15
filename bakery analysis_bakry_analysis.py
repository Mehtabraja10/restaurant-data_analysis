import pandas as pd
import matplotlib.pyplot as plt


font1 = {'family':'serif','color':'blue','size':15}


bkd=pd.read_csv('Bakery_Data.csv')
print(bkd.info())
bkd['datetime']=pd.to_datetime(bkd['datetime'])

hourly_data= bkd.groupby('hour').agg(total=('total', 'sum')).reset_index()
#print(hourly_data.info())
print(hourly_data.head(9))


plt.bar(hourly_data['hour'], hourly_data['total'])
plt.xlabel('Opening Hour')
plt.ylabel('Total amount of purchases')
plt.title('Total amount of purchases that happened during the hour', fontdict= font1)
plt.show()


day_data=bkd.groupby('day of week').agg(total=('total', 'sum')).reset_index()

print(day_data.to_string())


plt.bar(day_data['day of week'], day_data['total'])
plt.xlabel('Day')
plt.ylabel('Total amount of purchases')
plt.title('Total amount of purchases that happened on Day', fontdict= font1)
plt.show()


food_sales=bkd.loc[:,'angbutter':'merinque cookies'].sum()

print('\n' , food_sales)
plt.figure(figsize=(12, 6))
plt.bar(food_sales.index, food_sales.values)
plt.xlabel('different food items')
plt.ylabel('Total amount of purchases')
plt.title('Total amount of purchases of different food items', fontdict= font1)
plt.xticks( rotation= 45 , ha= 'right' )
plt.show()

drink_sales=bkd.loc[:,'americano':'berry ade'].sum()
print( '\n' , drink_sales)





plt.bar(drink_sales.index, drink_sales.values)
plt.xlabel('different beverage items')
plt.ylabel('Total amount of purchases')
plt.title('Total amount of purchases of different beverage items', fontdict= font1)
plt.show()



bkd['food items']=bkd.loc[:,'angbutter':'merinque cookies'].sum(axis= 1)
bkd['drinks']= bkd.loc[:,'americano':'berry ade'].sum(axis=1)

food_items= bkd['food items'].sum()
print( 'total food items : ', int(food_items))

drink_items=bkd['drinks'].sum()
print( 'total beverage items : ', int(drink_items))


hsd=bkd.groupby('hour').agg( Food_sales=('food items', 'sum'), Drink_sales=('drinks', 'sum')).reset_index()
hsd['%food_sales']=(hsd['Food_sales'] / (hsd['Food_sales'] + hsd['Drink_sales']) )*100
hsd['%drink_sales']=(hsd['Drink_sales'] / (hsd['Food_sales'] + hsd['Drink_sales']) )*100
print(hsd.to_string())


plt.plot(hsd['hour'], hsd['Food_sales'], 'r', label='food')
plt.plot(hsd['hour'], hsd['Drink_sales'], 'g', label='drinks')
plt.xlabel('Hours')
plt.xticks(range(11, 24))
plt.ylabel(' sales')
plt.title('Sales of the food and drink items per hour', fontdict= font1)
plt.legend()
plt.show()




plt.bar(hsd['hour'], hsd['%food_sales'] ,label= "food")
plt.bar(hsd['hour'], hsd['%drink_sales'], bottom=hsd['%food_sales'], label='drinks')
plt.xticks(range(11, 24))
plt.xlabel('Hour')
plt.ylabel('Percentage')
plt.title('100% Stacked chart of food and drinks', fontdict= font1)
plt.legend(loc='upper left', bbox_to_anchor=(1.02,1))
plt.ylim(0,100)
plt.show()
