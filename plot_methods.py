from matplotlib import pyplot as plt
import seaborn as sns

def display_histogram(list):
    plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})
    plt.hist(list, bins=50)
    plt.gca().set(title='Frequency Histogram', ylabel='Frequency');

def display_heatmap(list):
    n = int(len(list) ** 0.5)
    my_matrix = [list[i:i+n] for i in range(0, len(list), n)]
    sns.heatmap(my_matrix, cmap='coolwarm')
    plt.show()
