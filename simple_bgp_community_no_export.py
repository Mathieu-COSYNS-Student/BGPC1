from ipmininet.router.config import BGP, CommunityList
from ipmininet.router.config.zebra import RouteMapSetAction
from simple_bgp_network import SimpleBGPTopo


class NoExportTopo(SimpleBGPTopo):

    def create_community_lists(self):
        community_list = CommunityList(
            'NO_EXPORT', community='65535:65281')

        return [community_list]

    def set_route_maps_for_community(self, community_list, as1r1, as2r1, as2r2, as3r1):
        for route_map_name in ['as1r1-ipv4-in', 'as1r1-ipv6-in']:
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
