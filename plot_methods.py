from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def display_histogram(list):
   plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
   _, ax = plt.subplots()
   _set_histogram(ax, list)
   _set_data_table(ax, list)
   plt.show()


def display_heatmap(list):
    ax = sns.heatmap([list], cmap='coolwarm', center=0, cbar=True, cbar_kws={'orientation': 'horizontal'})
    ax.set(xticks=[], yticks=[])
    plt.show()


def create_dataframe(full_polarity_list):
    return pd.DataFrame(full_polarity_list, columns=['header', 'polarity', 'url'])


def _set_histogram(ax, list):
    ax.hist(list, bins=50, density=False, color='#69b3a2')
    ax.set_xlabel('Polarity')
    ax.set_ylabel('Number of articles')
    

def _set_data_table(ax, list):
    statistics = {'Mean': np.mean(list), 'Median': np.median(list), 'Std Dev': np.std(list)}
    cell_text = [[f"{k}: {v:.2f}" for k, v in statistics.items()]]
    table = ax.table(cellText=cell_text, loc='top', cellLoc='left')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)
