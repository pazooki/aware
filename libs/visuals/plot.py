import matplotlib.pyplot as plt
import matplotlib.animation as anime


class Animate(object):
    def __init__(self, input_iter):
        self.fig, self.ax = plt.subplots()
        self.data = list(input_iter)
        self.line, = self.ax.plot([], [], lw=2)
        self.ax.set_ylim(-5.0, 5.0)
        self.ax.set_xlim(0, 200)
        self.ax.grid()
        self.xdata, self.ydata = [], []

    def animate(self, data):
        x, y = data
        self.xdata.append(x)
        self.ydata.append(y)
        xmin, xmax = self.ax.get_xlim()
        if x >= xmax:
            self.ax.set_xlim(xmin, 2*xmax)
            self.ax.figure.canvas.draw()
        self.line.set_data(self.xdata, self.ydata)
        return self.line,

    def play(self):
        ani = anime.FuncAnimation(self.fig, self.animate, self.data,
                                  blit=False, interval=10, repeat=False)
        plt.show()