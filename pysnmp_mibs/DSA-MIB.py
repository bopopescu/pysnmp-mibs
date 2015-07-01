#
# PySNMP MIB module DSA-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/DSA-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:27:36 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( applIndex, DistinguishedName, ) = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex", "DistinguishedName")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TimeStamp, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
dsaMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 29))
if mibBuilder.loadTexts: dsaMIB.setOrganization('IETF Mail and Directory Management Working\n                         Group')
if mibBuilder.loadTexts: dsaMIB.setContactInfo('        Glenn Mansfield\n\n              Postal: AIC Systems Laboratory\n                      6-6-3, Minami Yoshinari\n                      Aoba-ku, Sendai, 989-32\n                      JP\n\n              Tel:    +81 22 279 3310\n              Fax:    +81 22 279 3640\n              E-Mail: glenn@aic.co.jp')
if mibBuilder.loadTexts: dsaMIB.setDescription(' The MIB module for monitoring Directory System Agents.')
dsaOpsTable = MibTable((1, 3, 6, 1, 2, 1, 29, 1), )
if mibBuilder.loadTexts: dsaOpsTable.setDescription(' The table holding information related to the\n                DSA operations.')
dsaOpsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 29, 1, 1), ).setIndexNames((0, "DSA-MIB", "applIndex"))
if mibBuilder.loadTexts: dsaOpsEntry.setDescription(' Entry containing operations related statistics\n                for a DSA.')
dsaAnonymousBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaAnonymousBinds.setDescription(' Number of anonymous  binds to this DSA from DUAs\n                since application start.')
dsaUnauthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaUnauthBinds.setDescription(' Number of un-authenticated binds to this\n                DSA since application start.')
dsaSimpleAuthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaSimpleAuthBinds.setDescription(' Number of binds to this DSA that were authenticated\n                using simple authentication procedures since\n                application start.')
dsaStrongAuthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaStrongAuthBinds.setDescription(' Number of binds to this DSA that were authenticated\n                using the strong authentication procedures since\n                application start. This includes the binds that were\n                authenticated using external authentication procedures.')
dsaBindSecurityErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaBindSecurityErrors.setDescription(' Number of bind operations that have been rejected\n                by this DSA due to inappropriateAuthentication or\n                invalidCredentials.')
dsaInOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaInOps.setDescription(' Number of operations forwarded to this DSA\n                from DUAs or other DSAs since application\n                start up.')
dsaReadOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaReadOps.setDescription(' Number of read operations serviced by\n                this DSA since application startup.')
dsaCompareOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaCompareOps.setDescription(' Number of compare operations serviced by\n                this DSA  since application startup.')
dsaAddEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaAddEntryOps.setDescription(' Number of addEntry operations serviced by\n                this DSA since application startup.')
dsaRemoveEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaRemoveEntryOps.setDescription(' Number of removeEntry operations serviced by\n                this DSA since application startup.')
dsaModifyEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaModifyEntryOps.setDescription(' Number of modifyEntry operations serviced by\n                this DSA since application startup.')
dsaModifyRDNOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaModifyRDNOps.setDescription(' Number of modifyRDN operations serviced by\n                this DSA since application startup.')
dsaListOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaListOps.setDescription(' Number of list operations serviced by\n                this DSA since application startup.')
dsaSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaSearchOps.setDescription(' Number of search operations- baseObjectSearches,\n                oneLevelSearches and  subTreeSearches, serviced\n                by this DSA  since application startup.')
dsaOneLevelSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaOneLevelSearchOps.setDescription(' Number of oneLevelSearch operations serviced\n                by this DSA since application startup.')
dsaWholeTreeSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaWholeTreeSearchOps.setDescription(' Number of wholeTreeSearch operations serviced\n                by this DSA since application startup.')
dsaReferrals = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaReferrals.setDescription(' Number of referrals returned by this DSA in response\n                to requests for operations since application startup.')
dsaChainings = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaChainings.setDescription(' Number of operations forwarded by this DSA\n                to other DSAs since application startup.')
dsaSecurityErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaSecurityErrors.setDescription(' Number of operations forwarded to this DSA\n                which did not meet the security requirements. ')
dsaErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaErrors.setDescription(' Number of operations that could not be serviced\n                due to errors other than security errors, and\n                referrals.\n                A partially serviced operation will not be counted\n                as an error.\n                The errors include NameErrors, UpdateErrors, Attribute\n                errors and ServiceErrors.')
dsaEntriesTable = MibTable((1, 3, 6, 1, 2, 1, 29, 2), )
if mibBuilder.loadTexts: dsaEntriesTable.setDescription(' The table holding information related to the\n\n                entry statistics and cache performance of the DSAs.')
dsaEntriesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 29, 2, 1), ).setIndexNames((0, "DSA-MIB", "applIndex"))
if mibBuilder.loadTexts: dsaEntriesEntry.setDescription(' Entry containing statistics pertaining to entries\n                held by a DSA.')
dsaMasterEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 2, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaMasterEntries.setDescription(' Number of entries mastered in the DSA.')
dsaCopyEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaCopyEntries.setDescription(' Number of entries for which systematic (slave)\n                copies are maintained in the DSA.')
dsaCacheEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaCacheEntries.setDescription(' Number of entries cached (non-systematic copies) in\n                the DSA. This will include the entries that are\n                cached partially. The negative cache is not counted.')
dsaCacheHits = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaCacheHits.setDescription(' Number of operations that were serviced from\n                the locally held cache since application\n                startup.')
dsaSlaveHits = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaSlaveHits.setDescription(' Number of operations that were serviced from\n                the locally held object replications [ shadow\n                entries] since application startup.')
dsaIntTable = MibTable((1, 3, 6, 1, 2, 1, 29, 3), )
if mibBuilder.loadTexts: dsaIntTable.setDescription(' Each row of this table contains some details\n                      related to the history of the interaction\n                      of the monitored DSAs with their respective\n                      peer DSAs.')
dsaIntEntry = MibTableRow((1, 3, 6, 1, 2, 1, 29, 3, 1), ).setIndexNames((0, "DSA-MIB", "applIndex"), (0, "DSA-MIB", "dsaIntIndex"))
if mibBuilder.loadTexts: dsaIntEntry.setDescription(' Entry containing interaction details of a DSA\n                      with a peer DSA.')
dsaIntIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: dsaIntIndex.setDescription(' Together with applIndex it forms the unique key to\n                identify the conceptual row which contains useful info\n                on the (attempted) interaction between the DSA (referred\n                to by applIndex) and a peer DSA.')
dsaName = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 2), DistinguishedName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaName.setDescription(' Distinguished Name of the peer DSA to which this\n                entry pertains.')
dsaTimeOfCreation = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaTimeOfCreation.setDescription(' The value of sysUpTime when this row was created.\n                If the entry was created before the network management\n                subsystem was initialized, this object will contain\n                a value of zero.')
dsaTimeOfLastAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaTimeOfLastAttempt.setDescription(' The value of sysUpTime when the last attempt was made\n                to contact this DSA. If the last attempt was made before\n                the network management subsystem was initialized, this\n                object will contain a value of zero.')
dsaTimeOfLastSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaTimeOfLastSuccess.setDescription(' The value of sysUpTime when the last attempt made to\n                contact this DSA was successful. If there have\n                been no successful attempts this entry will have a value\n                of zero. If the last successful attempt was made before\n                the network management subsystem was initialized, this\n                object will contain a value of zero.')
dsaFailuresSinceLastSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaFailuresSinceLastSuccess.setDescription(' The number of failures since the last time an\n                attempt to contact this DSA was successful. If\n                there has been no successful attempts, this counter\n                will contain the number of failures since this entry\n                was created.')
dsaFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaFailures.setDescription(' Cumulative failures since the creation of\n                this entry.')
dsaSuccesses = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaSuccesses.setDescription(' Cumulative successes since the creation of\n                this entry.')
dsaConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 29, 4))
dsaGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 29, 4, 1))
dsaCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 29, 4, 2))
dsaOpsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 29, 4, 2, 1)).setObjects(*(("DSA-MIB", "dsaOpsGroup"),))
if mibBuilder.loadTexts: dsaOpsCompliance.setDescription('The compliance statement for SNMPv2 entities\n                    which implement the DSA-MIB for monitoring\n                    DSA operations.')
dsaEntryCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 29, 4, 2, 2)).setObjects(*(("DSA-MIB", "dsaOpsGroup"), ("DSA-MIB", "dsaEntryGroup"),))
if mibBuilder.loadTexts: dsaEntryCompliance.setDescription('The compliance statement for SNMPv2 entities\n                    which implement the DSA-MIB for monitoring\n                    DSA operations,  entry statistics and cache\n                    performance.')
dsaIntCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 29, 4, 2, 3)).setObjects(*(("DSA-MIB", "dsaOpsGroup"), ("DSA-MIB", "dsaIntGroup"),))
if mibBuilder.loadTexts: dsaIntCompliance.setDescription(' The compliance statement  for SNMPv2  entities\n                      which implement the DSA-MIB for monitoring DSA\n                      operations and the interaction of the DSA with\n                      peer DSAs.')
dsaOpsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 29, 4, 1, 1)).setObjects(*(("DSA-MIB", "dsaAnonymousBinds"), ("DSA-MIB", "dsaUnauthBinds"), ("DSA-MIB", "dsaSimpleAuthBinds"), ("DSA-MIB", "dsaStrongAuthBinds"), ("DSA-MIB", "dsaBindSecurityErrors"), ("DSA-MIB", "dsaInOps"), ("DSA-MIB", "dsaReadOps"), ("DSA-MIB", "dsaCompareOps"), ("DSA-MIB", "dsaAddEntryOps"), ("DSA-MIB", "dsaRemoveEntryOps"), ("DSA-MIB", "dsaModifyEntryOps"), ("DSA-MIB", "dsaModifyRDNOps"), ("DSA-MIB", "dsaListOps"), ("DSA-MIB", "dsaSearchOps"), ("DSA-MIB", "dsaOneLevelSearchOps"), ("DSA-MIB", "dsaWholeTreeSearchOps"), ("DSA-MIB", "dsaReferrals"), ("DSA-MIB", "dsaChainings"), ("DSA-MIB", "dsaSecurityErrors"), ("DSA-MIB", "dsaErrors"),))
if mibBuilder.loadTexts: dsaOpsGroup.setDescription(' A collection of objects for monitoring the DSA\n                      operations.')
dsaEntryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 29, 4, 1, 2)).setObjects(*(("DSA-MIB", "dsaMasterEntries"), ("DSA-MIB", "dsaCopyEntries"), ("DSA-MIB", "dsaCacheEntries"), ("DSA-MIB", "dsaCacheHits"), ("DSA-MIB", "dsaSlaveHits"),))
if mibBuilder.loadTexts: dsaEntryGroup.setDescription(' A collection of objects for monitoring the DSA\n                      entry statistics and cache performance.')
dsaIntGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 29, 4, 1, 3)).setObjects(*(("DSA-MIB", "dsaName"), ("DSA-MIB", "dsaTimeOfCreation"), ("DSA-MIB", "dsaTimeOfLastAttempt"), ("DSA-MIB", "dsaTimeOfLastSuccess"), ("DSA-MIB", "dsaFailuresSinceLastSuccess"), ("DSA-MIB", "dsaFailures"), ("DSA-MIB", "dsaSuccesses"),))
if mibBuilder.loadTexts: dsaIntGroup.setDescription(" A collection of objects for monitoring the DSA's\n                      interaction with peer DSAs.")
mibBuilder.exportSymbols("DSA-MIB", dsaGroups=dsaGroups, dsaModifyRDNOps=dsaModifyRDNOps, dsaUnauthBinds=dsaUnauthBinds, dsaFailuresSinceLastSuccess=dsaFailuresSinceLastSuccess, dsaWholeTreeSearchOps=dsaWholeTreeSearchOps, dsaAddEntryOps=dsaAddEntryOps, dsaFailures=dsaFailures, dsaSimpleAuthBinds=dsaSimpleAuthBinds, dsaCompliances=dsaCompliances, dsaRemoveEntryOps=dsaRemoveEntryOps, dsaEntryGroup=dsaEntryGroup, dsaTimeOfLastSuccess=dsaTimeOfLastSuccess, dsaIntCompliance=dsaIntCompliance, dsaSlaveHits=dsaSlaveHits, dsaErrors=dsaErrors, dsaOpsGroup=dsaOpsGroup, dsaCacheHits=dsaCacheHits, dsaStrongAuthBinds=dsaStrongAuthBinds, dsaIntGroup=dsaIntGroup, dsaEntriesEntry=dsaEntriesEntry, dsaCopyEntries=dsaCopyEntries, dsaChainings=dsaChainings, dsaIntTable=dsaIntTable, dsaReferrals=dsaReferrals, dsaMIB=dsaMIB, dsaEntriesTable=dsaEntriesTable, dsaOpsTable=dsaOpsTable, dsaTimeOfLastAttempt=dsaTimeOfLastAttempt, dsaListOps=dsaListOps, dsaSecurityErrors=dsaSecurityErrors, dsaOpsCompliance=dsaOpsCompliance, dsaOpsEntry=dsaOpsEntry, dsaIntEntry=dsaIntEntry, dsaInOps=dsaInOps, dsaBindSecurityErrors=dsaBindSecurityErrors, dsaOneLevelSearchOps=dsaOneLevelSearchOps, dsaModifyEntryOps=dsaModifyEntryOps, dsaConformance=dsaConformance, dsaTimeOfCreation=dsaTimeOfCreation, dsaCompareOps=dsaCompareOps, dsaReadOps=dsaReadOps, dsaMasterEntries=dsaMasterEntries, dsaSuccesses=dsaSuccesses, dsaAnonymousBinds=dsaAnonymousBinds, dsaIntIndex=dsaIntIndex, PYSNMP_MODULE_ID=dsaMIB, dsaSearchOps=dsaSearchOps, dsaName=dsaName, dsaCacheEntries=dsaCacheEntries, dsaEntryCompliance=dsaEntryCompliance)
