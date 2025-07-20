import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = (df['weight']/((df['height']/100)**2)).apply(lambda bmi: 1 if bmi > 25 else 0)

# 3
df['cholesterol'] = (df['cholesterol']).apply(lambda x : 0 if x == 1 else 1)
df['gluc'] = (df['gluc']).apply(lambda x : 0 if x == 1 else 1)

#print(df.head())


# 4
def draw_cat_plot():
    cat = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']

    df_cat = pd.melt(df,id_vars = ['cardio'], value_vars = cat)


    # 6
    df_cat['total'] = 1
    

    # 7
    df_cat = df_cat.groupby(['cardio','variable','value'],as_index = False).count()


    # 8
    fig = sns.catplot(
        data = df_cat,
        x = 'variable',
        y = 'total',
        hue = 'value',
        col = 'cardio',
        kind = 'bar' 
    ).fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo']<=df['ap_hi']) &
        (df['height']>=df['height'].quantile(0.025)) &
        (df['height']<=df['height'].quantile(0.975)) &
        (df['weight']>=df['weight'].quantile(0.025)) &
        (df['weight']<=df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(11,9))

    # 15

    sns.heatmap(
        corr,
        mask = mask,
        annot = True,
        fmt = '.1f',
        linewidths=.5,
        square = True,
        center = 0,
        cbar_kws = {'shrink':.5}
    )



    # 16
    fig.savefig('heatmap.png')
    return fig
