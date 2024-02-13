import subprocess
import sys

import copy_scripts


class NS3Simulation:
    def __init__(
        self,
        filename="customfirst",
        copy_scripts=False,
        tcp_variant="TcpWestwoodPlus",
        duration=3,
        tracing=True,
        pcap_tracing=True,
    ):
        self.filename = filename
        self.copy_scripts = copy_scripts
        self.tcp_variant = tcp_variant
        self.duration = duration
        self.tracing = tracing
        self.pcap_tracing = pcap_tracing

    def set_filename(self, filename):
        self.filename = filename

    def enable_copy_scripts(self):
        self.copy_scripts = True

    def disable_copy_scripts(self):
        self.copy_scripts = False

    def set_tcp_variant(self, tcp_variant):
        self.tcp_variant = tcp_variant

    def set_duration(self, duration):
        self.duration = duration

    def enable_tracing(self):
        self.tracing = True

    def disable_tracing(self):
        self.tracing = False

    def enable_pcap_tracing(self):
        self.pcap_tracing = True

    def disable_pcap_tracing(self):
        self.pcap_tracing = False

    def run(self):
        if self.copy_scripts:
            copy_scripts.copy_cc_files(
                "my_scripts", "./ns-allinone-3.40/ns-3.40/scratch"
            )

        ns3_command = f'./ns-allinone-3.40/ns-3.40/ns3 run "scratch/{self.filename} --transport_prot={self.tcp_variant} --duration={self.duration} --tracing={str(self.tracing).lower()} --pcap_tracing={str(self.pcap_tracing).lower()}"'
        print(f"Running ns3 command: {ns3_command}")
        subprocess.run(ns3_command, shell=True)


def main():
    simulation = NS3Simulation()

    if "--copy-scripts" in sys.argv:
        simulation.enable_copy_scripts()
        sys.argv.remove("--copy-scripts")

    if "--tcp_variant" in sys.argv:
        tcp_variant_index = sys.argv.index("--tcp_variant")
        if len(sys.argv) > tcp_variant_index + 1:
            simulation.set_tcp_variant(sys.argv[tcp_variant_index + 1])
            sys.argv.pop(tcp_variant_index + 1)
        sys.argv.remove("--tcp_variant")

    if "--duration" in sys.argv:
        duration_index = sys.argv.index("--duration")
        if len(sys.argv) > duration_index + 1:
            simulation.set_duration(int(sys.argv[duration_index + 1]))
            sys.argv.pop(duration_index + 1)
        sys.argv.remove("--duration")

    if "--disable_tracing" in sys.argv:
        simulation.disable_tracing()
        sys.argv.remove("--disable_tracing")

    if "--disable_pcap_tracing" in sys.argv:
        simulation.disable_pcap_tracing()
        sys.argv.remove("--disable_pcap_tracing")

    if len(sys.argv) > 1:
        simulation.set_filename(sys.argv[1])

    simulation.run()


if __name__ == "__main__":
    main()
