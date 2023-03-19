from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


def display_histogram(list):
    plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
    plt.hist(list, bins=50)
    plt.gca().set(title='Frequency Histogram', ylabel='Frequency')


def display_heatmap(list):
    ax = sns.heatmap([list], cmap='coolwarm', center=0, cbar=True, cbar_kws={'orientation': 'horizontal'})
    ax.set(xticks=[], yticks=[])
    plt.show()

def create_dataframe(full_polarity_list):
    return pd.DataFrame(full_polarity_list, columns=['header', 'polarity', 'url'])
