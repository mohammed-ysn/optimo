import subprocess
import os

import copy_scripts

SIMULATION_OUTPUT_DIR = "simulation_output"


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
        if not os.path.isfile(f"./ns-allinone-3.40/ns-3.40/scratch/{filename}.cc"):
            print(
                f"Warning: file ./ns-allinone-3.40/ns-3.40/scratch/{filename}.cc not found"
            )
            print("Hint: You may want to set the copy_scripts parameter to True")

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
        # Transport protocol to use: TcpNewReno, TcpLinuxReno,
        # TcpHybla, TcpHighSpeed, TcpHtcp, TcpVegas, TcpScalable, TcpVeno,
        # TcpBic, TcpYeah, TcpIllinois, TcpWestwoodPlus, TcpLedbat,
        # TcpLp, TcpDctcp, TcpCubic, TcpBbr
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
                "ns3_scripts", "./ns-allinone-3.40/ns-3.40/scratch"
            )

        # Create the output directory if it does not exist
        if not os.path.exists(SIMULATION_OUTPUT_DIR):
            os.makedirs(SIMULATION_OUTPUT_DIR)

        ns3_command = (
            f'./ns-allinone-3.40/ns-3.40/ns3 run "scratch/{self.filename} '
            f"--transport_prot={self.tcp_variant} "
            f"--duration={self.duration} "
            f"--tracing={str(self.tracing).lower()} "
            f"--pcap_tracing={str(self.pcap_tracing).lower()}"
            '" '
            f"--cwd={SIMULATION_OUTPUT_DIR}"
        )
        print(f"Running ns3 command: {ns3_command}")
        subprocess.run(ns3_command, shell=True)
