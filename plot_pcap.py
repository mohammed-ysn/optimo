from scapy.all import *
import matplotlib.pyplot as plt


def plot_ip_addresses(pcap_file):
    packets = rdpcap(pcap_file)

    src_ips = [packet[IP].src for packet in packets if IP in packet]
    dest_ips = [packet[IP].dst for packet in packets if IP in packet]

    plt.figure(figsize=(10, 6))
    plt.hist(
        [src_ips, dest_ips],
        bins=30,
        color=["blue", "red"],
        label=["Source IPs", "Destination IPs"],
    )
    plt.xlabel("IP Addresses")
    plt.ylabel("Frequency")
    plt.title("Source and Destination IP Addresses Distribution")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_interarrival_times(pcap_file):
    packets = rdpcap(pcap_file)

    interarrival_times = [
        (packets[i + 1].time - packet.time) for i, packet in enumerate(packets[:-1])
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(
        range(len(interarrival_times)),
        interarrival_times,
        marker="o",
        markersize=2,
        linestyle="-",
    )
    plt.xlabel("Packet Index")
    plt.ylabel("Inter-arrival Time (seconds)")
    plt.title("Inter-arrival Time of Packets")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    pcap_file = "./ns-allinone-3.40/ns-3.40/tcp-star-server-0-1.pcap"
    plot_ip_addresses(pcap_file)
    plot_interarrival_times(pcap_file)
