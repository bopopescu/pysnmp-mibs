# PySNMP SMI module. Autogenerated from smidump -f python DSA-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:29:00 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( DistinguishedName, applIndex, ) = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "DistinguishedName", "applIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( DisplayString, TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp")

# Objects

dsaMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 29)).setRevisions(("1993-11-25 00:00",))
if mibBuilder.loadTexts: dsaMIB.setOrganization("IETF Mail and Directory Management Working\nGroup")
if mibBuilder.loadTexts: dsaMIB.setContactInfo("        Glenn Mansfield\n\nPostal: AIC Systems Laboratory\n        6-6-3, Minami Yoshinari\n        Aoba-ku, Sendai, 989-32\n        JP\n\nTel:    +81 22 279 3310\nFax:    +81 22 279 3640\nE-Mail: glenn@aic.co.jp")
if mibBuilder.loadTexts: dsaMIB.setDescription(" The MIB module for monitoring Directory System Agents.")
dsaOpsTable = MibTable((1, 3, 6, 1, 2, 1, 29, 1))
if mibBuilder.loadTexts: dsaOpsTable.setDescription(" The table holding information related to the\nDSA operations.")
dsaOpsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 29, 1, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: dsaOpsEntry.setDescription(" Entry containing operations related statistics\nfor a DSA.")
dsaAnonymousBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaAnonymousBinds.setDescription(" Number of anonymous  binds to this DSA from DUAs\nsince application start.")
dsaUnauthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaUnauthBinds.setDescription(" Number of un-authenticated binds to this\nDSA since application start.")
dsaSimpleAuthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaSimpleAuthBinds.setDescription(" Number of binds to this DSA that were authenticated\nusing simple authentication procedures since\napplication start.")
dsaStrongAuthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaStrongAuthBinds.setDescription(" Number of binds to this DSA that were authenticated\nusing the strong authentication procedures since\napplication start. This includes the binds that were\nauthenticated using external authentication procedures.")
dsaBindSecurityErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaBindSecurityErrors.setDescription(" Number of bind operations that have been rejected\nby this DSA due to inappropriateAuthentication or\ninvalidCredentials.")
dsaInOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaInOps.setDescription(" Number of operations forwarded to this DSA\nfrom DUAs or other DSAs since application\nstart up.")
dsaReadOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaReadOps.setDescription(" Number of read operations serviced by\nthis DSA since application startup.")
dsaCompareOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaCompareOps.setDescription(" Number of compare operations serviced by\nthis DSA  since application startup.")
dsaAddEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaAddEntryOps.setDescription(" Number of addEntry operations serviced by\nthis DSA since application startup.")
dsaRemoveEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaRemoveEntryOps.setDescription(" Number of removeEntry operations serviced by\nthis DSA since application startup.")
dsaModifyEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaModifyEntryOps.setDescription(" Number of modifyEntry operations serviced by\nthis DSA since application startup.")
dsaModifyRDNOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaModifyRDNOps.setDescription(" Number of modifyRDN operations serviced by\nthis DSA since application startup.")
dsaListOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaListOps.setDescription(" Number of list operations serviced by\nthis DSA since application startup.")
dsaSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaSearchOps.setDescription(" Number of search operations- baseObjectSearches,\noneLevelSearches and  subTreeSearches, serviced\nby this DSA  since application startup.")
dsaOneLevelSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaOneLevelSearchOps.setDescription(" Number of oneLevelSearch operations serviced\nby this DSA since application startup.")
dsaWholeTreeSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaWholeTreeSearchOps.setDescription(" Number of wholeTreeSearch operations serviced\nby this DSA since application startup.")
dsaReferrals = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaReferrals.setDescription(" Number of referrals returned by this DSA in response\nto requests for operations since application startup.")
dsaChainings = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaChainings.setDescription(" Number of operations forwarded by this DSA\nto other DSAs since application startup.")
dsaSecurityErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaSecurityErrors.setDescription(" Number of operations forwarded to this DSA\nwhich did not meet the security requirements. ")
dsaErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaErrors.setDescription(" Number of operations that could not be serviced\ndue to errors other than security errors, and\nreferrals.\nA partially serviced operation will not be counted\nas an error.\nThe errors include NameErrors, UpdateErrors, Attribute\nerrors and ServiceErrors.")
dsaEntriesTable = MibTable((1, 3, 6, 1, 2, 1, 29, 2))
if mibBuilder.loadTexts: dsaEntriesTable.setDescription(" The table holding information related to the\nentry statistics and cache performance of the DSAs.")
dsaEntriesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 29, 2, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: dsaEntriesEntry.setDescription(" Entry containing statistics pertaining to entries\nheld by a DSA.")
dsaMasterEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 2, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaMasterEntries.setDescription(" Number of entries mastered in the DSA.")
dsaCopyEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaCopyEntries.setDescription(" Number of entries for which systematic (slave)\ncopies are maintained in the DSA.")
dsaCacheEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaCacheEntries.setDescription(" Number of entries cached (non-systematic copies) in\nthe DSA. This will include the entries that are\ncached partially. The negative cache is not counted.")
dsaCacheHits = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaCacheHits.setDescription(" Number of operations that were serviced from\nthe locally held cache since application\nstartup.")
dsaSlaveHits = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaSlaveHits.setDescription(" Number of operations that were serviced from\nthe locally held object replications [ shadow\nentries] since application startup.")
dsaIntTable = MibTable((1, 3, 6, 1, 2, 1, 29, 3))
if mibBuilder.loadTexts: dsaIntTable.setDescription(" Each row of this table contains some details\nrelated to the history of the interaction\nof the monitored DSAs with their respective\npeer DSAs.")
dsaIntEntry = MibTableRow((1, 3, 6, 1, 2, 1, 29, 3, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "DSA-MIB", "dsaIntIndex"))
if mibBuilder.loadTexts: dsaIntEntry.setDescription(" Entry containing interaction details of a DSA\nwith a peer DSA.")
dsaIntIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: dsaIntIndex.setDescription(" Together with applIndex it forms the unique key to\nidentify the conceptual row which contains useful info\non the (attempted) interaction between the DSA (referred\nto by applIndex) and a peer DSA.")
dsaName = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 2), DistinguishedName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaName.setDescription(" Distinguished Name of the peer DSA to which this\nentry pertains.")
dsaTimeOfCreation = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaTimeOfCreation.setDescription(" The value of sysUpTime when this row was created.\nIf the entry was created before the network management\nsubsystem was initialized, this object will contain\na value of zero.")
dsaTimeOfLastAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaTimeOfLastAttempt.setDescription(" The value of sysUpTime when the last attempt was made\nto contact this DSA. If the last attempt was made before\nthe network management subsystem was initialized, this\nobject will contain a value of zero.")
dsaTimeOfLastSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaTimeOfLastSuccess.setDescription(" The value of sysUpTime when the last attempt made to\ncontact this DSA was successful. If there have\nbeen no successful attempts this entry will have a value\nof zero. If the last successful attempt was made before\nthe network management subsystem was initialized, this\nobject will contain a value of zero.")
dsaFailuresSinceLastSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaFailuresSinceLastSuccess.setDescription(" The number of failures since the last time an\nattempt to contact this DSA was successful. If\nthere has been no successful attempts, this counter\nwill contain the number of failures since this entry\nwas created.")
dsaFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaFailures.setDescription(" Cumulative failures since the creation of\nthis entry.")
dsaSuccesses = MibTableColumn((1, 3, 6, 1, 2, 1, 29, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsaSuccesses.setDescription(" Cumulative successes since the creation of\nthis entry.")
dsaConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 29, 4))
dsaGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 29, 4, 1))
dsaCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 29, 4, 2))

# Augmentions

# Groups

dsaOpsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 29, 4, 1, 1)).setObjects(("DSA-MIB", "dsaSearchOps"), ("DSA-MIB", "dsaReferrals"), ("DSA-MIB", "dsaModifyRDNOps"), ("DSA-MIB", "dsaSecurityErrors"), ("DSA-MIB", "dsaReadOps"), ("DSA-MIB", "dsaErrors"), ("DSA-MIB", "dsaListOps"), ("DSA-MIB", "dsaAddEntryOps"), ("DSA-MIB", "dsaChainings"), ("DSA-MIB", "dsaCompareOps"), ("DSA-MIB", "dsaOneLevelSearchOps"), ("DSA-MIB", "dsaStrongAuthBinds"), ("DSA-MIB", "dsaAnonymousBinds"), ("DSA-MIB", "dsaSimpleAuthBinds"), ("DSA-MIB", "dsaUnauthBinds"), ("DSA-MIB", "dsaWholeTreeSearchOps"), ("DSA-MIB", "dsaBindSecurityErrors"), ("DSA-MIB", "dsaInOps"), ("DSA-MIB", "dsaRemoveEntryOps"), ("DSA-MIB", "dsaModifyEntryOps"), )
if mibBuilder.loadTexts: dsaOpsGroup.setDescription(" A collection of objects for monitoring the DSA\noperations.")
dsaEntryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 29, 4, 1, 2)).setObjects(("DSA-MIB", "dsaCacheHits"), ("DSA-MIB", "dsaCopyEntries"), ("DSA-MIB", "dsaCacheEntries"), ("DSA-MIB", "dsaMasterEntries"), ("DSA-MIB", "dsaSlaveHits"), )
if mibBuilder.loadTexts: dsaEntryGroup.setDescription(" A collection of objects for monitoring the DSA\nentry statistics and cache performance.")
dsaIntGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 29, 4, 1, 3)).setObjects(("DSA-MIB", "dsaName"), ("DSA-MIB", "dsaTimeOfCreation"), ("DSA-MIB", "dsaFailuresSinceLastSuccess"), ("DSA-MIB", "dsaSuccesses"), ("DSA-MIB", "dsaFailures"), ("DSA-MIB", "dsaTimeOfLastAttempt"), ("DSA-MIB", "dsaTimeOfLastSuccess"), )
if mibBuilder.loadTexts: dsaIntGroup.setDescription(" A collection of objects for monitoring the DSA's\ninteraction with peer DSAs.")

# Compliances

dsaOpsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 29, 4, 2, 1)).setObjects(("DSA-MIB", "dsaOpsGroup"), )
if mibBuilder.loadTexts: dsaOpsCompliance.setDescription("The compliance statement for SNMPv2 entities\nwhich implement the DSA-MIB for monitoring\nDSA operations.")
dsaEntryCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 29, 4, 2, 2)).setObjects(("DSA-MIB", "dsaOpsGroup"), ("DSA-MIB", "dsaEntryGroup"), )
if mibBuilder.loadTexts: dsaEntryCompliance.setDescription("The compliance statement for SNMPv2 entities\nwhich implement the DSA-MIB for monitoring\nDSA operations,  entry statistics and cache\nperformance.")
dsaIntCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 29, 4, 2, 3)).setObjects(("DSA-MIB", "dsaOpsGroup"), ("DSA-MIB", "dsaIntGroup"), )
if mibBuilder.loadTexts: dsaIntCompliance.setDescription(" The compliance statement  for SNMPv2  entities\nwhich implement the DSA-MIB for monitoring DSA\noperations and the interaction of the DSA with\npeer DSAs.")

# Exports

# Module identity
mibBuilder.exportSymbols("DSA-MIB", PYSNMP_MODULE_ID=dsaMIB)

# Objects
mibBuilder.exportSymbols("DSA-MIB", dsaMIB=dsaMIB, dsaOpsTable=dsaOpsTable, dsaOpsEntry=dsaOpsEntry, dsaAnonymousBinds=dsaAnonymousBinds, dsaUnauthBinds=dsaUnauthBinds, dsaSimpleAuthBinds=dsaSimpleAuthBinds, dsaStrongAuthBinds=dsaStrongAuthBinds, dsaBindSecurityErrors=dsaBindSecurityErrors, dsaInOps=dsaInOps, dsaReadOps=dsaReadOps, dsaCompareOps=dsaCompareOps, dsaAddEntryOps=dsaAddEntryOps, dsaRemoveEntryOps=dsaRemoveEntryOps, dsaModifyEntryOps=dsaModifyEntryOps, dsaModifyRDNOps=dsaModifyRDNOps, dsaListOps=dsaListOps, dsaSearchOps=dsaSearchOps, dsaOneLevelSearchOps=dsaOneLevelSearchOps, dsaWholeTreeSearchOps=dsaWholeTreeSearchOps, dsaReferrals=dsaReferrals, dsaChainings=dsaChainings, dsaSecurityErrors=dsaSecurityErrors, dsaErrors=dsaErrors, dsaEntriesTable=dsaEntriesTable, dsaEntriesEntry=dsaEntriesEntry, dsaMasterEntries=dsaMasterEntries, dsaCopyEntries=dsaCopyEntries, dsaCacheEntries=dsaCacheEntries, dsaCacheHits=dsaCacheHits, dsaSlaveHits=dsaSlaveHits, dsaIntTable=dsaIntTable, dsaIntEntry=dsaIntEntry, dsaIntIndex=dsaIntIndex, dsaName=dsaName, dsaTimeOfCreation=dsaTimeOfCreation, dsaTimeOfLastAttempt=dsaTimeOfLastAttempt, dsaTimeOfLastSuccess=dsaTimeOfLastSuccess, dsaFailuresSinceLastSuccess=dsaFailuresSinceLastSuccess, dsaFailures=dsaFailures, dsaSuccesses=dsaSuccesses, dsaConformance=dsaConformance, dsaGroups=dsaGroups, dsaCompliances=dsaCompliances)

# Groups
mibBuilder.exportSymbols("DSA-MIB", dsaOpsGroup=dsaOpsGroup, dsaEntryGroup=dsaEntryGroup, dsaIntGroup=dsaIntGroup)

# Compliances
mibBuilder.exportSymbols("DSA-MIB", dsaOpsCompliance=dsaOpsCompliance, dsaEntryCompliance=dsaEntryCompliance, dsaIntCompliance=dsaIntCompliance)
