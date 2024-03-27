import argparse
from simulation import NS3Simulation


def main():
    parser = argparse.ArgumentParser(description="Run NS3Simulation")
    parser.add_argument(
        "--copy-scripts", action="store_true", help="Copy scripts flag (default: False)"
    )
    args = parser.parse_args()

    copy_scripts = args.copy_scripts

    sim = NS3Simulation("tcp-comparison", copy_scripts=copy_scripts)
    sim.run()


if __name__ == "__main__":
    main()
