# PySNMP SMI module. Autogenerated from smidump -f python HPR-IP-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:19 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( SnaControlPointName, ) = mibBuilder.importSymbols("APPN-MIB", "SnaControlPointName")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( hprCompliances, hprGroups, hprObjects, ) = mibBuilder.importSymbols("HPR-MIB", "hprCompliances", "hprGroups", "hprObjects")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, RowStatus, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")

# Types

class AppnTOSPrecedence(DisplayString):
    subtypeConstraints = DisplayString.subtypeConstraints + ( subtypes.ValueRangeConstraint(3, 3), )
    pass

class AppnTrafficType(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(3,2,1,5,4,), )
    namedValues = Integer.namedValues.clone(("low", 1), ("medium", 2), ("high", 3), ("network", 4), ("llcAndFnRoutedNlp", 5), )
    pass


# Objects

hprIp = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 6, 1, 5))
hprIpActiveLsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1))
hprIpActiveLsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1)).setIndexNames((0, "HPR-IP-MIB", "hprIpActiveLsLsName"), (0, "HPR-IP-MIB", "hprIpActiveLsAppnTrafficType"))
hprIpActiveLsLsName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 1)).setColumnInitializer(MibVariable((), DisplayString().addConstraints(subtypes.ValueRangeConstraint(1, 10))).setMaxAccess("noaccess"))
hprIpActiveLsAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 2)).setColumnInitializer(MibVariable((), AppnTrafficType()).setMaxAccess("noaccess"))
hprIpActiveLsUdpPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
hprIpAppnPortTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2))
hprIpAppnPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1)).setIndexNames((0, "HPR-IP-MIB", "hprIpAppnPortName"), (0, "HPR-IP-MIB", "hprIpAppnPortAppnTrafficType"))
hprIpAppnPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 1)).setColumnInitializer(MibVariable((), DisplayString().addConstraints(subtypes.ValueRangeConstraint(1, 10))).setMaxAccess("noaccess"))
hprIpAppnPortAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 2)).setColumnInitializer(MibVariable((), AppnTrafficType()).setMaxAccess("noaccess"))
hprIpAppnPortTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 3)).setColumnInitializer(MibVariable((), AppnTOSPrecedence()).setMaxAccess("readwrite"))
hprIpLsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3))
hprIpLsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1)).setIndexNames((0, "HPR-IP-MIB", "hprIpLsLsName"), (0, "HPR-IP-MIB", "hprIpLsAppnTrafficType"))
hprIpLsLsName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 1)).setColumnInitializer(MibVariable((), DisplayString().addConstraints(subtypes.ValueRangeConstraint(1, 10))).setMaxAccess("noaccess"))
hprIpLsAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 2)).setColumnInitializer(MibVariable((), AppnTrafficType()).setMaxAccess("noaccess"))
hprIpLsTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 3)).setColumnInitializer(MibVariable((), AppnTOSPrecedence()).setMaxAccess("readwrite"))
hprIpLsRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 4)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
hprIpCnTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4))
hprIpCnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1)).setIndexNames((0, "HPR-IP-MIB", "hprIpCnVrnName"), (0, "HPR-IP-MIB", "hprIpCnAppnTrafficType"))
hprIpCnVrnName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 1)).setColumnInitializer(MibVariable((), SnaControlPointName()).setMaxAccess("noaccess"))
hprIpCnAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 2)).setColumnInitializer(MibVariable((), AppnTrafficType()).setMaxAccess("noaccess"))
hprIpCnTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 3)).setColumnInitializer(MibVariable((), AppnTOSPrecedence()).setMaxAccess("readwrite"))
hprIpCnRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 4)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))

# Augmentions

# Groups

hprIpMonitoringGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 5)).setObjects(("HPR-IP-MIB", "hprIpActiveLsUdpPackets"), )
hprIpConfigurationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 6)).setObjects(("HPR-IP-MIB", "hprIpLsTOSPrecedence"), ("HPR-IP-MIB", "hprIpCnTOSPrecedence"), ("HPR-IP-MIB", "hprIpAppnPortTOSPrecedence"), ("HPR-IP-MIB", "hprIpLsRowStatus"), ("HPR-IP-MIB", "hprIpCnRowStatus"), )

# Exports

# Types
mibBuilder.exportSymbols("HPR-IP-MIB", AppnTOSPrecedence=AppnTOSPrecedence, AppnTrafficType=AppnTrafficType)

# Objects
mibBuilder.exportSymbols("HPR-IP-MIB", hprIp=hprIp, hprIpActiveLsTable=hprIpActiveLsTable, hprIpActiveLsEntry=hprIpActiveLsEntry, hprIpActiveLsLsName=hprIpActiveLsLsName, hprIpActiveLsAppnTrafficType=hprIpActiveLsAppnTrafficType, hprIpActiveLsUdpPackets=hprIpActiveLsUdpPackets, hprIpAppnPortTable=hprIpAppnPortTable, hprIpAppnPortEntry=hprIpAppnPortEntry, hprIpAppnPortName=hprIpAppnPortName, hprIpAppnPortAppnTrafficType=hprIpAppnPortAppnTrafficType, hprIpAppnPortTOSPrecedence=hprIpAppnPortTOSPrecedence, hprIpLsTable=hprIpLsTable, hprIpLsEntry=hprIpLsEntry, hprIpLsLsName=hprIpLsLsName, hprIpLsAppnTrafficType=hprIpLsAppnTrafficType, hprIpLsTOSPrecedence=hprIpLsTOSPrecedence, hprIpLsRowStatus=hprIpLsRowStatus, hprIpCnTable=hprIpCnTable, hprIpCnEntry=hprIpCnEntry, hprIpCnVrnName=hprIpCnVrnName, hprIpCnAppnTrafficType=hprIpCnAppnTrafficType, hprIpCnTOSPrecedence=hprIpCnTOSPrecedence, hprIpCnRowStatus=hprIpCnRowStatus)

# Groups
mibBuilder.exportSymbols("HPR-IP-MIB", hprIpMonitoringGroup=hprIpMonitoringGroup, hprIpConfigurationGroup=hprIpConfigurationGroup)
