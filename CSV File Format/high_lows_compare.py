""" Sitka-Death Valley Comparison """

from datetime import datetime 
import csv 

from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

def get_weather_date(filename,highs,lows,dates): 
    with open(filename) as f: 
        reader = csv.reader(f)
        header_row = next(reader)
    
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


# Get Death Valley Dataset.
highs,lows,dates = [],[],[]
get_weather_date('death_valley_2014.csv',highs,lows,dates)

# Plot Death Valley Dataset. 
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,color='red',alpha=0.3,linewidth=2)
plt.plot(dates,lows,color='blue',alpha=0.3,linewidth=2)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.05,label='Death Valley, CA Temp Range')

# Get Sitka Dataset.
highs,lows,dates = [],[],[]
get_weather_date('sitka_weather_2014.csv',highs,lows,dates)

# Plot Death Valley Dataset. 
plt.plot(dates,highs,color='red',alpha=0.6,linewidth=2)
plt.plot(dates,lows,color='blue',alpha=0.6,linewidth=2)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.15,label='Sitka, Ak Temp Range')


# Format Plot.
title = 'Daily high and low temperatures - 2014'
title += '\nSitka, Ak and Death Valley, CA'
plt.title(title)
plt.ylabel('Temperatures (F)')
plt.ylim(10,120)
fig.autofmt_xdate()
plt.legend()

plt.show()




