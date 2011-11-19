# PySNMP SMI module. Autogenerated from smidump -f python IFCP-MGMT-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:29:23 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( PhysicalIndexOrZero, ) = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndexOrZero")
( FcAddressIdOrZero, FcNameIdOrZero, ) = mibBuilder.importSymbols("FC-MGMT-MIB", "FcAddressIdOrZero", "FcNameIdOrZero")
( ZeroBasedCounter64, ) = mibBuilder.importSymbols("HCNUM-TC", "ZeroBasedCounter64")
( InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
( InetAddress, InetAddressType, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
( ZeroBasedCounter32, ) = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "transmission")
( StorageType, TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "TextualConvention", "TimeStamp", "TruthValue")

# Types

class IfcpAddressMode(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,1,)
    namedValues = NamedValues(("addressTransparent", 1), ("addressTranslation", 2), )
    
class IfcpIpTOVorZero(TextualConvention, Unsigned32):
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,3600)
    
class IfcpLTIorZero(TextualConvention, Unsigned32):
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,65535)
    
class IfcpSessionStates(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,2,3,)
    namedValues = NamedValues(("down", 1), ("openPending", 2), ("open", 3), )
    

# Objects

ifcpMgmtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 230)).setRevisions(("2006-01-17 00:00",))
if mibBuilder.loadTexts: ifcpMgmtMIB.setOrganization("IETF IPS Working Group")
if mibBuilder.loadTexts: ifcpMgmtMIB.setContactInfo("\nAttn: Kevin Gibbons\n      McDATA Corporation\n      4555 Great America Pkwy\n      Santa Clara, CA 95054-1208 USA\n      Phone: (408) 567-5765\n      EMail: kevin.gibbons@mcdata.com\n\n      Charles Monia\n      Consultant\n      7553 Morevern Circle\n      San Jose, CA 95135 USA\n      EMail: charles_monia@yahoo.com\n\n      Josh Tseng\n      Riverbed Technology\n      501 2nd Street, Suite 410\n      San Francisco, CA 94107 USA\n      Phone: (650) 274-2109\n      EMail: joshtseng@yahoo.com\n\n      Franco Travostino\n      Nortel\n      600 Technology Park Drive\n      Billerica, MA 01821 USA\n      Phone: (978) 288-7708\n      EMail: travos@nortel.com")
if mibBuilder.loadTexts: ifcpMgmtMIB.setDescription("This module defines management information specific\nto internet Fibre Channel Protocol (iFCP) gateway\nmanagement.\n\nCopyright (C) The Internet Society 2006.  This\nversion of this MIB module is part of RFC 4369; see\nthe RFC itself for full legal notices.")
ifcpGatewayObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 1))
ifcpLclGatewayInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 1, 1))
ifcpLclGtwyInstTable = MibTable((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1))
if mibBuilder.loadTexts: ifcpLclGtwyInstTable.setDescription("Information about all local iFCP Gateway instances that can\nbe monitored and controlled.  This table contains an entry\nfor each local iFCP Gateway instance that is being managed.")
ifcpLclGtwyInstEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1)).setIndexNames((0, "IFCP-MGMT-MIB", "ifcpLclGtwyInstIndex"))
if mibBuilder.loadTexts: ifcpLclGtwyInstEntry.setDescription("An entry in the local iFCP Gateway Instance table.\nParameters and settings for the gateway are found here.")
ifcpLclGtwyInstIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ifcpLclGtwyInstIndex.setDescription("An arbitrary integer value to uniquely identify this iFCP\nGateway from other local Gateway instances.")
ifcpLclGtwyInstPhyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 2), PhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpLclGtwyInstPhyIndex.setDescription("An index indicating the location of this local gateway within\na larger entity, if one exists.  If supported, this is the\nentPhysicalIndex from the Entity MIB (Version 3), for this\niFCP Gateway.  If not supported, or if not related to a\nphysical entity, then the value of this object is 0.")
ifcpLclGtwyInstVersionMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpLclGtwyInstVersionMin.setDescription("The minimum iFCP protocol version supported by the local iFCP\ngateway instance.")
ifcpLclGtwyInstVersionMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpLclGtwyInstVersionMax.setDescription("The maximum iFCP protocol version supported by the local iFCP\ngateway instance.")
ifcpLclGtwyInstAddrTransMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 5), IfcpAddressMode().clone('addressTranslation')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpLclGtwyInstAddrTransMode.setDescription("The local iFCP gateway operating mode.  Changing this value\nmay cause existing sessions to be disrupted.")
ifcpLclGtwyInstFcBrdcstSupport = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpLclGtwyInstFcBrdcstSupport.setDescription("Whether the local iFCP gateway supports FC Broadcast.\nChanging this value may cause existing sessions to be\ndisrupted.")
ifcpLclGtwyInstDefaultIpTOV = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 7), IfcpIpTOVorZero().clone('6')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpLclGtwyInstDefaultIpTOV.setDescription("The default IP_TOV used for iFCP sessions at this gateway.\nThis is the default maximum propagation delay that will be\nused for an iFCP session.  The value can be changed on a\nper-session basis.  The valid range is 0 - 3600 seconds.\nA value of 0 implies that fibre channel frame lifetime limits\nwill not be enforced.")
ifcpLclGtwyInstDefaultLTInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 8), IfcpLTIorZero().clone('10')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpLclGtwyInstDefaultLTInterval.setDescription("The default Liveness Test Interval (LTI), in seconds, used\nfor iFCP sessions at this gateway.  This is the default\nvalue for an iFCP session and can be changed on a\nper-session basis.  The valid range is 0 - 65535 seconds.\nA value of 0 implies no Liveness Test Interval will be\nperformed on a session.")
ifcpLclGtwyInstDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpLclGtwyInstDescr.setDescription("A user-entered description for this iFCP Gateway.")
ifcpLclGtwyInstNumActiveSessions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpLclGtwyInstNumActiveSessions.setDescription("The current total number of iFCP sessions in the open or\nopen-pending state.")
ifcpLclGtwyInstStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 11), StorageType().clone('nonVolatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpLclGtwyInstStorageType.setDescription("The storage type for this row.  Parameter values defined\nfor a gateway are usually non-volatile, but may be volatile\nor permanent in some configurations.  If permanent, then\nthe following parameters must have read-write access:\nifcpLclGtwyInstAddrTransMode, ifcpLclGtwyInstDefaultIpTOV,\nand ifcpLclGtwyInstDefaultLTInterval.")
ifcpNportSessionInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 1, 2))
ifcpSessionAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1))
if mibBuilder.loadTexts: ifcpSessionAttributesTable.setDescription("An iFCP session consists of the pair of N_PORTs comprising\nthe session endpoints joined by a single TCP/IP connection.\nThis table provides information on each iFCP session\ncurrently using a local iFCP Gateway instance.  iFCP sessions\nare created and removed by the iFCP Gateway instances, which\nare reflected in this table.")
ifcpSessionAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1)).setIndexNames((0, "IFCP-MGMT-MIB", "ifcpLclGtwyInstIndex"), (0, "IFCP-MGMT-MIB", "ifcpSessionIndex"))
if mibBuilder.loadTexts: ifcpSessionAttributesEntry.setDescription("Each entry contains information about one iFCP session consisting\nof a pair of N_PORTs joined by a single TCP/IP connection.  This\ntable's INDEX includes ifcpLclGtwyInstIndex, which identifies the\nlocal iFCP Gateway instance that created the session for the\nentry.\n\nSoon after an entry is created in this table for an iFCP session, it\nwill correspond to an entry in the tcpConnectionTable of the TCP-MIB\n(RFC 4022).  The corresponding entry might represent a preexisting\nTCP connection, or it might be a newly-created entry.  (Note that if\nIPv4 is being used, an entry in RFC 2012's tcpConnTable may also\ncorrespond.)  The values of ifcpSessionLclPrtlAddrType and\nifcpSessionRmtPrtlIfAddrType in this table and the values of\ntcpConnectionLocalAddressType and tcpConnectionRemAddressType used\nas INDEX values for the corresponding entry in the\ntcpConnectionTable should be the same; this makes it simpler to\nlocate a session's TCP connection in the TCP-MIB.  (Of course, all\nfour values need to be 'ipv4' if there's a corresponding entry in\nthe tcpConnTable.)\n\nIf an entry is created in this table for a session, prior to\nknowing which local and/or remote port numbers will be used for\nthe TCP connection, then ifcpSessionLclPrtlTcpPort and/or\nifcpSessionRmtPrtlTcpPort have the value zero until such time as\nthey can be updated to the port numbers (to be) used for the\nconnection.  (Thus, a port value of zero should not be used to\nlocate a session's TCP connection in the TCP-MIB.)\n\nWhen the TCP connection terminates, the entry in the\ntcpConnectionTable and the entry in this table both get deleted\n(and, if applicable, so does the entry in the tcpConnTable).")
ifcpSessionIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ifcpSessionIndex.setDescription("The iFCP session index is a unique value used as an index\nto the table, along with a specific local iFCP Gateway\ninstance.  This index is used because the local N Port and\nremote N Port information would create an complex index that\nwould be difficult to implement.")
ifcpSessionLclPrtlIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclPrtlIfIndex.setDescription("This is the interface index in the IF-MIB ifTable being used\nas the local portal in this session, as described in the\nIF-MIB.  If the local portal is not associated with an entry\nin the ifTable, then the value is 0.  The ifType of the\ninterface will generally be a type that supports IP, but an\nimplementation may support iFCP using other protocols.  This\nobject can be used to obtain additional information about the\ninterface.")
ifcpSessionLclPrtlAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclPrtlAddrType.setDescription("The type of address in ifcpSessionLclIfAddr.")
ifcpSessionLclPrtlAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclPrtlAddr.setDescription("This is the external IP address of the interface being used\nfor the iFCP local portal in this session.  The address type\nis defined in ifcpSessionLclPrtlAddrType.  If the value is a\nDNS name, then the name is resolved once, during the initial\nsession instantiation.")
ifcpSessionLclPrtlTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 5), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclPrtlTcpPort.setDescription("This is the TCP port number that is being used for the iFCP\nlocal portal in this session.  This is normally an ephemeral\nport number selected by the gateway.  The value may be 0\nduring an initial setup period.")
ifcpSessionLclNpWwun = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 6), FcNameIdOrZero().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclNpWwun.setDescription("World Wide Unique Name of the local N Port.  For an unbound\nsession, this variable will be a zero-length string.")
ifcpSessionLclNpFcid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 7), FcAddressIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclNpFcid.setDescription("Fibre Channel Identifier of the local N Port.  For an unbound\nsession, this variable will be a zero-length string.")
ifcpSessionRmtNpWwun = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 8), FcNameIdOrZero().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtNpWwun.setDescription("World Wide Unique Name of the remote N Port.  For an unbound\nsession, this variable will be a zero-length string.")
ifcpSessionRmtPrtlIfAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtPrtlIfAddrType.setDescription("The type of address in ifcpSessionRmtPrtlIfAddr.")
ifcpSessionRmtPrtlIfAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtPrtlIfAddr.setDescription("This is the remote gateway IP address being used for the\nportal on the remote iFCP gateway.  The address type is\ndefined in ifcpSessionRmtPrtlIfAddrType.  If the value is a\nDNS name, then the name is resolved once, during the initial\nsession instantiation.")
ifcpSessionRmtPrtlTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 11), InetPortNumber().clone('3420')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtPrtlTcpPort.setDescription("This is the TCP port number being used for the portal on the\nremote iFCP gateway.  Generally, this will be the iFCP\ncanonical port.  The value may be 0 during an initial setup\nperiod.")
ifcpSessionRmtNpFcid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 12), FcAddressIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtNpFcid.setDescription("Fibre Channel Identifier of the remote N Port.  For an\nunbound session, this variable will be a zero-length string.")
ifcpSessionRmtNpFcidAlias = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 13), FcAddressIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtNpFcidAlias.setDescription("Fibre Channel Identifier Alias assigned by the local gateway\nfor the remote N Port.  For an unbound session, this variable\nwill be a zero-length string.")
ifcpSessionIpTOV = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 14), IfcpIpTOVorZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpSessionIpTOV.setDescription("The IP_TOV being used for this iFCP session.  This is the\nmaximum propagation delay that will be used for the iFCP\nsession.  The value can be changed on a per-session basis\nand initially defaults to ifcpLclGtwyInstDefaultIpTOV for\nthe local gateway instance.  The valid range is 0 - 3600\nseconds.  A value of 0 implies fibre channel frame lifetime\nlimits will not be enforced.")
ifcpSessionLclLTIntvl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 15), IfcpLTIorZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclLTIntvl.setDescription("The Liveness Test Interval (LTI) used for this iFCP session.\nThe value can be changed on a per-session basis and initially\ndefaults to ifcpLclGtwyInstDefaultLTInterval for the local\ngateway instance.  The valid range is 0 - 65535 seconds.\nA value of 0 implies that the gateway will not originate\nLiveness Test messages for the session.")
ifcpSessionRmtLTIntvl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 16), IfcpLTIorZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtLTIntvl.setDescription("The Liveness Test Interval (LTI) as requested by the remote\ngateway instance to use for this iFCP session.  This value may\nchange over the life of the session.  The valid range is 0 -\n65535 seconds.  A value of 0 implies that the remote gateway\nhas not been requested to originate Liveness Test messages for\n\n\n\nthe session.")
ifcpSessionBound = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionBound.setDescription("This value indicates whether this session is bound to a\nspecific local and remote N Port.  Sessions by default are\nunbound and ready for future assignment to a local and remote\nN Port.")
ifcpSessionStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 18), StorageType().clone('nonVolatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionStorageType.setDescription("The storage type for this row.  Parameter values defined\nfor a session are usually non-volatile, but may be volatile\nor permanent in some configurations.  If permanent, then\nifcpSessionIpTOV must have read-write access.")
ifcpSessionStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2))
if mibBuilder.loadTexts: ifcpSessionStatsTable.setDescription("This table provides statistics on an iFCP session.")
ifcpSessionStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1))
if mibBuilder.loadTexts: ifcpSessionStatsEntry.setDescription("Provides iFCP-specific statistics per session.")
ifcpSessionState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 1), IfcpSessionStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionState.setDescription("The current session operating state.")
ifcpSessionDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionDuration.setDescription("This indicates, in seconds, how long the iFCP session has\nbeen in an open or open-pending state.  When a session is\ndown, the value is reset to 0.")
ifcpSessionTxOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 3), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionTxOctets.setDescription("The total number of octets transmitted by the iFCP gateway\nfor this session.  Discontinuities in the value of this\ncounter can occur at reinitialization of the management\nsystem, and at other times as indicated by the value of\nifcpSessionDiscontinuityTime.")
ifcpSessionRxOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 4), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRxOctets.setDescription("The total number of octets received by the iFCP gateway for\nthis session.  Discontinuities in the value of this\ncounter can occur at reinitialization of the management\nsystem, and at other times as indicated by the value of\nifcpSessionDiscontinuityTime.")
ifcpSessionTxFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 5), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionTxFrames.setDescription("The total number of iFCP frames transmitted by the gateway\nfor this session.  Discontinuities in the value of this\ncounter can occur at reinitialization of the management\nsystem, and at other times as indicated by the value of\nifcpSessionDiscontinuityTime.")
ifcpSessionRxFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 6), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRxFrames.setDescription("The total number of iFCP frames received by the gateway\nfor this session.  Discontinuities in the value of this\ncounter can occur at reinitialization of the management\nsystem, and at other times as indicated by the value of\nifcpSessionDiscontinuityTime.")
ifcpSessionStaleFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 7), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionStaleFrames.setDescription("The total number of received iFCP frames that were stale and\ndiscarded by the gateway for this session.  Discontinuities\nin the value of this counter can occur at reinitialization\nof the management system, and at other times as indicated by\nthe value of ifcpSessionDiscontinuityTime.")
ifcpSessionHeaderCRCErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 8), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionHeaderCRCErrors.setDescription("The total number of CRC errors that occurred in the frame\nheader, detected by the gateway for this session.  Usually,\na single Header CRC error is sufficient to terminate an\niFCP session.  Discontinuities in the value of this\ncounter can occur at reinitialization of the management\nsystem, and at other times as indicated by the value of\nifcpSessionDiscontinuityTime.")
ifcpSessionFcPayloadCRCErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 9), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionFcPayloadCRCErrors.setDescription("The total number of CRC errors that occurred in the Fibre\nChannel frame payload, detected by the gateway for this\nsession.  Discontinuities in the value of this counter can\noccur at reinitialization of the management system, and\nat other times as indicated by the value of\nifcpSessionDiscontinuityTime.")
ifcpSessionOtherErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 10), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionOtherErrors.setDescription("The total number of errors, other than errors explicitly\nmeasured, detected by the gateway for this session.\nDiscontinuities in the value of this counter can occur at\nreinitialization of the management system, and at other\ntimes as indicated by the value of\nifcpSessionDiscontinuityTime.")
ifcpSessionDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which\nany one (or more) of the ifcpSessionStatsTable counters\nsuffered a discontinuity.  The relevant counters are the\nspecific Counter64-based instances associated with the\nifcpSessionStatsTable: ifcpSessionTxOctets,\n\n\n\nifcpSessionRxOctets, ifcpSessionTxFrames,\nifcpSessionRxFrames, ifcpSessionStaleFrames,\nifcpSessionHeaderCRCErrors, ifcpSessionFcPayloadCRCErrors,\nand ifcpSessionOtherErrors.  If no such discontinuities have\noccurred since the last reinitialization of the local\nmanagement subsystem, then this object contains a zero value.")
ifcpSessionLcStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3))
if mibBuilder.loadTexts: ifcpSessionLcStatsTable.setDescription("This table provides low capacity statistics for an iFCP\nsession.  These are provided for backward compatibility with\nsystems that do not support Counter64-based objects.  At\n1-Gbps rates, a Counter32-based object can wrap as often as\nevery 34 seconds.  Counter32-based objects can be sufficient\nfor many situations.  However, when possible, it is\nrecommended to use the high capacity statistics in\nifcpSessionStatsTable based on Counter64 objects.")
ifcpSessionLcStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1))
if mibBuilder.loadTexts: ifcpSessionLcStatsEntry.setDescription("Provides iFCP-specific statistics per session.")
ifcpSessionLcTxOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 1), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcTxOctets.setDescription("The total number of octets transmitted by the iFCP gateway\nfor this session.")
ifcpSessionLcRxOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 2), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcRxOctets.setDescription("The total number of octets received by the iFCP gateway for\nthis session.")
ifcpSessionLcTxFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 3), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcTxFrames.setDescription("The total number of iFCP frames transmitted by the gateway\nfor this session.")
ifcpSessionLcRxFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 4), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcRxFrames.setDescription("The total number of iFCP frames received by the gateway\nfor this session.")
ifcpSessionLcStaleFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 5), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcStaleFrames.setDescription("The total number of received iFCP frames that were stale and\ndiscarded by the gateway for this session.")
ifcpSessionLcHeaderCRCErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 6), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcHeaderCRCErrors.setDescription("The total number of CRC errors that occurred in the frame\nheader, detected by the gateway for this session.  Usually,\na single Header CRC error is sufficient to terminate an\niFCP session.")
ifcpSessionLcFcPayloadCRCErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcFcPayloadCRCErrors.setDescription("The total number of CRC errors that occurred in the Fibre\nChannel frame payload, detected by the gateway for this\nsession.")
ifcpSessionLcOtherErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 8), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcOtherErrors.setDescription("The total number of errors, other than errors explicitly\nmeasured, detected by the gateway for this session.")
ifcpGatewayConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 2))
ifcpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 2, 1))
ifcpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 2, 2))

# Augmentions
ifcpSessionAttributesEntry.registerAugmentions(("IFCP-MGMT-MIB", "ifcpSessionStatsEntry"))
ifcpSessionStatsEntry.setIndexNames(*ifcpSessionAttributesEntry.getIndexNames())
ifcpSessionAttributesEntry.registerAugmentions(("IFCP-MGMT-MIB", "ifcpSessionLcStatsEntry"))
ifcpSessionLcStatsEntry.setIndexNames(*ifcpSessionAttributesEntry.getIndexNames())

# Groups

ifcpLclGatewayGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 1)).setObjects(("IFCP-MGMT-MIB", "ifcpLclGtwyInstDefaultLTInterval"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstVersionMin"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstNumActiveSessions"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstStorageType"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstDefaultIpTOV"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstAddrTransMode"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstDescr"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstPhyIndex"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstFcBrdcstSupport"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstVersionMax"), )
if mibBuilder.loadTexts: ifcpLclGatewayGroup.setDescription("iFCP local device info group.  This group provides\ninformation about each gateway.")
ifcpLclGatewaySessionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 4)).setObjects(("IFCP-MGMT-MIB", "ifcpSessionLclNpWwun"), ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlTcpPort"), ("IFCP-MGMT-MIB", "ifcpSessionRmtNpFcidAlias"), ("IFCP-MGMT-MIB", "ifcpSessionRmtLTIntvl"), ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlTcpPort"), ("IFCP-MGMT-MIB", "ifcpSessionStorageType"), ("IFCP-MGMT-MIB", "ifcpSessionIpTOV"), ("IFCP-MGMT-MIB", "ifcpSessionLclLTIntvl"), ("IFCP-MGMT-MIB", "ifcpSessionBound"), ("IFCP-MGMT-MIB", "ifcpSessionRmtNpWwun"), ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlIfAddr"), ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlAddrType"), ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlIfIndex"), ("IFCP-MGMT-MIB", "ifcpSessionRmtNpFcid"), ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlIfAddrType"), ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlAddr"), ("IFCP-MGMT-MIB", "ifcpSessionLclNpFcid"), )
if mibBuilder.loadTexts: ifcpLclGatewaySessionGroup.setDescription("iFCP Session group.  This group provides information\nabout each iFCP session currently active between iFCP\ngateways.")
ifcpLclGatewaySessionStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 5)).setObjects(("IFCP-MGMT-MIB", "ifcpSessionFcPayloadCRCErrors"), ("IFCP-MGMT-MIB", "ifcpSessionRxFrames"), ("IFCP-MGMT-MIB", "ifcpSessionDuration"), ("IFCP-MGMT-MIB", "ifcpSessionHeaderCRCErrors"), ("IFCP-MGMT-MIB", "ifcpSessionState"), ("IFCP-MGMT-MIB", "ifcpSessionTxFrames"), ("IFCP-MGMT-MIB", "ifcpSessionTxOctets"), ("IFCP-MGMT-MIB", "ifcpSessionOtherErrors"), ("IFCP-MGMT-MIB", "ifcpSessionRxOctets"), ("IFCP-MGMT-MIB", "ifcpSessionStaleFrames"), ("IFCP-MGMT-MIB", "ifcpSessionDiscontinuityTime"), )
if mibBuilder.loadTexts: ifcpLclGatewaySessionStatsGroup.setDescription("iFCP Session Statistics group.  This group provides\nstatistics with 64-bit counters for each iFCP session\ncurrently active between iFCP gateways.  This group\nis only required for agents that can support Counter64-\nbased data types.")
ifcpLclGatewaySessionLcStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 6)).setObjects(("IFCP-MGMT-MIB", "ifcpSessionLcFcPayloadCRCErrors"), ("IFCP-MGMT-MIB", "ifcpSessionLcTxOctets"), ("IFCP-MGMT-MIB", "ifcpSessionLcTxFrames"), ("IFCP-MGMT-MIB", "ifcpSessionLcRxOctets"), ("IFCP-MGMT-MIB", "ifcpSessionLcStaleFrames"), ("IFCP-MGMT-MIB", "ifcpSessionLcRxFrames"), ("IFCP-MGMT-MIB", "ifcpSessionLcOtherErrors"), ("IFCP-MGMT-MIB", "ifcpSessionLcHeaderCRCErrors"), )
if mibBuilder.loadTexts: ifcpLclGatewaySessionLcStatsGroup.setDescription("iFCP Session Low Capacity Statistics group.  This group\nprovides statistics with low-capacity 32-bit counters\n\n\n\nfor each iFCP session currently active between iFCP\ngateways.  This group is only required for agents that\ndo not support Counter64-based data types, or that need\nto support SNMPv1 applications.")

# Compliances

ifcpGatewayCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 230, 2, 1, 1)).setObjects(("IFCP-MGMT-MIB", "ifcpLclGatewayGroup"), ("IFCP-MGMT-MIB", "ifcpLclGatewaySessionGroup"), ("IFCP-MGMT-MIB", "ifcpLclGatewaySessionLcStatsGroup"), ("IFCP-MGMT-MIB", "ifcpLclGatewaySessionStatsGroup"), )
if mibBuilder.loadTexts: ifcpGatewayCompliance.setDescription("Implementation requirements for iFCP MIB compliance.")

# Exports

# Module identity
mibBuilder.exportSymbols("IFCP-MGMT-MIB", PYSNMP_MODULE_ID=ifcpMgmtMIB)

# Types
mibBuilder.exportSymbols("IFCP-MGMT-MIB", IfcpAddressMode=IfcpAddressMode, IfcpIpTOVorZero=IfcpIpTOVorZero, IfcpLTIorZero=IfcpLTIorZero, IfcpSessionStates=IfcpSessionStates)

# Objects
mibBuilder.exportSymbols("IFCP-MGMT-MIB", ifcpMgmtMIB=ifcpMgmtMIB, ifcpGatewayObjects=ifcpGatewayObjects, ifcpLclGatewayInfo=ifcpLclGatewayInfo, ifcpLclGtwyInstTable=ifcpLclGtwyInstTable, ifcpLclGtwyInstEntry=ifcpLclGtwyInstEntry, ifcpLclGtwyInstIndex=ifcpLclGtwyInstIndex, ifcpLclGtwyInstPhyIndex=ifcpLclGtwyInstPhyIndex, ifcpLclGtwyInstVersionMin=ifcpLclGtwyInstVersionMin, ifcpLclGtwyInstVersionMax=ifcpLclGtwyInstVersionMax, ifcpLclGtwyInstAddrTransMode=ifcpLclGtwyInstAddrTransMode, ifcpLclGtwyInstFcBrdcstSupport=ifcpLclGtwyInstFcBrdcstSupport, ifcpLclGtwyInstDefaultIpTOV=ifcpLclGtwyInstDefaultIpTOV, ifcpLclGtwyInstDefaultLTInterval=ifcpLclGtwyInstDefaultLTInterval, ifcpLclGtwyInstDescr=ifcpLclGtwyInstDescr, ifcpLclGtwyInstNumActiveSessions=ifcpLclGtwyInstNumActiveSessions, ifcpLclGtwyInstStorageType=ifcpLclGtwyInstStorageType, ifcpNportSessionInfo=ifcpNportSessionInfo, ifcpSessionAttributesTable=ifcpSessionAttributesTable, ifcpSessionAttributesEntry=ifcpSessionAttributesEntry, ifcpSessionIndex=ifcpSessionIndex, ifcpSessionLclPrtlIfIndex=ifcpSessionLclPrtlIfIndex, ifcpSessionLclPrtlAddrType=ifcpSessionLclPrtlAddrType, ifcpSessionLclPrtlAddr=ifcpSessionLclPrtlAddr, ifcpSessionLclPrtlTcpPort=ifcpSessionLclPrtlTcpPort, ifcpSessionLclNpWwun=ifcpSessionLclNpWwun, ifcpSessionLclNpFcid=ifcpSessionLclNpFcid, ifcpSessionRmtNpWwun=ifcpSessionRmtNpWwun, ifcpSessionRmtPrtlIfAddrType=ifcpSessionRmtPrtlIfAddrType, ifcpSessionRmtPrtlIfAddr=ifcpSessionRmtPrtlIfAddr, ifcpSessionRmtPrtlTcpPort=ifcpSessionRmtPrtlTcpPort, ifcpSessionRmtNpFcid=ifcpSessionRmtNpFcid, ifcpSessionRmtNpFcidAlias=ifcpSessionRmtNpFcidAlias, ifcpSessionIpTOV=ifcpSessionIpTOV, ifcpSessionLclLTIntvl=ifcpSessionLclLTIntvl, ifcpSessionRmtLTIntvl=ifcpSessionRmtLTIntvl, ifcpSessionBound=ifcpSessionBound, ifcpSessionStorageType=ifcpSessionStorageType, ifcpSessionStatsTable=ifcpSessionStatsTable, ifcpSessionStatsEntry=ifcpSessionStatsEntry, ifcpSessionState=ifcpSessionState, ifcpSessionDuration=ifcpSessionDuration, ifcpSessionTxOctets=ifcpSessionTxOctets, ifcpSessionRxOctets=ifcpSessionRxOctets, ifcpSessionTxFrames=ifcpSessionTxFrames, ifcpSessionRxFrames=ifcpSessionRxFrames, ifcpSessionStaleFrames=ifcpSessionStaleFrames, ifcpSessionHeaderCRCErrors=ifcpSessionHeaderCRCErrors, ifcpSessionFcPayloadCRCErrors=ifcpSessionFcPayloadCRCErrors, ifcpSessionOtherErrors=ifcpSessionOtherErrors, ifcpSessionDiscontinuityTime=ifcpSessionDiscontinuityTime, ifcpSessionLcStatsTable=ifcpSessionLcStatsTable, ifcpSessionLcStatsEntry=ifcpSessionLcStatsEntry, ifcpSessionLcTxOctets=ifcpSessionLcTxOctets, ifcpSessionLcRxOctets=ifcpSessionLcRxOctets, ifcpSessionLcTxFrames=ifcpSessionLcTxFrames, ifcpSessionLcRxFrames=ifcpSessionLcRxFrames, ifcpSessionLcStaleFrames=ifcpSessionLcStaleFrames, ifcpSessionLcHeaderCRCErrors=ifcpSessionLcHeaderCRCErrors, ifcpSessionLcFcPayloadCRCErrors=ifcpSessionLcFcPayloadCRCErrors, ifcpSessionLcOtherErrors=ifcpSessionLcOtherErrors, ifcpGatewayConformance=ifcpGatewayConformance, ifcpCompliances=ifcpCompliances, ifcpGroups=ifcpGroups)

# Groups
mibBuilder.exportSymbols("IFCP-MGMT-MIB", ifcpLclGatewayGroup=ifcpLclGatewayGroup, ifcpLclGatewaySessionGroup=ifcpLclGatewaySessionGroup, ifcpLclGatewaySessionStatsGroup=ifcpLclGatewaySessionStatsGroup, ifcpLclGatewaySessionLcStatsGroup=ifcpLclGatewaySessionLcStatsGroup)

# Compliances
mibBuilder.exportSymbols("IFCP-MGMT-MIB", ifcpGatewayCompliance=ifcpGatewayCompliance)
