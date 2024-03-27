import subprocess
import os

import copy_scripts

SIMULATION_OUTPUT_DIR = "simulation_output"


class NS3Simulation:
    def __init__(
        self,
        filename,
        duration,
        copy_scripts=False,
        tcp_variant="TcpWestwoodPlus",
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

    def set_tcp_variant(self, tcp_variant):
        # Transport protocol to use: TcpNewReno, TcpLinuxReno,
        # TcpHybla, TcpHighSpeed, TcpHtcp, TcpVegas, TcpScalable, TcpVeno,
        # TcpBic, TcpYeah, TcpIllinois, TcpWestwoodPlus, TcpLedbat,
        # TcpLp, TcpDctcp, TcpCubic, TcpBbr
        self.tcp_variant = tcp_variant

    def set_duration(self, duration):
        self.duration = duration

    def run(self):
        if self.copy_scripts:
            copy_scripts.copy_cc_files(
                "ns3_scripts", "./ns-allinone-3.40/ns-3.40/scratch"
            )

        # Create the output directory if it does not exist
        if not os.path.exists(SIMULATION_OUTPUT_DIR):
            os.makedirs(SIMULATION_OUTPUT_DIR)

        ns3_command = (
            f'./ns-allinone-3.40/ns-3.40/ns3 run "scratch/optimo-{self.filename} '
            f"--transport_prot={self.tcp_variant} "
            f"--duration={self.duration} "
            f"--tracing=true "
            f"--pcap_tracing=true "
            '" '
            f"--cwd={SIMULATION_OUTPUT_DIR}"
        )
        print(f"Running ns3 command: {ns3_command}")
        subprocess.run(ns3_command, shell=True)
        print("Simulation completed!")
