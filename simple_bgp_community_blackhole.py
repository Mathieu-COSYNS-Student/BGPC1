from ipmininet.router.config import BGP, CommunityList
from ipmininet.router.config.zebra import RouteMapSetAction
from simple_bgp_network import SimpleBGPTopo
from mininet.log import info
from ipmininet.ipnet import IPNet


class BlackholeTopo(SimpleBGPTopo):

    def create_community_lists(self):
        community_list = CommunityList(
            'blackhole-list', community='2:666')

        return [community_list]

    def set_route_maps_for_community(self, community_list, as1r1, as2r1, as2r2, as3r1):
        for route_map_name in ['as1r1-ipv4-in', 'as1r1-ipv6-in']:
            as2r1.get_config(BGP).add_set_action(
                name=route_map_name,
                direction='in',
                peer=as1r1,
                matching=(community_list,),
                set_action=RouteMapSetAction(
                    'comm-list',
                    f'{community_list.name} delete'
                )
            )
            as2r1.get_config(BGP).set_local_pref(
                200, name=route_map_name, from_peer=as1r1, matching=(community_list,))
            as2r1.get_config(BGP).add_set_action(
                name=route_map_name,
                direction='in',
                peer=as1r1,
                matching=(community_list,),
                set_action=RouteMapSetAction(
                    'community',
                    'no-export'
                )
            )
            as2r1.get_config(BGP).add_set_action(
                name=route_map_name,
                direction='in',
                peer=as1r1,
                matching=(community_list,),
                set_action=RouteMapSetAction(
                    'ip',
                    'next-hop 192.0.2.1'
                )
            )

    def after_start(self, net: IPNet):
        node = net.getNodeByName('has2r1')
        info('Adding blackhole ip to %s...\n' % 'has2r1')
        node.cmd('ip route add blackhole 192.0.2.1/32')
