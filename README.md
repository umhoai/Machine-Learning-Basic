# Add annotations to the plot
for index, value in enumerate(df['Gender'].value_counts()):
    plt.text(index, value+1, str(value), ha='center')
