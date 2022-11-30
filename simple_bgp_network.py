from ipmininet.iptopo import IPTopo
from ipmininet.router.config import BGP, ebgp_session, AccessList, CommunityList
import ipmininet.router.config.bgp as _bgp


class SimpleBGPTopo(IPTopo):
    """This topology builds a 3-AS network exchanging BGP reachability
    information"""

    def build(self, *args, **kwargs):
        """
           +----------+                                   +--------+
                      |                                   |
         AS1          |                  AS2              |        AS3
                      |                                   |
                      |                                   |
    +-------+   eBGP  |  +-------+     iBGP    +-------+  |  eBGP   +-------+
    | as1r1 +------------+ as2r1 +-------------+ as2r2 +------------+ as3r1 |
    +-------+         |  +-------+             +-------+  |         +-------+
                      |                                   |
                      |                                   |
                      |                                   |
         +------------+                                   +--------+
        """
        # Add all routers
        as1r1 = self.bgp('as1r1')
        as2r1 = self.bgp('as2r1')
        as2r2 = self.bgp('as2r2')
        as3r1 = self.bgp('as3r1')

        # Add links
        self.addLink(as1r1, as2r1)
        self.addLink(as2r1, as2r2)
        self.addLink(as3r1, as2r2)

        # Add an access list to 'any' for both ipv4 and ipv6 AFI
        # This can be an IP prefix or address instead
        all_al4 = AccessList(family='ipv4', name='allv4', entries=('any',))
        all_al6 = AccessList(family='ipv6', name='allv6', entries=('any',))

        # Add a community list to as2r1
        test_community_list = CommunityList('test-community', community='2:80')

        self.setRouteMapsForCommunity(
            test_community_list, as1r1, as2r1, as2r2, as3r1)

        # as1r1 set the community of all the route sent to as2r1 and matching the access lists all_al{4,6} to 2:80
        as1r1.get_config(BGP).set_community(
            '2:80', to_peer=as2r1, matching=(all_al4, all_al6))

        # Set AS-ownerships
        self.addAS(1, (as1r1,))
        self.addAS(2, (as2r1, as2r2))
        self.addAS(3, (as3r1,))

        # Add iBGP
        self.addiBGPFullMesh(2, (as2r1, as2r2))

        # Add eBGP peering
        ebgp_session(self, as1r1, as2r1)
        ebgp_session(self, as3r1, as2r2)

        # Add test hosts
        for r in self.routers():
            self.addLink(r, self.addHost('h%s' % r))
        super(SimpleBGPTopo, self).build(*args, **kwargs)

    def bgp(self, name):
        r = self.addRouter(name)
        r.addDaemon(BGP, address_families=(
            _bgp.AF_INET(redistribute=('connected',)),
            _bgp.AF_INET6(redistribute=('connected',))))
        return r

    def setRouteMapsForCommunity(self, community_list, as1r1, as2r1, as2r2, as3r1):
        pass
