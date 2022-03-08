import sys
import subprocess
import argparse
import yaml
from huepy import *

from yaml.loader import SafeLoader
from datetime import date

from core.notify import discord

# Defines the pareser
parser = argparse.ArgumentParser()

# Arguments that can be supplied
parser.add_argument(
    "-workflow", help="Recon workflow file.", dest="workflow", required=True
)
parser.add_argument(
    "-config", help="Configuration file.", dest="config_file", required=True
)
parser.add_argument(
    "-notify",
    help="Enable discord notification for steps (Setup your config file first.)",
    dest="notify",
    action="store_true",
)
parser.add_argument("-name", help="Project name.", dest="project_name", required=True)
parser.add_argument("-silent", help="Silent mode.", dest="silent", action="store_true")
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


# Get configuration file
def get_config(config_file=None):
    if config_file:
        print(f"[{blue('INF')}] Loading configuration file: {config_file}")
        try:
            with open(f"{config_file}") as config_file:
                data = yaml.load(config_file, Loader=SafeLoader)
        except:
            print(f"[{red('WRN')}] Configuration file not found")
            sys.exit()
    else:
        print(f"[{red('WRN')}] Configuration file not found")
        sys.exit()
        # config_file = "~/.config/reconfy/config.yaml"
        # with open(config_file) as config_file:
        #     data = yaml.load(config_file, Loader=SafeLoader)

    return data


def notificate(config_data, content):
    if args.notify:
        discord_webhook_url = config_data["notifications"]["discord_webhook_url"]
        discord(discord_webhook_url, content)


# Function to run a YAML workflow
def run_workflow(workflow, config_data):
    # Loading workflows
    print(f"[{blue('INF')}] Loading workflow...")
    with open(f"{workflow}") as workflow:
        data = yaml.load(workflow, Loader=SafeLoader)

    # Print workflow loaded banner
    print(f"[{blue('RUN')}] [{data['id']}] (@{data['info']['author']})")

    # Get all steps
    steps = data["steps"]

    # Notificate the start of the workflow running
    notificate(
        config_data,
        f"[INF] Reconnaissance workflow started in {args.project_name} project",
    )

    # Run steps
    for step in steps:
        # Print all steps banners
        print(f"[{orange(data['id'])}] {step['name']}")
        # Get command from steps
        command = step["run"]

        try:
            notify = step["notify"]
        except:
            pass

        # Run the command
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
        )
        process.wait()

        # Send notification if notify is enabled
        notify_content = "[step-done] " + step["name"]
        notificate(config_data, notify_content)

    # Notifacate the end of the workflow running
    notificate(
        config_data,
        f"[INF] Reconnaissance workflow in {args.project_name} project finished",
    )


def main():
    print(cyan(banner()))
    config_data = get_config(config_file=args.config_file)
    run_workflow(args.workflow, config_data)


if __name__ == "__main__":
    main()
