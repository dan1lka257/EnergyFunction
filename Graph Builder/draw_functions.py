import argparse
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style, rcParams
from matplotlib.ticker import IndexLocator
from mpl_toolkits.axisartist.axislines import AxesZero


def argparser():
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(
            description=f"""

            This script builds two graphs of function f(x) = |x - 1/2|^n.
            
            First one is a direct mapping from a segment.
            Second graph is done by using homeomorphism from segment(with "glued" ends) to circle.


            You can input -n parameter in terminal.

            """
        )

        parser.add_argument(
            "-n",
            type=int,
            default=8,
            help=f"Integer number"
        )

        parsed_args = parser.parse_args()

        return parsed_args


def plot_builder(n):
    rcParams["axes.formatter.limits"] = (-2, 4)

    # function we gonna build
    def segment(dom, n):
        data1 = (dom, np.abs(dom - 0.5) ** n)
        return data1
    def circle(dom, n):
        x = np.cos(2 * np.pi * dom)
        y = np.sin(2 * np.pi * dom)
        z = np.abs(dom - 0.5) ** n
        data2 = (x, y, z)
        return data2

    # adds axis lines
    def axis_lines2d(ax1):
        for direction in ["xzero", "yzero"]:
            # adds arrows at the ends of each axis
            ax1.axis[direction].set_axisline_style("-|>")

            # adds X and Y-axis from the origin
            ax1.axis[direction].set_visible(True)

        for direction in ["left", "right", "bottom", "top"]:
            # hides borders
            ax1.axis[direction].set_visible(False)

    # sets axis labels and initial position
    def graphs_settings(ax1, ax2):

        ax1.set_xlabel('X', fontweight='bold', fontsize=14)
        ax1.set_ylabel('Y', fontweight='bold', fontsize=14)
        ax1.set_title('Mapping f(x) = |x - 1/2|^n from segment', fontweight='bold', fontsize=16)
        axis_lines2d(ax1)

        ax2.set_xlabel('X', fontweight='bold', fontsize=12)
        ax2.set_ylabel('Y', fontweight='bold', fontsize=14)
        ax2.set_zlabel('Z', fontweight='bold', fontsize=14)
        ax2.set_title('Mapping |x-1/2|^n from a circle', fontweight='bold', fontsize=16)
        ax2.view_init(45, 215)

        ax1.grid()

        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()

    # Plots the figure
    fig = plt.figure(figsize=(7, 4))
    ax1 = fig.add_subplot(121, axes_class=AxesZero)
    ax2 = fig.add_subplot(122, projection="3d")
    accuracy = 5000
    domain = np.linspace(0, 1, num=accuracy, endpoint=True)
    data1 = segment(domain, n)
    data2 = circle(domain, n)
    ax1.plot(*data1)
    ax2.plot(*data2)
    ax2.plot(data2[0], data2[1], np.zeros(accuracy), alpha=0.4)

    graphs_settings(ax1, ax2)
    plt.show()


plot_builder(*vars(argparser()).values())
