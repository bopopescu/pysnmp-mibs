# PySNMP SMI module. Autogenerated from smidump -f python TCPIPX-MIB
# by libsmi2pysnmp-0.0.9-alpha at Thu Mar 26 19:36:38 2009,
# Python version (2, 4, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises")

# Types

class IpxAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(10,10)
    fixedLength = 10
    pass


# Objects

novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
mibDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
tcpx = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 29))
tcpxTcp = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 29, 1))
tcpIpxConnTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1))
if mibBuilder.loadTexts: tcpIpxConnTable.setDescription("A table containing information specific on\nTCP connection over IPX network layer.")
tcpIpxConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1)).setIndexNames((0, "TCPIPX-MIB", "tcpIpxConnLocalAddress"), (0, "TCPIPX-MIB", "tcpIpxConnLocalPort"), (0, "TCPIPX-MIB", "tcpIpxConnRemAddress"), (0, "TCPIPX-MIB", "tcpIpxConnRemPort"))
if mibBuilder.loadTexts: tcpIpxConnEntry.setDescription("Information about a particular current TCP\nconnection over IPX  An object of this type is\ntransient, in that it ceases to exist when (or\nsoon after) the connection makes the transition\nto the CLOSED state.")
tcpIpxConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,5,7,11,9,8,12,6,1,10,2,3,)).subtype(namedValues=namedval.NamedValues(("closed", 1), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpIpxConnState.setDescription("The state of this TCP connection.\n\nThe only value which may be set by a management\nstation is deleteTCB(12).  Accordingly, it is\nappropriate for an agent to return a `badValue'\nresponse if a management station attempts to set\nthis object to any other value.\n\nIf a management station sets this object to the\nvalue deleteTCB(12), then this has the effect of\ndeleting the TCB (as defined in RFC 793) of the\ncorresponding connection on the managed node,\nresulting in immediate termination of the\nconnection.\n\nAs an implementation-specific option, a RST\nsegment may be sent from the managed node to the\nother TCP endpoint (note however that RST\nsegments are not sent reliably).")
tcpIpxConnLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 2), IpxAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpIpxConnLocalAddress.setDescription("The local IPX address for this TCP connection.\nIn the case of a connection in the listen state\nwhich is willing to accept connections for any\ninterface, the value 00000000:000000000000 is\nused.  See tcpUnspecConnTable for connections in\nthe listen  state which is willing to accept\nconnects for any IP interface associated with\nthe node.")
tcpIpxConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpIpxConnLocalPort.setDescription("The local port number for this TCP connection.")
tcpIpxConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 4), IpxAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpIpxConnRemAddress.setDescription("The remote IPX address for this TCP connection.")
tcpIpxConnRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpIpxConnRemPort.setDescription("The remote port number for this TCP connection.")
tcpUnspecConnTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2))
if mibBuilder.loadTexts: tcpUnspecConnTable.setDescription("A table containing information specific on\nTCP connection over unspecified network layer.")
tcpUnspecConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1)).setIndexNames((0, "TCPIPX-MIB", "tcpUnspecConnLocalPort"))
if mibBuilder.loadTexts: tcpUnspecConnEntry.setDescription("Information about a particular current TCP\nconnection over unspecified network layer.  An\nobject of this type is transient, in that it\nceases to exist when the connection makes\ntransition beyond LISTEN state, or when (or\nsoon after) the connection makes transition\nto the CLOSED state,")
tcpUnspecConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(12,2,1,)).subtype(namedValues=namedval.NamedValues(("closed", 1), ("deleteTCB", 12), ("listen", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpUnspecConnState.setDescription("The state of this TCP connection.\n\nSince the TCP connection can belong to this table\nonly when its state is less than SYN_SENT, only\nclosed and listen state apply.\n\nThe only value which may be set by a management\nstation is deleteTCB(12).  Accordingly, it is\nappropriate for an agent to return a `badValue'\nresponse if a management station attempts to set\nthis object to any other value.\n\nIf a management station sets this object to the\nvalue deleteTCB(12), then this has the effect of\ndeleting the TCB (as defined in RFC 793) of the\ncorresponding connection on the managed node,\nresulting in immediate termination of the\nconnection.\n\nAs an implementation-specific option, a RST\nsegment may be sent from the managed node to the\nother TCP endpoint (note however that RST\nsegments are not sent reliably).")
tcpUnspecConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpUnspecConnLocalPort.setDescription("The local port number for this TCP connection.")
tcpxUdp = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 29, 2))
udpIpxTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1))
if mibBuilder.loadTexts: udpIpxTable.setDescription("A table containing UDP listener information.")
udpIpxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1)).setIndexNames((0, "TCPIPX-MIB", "udpIpxLocalAddress"), (0, "TCPIPX-MIB", "udpIpxLocalPort"))
if mibBuilder.loadTexts: udpIpxEntry.setDescription("Information about a particular current UDP\nlistener.")
udpIpxLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1, 1), IpxAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpIpxLocalAddress.setDescription("The local IPX address for this UDP listener.  In\nthe case of a UDP listener which is willing to\naccept datagrams for any interface, the value\n00000000:000000000000 is used.  See\nudpUnspecTable for UDP listener which is\nwilling to accept datagrams from any network\nlayer.")
udpIpxLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpIpxLocalPort.setDescription("The local port number for this UDP listener.")
udpUnspecTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2))
if mibBuilder.loadTexts: udpUnspecTable.setDescription("A table containing UDP listener information.")
udpUnspecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2, 1)).setIndexNames((0, "TCPIPX-MIB", "udpUnspecLocalPort"))
if mibBuilder.loadTexts: udpUnspecEntry.setDescription("Information about a particular current UDP\nlistener.")
udpUnspecLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpUnspecLocalPort.setDescription("The local port number for this UDP listener.")

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("TCPIPX-MIB", IpxAddress=IpxAddress)

# Objects
mibBuilder.exportSymbols("TCPIPX-MIB", novell=novell, mibDoc=mibDoc, tcpx=tcpx, tcpxTcp=tcpxTcp, tcpIpxConnTable=tcpIpxConnTable, tcpIpxConnEntry=tcpIpxConnEntry, tcpIpxConnState=tcpIpxConnState, tcpIpxConnLocalAddress=tcpIpxConnLocalAddress, tcpIpxConnLocalPort=tcpIpxConnLocalPort, tcpIpxConnRemAddress=tcpIpxConnRemAddress, tcpIpxConnRemPort=tcpIpxConnRemPort, tcpUnspecConnTable=tcpUnspecConnTable, tcpUnspecConnEntry=tcpUnspecConnEntry, tcpUnspecConnState=tcpUnspecConnState, tcpUnspecConnLocalPort=tcpUnspecConnLocalPort, tcpxUdp=tcpxUdp, udpIpxTable=udpIpxTable, udpIpxEntry=udpIpxEntry, udpIpxLocalAddress=udpIpxLocalAddress, udpIpxLocalPort=udpIpxLocalPort, udpUnspecTable=udpUnspecTable, udpUnspecEntry=udpUnspecEntry, udpUnspecLocalPort=udpUnspecLocalPort)

