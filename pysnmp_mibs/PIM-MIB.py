# PySNMP SMI module. Autogenerated from smidump -f python PIM-MIB
# by libsmi2pysnmp-0.0.9-alpha at Thu Mar 26 19:36:31 2009,
# Python version (2, 4, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( ipMRouteGroup, ipMRouteNextHopAddress, ipMRouteNextHopGroup, ipMRouteNextHopIfIndex, ipMRouteNextHopSource, ipMRouteNextHopSourceMask, ipMRouteSource, ipMRouteSourceMask, ) = mibBuilder.importSymbols("IPMROUTE-STD-MIB", "ipMRouteGroup", "ipMRouteNextHopAddress", "ipMRouteNextHopGroup", "ipMRouteNextHopIfIndex", "ipMRouteNextHopSource", "ipMRouteNextHopSourceMask", "ipMRouteSource", "ipMRouteSourceMask")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, experimental, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "experimental")
( RowStatus, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue")

# Objects

pimMIB = ModuleIdentity((1, 3, 6, 1, 3, 61)).setRevisions(("2000-09-28 00:00",))
if mibBuilder.loadTexts: pimMIB.setOrganization("IETF IDMR Working Group.")
if mibBuilder.loadTexts: pimMIB.setContactInfo(" Dave Thaler\nMicrosoft Corporation\nOne Microsoft Way\nRedmond, WA  98052-6399\nUS\n\nPhone: +1 425 703 8835\nEMail: dthaler@microsoft.com")
if mibBuilder.loadTexts: pimMIB.setDescription("The MIB module for management of PIM routers.")
pimMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 61, 1))
pimTraps = MibIdentifier((1, 3, 6, 1, 3, 61, 1, 0))
pim = MibIdentifier((1, 3, 6, 1, 3, 61, 1, 1))
pimJoinPruneInterval = MibScalar((1, 3, 6, 1, 3, 61, 1, 1, 1), Integer32()).setMaxAccess("readwrite").setUnits("seconds")
if mibBuilder.loadTexts: pimJoinPruneInterval.setDescription("The default interval at which periodic PIM-SM Join/Prune\nmessages are to be sent.")
pimInterfaceTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 2))
if mibBuilder.loadTexts: pimInterfaceTable.setDescription("The (conceptual) table listing the router's PIM interfaces.\nIGMP and PIM are enabled on all interfaces listed in this\ntable.")
pimInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 2, 1)).setIndexNames((0, "PIM-MIB", "pimInterfaceIfIndex"))
if mibBuilder.loadTexts: pimInterfaceEntry.setDescription("An entry (conceptual row) in the pimInterfaceTable.")
pimInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimInterfaceIfIndex.setDescription("The ifIndex value of this PIM interface.")
pimInterfaceAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimInterfaceAddress.setDescription("The IP address of the PIM interface.")
pimInterfaceNetMask = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimInterfaceNetMask.setDescription("The network mask for the IP address of the PIM interface.")
pimInterfaceMode = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("dense", 1), ("sparse", 2), ("sparseDense", 3), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimInterfaceMode.setDescription("The configured mode of this PIM interface.  A value of\nsparseDense is only valid for PIMv1.")
pimInterfaceDR = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimInterfaceDR.setDescription("The Designated Router on this PIM interface.  For point-to-\npoint interfaces, this object has the value 0.0.0.0.")
pimInterfaceHelloInterval = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 6), Integer32().clone(30)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimInterfaceHelloInterval.setDescription("The frequency at which PIM Hello messages are transmitted\non this interface.")
pimInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimInterfaceStatus.setDescription("The status of this entry.  Creating the entry enables PIM\non the interface; destroying the entry disables PIM on the\ninterface.")
pimInterfaceJoinPruneInterval = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimInterfaceJoinPruneInterval.setDescription("The frequency at which PIM Join/Prune messages are\ntransmitted on this PIM interface.  The default value of\nthis object is the pimJoinPruneInterval.")
pimInterfaceCBSRPreference = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 255)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimInterfaceCBSRPreference.setDescription("The preference value for the local interface as a candidate\nbootstrap router.  The value of -1 is used to indicate that\nthe local interface is not a candidate BSR interface.")
pimNeighborTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 3))
if mibBuilder.loadTexts: pimNeighborTable.setDescription("The (conceptual) table listing the router's PIM neighbors.")
pimNeighborEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 3, 1)).setIndexNames((0, "PIM-MIB", "pimNeighborAddress"))
if mibBuilder.loadTexts: pimNeighborEntry.setDescription("An entry (conceptual row) in the pimNeighborTable.")
pimNeighborAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 1), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimNeighborAddress.setDescription("The IP address of the PIM neighbor for which this entry\ncontains information.")
pimNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimNeighborIfIndex.setDescription("The value of ifIndex for the interface used to reach this\nPIM neighbor.")
pimNeighborUpTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimNeighborUpTime.setDescription("The time since this PIM neighbor (last) became a neighbor\nof the local router.")
pimNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimNeighborExpiryTime.setDescription("The minimum time remaining before this PIM neighbor will be\naged out.")
pimNeighborMode = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 3, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("dense", 1), ("sparse", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimNeighborMode.setDescription("The active PIM mode of this neighbor.  This object is\ndeprecated for PIMv2 routers since all neighbors on the\ninterface must be either dense or sparse as determined by\nthe protocol running on the interface.")
pimIpMRouteTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 4))
if mibBuilder.loadTexts: pimIpMRouteTable.setDescription("The (conceptual) table listing PIM-specific information on\na subset of the rows of the ipMRouteTable defined in the IP\nMulticast MIB.")
pimIpMRouteEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 4, 1)).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteGroup"), (0, "IPMROUTE-STD-MIB", "ipMRouteSource"), (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"))
if mibBuilder.loadTexts: pimIpMRouteEntry.setDescription("An entry (conceptual row) in the pimIpMRouteTable.  There\nis one entry per entry in the ipMRouteTable whose incoming\ninterface is running PIM.")
pimIpMRouteUpstreamAssertTimer = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteUpstreamAssertTimer.setDescription("The time remaining before the router changes its upstream\nneighbor back to its RPF neighbor.  This timer is called the\nAssert timer in the PIM Sparse and Dense mode specification.\n\n\nA value of 0 indicates that no Assert has changed the\nupstream neighbor away from the RPF neighbor.")
pimIpMRouteAssertMetric = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteAssertMetric.setDescription("The metric advertised by the assert winner on the upstream\ninterface, or 0 if no such assert is in received.")
pimIpMRouteAssertMetricPref = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteAssertMetricPref.setDescription("The preference advertised by the assert winner on the\nupstream interface, or 0 if no such assert is in effect.")
pimIpMRouteAssertRPTBit = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteAssertRPTBit.setDescription("The value of the RPT-bit advertised by the assert winner on\nthe upstream interface, or false if no such assert is in\neffect.")
pimIpMRouteFlags = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 4, 1, 5), Bits().subtype(namedValues=namedval.NamedValues(("rpt", 0), ("spt", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteFlags.setDescription("This object describes PIM-specific flags related to a\nmulticast state entry.  See the PIM Sparse Mode\nspecification for the meaning of the RPT and SPT bits.")
pimRPTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 5))
if mibBuilder.loadTexts: pimRPTable.setDescription("The (conceptual) table listing PIM version 1 information\nfor the Rendezvous Points (RPs) for IP multicast groups.\nThis table is deprecated since its function is replaced by\nthe pimRPSetTable for PIM version 2.")
pimRPEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 5, 1)).setIndexNames((0, "PIM-MIB", "pimRPGroupAddress"), (0, "PIM-MIB", "pimRPAddress"))
if mibBuilder.loadTexts: pimRPEntry.setDescription("An entry (conceptual row) in the pimRPTable.  There is one\nentry per RP address for each IP multicast group.")
pimRPGroupAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 1), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimRPGroupAddress.setDescription("The IP multicast group address for which this entry\ncontains information about an RP.")
pimRPAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 2), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimRPAddress.setDescription("The unicast address of the RP.")
pimRPState = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("up", 1), ("down", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimRPState.setDescription("The state of the RP.")
pimRPStateTimer = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimRPStateTimer.setDescription("The minimum time remaining before the next state change.\nWhen pimRPState is up, this is the minimum time which must\nexpire until it can be declared down.  When pimRPState is\ndown, this is the time until it will be declared up (in\norder to retry).")
pimRPLastChange = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimRPLastChange.setDescription("The value of sysUpTime at the time when the corresponding\ninstance of pimRPState last changed its value.")
pimRPRowStatus = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimRPRowStatus.setDescription("The status of this row, by which new entries may be\ncreated, or old entries deleted from this table.")
pimRPSetTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 6))
if mibBuilder.loadTexts: pimRPSetTable.setDescription("The (conceptual) table listing PIM information for\ncandidate Rendezvous Points (RPs) for IP multicast groups.\nWhen the local router is the BSR, this information is\nobtained from received Candidate-RP-Advertisements.  When\nthe local router is not the BSR, this information is\nobtained from received RP-Set messages.")
pimRPSetEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 6, 1)).setIndexNames((0, "PIM-MIB", "pimRPSetComponent"), (0, "PIM-MIB", "pimRPSetGroupAddress"), (0, "PIM-MIB", "pimRPSetGroupMask"), (0, "PIM-MIB", "pimRPSetAddress"))
if mibBuilder.loadTexts: pimRPSetEntry.setDescription("An entry (conceptual row) in the pimRPSetTable.")
pimRPSetGroupAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 1), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimRPSetGroupAddress.setDescription("The IP multicast group address which, when combined with\npimRPSetGroupMask, gives the group prefix for which this\nentry contains information about the Candidate-RP.")
pimRPSetGroupMask = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 2), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimRPSetGroupMask.setDescription("The multicast group address mask which, when combined with\npimRPSetGroupAddress, gives the group prefix for which this\nentry contains information about the Candidate-RP.")
pimRPSetAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 3), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimRPSetAddress.setDescription("The IP address of the Candidate-RP.")
pimRPSetHoldTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimRPSetHoldTime.setDescription("The holdtime of a Candidate-RP.  If the local router is not\nthe BSR, this value is 0.")
pimRPSetExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimRPSetExpiryTime.setDescription("The minimum time remaining before the Candidate-RP will be\ndeclared down.  If the local router is not the BSR, this\nvalue is 0.")
pimRPSetComponent = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimRPSetComponent.setDescription(" A number uniquely identifying the component.  Each\nprotocol instance connected to a separate domain should have\na different index value.")
pimIpMRouteNextHopTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 7))
if mibBuilder.loadTexts: pimIpMRouteNextHopTable.setDescription("The (conceptual) table listing PIM-specific information on\na subset of the rows of the ipMRouteNextHopTable defined in\nthe IP Multicast MIB.")
pimIpMRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 7, 1)).setIndexNames((0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"), (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"))
if mibBuilder.loadTexts: pimIpMRouteNextHopEntry.setDescription("An entry (conceptual row) in the pimIpMRouteNextHopTable.\nThere is one entry per entry in the ipMRouteNextHopTable\nwhose interface is running PIM and whose\nipMRouteNextHopState is pruned(1).")
pimIpMRouteNextHopPruneReason = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 7, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("prune", 2), ("assert", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimIpMRouteNextHopPruneReason.setDescription("This object indicates why the downstream interface was\npruned, whether in response to a PIM prune message or due to\nPIM Assert processing.")
pimCandidateRPTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 11))
if mibBuilder.loadTexts: pimCandidateRPTable.setDescription("The (conceptual) table listing the IP multicast groups for\nwhich the local router is to advertise itself as a\nCandidate-RP when the value of pimComponentCRPHoldTime is\nnon-zero.  If this table is empty, then the local router\n\n\nwill advertise itself as a Candidate-RP for all groups\n(providing the value of pimComponentCRPHoldTime is non-\nzero).")
pimCandidateRPEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 11, 1)).setIndexNames((0, "PIM-MIB", "pimCandidateRPGroupAddress"), (0, "PIM-MIB", "pimCandidateRPGroupMask"))
if mibBuilder.loadTexts: pimCandidateRPEntry.setDescription("An entry (conceptual row) in the pimCandidateRPTable.")
pimCandidateRPGroupAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 1), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimCandidateRPGroupAddress.setDescription("The IP multicast group address which, when combined with\npimCandidateRPGroupMask, identifies a group prefix for which\nthe local router will advertise itself as a Candidate-RP.")
pimCandidateRPGroupMask = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 2), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimCandidateRPGroupMask.setDescription("The multicast group address mask which, when combined with\npimCandidateRPGroupMask, identifies a group prefix for which\nthe local router will advertise itself as a Candidate-RP.")
pimCandidateRPAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimCandidateRPAddress.setDescription("The (unicast) address of the interface which will be\n\n\nadvertised as a Candidate-RP.")
pimCandidateRPRowStatus = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 11, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimCandidateRPRowStatus.setDescription("The status of this row, by which new entries may be\ncreated, or old entries deleted from this table.")
pimComponentTable = MibTable((1, 3, 6, 1, 3, 61, 1, 1, 12))
if mibBuilder.loadTexts: pimComponentTable.setDescription("The (conceptual) table containing objects specific to a PIM\ndomain.  One row exists for each domain to which the router\nis connected.  A PIM-SM domain is defined as an area of the\nnetwork over which Bootstrap messages are forwarded.\nTypically, a PIM-SM router will be a member of exactly one\ndomain.  This table also supports, however, routers which\nmay form a border between two PIM-SM domains and do not\nforward Bootstrap messages between them.")
pimComponentEntry = MibTableRow((1, 3, 6, 1, 3, 61, 1, 1, 12, 1)).setIndexNames((0, "PIM-MIB", "pimComponentIndex"))
if mibBuilder.loadTexts: pimComponentEntry.setDescription("An entry (conceptual row) in the pimComponentTable.")
pimComponentIndex = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pimComponentIndex.setDescription("A number uniquely identifying the component.  Each protocol\ninstance connected to a separate domain should have a\ndifferent index value.  Routers that only support membership\nin a single PIM-SM domain should use a pimComponentIndex\nvalue of 1.")
pimComponentBSRAddress = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimComponentBSRAddress.setDescription("The IP address of the bootstrap router (BSR) for the local\nPIM region.")
pimComponentBSRExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pimComponentBSRExpiryTime.setDescription("The minimum time remaining before the bootstrap router in\nthe local domain will be declared down.  For candidate BSRs,\nthis is the time until the component sends an RP-Set\nmessage.  For other routers, this is the time until it may\naccept an RP-Set message from a lower candidate BSR.")
pimComponentCRPHoldTime = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimComponentCRPHoldTime.setDescription("The holdtime of the component when it is a candidate RP in\nthe local domain.  The value of 0 is used to indicate that\nthe local system is not a Candidate-RP.")
pimComponentStatus = MibTableColumn((1, 3, 6, 1, 3, 61, 1, 1, 12, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pimComponentStatus.setDescription("The status of this entry.  Creating the entry creates\nanother protocol instance; destroying the entry disables a\nprotocol instance.")
pimMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 61, 2))
pimMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 61, 2, 1))
pimMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 61, 2, 2))

# Augmentions

# Notifications

pimNeighborLoss = NotificationType((1, 3, 6, 1, 3, 61, 1, 0, 1)).setObjects(("PIM-MIB", "pimNeighborIfIndex"), )

# Groups

pimAssertGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 7)).setObjects(("PIM-MIB", "pimIpMRouteAssertRPTBit"), ("PIM-MIB", "pimIpMRouteAssertMetric"), ("PIM-MIB", "pimIpMRouteAssertMetricPref"), )
pimNotificationGroup = NotificationGroup((1, 3, 6, 1, 3, 61, 2, 2, 1)).setObjects(("PIM-MIB", "pimNeighborLoss"), )
pimNextHopGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 6)).setObjects(("PIM-MIB", "pimIpMRouteNextHopPruneReason"), )
pimDenseV2MIBGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 5)).setObjects(("PIM-MIB", "pimInterfaceMode"), ("PIM-MIB", "pimInterfaceDR"), ("PIM-MIB", "pimNeighborIfIndex"), ("PIM-MIB", "pimInterfaceStatus"), ("PIM-MIB", "pimNeighborExpiryTime"), ("PIM-MIB", "pimInterfaceHelloInterval"), ("PIM-MIB", "pimInterfaceNetMask"), ("PIM-MIB", "pimNeighborUpTime"), ("PIM-MIB", "pimInterfaceAddress"), )
pimV1MIBGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 4)).setObjects(("PIM-MIB", "pimJoinPruneInterval"), ("PIM-MIB", "pimInterfaceMode"), ("PIM-MIB", "pimInterfaceStatus"), ("PIM-MIB", "pimRPRowStatus"), ("PIM-MIB", "pimNeighborIfIndex"), ("PIM-MIB", "pimRPLastChange"), ("PIM-MIB", "pimRPStateTimer"), ("PIM-MIB", "pimNeighborExpiryTime"), ("PIM-MIB", "pimRPState"), ("PIM-MIB", "pimInterfaceHelloInterval"), ("PIM-MIB", "pimInterfaceJoinPruneInterval"), ("PIM-MIB", "pimNeighborMode"), ("PIM-MIB", "pimInterfaceNetMask"), ("PIM-MIB", "pimInterfaceDR"), ("PIM-MIB", "pimNeighborUpTime"), ("PIM-MIB", "pimInterfaceAddress"), )
pimV2MIBGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 2)).setObjects(("PIM-MIB", "pimJoinPruneInterval"), ("PIM-MIB", "pimInterfaceMode"), ("PIM-MIB", "pimInterfaceDR"), ("PIM-MIB", "pimRPSetExpiryTime"), ("PIM-MIB", "pimNeighborIfIndex"), ("PIM-MIB", "pimInterfaceStatus"), ("PIM-MIB", "pimComponentCRPHoldTime"), ("PIM-MIB", "pimComponentBSRAddress"), ("PIM-MIB", "pimNeighborExpiryTime"), ("PIM-MIB", "pimInterfaceHelloInterval"), ("PIM-MIB", "pimComponentStatus"), ("PIM-MIB", "pimInterfaceCBSRPreference"), ("PIM-MIB", "pimInterfaceJoinPruneInterval"), ("PIM-MIB", "pimIpMRouteFlags"), ("PIM-MIB", "pimInterfaceNetMask"), ("PIM-MIB", "pimRPSetHoldTime"), ("PIM-MIB", "pimIpMRouteUpstreamAssertTimer"), ("PIM-MIB", "pimComponentBSRExpiryTime"), ("PIM-MIB", "pimNeighborUpTime"), ("PIM-MIB", "pimInterfaceAddress"), )
pimV2CandidateRPMIBGroup = ObjectGroup((1, 3, 6, 1, 3, 61, 2, 2, 3)).setObjects(("PIM-MIB", "pimCandidateRPAddress"), ("PIM-MIB", "pimCandidateRPRowStatus"), )

# Exports

# Module identity
mibBuilder.exportSymbols("PIM-MIB", PYSNMP_MODULE_ID=pimMIB)

# Objects
mibBuilder.exportSymbols("PIM-MIB", pimMIB=pimMIB, pimMIBObjects=pimMIBObjects, pimTraps=pimTraps, pim=pim, pimJoinPruneInterval=pimJoinPruneInterval, pimInterfaceTable=pimInterfaceTable, pimInterfaceEntry=pimInterfaceEntry, pimInterfaceIfIndex=pimInterfaceIfIndex, pimInterfaceAddress=pimInterfaceAddress, pimInterfaceNetMask=pimInterfaceNetMask, pimInterfaceMode=pimInterfaceMode, pimInterfaceDR=pimInterfaceDR, pimInterfaceHelloInterval=pimInterfaceHelloInterval, pimInterfaceStatus=pimInterfaceStatus, pimInterfaceJoinPruneInterval=pimInterfaceJoinPruneInterval, pimInterfaceCBSRPreference=pimInterfaceCBSRPreference, pimNeighborTable=pimNeighborTable, pimNeighborEntry=pimNeighborEntry, pimNeighborAddress=pimNeighborAddress, pimNeighborIfIndex=pimNeighborIfIndex, pimNeighborUpTime=pimNeighborUpTime, pimNeighborExpiryTime=pimNeighborExpiryTime, pimNeighborMode=pimNeighborMode, pimIpMRouteTable=pimIpMRouteTable, pimIpMRouteEntry=pimIpMRouteEntry, pimIpMRouteUpstreamAssertTimer=pimIpMRouteUpstreamAssertTimer, pimIpMRouteAssertMetric=pimIpMRouteAssertMetric, pimIpMRouteAssertMetricPref=pimIpMRouteAssertMetricPref, pimIpMRouteAssertRPTBit=pimIpMRouteAssertRPTBit, pimIpMRouteFlags=pimIpMRouteFlags, pimRPTable=pimRPTable, pimRPEntry=pimRPEntry, pimRPGroupAddress=pimRPGroupAddress, pimRPAddress=pimRPAddress, pimRPState=pimRPState, pimRPStateTimer=pimRPStateTimer, pimRPLastChange=pimRPLastChange, pimRPRowStatus=pimRPRowStatus, pimRPSetTable=pimRPSetTable, pimRPSetEntry=pimRPSetEntry, pimRPSetGroupAddress=pimRPSetGroupAddress, pimRPSetGroupMask=pimRPSetGroupMask, pimRPSetAddress=pimRPSetAddress, pimRPSetHoldTime=pimRPSetHoldTime, pimRPSetExpiryTime=pimRPSetExpiryTime, pimRPSetComponent=pimRPSetComponent, pimIpMRouteNextHopTable=pimIpMRouteNextHopTable, pimIpMRouteNextHopEntry=pimIpMRouteNextHopEntry, pimIpMRouteNextHopPruneReason=pimIpMRouteNextHopPruneReason, pimCandidateRPTable=pimCandidateRPTable, pimCandidateRPEntry=pimCandidateRPEntry, pimCandidateRPGroupAddress=pimCandidateRPGroupAddress, pimCandidateRPGroupMask=pimCandidateRPGroupMask, pimCandidateRPAddress=pimCandidateRPAddress, pimCandidateRPRowStatus=pimCandidateRPRowStatus, pimComponentTable=pimComponentTable, pimComponentEntry=pimComponentEntry, pimComponentIndex=pimComponentIndex, pimComponentBSRAddress=pimComponentBSRAddress, pimComponentBSRExpiryTime=pimComponentBSRExpiryTime, pimComponentCRPHoldTime=pimComponentCRPHoldTime, pimComponentStatus=pimComponentStatus, pimMIBConformance=pimMIBConformance, pimMIBCompliances=pimMIBCompliances, pimMIBGroups=pimMIBGroups)

# Notifications
mibBuilder.exportSymbols("PIM-MIB", pimNeighborLoss=pimNeighborLoss)

# Groups
mibBuilder.exportSymbols("PIM-MIB", pimAssertGroup=pimAssertGroup, pimNotificationGroup=pimNotificationGroup, pimNextHopGroup=pimNextHopGroup, pimDenseV2MIBGroup=pimDenseV2MIBGroup, pimV1MIBGroup=pimV1MIBGroup, pimV2MIBGroup=pimV2MIBGroup, pimV2CandidateRPMIBGroup=pimV2CandidateRPMIBGroup)
