# PySNMP SMI module. Autogenerated from smidump -f python PINT-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:29 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")
( sysApplInstallPkgEntry, ) = mibBuilder.importSymbols("SYSAPPL-MIB", "sysApplInstallPkgEntry")

# Types

class PintPerfStatPeriod(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(3,4,2,1,), )
    namedValues = Integer.namedValues.clone(("last30sec", 1), ("last15min", 2), ("last24Hr", 3), ("sinceReboot", 4), )
    pass

class PintServiceType(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(3,2,4,1,), )
    namedValues = Integer.namedValues.clone(("r2C", 1), ("r2F", 2), ("r2FB", 3), ("r2HC", 4), )
    pass


# Objects

pintMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 93))
pintServerConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 1))
pintReleaseNumber = MibVariable((1, 3, 6, 1, 2, 1, 93, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
pintSysContact = MibVariable((1, 3, 6, 1, 2, 1, 93, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
pintApplInstallPkgTable = MibTable((1, 3, 6, 1, 2, 1, 93, 1, 3))
pintApplInstallPkgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 1, 3, 1))
pintApplInstallPkgDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 1, 3, 1, 1)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readonly"))
pintRegisteredGatewayTable = MibTable((1, 3, 6, 1, 2, 1, 93, 1, 4))
pintRegisteredGatewayEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 1, 4, 1))
pintRegisteredGatewayName = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 1, 4, 1, 1)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readonly"))
pintRegisteredGatewayDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 1, 4, 1, 2)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readonly"))
pintServerMonitor = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 2))
pintServerGlobalPerf = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 2, 1))
pintServerGlobalStatsTable = MibTable((1, 3, 6, 1, 2, 1, 93, 2, 1, 1))
pintServerGlobalStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1)).setIndexNames((0, "PINT-MIB", "pintServerServiceTypeIndex"), (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"))
pintServerServiceTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 1)).setColumnInitializer(MibVariable((), PintServiceType()).setMaxAccess("noaccess"))
pintServerPerfStatPeriodIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), PintPerfStatPeriod()).setMaxAccess("noaccess"))
pintServerGlobalCallsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerGlobalSuccessfulCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerGlobalDisconnectedCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerGlobalDisCUAutFCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerGlobalDisServProbCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerGlobalDisGatProbCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 1, 1, 1, 8)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerClientPerf = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 2, 2))
pintServerClientStatsTable = MibTable((1, 3, 6, 1, 2, 1, 93, 2, 2, 1))
pintServerClientStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1)).setIndexNames((0, "PINT-MIB", "pintServerClientAddress"), (0, "PINT-MIB", "pintServerServiceTypeIndex"), (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"))
pintServerClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 1)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("noaccess"))
pintServerClientCallsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerClientSuccessfulCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerClientDisconnectedCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerClientDisCAutFCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerClientDisEFProbCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 2, 1, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerUserIdPerf = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 2, 3))
pintServerUserIdStatsTable = MibTable((1, 3, 6, 1, 2, 1, 93, 2, 3, 1))
pintServerUserIdStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1)).setIndexNames((0, "PINT-MIB", "pintServerUserIdName"), (0, "PINT-MIB", "pintServerServiceTypeIndex"), (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"))
pintServerUserIdName = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 1)).setColumnInitializer(MibVariable((), SnmpAdminString().addConstraints(subtypes.ValueRangeConstraint(0, 64))).setMaxAccess("noaccess"))
pintServerUserIdCallsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerUserIdSuccessfulCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerUserIdDisconnectedCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 4)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerUserIdDiscUIdAFailCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 5)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerUserIdEFProbCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 3, 1, 1, 6)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerGatewayPerf = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 2, 4))
pintServerGatewayStatsTable = MibTable((1, 3, 6, 1, 2, 1, 93, 2, 4, 1))
pintServerGatewayStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1)).setIndexNames((0, "PINT-MIB", "pintRegisteredGatewayName"), (0, "PINT-MIB", "pintServerServiceTypeIndex"), (0, "PINT-MIB", "pintServerPerfStatPeriodIndex"))
pintServerGatewayCallsReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1, 1)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerGatewaySuccessfulCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintServerGatewayDisconnectedCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 93, 2, 4, 1, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
pintMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 3))
pintMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 3, 1))
pintMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 93, 3, 2))

# Augmentions
sysApplInstallPkgEntry, = mibBuilder.importSymbols("SYSAPPL-MIB", "sysApplInstallPkgEntry")
sysApplInstallPkgEntry.registerAugmentions(("PINT-MIB", "pintRegisteredGatewayEntry"))
sysApplInstallPkgEntry, = mibBuilder.importSymbols("SYSAPPL-MIB", "sysApplInstallPkgEntry")
sysApplInstallPkgEntry.registerAugmentions(("PINT-MIB", "pintApplInstallPkgEntry"))

# Groups

pintMibMonitorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 93, 3, 2, 2)).setObjects(("PINT-MIB", "pintServerGatewayCallsReceived"), ("PINT-MIB", "pintServerGatewaySuccessfulCalls"), ("PINT-MIB", "pintServerGlobalDisGatProbCalls"), ("PINT-MIB", "pintServerGlobalSuccessfulCalls"), ("PINT-MIB", "pintServerUserIdDisconnectedCalls"), ("PINT-MIB", "pintServerClientDisEFProbCalls"), ("PINT-MIB", "pintServerClientSuccessfulCalls"), ("PINT-MIB", "pintServerGlobalDisconnectedCalls"), ("PINT-MIB", "pintServerUserIdEFProbCalls"), ("PINT-MIB", "pintServerGlobalDisCUAutFCalls"), ("PINT-MIB", "pintServerGlobalDisServProbCalls"), ("PINT-MIB", "pintServerGatewayDisconnectedCalls"), ("PINT-MIB", "pintServerClientCallsReceived"), ("PINT-MIB", "pintServerGlobalCallsReceived"), ("PINT-MIB", "pintServerUserIdSuccessfulCalls"), ("PINT-MIB", "pintServerUserIdCallsReceived"), ("PINT-MIB", "pintServerUserIdDiscUIdAFailCalls"), ("PINT-MIB", "pintServerClientDisconnectedCalls"), ("PINT-MIB", "pintServerClientDisCAutFCalls"), )
pintMibConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 93, 3, 2, 1)).setObjects(("PINT-MIB", "pintSysContact"), ("PINT-MIB", "pintApplInstallPkgDescription"), ("PINT-MIB", "pintRegisteredGatewayDescription"), ("PINT-MIB", "pintReleaseNumber"), ("PINT-MIB", "pintRegisteredGatewayName"), )

# Exports

# Types
mibBuilder.exportSymbols("PINT-MIB", PintPerfStatPeriod=PintPerfStatPeriod, PintServiceType=PintServiceType)

# Objects
mibBuilder.exportSymbols("PINT-MIB", pintMib=pintMib, pintServerConfig=pintServerConfig, pintReleaseNumber=pintReleaseNumber, pintSysContact=pintSysContact, pintApplInstallPkgTable=pintApplInstallPkgTable, pintApplInstallPkgEntry=pintApplInstallPkgEntry, pintApplInstallPkgDescription=pintApplInstallPkgDescription, pintRegisteredGatewayTable=pintRegisteredGatewayTable, pintRegisteredGatewayEntry=pintRegisteredGatewayEntry, pintRegisteredGatewayName=pintRegisteredGatewayName, pintRegisteredGatewayDescription=pintRegisteredGatewayDescription, pintServerMonitor=pintServerMonitor, pintServerGlobalPerf=pintServerGlobalPerf, pintServerGlobalStatsTable=pintServerGlobalStatsTable, pintServerGlobalStatsEntry=pintServerGlobalStatsEntry, pintServerServiceTypeIndex=pintServerServiceTypeIndex, pintServerPerfStatPeriodIndex=pintServerPerfStatPeriodIndex, pintServerGlobalCallsReceived=pintServerGlobalCallsReceived, pintServerGlobalSuccessfulCalls=pintServerGlobalSuccessfulCalls, pintServerGlobalDisconnectedCalls=pintServerGlobalDisconnectedCalls, pintServerGlobalDisCUAutFCalls=pintServerGlobalDisCUAutFCalls, pintServerGlobalDisServProbCalls=pintServerGlobalDisServProbCalls, pintServerGlobalDisGatProbCalls=pintServerGlobalDisGatProbCalls, pintServerClientPerf=pintServerClientPerf, pintServerClientStatsTable=pintServerClientStatsTable, pintServerClientStatsEntry=pintServerClientStatsEntry, pintServerClientAddress=pintServerClientAddress, pintServerClientCallsReceived=pintServerClientCallsReceived, pintServerClientSuccessfulCalls=pintServerClientSuccessfulCalls, pintServerClientDisconnectedCalls=pintServerClientDisconnectedCalls, pintServerClientDisCAutFCalls=pintServerClientDisCAutFCalls, pintServerClientDisEFProbCalls=pintServerClientDisEFProbCalls, pintServerUserIdPerf=pintServerUserIdPerf, pintServerUserIdStatsTable=pintServerUserIdStatsTable, pintServerUserIdStatsEntry=pintServerUserIdStatsEntry, pintServerUserIdName=pintServerUserIdName, pintServerUserIdCallsReceived=pintServerUserIdCallsReceived, pintServerUserIdSuccessfulCalls=pintServerUserIdSuccessfulCalls, pintServerUserIdDisconnectedCalls=pintServerUserIdDisconnectedCalls, pintServerUserIdDiscUIdAFailCalls=pintServerUserIdDiscUIdAFailCalls, pintServerUserIdEFProbCalls=pintServerUserIdEFProbCalls, pintServerGatewayPerf=pintServerGatewayPerf, pintServerGatewayStatsTable=pintServerGatewayStatsTable, pintServerGatewayStatsEntry=pintServerGatewayStatsEntry, pintServerGatewayCallsReceived=pintServerGatewayCallsReceived, pintServerGatewaySuccessfulCalls=pintServerGatewaySuccessfulCalls, pintServerGatewayDisconnectedCalls=pintServerGatewayDisconnectedCalls, pintMibConformance=pintMibConformance, pintMibCompliances=pintMibCompliances, pintMibGroups=pintMibGroups)

# Groups
mibBuilder.exportSymbols("PINT-MIB", pintMibMonitorGroup=pintMibMonitorGroup, pintMibConfigGroup=pintMibConfigGroup)
