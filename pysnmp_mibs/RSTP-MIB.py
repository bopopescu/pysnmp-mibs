#
# PySNMP MIB module RSTP-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/RSTP-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:31:43 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( dot1dStp, dot1dStpPortEntry, ) = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStp", "dot1dStpPortEntry")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( TruthValue, DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rstpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 134)).setRevisions(("2005-12-07 00:00",))
if mibBuilder.loadTexts: rstpMIB.setOrganization('IETF Bridge MIB Working Group')
if mibBuilder.loadTexts: rstpMIB.setContactInfo('Email: Bridge-mib@ietf.org')
if mibBuilder.loadTexts: rstpMIB.setDescription('The Bridge MIB Extension module for managing devices\n            that support the Rapid Spanning Tree Protocol defined\n            by IEEE 802.1w.\n\n            Copyright (C) The Internet Society (2005).  This version of\n            this MIB module is part of RFC 4318; See the RFC itself for\n            full legal notices.')
rstpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 134, 0))
rstpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 134, 1))
rstpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 134, 2))
dot1dStpVersion = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 16), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 2,)).clone(namedValues=NamedValues(("stpCompatible", 0), ("rstp", 2),)).clone('rstp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpVersion.setDescription("The version of Spanning Tree Protocol the bridge is\n            currently running.  The value 'stpCompatible(0)'\n            indicates the Spanning Tree Protocol specified in\n            IEEE 802.1D-1998 and 'rstp(2)' indicates the Rapid\n            Spanning Tree Protocol specified in IEEE 802.1w and\n            clause 17 of 802.1D-2004.  The values are directly from\n            the IEEE standard.  New values may be defined as future\n            versions of the protocol become available.\n\n            The value of this object MUST be retained across\n            reinitializations of the management system.")
dot1dStpTxHoldCount = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpTxHoldCount.setDescription('The value used by the Port Transmit state machine to limit\n            the maximum transmission rate.\n\n            The value of this object MUST be retained across\n            reinitializations of the management system.')
dot1dStpExtPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 2, 19), )
if mibBuilder.loadTexts: dot1dStpExtPortTable.setDescription('A table that contains port-specific Rapid Spanning Tree\n            information.')
dot1dStpExtPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 2, 19, 1), )
dot1dStpPortEntry.registerAugmentions(("RSTP-MIB", "dot1dStpExtPortEntry"))
dot1dStpExtPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
if mibBuilder.loadTexts: dot1dStpExtPortEntry.setDescription('A list of Rapid Spanning Tree information maintained by\n            each port.')
dot1dStpPortProtocolMigration = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortProtocolMigration.setDescription('When operating in RSTP (version 2) mode, writing true(1)\n            to this object forces this port to transmit RSTP BPDUs.\n            Any other operation on this object has no effect and\n            it always returns false(2) when read.')
dot1dStpPortAdminEdgePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortAdminEdgePort.setDescription("The administrative value of the Edge Port parameter.  A\n            value of true(1) indicates that this port should be\n            assumed as an edge-port, and a value of false(2) indicates\n            that this port should be assumed as a non-edge-port.\n            Setting this object will also cause the corresponding\n            instance of dot1dStpPortOperEdgePort to change to the\n            same value.  Note that even when this object's value\n            is true, the value of the corresponding instance of\n            dot1dStpPortOperEdgePort can be false if a BPDU has\n            been received.\n\n            The value of this object MUST be retained across\n            reinitializations of the management system.")
dot1dStpPortOperEdgePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortOperEdgePort.setDescription('The operational value of the Edge Port parameter.  The\n            object is initialized to the value of the corresponding\n            instance of dot1dStpPortAdminEdgePort.  When the\n            corresponding instance of dot1dStpPortAdminEdgePort is\n            set, this object will be changed as well.  This object\n            will also be changed to false on reception of a BPDU.')
dot1dStpPortAdminPointToPoint = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 4), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2,)).clone(namedValues=NamedValues(("forceTrue", 0), ("forceFalse", 1), ("auto", 2),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortAdminPointToPoint.setDescription('The administrative point-to-point status of the LAN segment\n            attached to this port, using the enumeration values of the\n            IEEE 802.1w clause.  A value of forceTrue(0) indicates\n            that this port should always be treated as if it is\n            connected to a point-to-point link.  A value of\n            forceFalse(1) indicates that this port should be treated as\n            having a shared media connection.  A value of auto(2)\n            indicates that this port is considered to have a\n            point-to-point link if it is an Aggregator and all of its\n            members are aggregatable, or if the MAC entity\n            is configured for full duplex operation, either through\n            auto-negotiation or by management means.  Manipulating this\n            object changes the underlying adminPortToPortMAC.\n\n            The value of this object MUST be retained across\n            reinitializations of the management system.')
dot1dStpPortOperPointToPoint = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortOperPointToPoint.setDescription('The operational point-to-point status of the LAN segment\n            attached to this port.  It indicates whether a port is\n            considered to have a point-to-point connection.\n            If adminPointToPointMAC is set to auto(2), then the value\n            of operPointToPointMAC is determined in accordance with the\n            specific procedures defined for the MAC entity concerned,\n            as defined in IEEE 802.1w, clause 6.5.  The value is\n            determined dynamically; that is, it is re-evaluated whenever\n            the value of adminPointToPointMAC changes, and whenever\n            the specific procedures defined for the MAC entity evaluate\n            a change in its point-to-point status.')
dot1dStpPortAdminPathCost = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortAdminPathCost.setDescription("The administratively assigned value for the contribution\n            of this port to the path cost of paths toward the spanning\n            tree root.\n\n            Writing a value of '0' assigns the automatically calculated\n            default Path Cost value to the port.  If the default Path\n            Cost is being used, this object returns '0' when read.\n\n            This complements the object dot1dStpPortPathCost or\n            dot1dStpPortPathCost32, which returns the operational value\n            of the path cost.\n            The value of this object MUST be retained across\n            reinitializations of the management system.")
rstpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 134, 2, 1))
rstpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 134, 2, 2))
rstpBridgeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 134, 2, 1, 1)).setObjects(*(("RSTP-MIB", "dot1dStpVersion"), ("RSTP-MIB", "dot1dStpTxHoldCount"),))
if mibBuilder.loadTexts: rstpBridgeGroup.setDescription('Rapid Spanning Tree information for the bridge.')
rstpPortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 134, 2, 1, 2)).setObjects(*(("RSTP-MIB", "dot1dStpPortProtocolMigration"), ("RSTP-MIB", "dot1dStpPortAdminEdgePort"), ("RSTP-MIB", "dot1dStpPortOperEdgePort"), ("RSTP-MIB", "dot1dStpPortAdminPointToPoint"), ("RSTP-MIB", "dot1dStpPortOperPointToPoint"), ("RSTP-MIB", "dot1dStpPortAdminPathCost"),))
if mibBuilder.loadTexts: rstpPortGroup.setDescription('Rapid Spanning Tree information for individual ports.')
rstpCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 134, 2, 2, 1)).setObjects(*(("RSTP-MIB", "rstpBridgeGroup"), ("RSTP-MIB", "rstpPortGroup"),))
if mibBuilder.loadTexts: rstpCompliance.setDescription('The compliance statement for device support of Rapid\n            Spanning Tree Protocol (RSTP) bridging services.')
mibBuilder.exportSymbols("RSTP-MIB", dot1dStpTxHoldCount=dot1dStpTxHoldCount, dot1dStpPortOperEdgePort=dot1dStpPortOperEdgePort, rstpPortGroup=rstpPortGroup, rstpCompliance=rstpCompliance, rstpConformance=rstpConformance, rstpGroups=rstpGroups, dot1dStpPortAdminEdgePort=dot1dStpPortAdminEdgePort, dot1dStpExtPortEntry=dot1dStpExtPortEntry, rstpMIB=rstpMIB, dot1dStpVersion=dot1dStpVersion, rstpBridgeGroup=rstpBridgeGroup, rstpObjects=rstpObjects, dot1dStpPortAdminPathCost=dot1dStpPortAdminPathCost, PYSNMP_MODULE_ID=rstpMIB, dot1dStpPortAdminPointToPoint=dot1dStpPortAdminPointToPoint, dot1dStpExtPortTable=dot1dStpExtPortTable, dot1dStpPortProtocolMigration=dot1dStpPortProtocolMigration, rstpNotifications=rstpNotifications, dot1dStpPortOperPointToPoint=dot1dStpPortOperPointToPoint, rstpCompliances=rstpCompliances)
