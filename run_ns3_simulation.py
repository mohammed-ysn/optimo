import subprocess
import sys

import copy_scripts


def main():
    if "--copy-scripts" in sys.argv:
        copy_scripts.copy_cc_files("my_scripts", "./ns-allinone-3.40/ns-3.40/scratch")
        sys.argv.remove("--copy-scripts")

    # Transport protocol to use: TcpNewReno, TcpLinuxReno,
    # TcpHybla, TcpHighSpeed, TcpHtcp, TcpVegas, TcpScalable, TcpVeno,
    # TcpBic, TcpYeah, TcpIllinois, TcpWestwoodPlus, TcpLedbat,
    # TcpLp, TcpDctcp, TcpCubic, TcpBbr
    tcp_variant = "TcpWestwoodPlus"
    if "--tcp_variant" in sys.argv:
        tcp_variant = sys.argv[sys.argv.index("--tcp_variant") + 1]
        sys.argv.remove("--tcp_variant")
        sys.argv.remove(tcp_variant)

    filename = sys.argv[1] if len(sys.argv) > 1 else "customfirst"
    ns3_command = f'./ns-allinone-3.40/ns-3.40/ns3 run "scratch/{filename} --transport_prot={tcp_variant} --duration=3 --tracing=true --pcap_tracing=true"'
    print(ns3_command)

    print(f"Running ns3 command: {ns3_command}")
    subprocess.run(ns3_command, shell=True)


if __name__ == "__main__":
    main()
