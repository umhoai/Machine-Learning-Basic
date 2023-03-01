for p in ax.patches:
    ax.annotate(int(p.get_width()),((p.get_x() + p.get_width()), p.get_y()), xytext=(1, -18),fontsize=9,color='#004d00',textcoords='offset points', horizontalalignment='right')
