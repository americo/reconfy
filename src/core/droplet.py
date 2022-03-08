import digitalocean


def create_tag(token):
    tag = digitalocean.Tag(token=token, name="reconfy")
    tag.create()  # create tag if not already created
    tag.add_droplets(["DROPLET_ID"])


def create_droplet(number, token):
    manager = digitalocean.Manager(token=token)
    keys = manager.get_all_sshkeys()

    droplet = digitalocean.Droplet(
        token=manager.token,
        name=f"Reconfy-{number}",
        region="nyc1",  # New York City
        image="ubuntu-20-04-x64",  # Ubuntu 20.04 x64
        size_slug="s-1vcpu-1gb",  # 1GB RAM, 1 vCPU
        ssh_keys=keys,  # Automatic conversion
        backups=False,
    )
    droplet.create()
    print(droplet)
    tag = digitalocean.Tag(token=token, name="reconfy")
    tag.create()
    tag.add_droplets(droplet)
    return keys


def delete_droplet():
    pass


def main():
    create_droplet("1", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


if __name__ == "__main__":
    main()
