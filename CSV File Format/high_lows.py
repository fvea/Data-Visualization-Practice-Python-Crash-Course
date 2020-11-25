import csv 

from matplotlib import pyplot as plt 

from datetime import datetime

plt.style.use('fivethirtyeight')

filename = 'death_valley_2014.csv'
# Get High Temps and Date from File.
with open(filename) as f: 
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs, dates,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f'{current_date} : missing data!')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data. 
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,color='red',alpha=0.5,label='High Temps',linewidth=2)
plt.plot(dates,lows,color='blue',alpha=0.5,label='Low Temps',linewidth=2)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Format plot. 
title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
plt.title(title)
plt.xlabel('')
fig.autofmt_xdate()
plt.ylabel('Temperature (F)')
#plt.tick_params(axis='both',which='majors',labelsize=16)


plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

