import csv 
from datetime import datetime

from matplotlib import pyplot as plt 


with open('death_valley_2014.csv') as csv_obj: 
    csv_reader = csv.reader(csv_obj)
    header_row = next(csv_reader)

    #for index,col_header in enumerate(header_row): 
        #print(f'{index} : {col_header}')

    highs,dates,lows = [],[],[]
    for row in csv_reader: 
        try: 
            high = int(row[7])
            low = int(row[9])
            date = datetime.strptime(row[0],'%Y-%m-%d')
        except ValueError: 
            pass
        else: 
            highs.append(high)
            lows.append(low)
            dates.append(date)



# Plot data.
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,color='red',linewidth=2,label='Max Humidity',alpha=0.5)
plt.plot(dates,lows,color='blue',linewidth=2,label='Min Humidity',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
fig.autofmt_xdate()
plt.title('Humidity Amount - 2014\nDeath Valley, CA')
plt.xlabel('')
plt.ylabel('Humidity Amount')
plt.legend()
plt.show()