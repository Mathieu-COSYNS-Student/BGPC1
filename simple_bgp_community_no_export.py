from ipmininet.router.config import BGP, CommunityList
from ipmininet.router.config.zebra import RouteMapSetAction
from simple_bgp_network import SimpleBGPTopo


class NoExportTopo(SimpleBGPTopo):

    def send_extra_communities(self) -> str:
        return 'no-export'
