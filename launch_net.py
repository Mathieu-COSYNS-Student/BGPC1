import ipmininet
from ipmininet.ipnet import IPNet
from ipmininet.cli import IPCLI
from ipmininet.clean import cleanup
from mininet.log import lg, LEVELS

from simple_bgp_network import SimpleBGPTopo
from simple_bgp_community_local_pref import LocalPrefTopo
from simple_bgp_community_prepend_as import PrependASTopo
from simple_bgp_community_no_advertise import NoAdvertise
from simple_bgp_community_no_export import NoExport
from simple_bgp_community_prepend_as_2 import PrependAS2Topo

import argparse

TOPOS = {
    'simple_bgp_network': SimpleBGPTopo,
    'simple_bgp_community_local_pref': LocalPrefTopo,
    'simple_bgp_community_prepend_as': PrependASTopo,
    'simple_bgp_community_no_advertise': NoAdvertise,
    'simple_bgp_community_no_export': NoExport,
    'simple_bgp_community_prepend_as_2': PrependAS2Topo,
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topo', choices=TOPOS.keys(), default='simple_bgp_network',
                        help='the topology that you want to start')
    parser.add_argument('--log', choices=LEVELS.keys(), default='info',
                        help='The level of details in the logs')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    lg.setLogLevel(args.log)
    if args.log == 'debug':
        ipmininet.DEBUG_FLAG = True
    kwargs = {}
    net = IPNet(topo=TOPOS[args.topo](**kwargs))
    try:
        net.start()
        IPCLI(net)
    finally:
        net.stop()
        cleanup()
