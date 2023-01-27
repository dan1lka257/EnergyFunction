import argparse
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

def argparser():
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(
            description="""

            This script builds graph of function f(x) = |x - 1/2|^n.
            First one is a direct mapping from a segment.
            Second one is done by using homeomorphism from segment(with identified ends) to circle.
            You can input -n parameter in terminal.
            
            """
        )

        parser.add_argument(
            "-n",
            type=int,
            default=1,
            help=f"An Integer Parameter"
        )

        parsed_args = parser.parse_args()

        return parsed_args


def plot_builder(n):

    style.use("seaborn-darkgrid")

    def f(dom, n):
        data1 = (dom, np.abs(dom - 0.5) ** n)
        x = np.cos(2 * np.pi * dom)
        y = np.sin(2 * np.pi * dom)
        z = np.abs(np.arccos(x) / (2 * np.pi) - 0.5) ** n
        data2 = (x, y, z)
        return (data1, data2)

    #     Plotting the figure
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122,projection="3d")
    count = 5000
    domain = np.linspace(0, 1, num=count, endpoint=True)
    data1, data2 = f(domain, n)

    ax1.plot(*data1)
    ax1.set_xlabel('X', fontweight='bold', fontsize=14)
    ax1.set_ylabel('Y', fontweight='bold', fontsize=14)
    ax1.set_title('Mapping f(x) = |x - 1/2|^n from segment', fontweight='bold', fontsize=16)


    ax2.plot(*data2)
    ax2.plot(data2[0], data2[1], np.zeros(count), alpha=0.4)
    ax2.set_xlabel('X', fontweight='bold', fontsize=12)
    ax2.set_ylabel('Y', fontweight='bold', fontsize=14)
    ax2.set_zlabel('Z', fontweight='bold', fontsize=14)
    ax2.set_title('Mapping |x-1/2|^n from a circle', fontweight='bold', fontsize=16)
    ax2.view_init(45,215)

    #     Scaling
    ax2.set_xlim(np.min(data2[0]), np.max(data2[0]))
    ax2.set_ylim(np.min(data2[1]), np.max(data2[1]))
    ax2.set_zlim(np.min(data2[2]), np.max(data2[2]))
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()


plot_builder(*vars(argparser()).values())
