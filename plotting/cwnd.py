import os
import matplotlib.pyplot as plt


def read_data(file_path):
    x = []
    y = []
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split()
            x.append(float(data[0]))
            y.append(float(data[1]))
    return x, y

cwnd_file = os.path.join(
    os.path.dirname(__file__),
    "../simulation_output/TcpVariantsComparison-cwnd.data",
)
x, y = read_data(cwnd_file)
plt.scatter(x, y, label="Congestion Window", color="blue", marker=".")
plt.xlabel("Time (seconds)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
