from ipmininet.router.config import BGP, CommunityList
from ipmininet.router.config.zebra import RouteMapSetAction
from simple_bgp_network import SimpleBGPTopo


class GracefullShutdownTopo(SimpleBGPTopo):

    def create_community_lists(self):
        community_list = CommunityList(
            'gracefull-shutdown-list', community='65535:0')

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
                20, name=route_map_name, from_peer=as1r1, matching=(community_list,))
