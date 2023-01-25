import argparse
import numpy as np
from matplotlib import pyplot as plt

def argparser():
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(
            description="""

            Welcome to Graphic Artist.

            -n is an integer degree parameter.

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
    radius = 5
#     Segment [0, 1]
    domain = np.linspace(0, 1, num=100, endpoint=True)
    phi = 2 * np.pi * domain
    
#     Adding the axes
    x = radius * np.cos(phi)        #   homeomorphism from segment [0,1] (1~0) to circle is the set of points such as: (cos(2pi*x), sin(2pi*x))
    y = radius * np.sin(phi)
    z = np.abs(np.arccos(x/radius) / (2* np.pi) - 0.5) ** n

#     Plotting the figure
    fig = plt.figure("Zagogulina")
    ax = fig.add_subplot(111, projection="3d")

    ax.plot(x, y, z)
#     Plotting domain area
    ax.plot(x,y, np.zeros(100))

#     Visual settings
    ax.set_xlabel('X', fontweight='bold', fontsize=14)
    ax.set_ylabel('Y', fontweight='bold', fontsize=14)
    ax.set_zlabel('Z', fontweight='bold', fontsize=14)
    ax.set_title('Zagogulina', fontweight='bold', fontsize=16)

#     Scaling
    ax.set_xlim(-radius, radius)
    ax.set_ylim(-radius, radius)
    ax.set_zlim(0, radius/24)

    plt.show()


plot_builder(*vars(argparser()).values())
