from ipmininet.router.config import BGP, CommunityList
from ipmininet.router.config.zebra import RouteMapSetAction
from simple_bgp_network import SimpleBGPTopo


class PrependAS2Topo(SimpleBGPTopo):

    def create_community_lists(self):
        community_list = CommunityList(
            'prepend-as-once-list', community='2:90')
        community_list_2 = CommunityList(
            'prepend-as-twice-list', community='2:91')

        return [community_list_2, community_list]

    def set_route_maps_for_community(self, community_list, as1r1, as2r1, as2r2, as3r1):
        if community_list.name == 'prepend-as-once-list':
            for route_map_name in ['as3r1-ipv4-out', 'as3r1-ipv6-out']:
                as2r2.get_config(BGP).permit(
                    name=route_map_name,
                    from_peer=as2r2,
                    to_peer=as3r1,
                    matching=(community_list,),
                    order=20
                )
                as2r2.get_config(BGP).add_set_action(
                    name=route_map_name,
                    direction='out',
                    peer=as3r1,
                    matching=(community_list,),
                    set_action=RouteMapSetAction(
                        'as-path',
                        'prepend 2'
                    )
                )
                self.route_map_add_exit_policy(
                    as2r2, route_map_name, route_map_order=20, exit_policy='goto 100')
                as2r2.get_config(BGP).permit(
                    name=route_map_name,
                    from_peer=as2r2,
                    to_peer=as3r1,
                    matching=(community_list,),
                    order=120
                )
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
                self.route_map_add_exit_policy(
                    as2r2, route_map_name, route_map_order=120, exit_policy='next')
        if community_list.name == 'prepend-as-twice-list':
            for route_map_name in ['as3r1-ipv4-out', 'as3r1-ipv6-out']:
                as2r2.get_config(BGP).permit(
                    name=route_map_name,
                    from_peer=as2r2,
                    to_peer=as3r1,
                    matching=(community_list,),
                    order=10
                )
                as2r2.get_config(BGP).add_set_action(
                    name=route_map_name,
                    direction='out',
                    peer=as3r1,
                    matching=(community_list,),
                    set_action=RouteMapSetAction(
                        'as-path',
                        'prepend 2 2'
                    )
                )
                self.route_map_add_exit_policy(
                    as2r2, route_map_name, route_map_order=10, exit_policy='goto 100')
                as2r2.get_config(BGP).permit(
                    name=route_map_name,
                    from_peer=as2r2,
                    to_peer=as3r1,
                    matching=(community_list,),
                    order=110
                )
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
                self.route_map_add_exit_policy(
                    as2r2, route_map_name, route_map_order=110, exit_policy='next')
