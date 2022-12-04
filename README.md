# BGPC1

## Launch the CLI

To launch the CLI and test the topologies, run
```bash
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

* To get the routes in `ipv6` of a node NODE
```bash
mininet> NODE route -6
```
* To get all the prefixes received by a node NODE using bgpd.
Enter first:
```bash
mininet> noecho NODE telnet localhost bgpd
```
Enter the password zebra and enter the following command:
```bash
NODE> show show bgp ipv6
```
* To get informations about the different links and interfaces
```bash
mininet> links
```

## Contribute

If you find errors, do not hesitate to raise an issue. 
If you want to add topologies, feel free to open a pull request.
