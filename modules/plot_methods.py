import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def display_histogram(sentiment_df):
    polarities = sentiment_df['polarity']
    plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
    fig, ax = plt.subplots()
    fig.suptitle(sentiment_df.name)
    _set_histogram(ax, polarities)
    _set_data_table(ax, polarities)
    plt.show()


def display_heatmap(sentiment_df):
    polarities = sentiment_df['polarity']
    cmap=LinearSegmentedColormap.from_list('rg',["r", "w", "g"], N=256) 
    ax = sns.heatmap([polarities], cmap=cmap, center=0, cbar=True, cbar_kws={'orientation': 'horizontal'})
    ax.set(xticks=[], yticks=[])
    plt.title(sentiment_df.name)
    plt.show()


def create_dataframe(full_polarity_list):
    return pd.DataFrame(full_polarity_list, columns=['header', 'polarity', 'url'])


def _set_histogram(ax, list):
    x_values = np.arange(-1, 1.2, 0.25)
    ax.hist(list, bins=x_values, density=False, color='#69b3a2')
    ax.set_xlabel('Polarity')
    ax.set_ylabel('Number of articles')
    ax.grid()
    ax.xaxis.set_ticks(x_values)
    ax.margins(x=0)
    

def _set_data_table(ax, list):
    statistics = {'Mean': np.mean(list), 'Median': np.median(list), 'Std Dev': np.std(list)}
    cell_text = [[f"{k}: {v:.2f}" for k, v in statistics.items()]]
    table = ax.table(cellText=cell_text, loc='top', cellLoc='left')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)
