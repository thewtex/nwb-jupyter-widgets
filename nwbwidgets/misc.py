import matplotlib.pyplot as plt
import numpy as np


def show_annotations(annotations, **kwargs):
    default_kwargs = {'marker': "|", 'linestyle': ''}
    for key, val in default_kwargs.items():
        if key not in kwargs:
            kwargs[key] = val

    fig, ax = plt.subplots()
    ax.plot(annotations.timestamps, np.ones(len(annotations.timestamps)), **kwargs)
    ax.set_xlabel('time (s)')
    return fig
