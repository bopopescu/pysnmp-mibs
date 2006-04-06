# PySNMP SMI module. Autogenerated from smidump -f python MPLS-LDP-ATM-STD-MIB
# by libsmi2pysnmp-0.0.6-alpha at Thu Apr  6 13:19:26 2006,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( AtmVpIdentifier, ) = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier")
( InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
( mplsLdpEntityIndex, mplsLdpEntityLdpId, mplsLdpPeerLdpId, ) = mibBuilder.importSymbols("MPLS-LDP-STD-MIB", "mplsLdpEntityIndex", "mplsLdpEntityLdpId", "mplsLdpPeerLdpId")
( MplsAtmVcIdentifier, mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsAtmVcIdentifier", "mplsStdMIB")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( RowStatus, StorageType, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType")

# Objects

mplsLdpAtmStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 5)).setRevisions(("2004-06-03 00:00",))
mplsLdpAtmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 5, 1))
mplsLdpEntityAtmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1))
mplsLdpEntityAtmTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1))
mplsLdpEntityAtmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"))
mplsLdpEntityAtmIfIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
mplsLdpEntityAtmMergeCap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,0,2,1,)).subtype(namedValues=namedval.NamedValues(("notSupported", 0), ("vpMerge", 1), ("vcMerge", 2), ("vpAndVcMerge", 3), ))).setMaxAccess("readwrite")
mplsLdpEntityAtmLRComponents = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
mplsLdpEntityAtmVcDirectionality = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(0,1,)).subtype(namedValues=namedval.NamedValues(("bidirectional", 0), ("unidirectional", 1), ))).setMaxAccess("readwrite")
mplsLdpEntityAtmLsrConnectivity = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("direct", 1), ("indirect", 2), )).clone(1)).setMaxAccess("readwrite")
mplsLdpEntityAtmDefaultControlVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 6), AtmVpIdentifier()).setMaxAccess("readwrite")
mplsLdpEntityAtmDefaultControlVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 7), MplsAtmVcIdentifier()).setMaxAccess("readwrite")
mplsLdpEntityAtmUnlabTrafVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 8), AtmVpIdentifier()).setMaxAccess("readwrite")
mplsLdpEntityAtmUnlabTrafVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 9), MplsAtmVcIdentifier()).setMaxAccess("readwrite")
mplsLdpEntityAtmStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 10), StorageType()).setMaxAccess("readwrite")
mplsLdpEntityAtmRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 1, 1, 11), RowStatus()).setMaxAccess("readwrite")
mplsLdpEntityAtmLRTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2))
mplsLdpEntityAtmLREntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRMinVpi"), (0, "MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRMinVci"))
mplsLdpEntityAtmLRMinVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 1), AtmVpIdentifier()).setMaxAccess("noaccess")
mplsLdpEntityAtmLRMinVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 2), MplsAtmVcIdentifier()).setMaxAccess("noaccess")
mplsLdpEntityAtmLRMaxVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 3), AtmVpIdentifier()).setMaxAccess("readwrite")
mplsLdpEntityAtmLRMaxVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 4), MplsAtmVcIdentifier()).setMaxAccess("readwrite")
mplsLdpEntityAtmLRStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 5), StorageType()).setMaxAccess("readwrite")
mplsLdpEntityAtmLRRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
mplsLdpAtmSessionObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2))
mplsLdpAtmSessionTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1))
mplsLdpAtmSessionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1, 1)).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-STD-MIB", "mplsLdpPeerLdpId"), (0, "MPLS-LDP-ATM-STD-MIB", "mplsLdpSessionAtmLRLowerBoundVpi"), (0, "MPLS-LDP-ATM-STD-MIB", "mplsLdpSessionAtmLRLowerBoundVci"))
mplsLdpSessionAtmLRLowerBoundVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1, 1, 1), AtmVpIdentifier()).setMaxAccess("noaccess")
mplsLdpSessionAtmLRLowerBoundVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1, 1, 2), MplsAtmVcIdentifier()).setMaxAccess("noaccess")
mplsLdpSessionAtmLRUpperBoundVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1, 1, 3), AtmVpIdentifier()).setMaxAccess("readonly")
mplsLdpSessionAtmLRUpperBoundVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 5, 1, 2, 1, 1, 4), MplsAtmVcIdentifier()).setMaxAccess("readonly")
mplsLdpAtmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 5, 2))
mplsLdpAtmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 5, 2, 1))
mplsLdpAtmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 5, 2, 2))

# Augmentions

# Groups

mplsLdpAtmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 5, 2, 1, 1)).setObjects(("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmMergeCap"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLsrConnectivity"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRComponents"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRMaxVci"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmDefaultControlVci"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmRowStatus"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmUnlabTrafVpi"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpSessionAtmLRUpperBoundVpi"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmDefaultControlVpi"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmUnlabTrafVci"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRRowStatus"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRStorageType"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmIfIndexOrZero"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpSessionAtmLRUpperBoundVci"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmLRMaxVpi"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmVcDirectionality"), ("MPLS-LDP-ATM-STD-MIB", "mplsLdpEntityAtmStorageType"), )

# Exports

# Module identity
mibBuilder.exportSymbols("MPLS-LDP-ATM-STD-MIB", PYSNMP_MODULE_ID=mplsLdpAtmStdMIB)

# Objects
mibBuilder.exportSymbols("MPLS-LDP-ATM-STD-MIB", mplsLdpAtmStdMIB=mplsLdpAtmStdMIB, mplsLdpAtmObjects=mplsLdpAtmObjects, mplsLdpEntityAtmObjects=mplsLdpEntityAtmObjects, mplsLdpEntityAtmTable=mplsLdpEntityAtmTable, mplsLdpEntityAtmEntry=mplsLdpEntityAtmEntry, mplsLdpEntityAtmIfIndexOrZero=mplsLdpEntityAtmIfIndexOrZero, mplsLdpEntityAtmMergeCap=mplsLdpEntityAtmMergeCap, mplsLdpEntityAtmLRComponents=mplsLdpEntityAtmLRComponents, mplsLdpEntityAtmVcDirectionality=mplsLdpEntityAtmVcDirectionality, mplsLdpEntityAtmLsrConnectivity=mplsLdpEntityAtmLsrConnectivity, mplsLdpEntityAtmDefaultControlVpi=mplsLdpEntityAtmDefaultControlVpi, mplsLdpEntityAtmDefaultControlVci=mplsLdpEntityAtmDefaultControlVci, mplsLdpEntityAtmUnlabTrafVpi=mplsLdpEntityAtmUnlabTrafVpi, mplsLdpEntityAtmUnlabTrafVci=mplsLdpEntityAtmUnlabTrafVci, mplsLdpEntityAtmStorageType=mplsLdpEntityAtmStorageType, mplsLdpEntityAtmRowStatus=mplsLdpEntityAtmRowStatus, mplsLdpEntityAtmLRTable=mplsLdpEntityAtmLRTable, mplsLdpEntityAtmLREntry=mplsLdpEntityAtmLREntry, mplsLdpEntityAtmLRMinVpi=mplsLdpEntityAtmLRMinVpi, mplsLdpEntityAtmLRMinVci=mplsLdpEntityAtmLRMinVci, mplsLdpEntityAtmLRMaxVpi=mplsLdpEntityAtmLRMaxVpi, mplsLdpEntityAtmLRMaxVci=mplsLdpEntityAtmLRMaxVci, mplsLdpEntityAtmLRStorageType=mplsLdpEntityAtmLRStorageType, mplsLdpEntityAtmLRRowStatus=mplsLdpEntityAtmLRRowStatus, mplsLdpAtmSessionObjects=mplsLdpAtmSessionObjects, mplsLdpAtmSessionTable=mplsLdpAtmSessionTable, mplsLdpAtmSessionEntry=mplsLdpAtmSessionEntry, mplsLdpSessionAtmLRLowerBoundVpi=mplsLdpSessionAtmLRLowerBoundVpi, mplsLdpSessionAtmLRLowerBoundVci=mplsLdpSessionAtmLRLowerBoundVci, mplsLdpSessionAtmLRUpperBoundVpi=mplsLdpSessionAtmLRUpperBoundVpi, mplsLdpSessionAtmLRUpperBoundVci=mplsLdpSessionAtmLRUpperBoundVci, mplsLdpAtmConformance=mplsLdpAtmConformance, mplsLdpAtmGroups=mplsLdpAtmGroups, mplsLdpAtmCompliances=mplsLdpAtmCompliances)

# Groups
mibBuilder.exportSymbols("MPLS-LDP-ATM-STD-MIB", mplsLdpAtmGroup=mplsLdpAtmGroup)
