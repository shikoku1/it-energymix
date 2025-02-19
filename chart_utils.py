import matplotlib.pyplot as plt
import numpy as np


def yearlong_chart(title, data, labels):

    assert len(data) == len(labels)

    for dat in data:
        assert len(dat) == 365*24

    month_names = ["January", "February", "March", "April", "May", "June",
                           "July", "August", "September", "October", "November", "December"]

    month_durations = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    assert sum(month_durations) == 365

    fig, axs = plt.subplots(12)

    fig.subplots_adjust(hspace=0.8)

    # do not waste empty space above and below the plots
    fig.subplots_adjust(top=0.95)
    fig.subplots_adjust(bottom=0.05)

    for i in range(12):
        offset = sum(month_durations[:i])*24
        hrange = slice(offset, offset+month_durations[i]*24)

        axs[i].set(title=month_names[i])

        for j in range(len(data)):
            axs[i].plot(data[j][hrange], label=labels[j])

        # all montly plots share the same x axis
        axs[i].set_xlim(xmin=0, xmax=31*24)
        axs[i].set_xticks(np.arange(0, 31*24, 24))
        axs[i].set_xticklabels(np.arange(1, 32))

        # all montly plots share the same y axis
        axs[i].set_ylim(ymin=min([d.min() for d in data]), ymax=max([d.max() for d in data]))

        # vetical lines for each day
        for j in range(31):
            axs[i].axvline(x=j*24, color="lightgrey",
                           linestyle="--", alpha=0.8)

    fig.suptitle(title, fontsize=18)

    # do not repeat legend items for subplots
    handles, labels_ = axs[0].get_legend_handles_labels()
    by_label = dict(zip(labels_, handles))
    fig.legend(by_label.values(), by_label.keys(),
               loc="lower center", ncol=2, fontsize=12)

    plt.show()


def scatter_chart(title, data1, label1, data2, label2, trendline=False):
    fig, ax = plt.subplots()
    ax.scatter(data1,data2, s=0.1, color="blue")

    if trendline:
        coef = np.polyfit(data1, data2,1)
        poly = np.poly1d(coef) 
        ax.plot(data1, poly(data1), '-', label=poly, color="lightblue")


    ax.set_ylim(ymin=0)
    ax.set_xlim(xmin=0)
    ax.set(title=title, ylabel=label2, xlabel=label1)

    ax.grid()

    plt.show()
