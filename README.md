# BGPC1

## Install

Follow the [install guide](https://ipmininet.readthedocs.io/en/latest/install.html) of ipmininet using [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtualbox](https://www.virtualbox.org/wiki/Downloads) with consist of executing the following commands in a new directory:

```sh
vagrant init ipmininet/ubuntu-20.04
vagrant up
```

This will create the VM. To access the VM with SSH, just issue the following command in the same directory as the two previous one:

```sh
vagrant ssh
```

### Connect Vscode (Optional)

ipmininet is written in python and required to create a few file in order to build a custom typology. For the ease of development we use [Vscode](https://code.visualstudio.com/) with the _Remote - SSH_ extension. This extension allow us to use Vscode through _ssh_. The `vagrand ssh` command hide ssh details but they can be extracted using the following command:

```sh
vagrant ssh-config | sed 's/Host default/Host ipmininet/g' >> ~/.ssh/config
```

This command add the ssh configuration to your default ssh config file. This allow to enter the `ssh ipmininet` command instead of  `vagrand ssh` and connect Vscode. More info can be found in the following article https://medium.com/@lizrice/ssh-to-vagrant-from-vscode-5b2c5996bc0e.

### Clone repository

After made vagrant ssh and successfully connected to the IPMininet VM, make a clone on this repository in the VM.

### IPMininet issue [#122](https://github.com/cnp3/ipmininet/issues/122)

IPMininet API is not really intuitive to work with advanced BGP filters (see Issue [#99](https://github.com/cnp3/ipmininet/issues/99) and Issue [#107](https://github.com/cnp3/ipmininet/issues/107)) but we managed to achieve our goals anyway except for one point because of a bug.

During our experiments, we found a bug in ipmininet. It was impossible to configure a exit_policy or a call_action in route maps. We opened an issue ([#122](https://github.com/cnp3/ipmininet/issues/122)) in ipmininet github repository and proposed a pull request to fix it.

At the time of writing, our pull request is not yet merge. So your have to do a bit more work to configure ipmininet.

In the root folder of the repository enter the following commands:

```sh
sudo pip3 install virtualenv
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Launch the CLI

To launch the CLI and test the topologies, run
```sh
python3 launch_net.py --topo=TOPO
```

where TOPO is one the following topologies:
- simple_bgp_network
- simple_bgp_community_local_pref
- simple_bgp_community_prepend_as
- simple_bgp_community_prepend_as_2
- simple_bgp_community_no_advertise
- simple_bgp_community_no_export
- simple_bgp_community_gracefull_shutdown
- simple_bgp_community_blackhole

## Useful Commands

* Run ipmininet with one topology.
```sh
sudo python3 launch_net.py --topo=TODO
```

* List available nodes
```sh
mininet> nodes
```

* Get the routes in `ipv4`/`ipv6` of a node NODE
```sh
mininet> NODE route
mininet> NODE route -6
```

* Connect to a router for BGP configuration.
```sh
mininet> noecho NODE telnet localhost bgpd
// Password: zebra
```

* Show router configuration.
```sh
NODE> show running-config
```

* Show router bgp routes.
```sh
NODE> show bgp ipv4
NODE> show bgp ipv6
```

* Show list of community received/sent by a router.
```sh
NODE> show bgp community-info
```

* Edit bgp configuration
```sh
NODE> enable
NODE# configure terminal
```

* To get informations about the different links and interfaces
```bash
mininet> links
```

## Contribute

If you find errors, do not hesitate to raise an issue. 
If you want to add topologies, feel free to open a pull request.
