from ipmininet.router.config import BGP
from ipmininet.router.config.zebra import RouteMapSetAction
from simple_bgp_network import SimpleBGPTopo


class PrependASTopo(SimpleBGPTopo):

    def setRouteMapsForCommunity(self, community_list, as1r1, as2r1, as2r2, as3r1):
        for route_map_name in ['as3r1-ipv4-out', 'as3r1-ipv6-out']:
            as2r2.get_config(BGP).add_set_action(
                name=route_map_name,
                direction='out',
                peer=as3r1,
                matching=(community_list,),
                set_action=RouteMapSetAction(
                    'comm-list',
                    f'{community_list.name} delete'
                )
            )
            as2r2.get_config(BGP).add_set_action(
                name=route_map_name,
                direction='out',
                peer=as3r1,
                matching=(community_list,),
                set_action=RouteMapSetAction(
                    'as-path',
                    'prepend 5'
                )
            )
