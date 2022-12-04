from ipmininet.router.config import BGP, CommunityList
from ipmininet.router.config.zebra import RouteMapSetAction
from simple_bgp_network import SimpleBGPTopo


class GracefullShutdownTopo(SimpleBGPTopo):

    def create_community_lists(self):
        community_list = CommunityList(
            'gracefull-shutdown-list', community='65535:0')

        return [community_list]
