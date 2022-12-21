from ipmininet.router.config import BGP, CommunityList
from ipmininet.router.config.zebra import RouteMapSetAction
from simple_bgp_network import SimpleBGPTopo


class LocalPref2Topo(SimpleBGPTopo):

    def create_community_lists(self):
        community_list_pref_80 = CommunityList(
            'local-pref-80-list', community='2:80')
        community_list_pref_40 = CommunityList(
            'local-pref-40-list', community='2:81')

        return [community_list_pref_40, community_list_pref_80]

    def set_route_maps_for_community(self, community_list, as1r1, as2r1, as2r2, as3r1):
        if community_list.name == 'local-pref-80-list':
            for route_map_name in ['as1r1-ipv4-in', 'as1r1-ipv6-in']:
                as2r1.get_config(BGP).permit(
                    name=route_map_name,
                    from_peer=as1r1,
                    to_peer=as2r1,
                    matching=(community_list,),
                    order=10
                )
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
                self.route_map_add_exit_policy(
                    as2r1, route_map_name, route_map_order=10, exit_policy='next')

        if community_list.name == 'local-pref-40-list':
            for route_map_name in ['as1r1-ipv4-in', 'as1r1-ipv6-in']:
                as2r1.get_config(BGP).permit(
                    name=route_map_name,
                    from_peer=as1r1,
                    to_peer=as2r1,
                    matching=(community_list,),
                    order=20
                )
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
                    40, name=route_map_name, from_peer=as1r1, matching=(community_list,))
                self.route_map_add_exit_policy(
                    as2r1, route_map_name, route_map_order=20, exit_policy='next')