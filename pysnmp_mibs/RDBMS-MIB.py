# PySNMP SMI module. Autogenerated from smidump -f python RDBMS-MIB
# by libsmi2pysnmp-0.0.6-alpha at Thu Apr  6 13:19:32 2006,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( hrSystem, ) = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrSystem")
( applGroups, applIndex, ) = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applGroups", "applIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( AutonomousType, DateAndTime, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "DateAndTime", "DisplayString")

# Objects

rdbmsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 39)).setRevisions(("1994-06-15 06:55",))
rdbmsObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 39, 1))
rdbmsDbTable = MibTable((1, 3, 6, 1, 2, 1, 39, 1, 1))
rdbmsDbEntry = MibTableRow((1, 3, 6, 1, 2, 1, 39, 1, 1, 1)).setIndexNames((0, "RDBMS-MIB", "rdbmsDbIndex"))
rdbmsDbIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
rdbmsDbPrivateMibOID = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
rdbmsDbVendorName = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
rdbmsDbName = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
rdbmsDbContact = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
rdbmsDbInfoTable = MibTable((1, 3, 6, 1, 2, 1, 39, 1, 2))
rdbmsDbInfoEntry = MibTableRow((1, 3, 6, 1, 2, 1, 39, 1, 2, 1)).setIndexNames((0, "RDBMS-MIB", "rdbmsDbIndex"))
rdbmsDbInfoProductName = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
rdbmsDbInfoVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
rdbmsDbInfoSizeUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,5,1,2,4,)).subtype(namedValues=namedval.NamedValues(("bytes", 1), ("kbytes", 2), ("mbytes", 3), ("gbytes", 4), ("tbytes", 5), ))).setMaxAccess("readonly")
rdbmsDbInfoSizeAllocated = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readwrite")
rdbmsDbInfoSizeUsed = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
rdbmsDbInfoLastBackup = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 6), DateAndTime()).setMaxAccess("readonly")
rdbmsDbParamTable = MibTable((1, 3, 6, 1, 2, 1, 39, 1, 3))
rdbmsDbParamEntry = MibTableRow((1, 3, 6, 1, 2, 1, 39, 1, 3, 1)).setIndexNames((0, "RDBMS-MIB", "rdbmsDbIndex"), (0, "RDBMS-MIB", "rdbmsDbParamName"), (0, "RDBMS-MIB", "rdbmsDbParamSubIndex"))
rdbmsDbParamName = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 64))).setMaxAccess("noaccess")
rdbmsDbParamSubIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
rdbmsDbParamID = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 3, 1, 3), AutonomousType()).setMaxAccess("readonly")
rdbmsDbParamCurrValue = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 3, 1, 4), DisplayString()).setMaxAccess("readwrite")
rdbmsDbParamComment = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 3, 1, 5), DisplayString()).setMaxAccess("readwrite")
rdbmsDbLimitedResourceTable = MibTable((1, 3, 6, 1, 2, 1, 39, 1, 4))
rdbmsDbLimitedResourceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 39, 1, 4, 1)).setIndexNames((0, "RDBMS-MIB", "rdbmsDbIndex"), (0, "RDBMS-MIB", "rdbmsDbLimitedResourceName"))
rdbmsDbLimitedResourceName = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 1), DisplayString()).setMaxAccess("noaccess")
rdbmsDbLimitedResourceID = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 2), AutonomousType()).setMaxAccess("readonly")
rdbmsDbLimitedResourceLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readwrite")
rdbmsDbLimitedResourceCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
rdbmsDbLimitedResourceHighwater = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
rdbmsDbLimitedResourceFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
rdbmsDbLimitedResourceDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 7), DisplayString()).setMaxAccess("readwrite")
rdbmsSrvTable = MibTable((1, 3, 6, 1, 2, 1, 39, 1, 5))
rdbmsSrvEntry = MibTableRow((1, 3, 6, 1, 2, 1, 39, 1, 5, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
rdbmsSrvPrivateMibOID = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 5, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
rdbmsSrvVendorName = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
rdbmsSrvProductName = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
rdbmsSrvContact = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 5, 1, 4), DisplayString()).setMaxAccess("readwrite")
rdbmsSrvInfoTable = MibTable((1, 3, 6, 1, 2, 1, 39, 1, 6))
rdbmsSrvInfoEntry = MibTableRow((1, 3, 6, 1, 2, 1, 39, 1, 6, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
rdbmsSrvInfoStartupTime = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 1), DateAndTime()).setMaxAccess("readonly")
rdbmsSrvInfoFinishedTransactions = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 2), Gauge32()).setMaxAccess("readonly")
rdbmsSrvInfoDiskReads = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
rdbmsSrvInfoLogicalReads = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
rdbmsSrvInfoDiskWrites = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
rdbmsSrvInfoLogicalWrites = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
rdbmsSrvInfoPageReads = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
rdbmsSrvInfoPageWrites = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 8), Counter32()).setMaxAccess("readonly")
rdbmsSrvInfoDiskOutOfSpaces = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
rdbmsSrvInfoHandledRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 10), Counter32()).setMaxAccess("readonly")
rdbmsSrvInfoRequestRecvs = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 11), Counter32()).setMaxAccess("readonly")
rdbmsSrvInfoRequestSends = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 12), Counter32()).setMaxAccess("readonly")
rdbmsSrvInfoHighwaterInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 13), Gauge32()).setMaxAccess("readonly")
rdbmsSrvInfoMaxInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 14), Gauge32()).setMaxAccess("readwrite")
rdbmsSrvParamTable = MibTable((1, 3, 6, 1, 2, 1, 39, 1, 7))
rdbmsSrvParamEntry = MibTableRow((1, 3, 6, 1, 2, 1, 39, 1, 7, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "RDBMS-MIB", "rdbmsSrvParamName"), (0, "RDBMS-MIB", "rdbmsSrvParamSubIndex"))
rdbmsSrvParamName = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 7, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 64))).setMaxAccess("noaccess")
rdbmsSrvParamSubIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
rdbmsSrvParamID = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 7, 1, 3), AutonomousType()).setMaxAccess("readonly")
rdbmsSrvParamCurrValue = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 7, 1, 4), DisplayString()).setMaxAccess("readwrite")
rdbmsSrvParamComment = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 7, 1, 5), DisplayString()).setMaxAccess("readwrite")
rdbmsSrvLimitedResourceTable = MibTable((1, 3, 6, 1, 2, 1, 39, 1, 8))
rdbmsSrvLimitedResourceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 39, 1, 8, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "RDBMS-MIB", "rdbmsSrvLimitedResourceName"))
rdbmsSrvLimitedResourceName = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 1), DisplayString()).setMaxAccess("noaccess")
rdbmsSrvLimitedResourceID = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 2), AutonomousType()).setMaxAccess("readonly")
rdbmsSrvLimitedResourceLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readwrite")
rdbmsSrvLimitedResourceCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
rdbmsSrvLimitedResourceHighwater = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
rdbmsSrvLimitedResourceFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 6), Counter32()).setMaxAccess("readonly")
rdbmsSrvLimitedResourceDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 7), DisplayString()).setMaxAccess("readwrite")
rdbmsRelTable = MibTable((1, 3, 6, 1, 2, 1, 39, 1, 9))
rdbmsRelEntry = MibTableRow((1, 3, 6, 1, 2, 1, 39, 1, 9, 1)).setIndexNames((0, "RDBMS-MIB", "rdbmsDbIndex"), (0, "NETWORK-SERVICES-MIB", "applIndex"))
rdbmsRelState = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 9, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,5,4,1,2,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("active", 2), ("available", 3), ("restricted", 4), ("unavailable", 5), ))).setMaxAccess("readonly")
rdbmsRelActiveTime = MibTableColumn((1, 3, 6, 1, 2, 1, 39, 1, 9, 1, 2), DateAndTime()).setMaxAccess("readonly")
rdbmsWellKnownLimitedResources = MibIdentifier((1, 3, 6, 1, 2, 1, 39, 1, 10))
rdbmsLogSpace = MibIdentifier((1, 3, 6, 1, 2, 1, 39, 1, 10, 1))
rdbmsTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 39, 2))
rdbmsConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 39, 3))
rdbmsCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 39, 3, 1))
rdbmsGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 39, 3, 2))

# Augmentions

# Notifications

rdbmsOutOfSpace = NotificationType((1, 3, 6, 1, 2, 1, 39, 2, 2)).setObjects(("RDBMS-MIB", "rdbmsSrvInfoDiskOutOfSpaces"), )
rdbmsStateChange = NotificationType((1, 3, 6, 1, 2, 1, 39, 2, 1)).setObjects(("RDBMS-MIB", "rdbmsRelState"), )

# Groups

rdbmsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 39, 3, 2, 1)).setObjects(("RDBMS-MIB", "rdbmsDbVendorName"), ("RDBMS-MIB", "rdbmsSrvParamComment"), ("RDBMS-MIB", "rdbmsSrvVendorName"), ("RDBMS-MIB", "rdbmsSrvInfoStartupTime"), ("RDBMS-MIB", "rdbmsSrvInfoLogicalReads"), ("RDBMS-MIB", "rdbmsSrvInfoPageWrites"), ("RDBMS-MIB", "rdbmsSrvLimitedResourceHighwater"), ("RDBMS-MIB", "rdbmsSrvPrivateMibOID"), ("RDBMS-MIB", "rdbmsSrvParamCurrValue"), ("RDBMS-MIB", "rdbmsSrvInfoRequestRecvs"), ("RDBMS-MIB", "rdbmsSrvLimitedResourceLimit"), ("RDBMS-MIB", "rdbmsDbInfoLastBackup"), ("RDBMS-MIB", "rdbmsDbInfoProductName"), ("RDBMS-MIB", "rdbmsDbName"), ("RDBMS-MIB", "rdbmsDbLimitedResourceHighwater"), ("RDBMS-MIB", "rdbmsDbPrivateMibOID"), ("RDBMS-MIB", "rdbmsDbLimitedResourceLimit"), ("RDBMS-MIB", "rdbmsSrvInfoHighwaterInboundAssociations"), ("RDBMS-MIB", "rdbmsDbContact"), ("RDBMS-MIB", "rdbmsDbLimitedResourceDescription"), ("RDBMS-MIB", "rdbmsDbInfoSizeAllocated"), ("RDBMS-MIB", "rdbmsSrvLimitedResourceFailures"), ("RDBMS-MIB", "rdbmsSrvContact"), ("RDBMS-MIB", "rdbmsDbParamCurrValue"), ("RDBMS-MIB", "rdbmsSrvInfoDiskWrites"), ("RDBMS-MIB", "rdbmsSrvInfoFinishedTransactions"), ("RDBMS-MIB", "rdbmsSrvInfoMaxInboundAssociations"), ("RDBMS-MIB", "rdbmsSrvProductName"), ("RDBMS-MIB", "rdbmsSrvLimitedResourceCurrent"), ("RDBMS-MIB", "rdbmsSrvLimitedResourceDescription"), ("RDBMS-MIB", "rdbmsDbLimitedResourceFailures"), ("RDBMS-MIB", "rdbmsDbInfoSizeUnits"), ("RDBMS-MIB", "rdbmsDbParamComment"), ("RDBMS-MIB", "rdbmsSrvInfoPageReads"), ("RDBMS-MIB", "rdbmsRelActiveTime"), ("RDBMS-MIB", "rdbmsDbInfoSizeUsed"), ("RDBMS-MIB", "rdbmsDbLimitedResourceCurrent"), ("RDBMS-MIB", "rdbmsDbInfoVersion"), ("RDBMS-MIB", "rdbmsSrvInfoLogicalWrites"), ("RDBMS-MIB", "rdbmsSrvInfoHandledRequests"), ("RDBMS-MIB", "rdbmsSrvInfoRequestSends"), ("RDBMS-MIB", "rdbmsRelState"), ("RDBMS-MIB", "rdbmsSrvInfoDiskReads"), )

# Exports

# Module identity
mibBuilder.exportSymbols("RDBMS-MIB", PYSNMP_MODULE_ID=rdbmsMIB)

# Objects
mibBuilder.exportSymbols("RDBMS-MIB", rdbmsMIB=rdbmsMIB, rdbmsObjects=rdbmsObjects, rdbmsDbTable=rdbmsDbTable, rdbmsDbEntry=rdbmsDbEntry, rdbmsDbIndex=rdbmsDbIndex, rdbmsDbPrivateMibOID=rdbmsDbPrivateMibOID, rdbmsDbVendorName=rdbmsDbVendorName, rdbmsDbName=rdbmsDbName, rdbmsDbContact=rdbmsDbContact, rdbmsDbInfoTable=rdbmsDbInfoTable, rdbmsDbInfoEntry=rdbmsDbInfoEntry, rdbmsDbInfoProductName=rdbmsDbInfoProductName, rdbmsDbInfoVersion=rdbmsDbInfoVersion, rdbmsDbInfoSizeUnits=rdbmsDbInfoSizeUnits, rdbmsDbInfoSizeAllocated=rdbmsDbInfoSizeAllocated, rdbmsDbInfoSizeUsed=rdbmsDbInfoSizeUsed, rdbmsDbInfoLastBackup=rdbmsDbInfoLastBackup, rdbmsDbParamTable=rdbmsDbParamTable, rdbmsDbParamEntry=rdbmsDbParamEntry, rdbmsDbParamName=rdbmsDbParamName, rdbmsDbParamSubIndex=rdbmsDbParamSubIndex, rdbmsDbParamID=rdbmsDbParamID, rdbmsDbParamCurrValue=rdbmsDbParamCurrValue, rdbmsDbParamComment=rdbmsDbParamComment, rdbmsDbLimitedResourceTable=rdbmsDbLimitedResourceTable, rdbmsDbLimitedResourceEntry=rdbmsDbLimitedResourceEntry, rdbmsDbLimitedResourceName=rdbmsDbLimitedResourceName, rdbmsDbLimitedResourceID=rdbmsDbLimitedResourceID, rdbmsDbLimitedResourceLimit=rdbmsDbLimitedResourceLimit, rdbmsDbLimitedResourceCurrent=rdbmsDbLimitedResourceCurrent, rdbmsDbLimitedResourceHighwater=rdbmsDbLimitedResourceHighwater, rdbmsDbLimitedResourceFailures=rdbmsDbLimitedResourceFailures, rdbmsDbLimitedResourceDescription=rdbmsDbLimitedResourceDescription, rdbmsSrvTable=rdbmsSrvTable, rdbmsSrvEntry=rdbmsSrvEntry, rdbmsSrvPrivateMibOID=rdbmsSrvPrivateMibOID, rdbmsSrvVendorName=rdbmsSrvVendorName, rdbmsSrvProductName=rdbmsSrvProductName, rdbmsSrvContact=rdbmsSrvContact, rdbmsSrvInfoTable=rdbmsSrvInfoTable, rdbmsSrvInfoEntry=rdbmsSrvInfoEntry, rdbmsSrvInfoStartupTime=rdbmsSrvInfoStartupTime, rdbmsSrvInfoFinishedTransactions=rdbmsSrvInfoFinishedTransactions, rdbmsSrvInfoDiskReads=rdbmsSrvInfoDiskReads, rdbmsSrvInfoLogicalReads=rdbmsSrvInfoLogicalReads, rdbmsSrvInfoDiskWrites=rdbmsSrvInfoDiskWrites, rdbmsSrvInfoLogicalWrites=rdbmsSrvInfoLogicalWrites, rdbmsSrvInfoPageReads=rdbmsSrvInfoPageReads, rdbmsSrvInfoPageWrites=rdbmsSrvInfoPageWrites, rdbmsSrvInfoDiskOutOfSpaces=rdbmsSrvInfoDiskOutOfSpaces, rdbmsSrvInfoHandledRequests=rdbmsSrvInfoHandledRequests, rdbmsSrvInfoRequestRecvs=rdbmsSrvInfoRequestRecvs, rdbmsSrvInfoRequestSends=rdbmsSrvInfoRequestSends, rdbmsSrvInfoHighwaterInboundAssociations=rdbmsSrvInfoHighwaterInboundAssociations, rdbmsSrvInfoMaxInboundAssociations=rdbmsSrvInfoMaxInboundAssociations, rdbmsSrvParamTable=rdbmsSrvParamTable, rdbmsSrvParamEntry=rdbmsSrvParamEntry, rdbmsSrvParamName=rdbmsSrvParamName, rdbmsSrvParamSubIndex=rdbmsSrvParamSubIndex, rdbmsSrvParamID=rdbmsSrvParamID, rdbmsSrvParamCurrValue=rdbmsSrvParamCurrValue, rdbmsSrvParamComment=rdbmsSrvParamComment, rdbmsSrvLimitedResourceTable=rdbmsSrvLimitedResourceTable, rdbmsSrvLimitedResourceEntry=rdbmsSrvLimitedResourceEntry, rdbmsSrvLimitedResourceName=rdbmsSrvLimitedResourceName, rdbmsSrvLimitedResourceID=rdbmsSrvLimitedResourceID, rdbmsSrvLimitedResourceLimit=rdbmsSrvLimitedResourceLimit, rdbmsSrvLimitedResourceCurrent=rdbmsSrvLimitedResourceCurrent, rdbmsSrvLimitedResourceHighwater=rdbmsSrvLimitedResourceHighwater, rdbmsSrvLimitedResourceFailures=rdbmsSrvLimitedResourceFailures, rdbmsSrvLimitedResourceDescription=rdbmsSrvLimitedResourceDescription, rdbmsRelTable=rdbmsRelTable, rdbmsRelEntry=rdbmsRelEntry, rdbmsRelState=rdbmsRelState, rdbmsRelActiveTime=rdbmsRelActiveTime, rdbmsWellKnownLimitedResources=rdbmsWellKnownLimitedResources, rdbmsLogSpace=rdbmsLogSpace, rdbmsTraps=rdbmsTraps, rdbmsConformance=rdbmsConformance, rdbmsCompliances=rdbmsCompliances, rdbmsGroups=rdbmsGroups)

# Notifications
mibBuilder.exportSymbols("RDBMS-MIB", rdbmsOutOfSpace=rdbmsOutOfSpace, rdbmsStateChange=rdbmsStateChange)

# Groups
mibBuilder.exportSymbols("RDBMS-MIB", rdbmsGroup=rdbmsGroup)
