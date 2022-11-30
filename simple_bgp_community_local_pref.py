from ipmininet.router.config import BGP
from ipmininet.router.config.zebra import RouteMapSetAction
from simple_bgp_network import SimpleBGPTopo


class LocalPrefTopo(SimpleBGPTopo):

    def setRouteMapsForCommunity(self, community_list, as1r1, as2r1, as2r2, as3r1):
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
                80, name=route_map_name, from_peer=as1r1, matching=(community_list,))
