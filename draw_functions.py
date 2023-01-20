import argparse
import numpy as np
from matplotlib import pyplot as plt


def argparser():
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(
            description="""

            Welcome to Graphic Artist.

            You can choose from four available graphs: x**n

            -n is an integer degree parameter .

            """
        )

        parser.add_argument(
            "-n",
            type=int,
            default=2,
            help=f"Natural number"
        )

        parsed_args = parser.parse_args()

        return parsed_args
def plot_builder(n):
    domain = np.arange(-5, 5, 0.1)
    graph = plt.plot(domain, domain ** n)
    plt.show()

plot_builder(*vars(argparser()).values())
