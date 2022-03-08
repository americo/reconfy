import subprocess
import argparse
import yaml
from huepy import *

from yaml.loader import SafeLoader
from datetime import date

# Defines the pareser
parser = argparse.ArgumentParser()

# Arguments that can be supplied
parser.add_argument("-workflow", help="Recon workflow.", dest="workflow", required=True)
parser.add_argument("-silent", help="Silent mode.", dest="silent")
# Arguments to be parsed
args = parser.parse_args()


def banner():
    ban = """                     ___     
 ___ ___ ___ ___ ___|  _|_ _ 
|  _| -_|  _| . |   |  _| | |
|_| |___|___|___|_|_|_| |_  |
                        |___|   v1.0.0                        
    americojunior.com
    """
    return ban


# Function to run a YAML workflow
def run_workflow(workflow):
    # Loading workflows
    print(f"[{blue('INF')}] Loading workflow...")
    with open(f"{workflow}") as workflow:
        data = yaml.load(workflow, Loader=SafeLoader)

    # Print workflow loaded banner
    print(f"[{blue('RUN')}] [{data['id']}] (@{data['info']['author']})")

    # Get all steps
    steps = data["steps"]

    # Print all steps banners
    for count_steps in range(len(steps)):
        print(f"[{orange(data['id'])}] {data['steps'][count_steps]['name']}")

    # Run steps
    for step in steps:
        # Get command from steps
        command = step["run"]
        # Run the command
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
        )
        process.wait()


def main():
    print(cyan(banner()))
    run_workflow(args.workflow)


if __name__ == "__main__":
    main()
