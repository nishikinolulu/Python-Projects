import timeit
mysetup = '''import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = None
df2 = df.copy()'''

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
loop1 = '''for i in range(0,df2.shape[0]):

    if df2['gluc'][i] == 1:
        df2['gluc'][i] = 0
    else:
        df2['gluc'][i] = 1

for i in range(0,df2.shape[0]):

    if df2['cholesterol'][i] == 1:
        df2['cholesterol'][i] = 0
    else:
        df2['cholesterol'][i] = 1'''

print(timeit.timeit(setup=mysetup,
                    stmt=loop1,
                    number=1))

loop2 = '''for i in range(0,df2.shape[0]):

    if (df['gluc'][i] == 1) & (df['cholesterol'][i] == 1):
        df['gluc'][i] = 0
        df['cholesterol'][i] = 0

    elif (df['gluc'][i] == 1) & (df['cholesterol'][i] != 1):
        df['gluc'][i] = 0
        df['cholesterol'][i] = 1

    elif (df['gluc'][i] != 1) & (df['cholesterol'][i] == 1):
        df['gluc'][i] = 1
        df['cholesterol'][i] = 0

    else:
        df['cholesterol'][i] = 1
        df['gluc'][i] = 1'''

print(timeit.timeit(setup=mysetup,
                    stmt=loop2,
                    number=1))

loop3 = '''gluc0 = (df['gluc'] <= 1)
gluc1 = (df['gluc'] > 1)
df['gluc'][gluc0] = 0
df['gluc'][gluc1] = 1
print(df['gluc'].head(10))

chol0 = (df['cholesterol'] <= 1)
chol1 = (df['cholesterol'] > 1)
df['cholesterol'][chol0] = 0
df['cholesterol'][chol1] = 1'''

print(timeit.timeit(setup=mysetup,
                    stmt=loop3,
                    number=1))



# # Draw Categorical Plot
# def draw_cat_plot():
#     # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
#     df_cat = None


#     # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
#     df_cat = None
    

#     # Draw the catplot with 'sns.catplot()'



#     # Get the figure for the output
#     fig = None


#     # Do not modify the next two lines
#     fig.savefig('catplot.png')
#     return fig


# # Draw Heat Map
# def draw_heat_map():
#     # Clean the data
#     df_heat = None

#     # Calculate the correlation matrix
#     corr = None

#     # Generate a mask for the upper triangle
#     mask = None



#     # Set up the matplotlib figure
#     fig, ax = None

#     # Draw the heatmap with 'sns.heatmap()'



#     # Do not modify the next two lines
#     fig.savefig('heatmap.png')
#     return fig
 