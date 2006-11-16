# PySNMP SMI module. Autogenerated from smidump -f python MTA-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 19:13:31 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( URLString, applIndex, ) = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "URLString", "applIndex")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( TimeInterval, ) = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval")

# Objects

mta = ModuleIdentity((1, 3, 6, 1, 2, 1, 28)).setRevisions(("2000-03-03 00:00","1999-05-12 00:00","1997-08-17 00:00","1993-11-28 00:00",))
mtaTable = MibTable((1, 3, 6, 1, 2, 1, 28, 1))
mtaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 28, 1, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
mtaReceivedMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 1), Counter32()).setMaxAccess("readonly")
mtaStoredMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
mtaTransmittedMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 3), Counter32()).setMaxAccess("readonly")
mtaReceivedVolume = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 4), Counter32()).setMaxAccess("readonly")
mtaStoredVolume = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
mtaTransmittedVolume = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 6), Counter32()).setMaxAccess("readonly")
mtaReceivedRecipients = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 7), Counter32()).setMaxAccess("readonly")
mtaStoredRecipients = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
mtaTransmittedRecipients = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 9), Counter32()).setMaxAccess("readonly")
mtaSuccessfulConvertedMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 10), Counter32()).setMaxAccess("readonly")
mtaFailedConvertedMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 11), Counter32()).setMaxAccess("readonly")
mtaLoopsDetected = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 1, 1, 12), Counter32()).setMaxAccess("readonly")
mtaGroupTable = MibTable((1, 3, 6, 1, 2, 1, 28, 2))
mtaGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 28, 2, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "MTA-MIB", "mtaGroupIndex"))
mtaGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
mtaGroupReceivedMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 2), Counter32()).setMaxAccess("readonly")
mtaGroupRejectedMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 3), Counter32()).setMaxAccess("readonly")
mtaGroupStoredMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
mtaGroupTransmittedMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 5), Counter32()).setMaxAccess("readonly")
mtaGroupReceivedVolume = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 6), Counter32()).setMaxAccess("readonly")
mtaGroupStoredVolume = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
mtaGroupTransmittedVolume = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 8), Counter32()).setMaxAccess("readonly")
mtaGroupReceivedRecipients = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 9), Counter32()).setMaxAccess("readonly")
mtaGroupStoredRecipients = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 10), Gauge32()).setMaxAccess("readonly")
mtaGroupTransmittedRecipients = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 11), Counter32()).setMaxAccess("readonly")
mtaGroupOldestMessageStored = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 12), TimeInterval()).setMaxAccess("readonly")
mtaGroupInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
mtaGroupOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 14), Gauge32()).setMaxAccess("readonly")
mtaGroupAccumulatedInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 15), Counter32()).setMaxAccess("readonly")
mtaGroupAccumulatedOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 16), Counter32()).setMaxAccess("readonly")
mtaGroupLastInboundActivity = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 17), TimeInterval()).setMaxAccess("readonly")
mtaGroupLastOutboundActivity = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 18), TimeInterval()).setMaxAccess("readonly")
mtaGroupRejectedInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 19), Counter32()).setMaxAccess("readonly")
mtaGroupFailedOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 20), Counter32()).setMaxAccess("readonly")
mtaGroupInboundRejectionReason = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 21), SnmpAdminString()).setMaxAccess("readonly")
mtaGroupOutboundConnectFailureReason = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 22), SnmpAdminString()).setMaxAccess("readonly")
mtaGroupScheduledRetry = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 23), TimeInterval()).setMaxAccess("readonly")
mtaGroupMailProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 24), ObjectIdentifier()).setMaxAccess("readonly")
mtaGroupName = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 25), SnmpAdminString()).setMaxAccess("readonly")
mtaGroupSuccessfulConvertedMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 26), Counter32()).setMaxAccess("readonly")
mtaGroupFailedConvertedMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 27), Counter32()).setMaxAccess("readonly")
mtaGroupDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 28), SnmpAdminString()).setMaxAccess("readonly")
mtaGroupURL = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 29), URLString()).setMaxAccess("readonly")
mtaGroupCreationTime = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 30), TimeInterval()).setMaxAccess("readonly")
mtaGroupHierarchy = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 31), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2147483648L, 2147483647L))).setMaxAccess("readonly")
mtaGroupOldestMessageId = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 32), SnmpAdminString()).setMaxAccess("readonly")
mtaGroupLoopsDetected = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 33), Counter32()).setMaxAccess("readonly")
mtaGroupLastOutboundAssociationAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 2, 1, 34), TimeInterval()).setMaxAccess("readonly")
mtaGroupAssociationTable = MibTable((1, 3, 6, 1, 2, 1, 28, 3))
mtaGroupAssociationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 28, 3, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "MTA-MIB", "mtaGroupIndex"), (0, "MTA-MIB", "mtaGroupAssociationIndex"))
mtaGroupAssociationIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 3, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
mtaConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 28, 4))
mtaGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 28, 4, 1))
mtaCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 28, 4, 2))
mtaGroupErrorTable = MibTable((1, 3, 6, 1, 2, 1, 28, 5))
mtaGroupErrorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 28, 5, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "MTA-MIB", "mtaGroupIndex"), (0, "MTA-MIB", "mtaStatusCode"))
mtaGroupInboundErrorCount = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 5, 1, 1), Counter32()).setMaxAccess("readonly")
mtaGroupInternalErrorCount = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 5, 1, 2), Counter32()).setMaxAccess("readonly")
mtaGroupOutboundErrorCount = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 5, 1, 3), Counter32()).setMaxAccess("readonly")
mtaStatusCode = MibTableColumn((1, 3, 6, 1, 2, 1, 28, 5, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(4000000, 5999999))).setMaxAccess("noaccess")

# Augmentions

# Groups

mtaRFC2789ErrorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 28, 4, 1, 9)).setObjects(("MTA-MIB", "mtaGroupInternalErrorCount"), ("MTA-MIB", "mtaGroupOutboundErrorCount"), ("MTA-MIB", "mtaGroupInboundErrorCount"), )
mtaRFC1566Group = ObjectGroup((1, 3, 6, 1, 2, 1, 28, 4, 1, 10)).setObjects(("MTA-MIB", "mtaTransmittedVolume"), ("MTA-MIB", "mtaGroupTransmittedVolume"), ("MTA-MIB", "mtaGroupLastOutboundActivity"), ("MTA-MIB", "mtaGroupTransmittedMessages"), ("MTA-MIB", "mtaStoredRecipients"), ("MTA-MIB", "mtaTransmittedRecipients"), ("MTA-MIB", "mtaStoredMessages"), ("MTA-MIB", "mtaGroupTransmittedRecipients"), ("MTA-MIB", "mtaReceivedVolume"), ("MTA-MIB", "mtaStoredVolume"), ("MTA-MIB", "mtaGroupStoredVolume"), ("MTA-MIB", "mtaGroupRejectedInboundAssociations"), ("MTA-MIB", "mtaTransmittedMessages"), ("MTA-MIB", "mtaGroupReceivedRecipients"), ("MTA-MIB", "mtaGroupOldestMessageStored"), ("MTA-MIB", "mtaGroupStoredRecipients"), ("MTA-MIB", "mtaGroupReceivedMessages"), ("MTA-MIB", "mtaGroupLastInboundActivity"), ("MTA-MIB", "mtaGroupMailProtocol"), ("MTA-MIB", "mtaGroupReceivedVolume"), ("MTA-MIB", "mtaReceivedRecipients"), ("MTA-MIB", "mtaReceivedMessages"), ("MTA-MIB", "mtaGroupFailedOutboundAssociations"), ("MTA-MIB", "mtaGroupOutboundConnectFailureReason"), ("MTA-MIB", "mtaGroupAccumulatedInboundAssociations"), ("MTA-MIB", "mtaGroupInboundRejectionReason"), ("MTA-MIB", "mtaGroupStoredMessages"), ("MTA-MIB", "mtaGroupRejectedMessages"), ("MTA-MIB", "mtaGroupScheduledRetry"), ("MTA-MIB", "mtaGroupInboundAssociations"), ("MTA-MIB", "mtaGroupOutboundAssociations"), ("MTA-MIB", "mtaGroupName"), ("MTA-MIB", "mtaGroupAccumulatedOutboundAssociations"), )
mtaRFC2249Group = ObjectGroup((1, 3, 6, 1, 2, 1, 28, 4, 1, 4)).setObjects(("MTA-MIB", "mtaTransmittedVolume"), ("MTA-MIB", "mtaGroupTransmittedVolume"), ("MTA-MIB", "mtaGroupLastOutboundAssociationAttempt"), ("MTA-MIB", "mtaGroupCreationTime"), ("MTA-MIB", "mtaGroupLastOutboundActivity"), ("MTA-MIB", "mtaGroupTransmittedMessages"), ("MTA-MIB", "mtaStoredRecipients"), ("MTA-MIB", "mtaGroupHierarchy"), ("MTA-MIB", "mtaTransmittedRecipients"), ("MTA-MIB", "mtaStoredMessages"), ("MTA-MIB", "mtaGroupTransmittedRecipients"), ("MTA-MIB", "mtaReceivedVolume"), ("MTA-MIB", "mtaStoredVolume"), ("MTA-MIB", "mtaGroupURL"), ("MTA-MIB", "mtaFailedConvertedMessages"), ("MTA-MIB", "mtaGroupStoredVolume"), ("MTA-MIB", "mtaGroupOldestMessageId"), ("MTA-MIB", "mtaGroupRejectedInboundAssociations"), ("MTA-MIB", "mtaGroupDescription"), ("MTA-MIB", "mtaTransmittedMessages"), ("MTA-MIB", "mtaGroupReceivedRecipients"), ("MTA-MIB", "mtaGroupOldestMessageStored"), ("MTA-MIB", "mtaGroupStoredRecipients"), ("MTA-MIB", "mtaGroupFailedConvertedMessages"), ("MTA-MIB", "mtaGroupReceivedMessages"), ("MTA-MIB", "mtaGroupLastInboundActivity"), ("MTA-MIB", "mtaGroupMailProtocol"), ("MTA-MIB", "mtaGroupSuccessfulConvertedMessages"), ("MTA-MIB", "mtaGroupReceivedVolume"), ("MTA-MIB", "mtaGroupLoopsDetected"), ("MTA-MIB", "mtaReceivedRecipients"), ("MTA-MIB", "mtaReceivedMessages"), ("MTA-MIB", "mtaGroupFailedOutboundAssociations"), ("MTA-MIB", "mtaGroupOutboundConnectFailureReason"), ("MTA-MIB", "mtaGroupAccumulatedInboundAssociations"), ("MTA-MIB", "mtaGroupInboundRejectionReason"), ("MTA-MIB", "mtaGroupStoredMessages"), ("MTA-MIB", "mtaGroupRejectedMessages"), ("MTA-MIB", "mtaGroupAccumulatedOutboundAssociations"), ("MTA-MIB", "mtaGroupScheduledRetry"), ("MTA-MIB", "mtaGroupInboundAssociations"), ("MTA-MIB", "mtaGroupOutboundAssociations"), ("MTA-MIB", "mtaGroupName"), ("MTA-MIB", "mtaLoopsDetected"), ("MTA-MIB", "mtaSuccessfulConvertedMessages"), )
mtaRFC2249AssocGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 28, 4, 1, 5)).setObjects(("MTA-MIB", "mtaGroupAssociationIndex"), )
mtaRFC2789AssocGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 28, 4, 1, 8)).setObjects(("MTA-MIB", "mtaGroupAssociationIndex"), )
mtaRFC2789Group = ObjectGroup((1, 3, 6, 1, 2, 1, 28, 4, 1, 7)).setObjects(("MTA-MIB", "mtaTransmittedVolume"), ("MTA-MIB", "mtaGroupTransmittedVolume"), ("MTA-MIB", "mtaGroupLastOutboundAssociationAttempt"), ("MTA-MIB", "mtaGroupCreationTime"), ("MTA-MIB", "mtaGroupLastOutboundActivity"), ("MTA-MIB", "mtaGroupTransmittedMessages"), ("MTA-MIB", "mtaStoredRecipients"), ("MTA-MIB", "mtaGroupHierarchy"), ("MTA-MIB", "mtaTransmittedRecipients"), ("MTA-MIB", "mtaStoredMessages"), ("MTA-MIB", "mtaGroupTransmittedRecipients"), ("MTA-MIB", "mtaReceivedVolume"), ("MTA-MIB", "mtaStoredVolume"), ("MTA-MIB", "mtaGroupURL"), ("MTA-MIB", "mtaFailedConvertedMessages"), ("MTA-MIB", "mtaGroupStoredVolume"), ("MTA-MIB", "mtaGroupOldestMessageId"), ("MTA-MIB", "mtaGroupRejectedInboundAssociations"), ("MTA-MIB", "mtaGroupDescription"), ("MTA-MIB", "mtaTransmittedMessages"), ("MTA-MIB", "mtaGroupReceivedRecipients"), ("MTA-MIB", "mtaGroupOldestMessageStored"), ("MTA-MIB", "mtaGroupStoredRecipients"), ("MTA-MIB", "mtaGroupFailedConvertedMessages"), ("MTA-MIB", "mtaGroupReceivedMessages"), ("MTA-MIB", "mtaGroupLastInboundActivity"), ("MTA-MIB", "mtaGroupMailProtocol"), ("MTA-MIB", "mtaGroupSuccessfulConvertedMessages"), ("MTA-MIB", "mtaGroupReceivedVolume"), ("MTA-MIB", "mtaGroupLoopsDetected"), ("MTA-MIB", "mtaReceivedRecipients"), ("MTA-MIB", "mtaReceivedMessages"), ("MTA-MIB", "mtaGroupFailedOutboundAssociations"), ("MTA-MIB", "mtaGroupOutboundConnectFailureReason"), ("MTA-MIB", "mtaGroupAccumulatedInboundAssociations"), ("MTA-MIB", "mtaGroupInboundRejectionReason"), ("MTA-MIB", "mtaGroupStoredMessages"), ("MTA-MIB", "mtaGroupRejectedMessages"), ("MTA-MIB", "mtaGroupAccumulatedOutboundAssociations"), ("MTA-MIB", "mtaGroupScheduledRetry"), ("MTA-MIB", "mtaGroupInboundAssociations"), ("MTA-MIB", "mtaGroupOutboundAssociations"), ("MTA-MIB", "mtaGroupName"), ("MTA-MIB", "mtaLoopsDetected"), ("MTA-MIB", "mtaSuccessfulConvertedMessages"), )
mtaRFC2249ErrorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 28, 4, 1, 6)).setObjects(("MTA-MIB", "mtaGroupInternalErrorCount"), ("MTA-MIB", "mtaGroupOutboundErrorCount"), ("MTA-MIB", "mtaGroupInboundErrorCount"), )
mtaRFC1566AssocGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 28, 4, 1, 11)).setObjects(("MTA-MIB", "mtaGroupAssociationIndex"), )

# Exports

# Module identity
mibBuilder.exportSymbols("MTA-MIB", PYSNMP_MODULE_ID=mta)

# Objects
mibBuilder.exportSymbols("MTA-MIB", mta=mta, mtaTable=mtaTable, mtaEntry=mtaEntry, mtaReceivedMessages=mtaReceivedMessages, mtaStoredMessages=mtaStoredMessages, mtaTransmittedMessages=mtaTransmittedMessages, mtaReceivedVolume=mtaReceivedVolume, mtaStoredVolume=mtaStoredVolume, mtaTransmittedVolume=mtaTransmittedVolume, mtaReceivedRecipients=mtaReceivedRecipients, mtaStoredRecipients=mtaStoredRecipients, mtaTransmittedRecipients=mtaTransmittedRecipients, mtaSuccessfulConvertedMessages=mtaSuccessfulConvertedMessages, mtaFailedConvertedMessages=mtaFailedConvertedMessages, mtaLoopsDetected=mtaLoopsDetected, mtaGroupTable=mtaGroupTable, mtaGroupEntry=mtaGroupEntry, mtaGroupIndex=mtaGroupIndex, mtaGroupReceivedMessages=mtaGroupReceivedMessages, mtaGroupRejectedMessages=mtaGroupRejectedMessages, mtaGroupStoredMessages=mtaGroupStoredMessages, mtaGroupTransmittedMessages=mtaGroupTransmittedMessages, mtaGroupReceivedVolume=mtaGroupReceivedVolume, mtaGroupStoredVolume=mtaGroupStoredVolume, mtaGroupTransmittedVolume=mtaGroupTransmittedVolume, mtaGroupReceivedRecipients=mtaGroupReceivedRecipients, mtaGroupStoredRecipients=mtaGroupStoredRecipients, mtaGroupTransmittedRecipients=mtaGroupTransmittedRecipients, mtaGroupOldestMessageStored=mtaGroupOldestMessageStored, mtaGroupInboundAssociations=mtaGroupInboundAssociations, mtaGroupOutboundAssociations=mtaGroupOutboundAssociations, mtaGroupAccumulatedInboundAssociations=mtaGroupAccumulatedInboundAssociations, mtaGroupAccumulatedOutboundAssociations=mtaGroupAccumulatedOutboundAssociations, mtaGroupLastInboundActivity=mtaGroupLastInboundActivity, mtaGroupLastOutboundActivity=mtaGroupLastOutboundActivity, mtaGroupRejectedInboundAssociations=mtaGroupRejectedInboundAssociations, mtaGroupFailedOutboundAssociations=mtaGroupFailedOutboundAssociations, mtaGroupInboundRejectionReason=mtaGroupInboundRejectionReason, mtaGroupOutboundConnectFailureReason=mtaGroupOutboundConnectFailureReason, mtaGroupScheduledRetry=mtaGroupScheduledRetry, mtaGroupMailProtocol=mtaGroupMailProtocol, mtaGroupName=mtaGroupName, mtaGroupSuccessfulConvertedMessages=mtaGroupSuccessfulConvertedMessages, mtaGroupFailedConvertedMessages=mtaGroupFailedConvertedMessages, mtaGroupDescription=mtaGroupDescription, mtaGroupURL=mtaGroupURL, mtaGroupCreationTime=mtaGroupCreationTime, mtaGroupHierarchy=mtaGroupHierarchy, mtaGroupOldestMessageId=mtaGroupOldestMessageId, mtaGroupLoopsDetected=mtaGroupLoopsDetected, mtaGroupLastOutboundAssociationAttempt=mtaGroupLastOutboundAssociationAttempt, mtaGroupAssociationTable=mtaGroupAssociationTable, mtaGroupAssociationEntry=mtaGroupAssociationEntry, mtaGroupAssociationIndex=mtaGroupAssociationIndex, mtaConformance=mtaConformance, mtaGroups=mtaGroups, mtaCompliances=mtaCompliances, mtaGroupErrorTable=mtaGroupErrorTable, mtaGroupErrorEntry=mtaGroupErrorEntry, mtaGroupInboundErrorCount=mtaGroupInboundErrorCount, mtaGroupInternalErrorCount=mtaGroupInternalErrorCount, mtaGroupOutboundErrorCount=mtaGroupOutboundErrorCount, mtaStatusCode=mtaStatusCode)

# Groups
mibBuilder.exportSymbols("MTA-MIB", mtaRFC2789ErrorGroup=mtaRFC2789ErrorGroup, mtaRFC1566Group=mtaRFC1566Group, mtaRFC2249Group=mtaRFC2249Group, mtaRFC2249AssocGroup=mtaRFC2249AssocGroup, mtaRFC2789AssocGroup=mtaRFC2789AssocGroup, mtaRFC2789Group=mtaRFC2789Group, mtaRFC2249ErrorGroup=mtaRFC2249ErrorGroup, mtaRFC1566AssocGroup=mtaRFC1566AssocGroup)
