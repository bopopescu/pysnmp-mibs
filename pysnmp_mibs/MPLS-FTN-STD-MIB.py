# PySNMP SMI module. Autogenerated from smidump -f python MPLS-FTN-STD-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 19:13:29 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Dscp, ) = mibBuilder.importSymbols("DIFFSERV-DSCP-TC", "Dscp")
( InterfaceIndexOrZero, ifCounterDiscontinuityGroup, ifGeneralInformationGroup, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifCounterDiscontinuityGroup", "ifGeneralInformationGroup")
( InetAddress, InetAddressType, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
( mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( RowPointer, RowStatus, StorageType, TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "RowStatus", "StorageType", "TextualConvention", "TimeStamp")

# Types

class MplsFTNEntryIndex(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+constraint.ValueRangeConstraint(1,4294967295L)
    pass

class MplsFTNEntryIndexOrZero(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+constraint.ValueRangeConstraint(0,4294967295L)
    pass


# Objects

mplsFTNStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 8)).setRevisions(("2004-06-03 00:00",))
mplsFTNNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 8, 0))
mplsFTNObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 8, 1))
mplsFTNIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 1), MplsFTNEntryIndexOrZero()).setMaxAccess("readonly")
mplsFTNTableLastChanged = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 2), TimeStamp()).setMaxAccess("readonly")
mplsFTNTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3))
mplsFTNEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1)).setIndexNames((0, "MPLS-FTN-STD-MIB", "mplsFTNIndex"))
mplsFTNIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 1), MplsFTNEntryIndex()).setMaxAccess("noaccess")
mplsFTNRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
mplsFTNDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
mplsFTNMask = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 4), Bits().subtype(namedValues=namedval.NamedValues(("sourceAddr", 0), ("destAddr", 1), ("sourcePort", 2), ("destPort", 3), ("protocol", 4), ("dscp", 5), ))).setMaxAccess("readcreate")
mplsFTNAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 5), InetAddressType()).setMaxAccess("readcreate")
mplsFTNSourceAddrMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 6), InetAddress()).setMaxAccess("readcreate")
mplsFTNSourceAddrMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 7), InetAddress()).setMaxAccess("readcreate")
mplsFTNDestAddrMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 8), InetAddress()).setMaxAccess("readcreate")
mplsFTNDestAddrMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 9), InetAddress()).setMaxAccess("readcreate")
mplsFTNSourcePortMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 10), InetPortNumber().clone(0)).setMaxAccess("readcreate")
mplsFTNSourcePortMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 11), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
mplsFTNDestPortMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 12), InetPortNumber().clone(0)).setMaxAccess("readcreate")
mplsFTNDestPortMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 13), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
mplsFTNProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255)).clone(255)).setMaxAccess("readcreate")
mplsFTNDscp = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 15), Dscp()).setMaxAccess("readcreate")
mplsFTNActionType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 16), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("redirectLsp", 1), ("redirectTunnel", 2), ))).setMaxAccess("readcreate")
mplsFTNActionPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 17), RowPointer()).setMaxAccess("readcreate")
mplsFTNStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 3, 1, 18), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
mplsFTNMapTableLastChanged = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 4), TimeStamp()).setMaxAccess("readonly")
mplsFTNMapTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5))
mplsFTNMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1)).setIndexNames((0, "MPLS-FTN-STD-MIB", "mplsFTNMapIndex"), (0, "MPLS-FTN-STD-MIB", "mplsFTNMapPrevIndex"), (0, "MPLS-FTN-STD-MIB", "mplsFTNMapCurrIndex"))
mplsFTNMapIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 1), InterfaceIndexOrZero()).setMaxAccess("noaccess")
mplsFTNMapPrevIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 2), MplsFTNEntryIndexOrZero()).setMaxAccess("noaccess")
mplsFTNMapCurrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 3), MplsFTNEntryIndex()).setMaxAccess("noaccess")
mplsFTNMapRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,1,6,)).subtype(namedValues=namedval.NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6), ))).setMaxAccess("readcreate")
mplsFTNMapStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 5, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
mplsFTNPerfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6))
mplsFTNPerfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1)).setIndexNames((0, "MPLS-FTN-STD-MIB", "mplsFTNPerfIndex"), (0, "MPLS-FTN-STD-MIB", "mplsFTNPerfCurrIndex"))
mplsFTNPerfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 1), InterfaceIndexOrZero()).setMaxAccess("noaccess")
mplsFTNPerfCurrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 2), MplsFTNEntryIndex()).setMaxAccess("noaccess")
mplsFTNPerfMatchedPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 3), Counter64()).setMaxAccess("readonly")
mplsFTNPerfMatchedOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 4), Counter64()).setMaxAccess("readonly")
mplsFTNPerfDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 8, 1, 6, 1, 5), TimeStamp()).setMaxAccess("readonly")
mplsFTNConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 8, 2))
mplsFTNGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1))
mplsFTNCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 2))

# Augmentions

# Groups

mplsFTNMapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1, 2)).setObjects(("MPLS-FTN-STD-MIB", "mplsFTNMapTableLastChanged"), ("MPLS-FTN-STD-MIB", "mplsFTNMapStorageType"), ("MPLS-FTN-STD-MIB", "mplsFTNMapRowStatus"), )
mplsFTNPerfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1, 3)).setObjects(("MPLS-FTN-STD-MIB", "mplsFTNPerfDiscontinuityTime"), ("MPLS-FTN-STD-MIB", "mplsFTNPerfMatchedOctets"), ("MPLS-FTN-STD-MIB", "mplsFTNPerfMatchedPackets"), )
mplsFTNRuleGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 8, 2, 1, 1)).setObjects(("MPLS-FTN-STD-MIB", "mplsFTNSourcePortMax"), ("MPLS-FTN-STD-MIB", "mplsFTNAddrType"), ("MPLS-FTN-STD-MIB", "mplsFTNIndexNext"), ("MPLS-FTN-STD-MIB", "mplsFTNDestPortMin"), ("MPLS-FTN-STD-MIB", "mplsFTNTableLastChanged"), ("MPLS-FTN-STD-MIB", "mplsFTNDestPortMax"), ("MPLS-FTN-STD-MIB", "mplsFTNDestAddrMin"), ("MPLS-FTN-STD-MIB", "mplsFTNStorageType"), ("MPLS-FTN-STD-MIB", "mplsFTNSourceAddrMin"), ("MPLS-FTN-STD-MIB", "mplsFTNDescr"), ("MPLS-FTN-STD-MIB", "mplsFTNProtocol"), ("MPLS-FTN-STD-MIB", "mplsFTNSourcePortMin"), ("MPLS-FTN-STD-MIB", "mplsFTNDestAddrMax"), ("MPLS-FTN-STD-MIB", "mplsFTNActionPointer"), ("MPLS-FTN-STD-MIB", "mplsFTNActionType"), ("MPLS-FTN-STD-MIB", "mplsFTNSourceAddrMax"), ("MPLS-FTN-STD-MIB", "mplsFTNDscp"), ("MPLS-FTN-STD-MIB", "mplsFTNRowStatus"), ("MPLS-FTN-STD-MIB", "mplsFTNMask"), )

# Exports

# Module identity
mibBuilder.exportSymbols("MPLS-FTN-STD-MIB", PYSNMP_MODULE_ID=mplsFTNStdMIB)

# Types
mibBuilder.exportSymbols("MPLS-FTN-STD-MIB", MplsFTNEntryIndex=MplsFTNEntryIndex, MplsFTNEntryIndexOrZero=MplsFTNEntryIndexOrZero)

# Objects
mibBuilder.exportSymbols("MPLS-FTN-STD-MIB", mplsFTNStdMIB=mplsFTNStdMIB, mplsFTNNotifications=mplsFTNNotifications, mplsFTNObjects=mplsFTNObjects, mplsFTNIndexNext=mplsFTNIndexNext, mplsFTNTableLastChanged=mplsFTNTableLastChanged, mplsFTNTable=mplsFTNTable, mplsFTNEntry=mplsFTNEntry, mplsFTNIndex=mplsFTNIndex, mplsFTNRowStatus=mplsFTNRowStatus, mplsFTNDescr=mplsFTNDescr, mplsFTNMask=mplsFTNMask, mplsFTNAddrType=mplsFTNAddrType, mplsFTNSourceAddrMin=mplsFTNSourceAddrMin, mplsFTNSourceAddrMax=mplsFTNSourceAddrMax, mplsFTNDestAddrMin=mplsFTNDestAddrMin, mplsFTNDestAddrMax=mplsFTNDestAddrMax, mplsFTNSourcePortMin=mplsFTNSourcePortMin, mplsFTNSourcePortMax=mplsFTNSourcePortMax, mplsFTNDestPortMin=mplsFTNDestPortMin, mplsFTNDestPortMax=mplsFTNDestPortMax, mplsFTNProtocol=mplsFTNProtocol, mplsFTNDscp=mplsFTNDscp, mplsFTNActionType=mplsFTNActionType, mplsFTNActionPointer=mplsFTNActionPointer, mplsFTNStorageType=mplsFTNStorageType, mplsFTNMapTableLastChanged=mplsFTNMapTableLastChanged, mplsFTNMapTable=mplsFTNMapTable, mplsFTNMapEntry=mplsFTNMapEntry, mplsFTNMapIndex=mplsFTNMapIndex, mplsFTNMapPrevIndex=mplsFTNMapPrevIndex, mplsFTNMapCurrIndex=mplsFTNMapCurrIndex, mplsFTNMapRowStatus=mplsFTNMapRowStatus, mplsFTNMapStorageType=mplsFTNMapStorageType, mplsFTNPerfTable=mplsFTNPerfTable, mplsFTNPerfEntry=mplsFTNPerfEntry, mplsFTNPerfIndex=mplsFTNPerfIndex, mplsFTNPerfCurrIndex=mplsFTNPerfCurrIndex, mplsFTNPerfMatchedPackets=mplsFTNPerfMatchedPackets, mplsFTNPerfMatchedOctets=mplsFTNPerfMatchedOctets, mplsFTNPerfDiscontinuityTime=mplsFTNPerfDiscontinuityTime, mplsFTNConformance=mplsFTNConformance, mplsFTNGroups=mplsFTNGroups, mplsFTNCompliances=mplsFTNCompliances)

# Groups
mibBuilder.exportSymbols("MPLS-FTN-STD-MIB", mplsFTNMapGroup=mplsFTNMapGroup, mplsFTNPerfGroup=mplsFTNPerfGroup, mplsFTNRuleGroup=mplsFTNRuleGroup)
