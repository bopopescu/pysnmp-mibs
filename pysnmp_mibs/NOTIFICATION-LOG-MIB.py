# PySNMP SMI module. Autogenerated from smidump -f python NOTIFICATION-LOG-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 19:13:32 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, SnmpEngineID, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpEngineID")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Opaque, TimeTicks, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Opaque", "TimeTicks", "TimeTicks", "Unsigned32", "mib-2")
( DateAndTime, RowStatus, StorageType, TAddress, TDomain, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "StorageType", "TAddress", "TDomain", "TimeStamp")

# Objects

notificationLogMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 92)).setRevisions(("2000-11-27 00:00",))
notificationLogMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 1))
nlmConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 1, 1))
nlmConfigGlobalEntryLimit = MibScalar((1, 3, 6, 1, 2, 1, 92, 1, 1, 1), Unsigned32().clone(0)).setMaxAccess("readwrite")
nlmConfigGlobalAgeOut = MibScalar((1, 3, 6, 1, 2, 1, 92, 1, 1, 2), Unsigned32().clone(1440)).setMaxAccess("readwrite").setUnits("minutes")
nlmConfigLogTable = MibTable((1, 3, 6, 1, 2, 1, 92, 1, 1, 3))
nlmConfigLogEntry = MibTableRow((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1)).setIndexNames((0, "NOTIFICATION-LOG-MIB", "nlmLogName"))
nlmLogName = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
nlmConfigLogFilterName = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readcreate")
nlmConfigLogEntryLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 3), Unsigned32().clone(0)).setMaxAccess("readcreate")
nlmConfigLogAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), )).clone(1)).setMaxAccess("readcreate")
nlmConfigLogOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,3,)).subtype(namedValues=namedval.NamedValues(("disabled", 1), ("operational", 2), ("noFilter", 3), ))).setMaxAccess("readonly")
nlmConfigLogStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 6), StorageType()).setMaxAccess("readcreate")
nlmConfigLogEntryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
nlmStats = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 1, 2))
nlmStatsGlobalNotificationsLogged = MibScalar((1, 3, 6, 1, 2, 1, 92, 1, 2, 1), Counter32()).setMaxAccess("readonly").setUnits("notifications")
nlmStatsGlobalNotificationsBumped = MibScalar((1, 3, 6, 1, 2, 1, 92, 1, 2, 2), Counter32()).setMaxAccess("readonly").setUnits("notifications")
nlmStatsLogTable = MibTable((1, 3, 6, 1, 2, 1, 92, 1, 2, 3))
nlmStatsLogEntry = MibTableRow((1, 3, 6, 1, 2, 1, 92, 1, 2, 3, 1))
nlmStatsLogNotificationsLogged = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 2, 3, 1, 1), Counter32()).setMaxAccess("readonly")
nlmStatsLogNotificationsBumped = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
nlmLog = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 1, 3))
nlmLogTable = MibTable((1, 3, 6, 1, 2, 1, 92, 1, 3, 1))
nlmLogEntry = MibTableRow((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1)).setIndexNames((0, "NOTIFICATION-LOG-MIB", "nlmLogName"), (0, "NOTIFICATION-LOG-MIB", "nlmLogIndex"))
nlmLogIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
nlmLogTime = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
nlmLogDateAndTime = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
nlmLogEngineID = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 4), SnmpEngineID()).setMaxAccess("readonly")
nlmLogEngineTAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 5), TAddress()).setMaxAccess("readonly")
nlmLogEngineTDomain = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 6), TDomain()).setMaxAccess("readonly")
nlmLogContextEngineID = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 7), SnmpEngineID()).setMaxAccess("readonly")
nlmLogContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
nlmLogNotificationID = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 9), ObjectIdentifier()).setMaxAccess("readonly")
nlmLogVariableTable = MibTable((1, 3, 6, 1, 2, 1, 92, 1, 3, 2))
nlmLogVariableEntry = MibTableRow((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1)).setIndexNames((0, "NOTIFICATION-LOG-MIB", "nlmLogName"), (0, "NOTIFICATION-LOG-MIB", "nlmLogIndex"), (0, "NOTIFICATION-LOG-MIB", "nlmLogVariableIndex"))
nlmLogVariableIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
nlmLogVariableID = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
nlmLogVariableValueType = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,6,7,3,8,2,5,9,1,)).subtype(namedValues=namedval.NamedValues(("counter32", 1), ("unsigned32", 2), ("timeTicks", 3), ("integer32", 4), ("ipAddress", 5), ("octetString", 6), ("objectId", 7), ("counter64", 8), ("opaque", 9), ))).setMaxAccess("readonly")
nlmLogVariableCounter32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
nlmLogVariableUnsigned32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
nlmLogVariableTimeTicksVal = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
nlmLogVariableInteger32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
nlmLogVariableOctetStringVal = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 8), OctetString()).setMaxAccess("readonly")
nlmLogVariableIpAddressVal = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 9), IpAddress()).setMaxAccess("readonly")
nlmLogVariableOidVal = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 10), ObjectIdentifier()).setMaxAccess("readonly")
nlmLogVariableCounter64Val = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 11), Counter64()).setMaxAccess("readonly")
nlmLogVariableOpaqueVal = MibTableColumn((1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 12), Opaque()).setMaxAccess("readonly")
notificationLogMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 3))
notificationLogMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 3, 1))
notificationLogMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 92, 3, 2))

# Augmentions
nlmConfigLogEntry.registerAugmentions(("NOTIFICATION-LOG-MIB", "nlmStatsLogEntry"))
apply(nlmStatsLogEntry.setIndexNames, nlmConfigLogEntry.getIndexNames())

# Groups

notificationLogDateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 92, 3, 2, 4)).setObjects(("NOTIFICATION-LOG-MIB", "nlmLogDateAndTime"), )
notificationLogStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 92, 3, 2, 2)).setObjects(("NOTIFICATION-LOG-MIB", "nlmStatsGlobalNotificationsLogged"), ("NOTIFICATION-LOG-MIB", "nlmStatsLogNotificationsLogged"), ("NOTIFICATION-LOG-MIB", "nlmStatsGlobalNotificationsBumped"), ("NOTIFICATION-LOG-MIB", "nlmStatsLogNotificationsBumped"), )
notificationLogConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 92, 3, 2, 1)).setObjects(("NOTIFICATION-LOG-MIB", "nlmConfigLogFilterName"), ("NOTIFICATION-LOG-MIB", "nlmConfigGlobalAgeOut"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogAdminStatus"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogOperStatus"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogEntryLimit"), ("NOTIFICATION-LOG-MIB", "nlmConfigGlobalEntryLimit"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogStorageType"), ("NOTIFICATION-LOG-MIB", "nlmConfigLogEntryStatus"), )
notificationLogLogGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 92, 3, 2, 3)).setObjects(("NOTIFICATION-LOG-MIB", "nlmLogEngineID"), ("NOTIFICATION-LOG-MIB", "nlmLogContextName"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableCounter32Val"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableOctetStringVal"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableIpAddressVal"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableInteger32Val"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableOpaqueVal"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableUnsigned32Val"), ("NOTIFICATION-LOG-MIB", "nlmLogContextEngineID"), ("NOTIFICATION-LOG-MIB", "nlmLogNotificationID"), ("NOTIFICATION-LOG-MIB", "nlmLogEngineTDomain"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableCounter64Val"), ("NOTIFICATION-LOG-MIB", "nlmLogEngineTAddress"), ("NOTIFICATION-LOG-MIB", "nlmLogTime"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableID"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableValueType"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableOidVal"), ("NOTIFICATION-LOG-MIB", "nlmLogVariableTimeTicksVal"), )

# Exports

# Module identity
mibBuilder.exportSymbols("NOTIFICATION-LOG-MIB", PYSNMP_MODULE_ID=notificationLogMIB)

# Objects
mibBuilder.exportSymbols("NOTIFICATION-LOG-MIB", notificationLogMIB=notificationLogMIB, notificationLogMIBObjects=notificationLogMIBObjects, nlmConfig=nlmConfig, nlmConfigGlobalEntryLimit=nlmConfigGlobalEntryLimit, nlmConfigGlobalAgeOut=nlmConfigGlobalAgeOut, nlmConfigLogTable=nlmConfigLogTable, nlmConfigLogEntry=nlmConfigLogEntry, nlmLogName=nlmLogName, nlmConfigLogFilterName=nlmConfigLogFilterName, nlmConfigLogEntryLimit=nlmConfigLogEntryLimit, nlmConfigLogAdminStatus=nlmConfigLogAdminStatus, nlmConfigLogOperStatus=nlmConfigLogOperStatus, nlmConfigLogStorageType=nlmConfigLogStorageType, nlmConfigLogEntryStatus=nlmConfigLogEntryStatus, nlmStats=nlmStats, nlmStatsGlobalNotificationsLogged=nlmStatsGlobalNotificationsLogged, nlmStatsGlobalNotificationsBumped=nlmStatsGlobalNotificationsBumped, nlmStatsLogTable=nlmStatsLogTable, nlmStatsLogEntry=nlmStatsLogEntry, nlmStatsLogNotificationsLogged=nlmStatsLogNotificationsLogged, nlmStatsLogNotificationsBumped=nlmStatsLogNotificationsBumped, nlmLog=nlmLog, nlmLogTable=nlmLogTable, nlmLogEntry=nlmLogEntry, nlmLogIndex=nlmLogIndex, nlmLogTime=nlmLogTime, nlmLogDateAndTime=nlmLogDateAndTime, nlmLogEngineID=nlmLogEngineID, nlmLogEngineTAddress=nlmLogEngineTAddress, nlmLogEngineTDomain=nlmLogEngineTDomain, nlmLogContextEngineID=nlmLogContextEngineID, nlmLogContextName=nlmLogContextName, nlmLogNotificationID=nlmLogNotificationID, nlmLogVariableTable=nlmLogVariableTable, nlmLogVariableEntry=nlmLogVariableEntry, nlmLogVariableIndex=nlmLogVariableIndex, nlmLogVariableID=nlmLogVariableID, nlmLogVariableValueType=nlmLogVariableValueType, nlmLogVariableCounter32Val=nlmLogVariableCounter32Val, nlmLogVariableUnsigned32Val=nlmLogVariableUnsigned32Val, nlmLogVariableTimeTicksVal=nlmLogVariableTimeTicksVal, nlmLogVariableInteger32Val=nlmLogVariableInteger32Val, nlmLogVariableOctetStringVal=nlmLogVariableOctetStringVal, nlmLogVariableIpAddressVal=nlmLogVariableIpAddressVal, nlmLogVariableOidVal=nlmLogVariableOidVal, nlmLogVariableCounter64Val=nlmLogVariableCounter64Val, nlmLogVariableOpaqueVal=nlmLogVariableOpaqueVal, notificationLogMIBConformance=notificationLogMIBConformance, notificationLogMIBCompliances=notificationLogMIBCompliances, notificationLogMIBGroups=notificationLogMIBGroups)

# Groups
mibBuilder.exportSymbols("NOTIFICATION-LOG-MIB", notificationLogDateGroup=notificationLogDateGroup, notificationLogStatsGroup=notificationLogStatsGroup, notificationLogConfigGroup=notificationLogConfigGroup, notificationLogLogGroup=notificationLogLogGroup)
