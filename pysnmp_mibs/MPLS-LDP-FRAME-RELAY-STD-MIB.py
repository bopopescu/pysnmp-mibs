# PySNMP SMI module. Autogenerated from smidump -f python MPLS-LDP-FRAME-RELAY-STD-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 19:13:29 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( DLCI, ) = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "DLCI")
( InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
( mplsLdpEntityIndex, mplsLdpEntityLdpId, mplsLdpPeerLdpId, ) = mibBuilder.importSymbols("MPLS-LDP-STD-MIB", "mplsLdpEntityIndex", "mplsLdpEntityLdpId", "mplsLdpPeerLdpId")
( mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( RowStatus, StorageType, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType")

# Objects

mplsLdpFrameRelayStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 6)).setRevisions(("2004-06-03 00:00",))
mplsLdpFrameRelayObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 1))
mplsLdpEntityFrameRelayObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1))
mplsLdpEntityFrameRelayTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1))
mplsLdpEntityFrameRelayEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"))
mplsLdpEntityFrameRelayIfIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readcreate")
mplsLdpEntityFrameRelayMergeCap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(0,1,)).subtype(namedValues=namedval.NamedValues(("notSupported", 0), ("supported", 1), ))).setMaxAccess("readcreate")
mplsLdpEntityFrameRelayLRComponents = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
mplsLdpEntityFrameRelayVcDirectionality = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(0,1,)).subtype(namedValues=namedval.NamedValues(("bidirectional", 0), ("unidirection", 1), ))).setMaxAccess("readcreate")
mplsLdpEntityFrameRelayStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
mplsLdpEntityFrameRelayRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
mplsLdpEntityFrameRelayLRTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2))
mplsLdpEntityFrameRelayLREntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRMinDlci"))
mplsLdpEntityFrameRelayLRMinDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 1), DLCI()).setMaxAccess("noaccess")
mplsLdpEntityFrameRelayLRMaxDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 2), DLCI()).setMaxAccess("readcreate")
mplsLdpEntityFrameRelayLRLen = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(0,2,)).subtype(namedValues=namedval.NamedValues(("tenDlciBits", 0), ("twentyThreeDlciBits", 2), ))).setMaxAccess("readcreate")
mplsLdpEntityFrameRelayLRStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
mplsLdpEntityFrameRelayLRRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
mplsLdpFrameRelaySessionObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2))
mplsLdpFrameRelaySessionTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1))
mplsLdpFrameRelaySessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"), (0, "MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelaySessionMinDlci"))
mplsLdpFrameRelaySessionMinDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 1), DLCI()).setMaxAccess("noaccess")
mplsLdpFrameRelaySessionMaxDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 2), DLCI()).setMaxAccess("readonly")
mplsLdpFrameRelaySessionLen = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(0,2,)).subtype(namedValues=namedval.NamedValues(("tenDlciBits", 0), ("twentyThreeDlciBits", 2), ))).setMaxAccess("readonly")
mplsLdpFrameRelayConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 2))
mplsLdpFrameRelayGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 1))
mplsLdpFrameRelayCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 2))

# Augmentions

# Groups

mplsLdpFrameRelayGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 1, 1)).setObjects(("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRStorageType"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayIfIndexOrZero"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayMergeCap"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRLen"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelaySessionMaxDlci"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpFrameRelaySessionLen"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRRowStatus"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayRowStatus"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayVcDirectionality"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRComponents"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayStorageType"), ("MPLS-LDP-FRAME-RELAY-STD-MIB", "mplsLdpEntityFrameRelayLRMaxDlci"), )

# Exports

# Module identity
mibBuilder.exportSymbols("MPLS-LDP-FRAME-RELAY-STD-MIB", PYSNMP_MODULE_ID=mplsLdpFrameRelayStdMIB)

# Objects
mibBuilder.exportSymbols("MPLS-LDP-FRAME-RELAY-STD-MIB", mplsLdpFrameRelayStdMIB=mplsLdpFrameRelayStdMIB, mplsLdpFrameRelayObjects=mplsLdpFrameRelayObjects, mplsLdpEntityFrameRelayObjects=mplsLdpEntityFrameRelayObjects, mplsLdpEntityFrameRelayTable=mplsLdpEntityFrameRelayTable, mplsLdpEntityFrameRelayEntry=mplsLdpEntityFrameRelayEntry, mplsLdpEntityFrameRelayIfIndexOrZero=mplsLdpEntityFrameRelayIfIndexOrZero, mplsLdpEntityFrameRelayMergeCap=mplsLdpEntityFrameRelayMergeCap, mplsLdpEntityFrameRelayLRComponents=mplsLdpEntityFrameRelayLRComponents, mplsLdpEntityFrameRelayVcDirectionality=mplsLdpEntityFrameRelayVcDirectionality, mplsLdpEntityFrameRelayStorageType=mplsLdpEntityFrameRelayStorageType, mplsLdpEntityFrameRelayRowStatus=mplsLdpEntityFrameRelayRowStatus, mplsLdpEntityFrameRelayLRTable=mplsLdpEntityFrameRelayLRTable, mplsLdpEntityFrameRelayLREntry=mplsLdpEntityFrameRelayLREntry, mplsLdpEntityFrameRelayLRMinDlci=mplsLdpEntityFrameRelayLRMinDlci, mplsLdpEntityFrameRelayLRMaxDlci=mplsLdpEntityFrameRelayLRMaxDlci, mplsLdpEntityFrameRelayLRLen=mplsLdpEntityFrameRelayLRLen, mplsLdpEntityFrameRelayLRStorageType=mplsLdpEntityFrameRelayLRStorageType, mplsLdpEntityFrameRelayLRRowStatus=mplsLdpEntityFrameRelayLRRowStatus, mplsLdpFrameRelaySessionObjects=mplsLdpFrameRelaySessionObjects, mplsLdpFrameRelaySessionTable=mplsLdpFrameRelaySessionTable, mplsLdpFrameRelaySessionEntry=mplsLdpFrameRelaySessionEntry, mplsLdpFrameRelaySessionMinDlci=mplsLdpFrameRelaySessionMinDlci, mplsLdpFrameRelaySessionMaxDlci=mplsLdpFrameRelaySessionMaxDlci, mplsLdpFrameRelaySessionLen=mplsLdpFrameRelaySessionLen, mplsLdpFrameRelayConformance=mplsLdpFrameRelayConformance, mplsLdpFrameRelayGroups=mplsLdpFrameRelayGroups, mplsLdpFrameRelayCompliances=mplsLdpFrameRelayCompliances)

# Groups
mibBuilder.exportSymbols("MPLS-LDP-FRAME-RELAY-STD-MIB", mplsLdpFrameRelayGroup=mplsLdpFrameRelayGroup)
