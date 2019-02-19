# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head()


# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both'))
better_event = data['Better_Event'].value_counts(ascending=False).idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(df,column_name):
    country_list=[]
    country_list=list(df.nlargest(10,column_name)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

common = list(set(top_10)&set(top_10_summer)&set(top_10_winter))
print(common)



# --------------
#Code starts here
import matplotlib
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

def labels_plot(ax):
    rects = ax.patches
    plt.ylabel('Number of Medals')
    plt.xlabel('Countries');
    plt.rcParams['figure.figsize']= [20,10]
    font = {'family' : 'arial',
        'weight' : 'regular',
        'size'   : 12}

    matplotlib.rc('font', **font)
    
    for rect in rects:
    # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

    # Number of points between bar and label. Change to your liking.
        space = 5
    # Vertical alignment for positive values
        va = 'center'
    # If value of bar is negative: Place label below bar
        if y_value < 0:
        # Invert space to place label below
            space *= -1
        # Vertically align label at top
            va = 'top'

    # Use Y value as label and format number with one decimal place
        label = "{:.0f}".format(y_value)

    # Create annotation
        plt.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                    # positive and negative values.





index=range(10)
plt.figure(figsize=(20,10))
ax_1=plt.bar(index,summer_df['Total_Summer'])
plt.xticks(index,summer_df['Country_Name'])
plt.title('Top 10 Summer')
labels_plot(ax_1)
plt.show()

plt.figure(figsize=(20,10))
ax_2=plt.bar(index,winter_df['Total_Winter'])
plt.xticks(index,winter_df['Country_Name'])
plt.title('Top 10 Winter')
labels_plot(ax_2)
plt.show()

plt.figure(figsize=(20,10))
ax_3=plt.bar(index,top_df['Total_Medals'])
plt.xticks(index,top_df['Country_Name'])
plt.title('Top 10')
labels_plot(ax_3)
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = list(summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'])[0]

print(summer_max_ratio,summer_country_gold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = list(winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'])[0]

print(winter_max_ratio,winter_country_gold)

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = list(top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'])[0]

print(top_max_ratio,top_country_gold)


# --------------
#Code starts here
data_2 = data
data.drop(data.tail(1).index,inplace=True)
data_1 =data
data = data_2
data_1['Total_Points']= data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']
most_points=data_1['Total_Points'].max()
best_country = data_1.iloc[data_1['Total_Points'].idxmax()]['Country_Name']


# --------------
#Code starts here
best = data[data['Country_Name']== best_country][['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


