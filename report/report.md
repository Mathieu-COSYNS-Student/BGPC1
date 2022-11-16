## Project Goal

The goal of this project in to provide configuration guidelines on FRRouting or BIRD to reproduce the BGP communities deployed by a large ISP.

Those configurations guidelines should be validated and tested in emulated network.

## Testing environment

We have decided to use [ipmininet](https://github.com/cnp3/ipmininet) to do our experiments, validate and test our configurations.

### Setup

We followed the [install guide](https://ipmininet.readthedocs.io/en/latest/install.html) of ipmininet using [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtualbox](https://www.virtualbox.org/wiki/Downloads) with consist of executing the following commands in a new directory:

```
vagrant init ipmininet/ubuntu-20.04
vagrant up
```

This will create the VM. To access the VM with SSH, just issue the following command in the same directory as the two previous one:

```
vagrant ssh
```

ipmininet is written in python and required to create a few file in order to build a custom typology. For the ease of development we use [Vscode](https://code.visualstudio.com/) with the `Remote - SSH` extension. This extension allow us to use Vscode through `ssh`. The `vagrand ssh` command hide ssh details but they can be extracted using the following command:

```
vagrant ssh-config | sed 's/Host default/Host ipmininet/g' >> ~/.ssh/config
```

This command add the ssh configuration to your default ssh config file. This allow to enter the `ssh ipmininet` command instead of  `vagrand ssh` and connect Vscode. More info can be found in the following article https://medium.com/@lizrice/ssh-to-vagrant-from-vscode-5b2c5996bc0e.

### Topologies

Can be found at https://github.com/Mathieu-COSYNS-Student/BGPC1
(Still a work in progress)
