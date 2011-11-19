# PySNMP SMI module. Autogenerated from smidump -f python DIRECTORY-SERVER-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:28:47 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( DistinguishedName, URLString, applIndex, ) = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "DistinguishedName", "URLString", "applIndex")
( ZeroBasedCounter32, ) = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( DisplayString, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp")

# Objects

dsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 66)).setRevisions(("1999-06-07 00:00","1993-11-25 00:00",))
if mibBuilder.loadTexts: dsMIB.setOrganization("IETF Mail and Directory Management Working\nGroup")
if mibBuilder.loadTexts: dsMIB.setContactInfo("                      Glenn Mansfield\nPostal: Cyber Solutions Inc.\n        6-6-3, Minami Yoshinari\n        Aoba-ku, Sendai, Japan 989-3204.\n\n   Tel: +81-22-303-4012\n   Fax: +81-22-303-4015\nE-mail: glenn@cysols.com\nWorking Group E-mail: ietf-madman@innosoft.com\nTo subscribe: ietf-madman-request@innosoft.com")
if mibBuilder.loadTexts: dsMIB.setDescription(" The MIB module for monitoring Directory Services.")
dsTable = MibTable((1, 3, 6, 1, 2, 1, 66, 1))
if mibBuilder.loadTexts: dsTable.setDescription(" The table holding information related to the Directory\nServers.")
dsTableEntry = MibTableRow((1, 3, 6, 1, 2, 1, 66, 1, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: dsTableEntry.setDescription(" Entry containing summary description for a Directory\nServer.")
dsServerType = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 1), Bits().subtype(namedValues=NamedValues(("frontEndDirectoryServer", 0), ("backEndDirectoryServer", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsServerType.setDescription("This object indicates whether the server is\na frontend or, a backend or, both. If the server\nis a frontend, then the frontEndDirectoryServer\nbit will be set. Similarly for the backend.")
dsServerDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsServerDescription.setDescription("A text description of the application.  This information\nis intended to identify and briefly describe the\napplication in a status display.")
dsMasterEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsMasterEntries.setDescription(" Number of entries mastered in the Directory Server.")
dsCopyEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsCopyEntries.setDescription(" Number of entries for which systematic (slave)\ncopies are maintained in the Directory Server.")
dsCacheEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsCacheEntries.setDescription(" Number of entries cached (non-systematic copies) in\nthe Directory Server. This will include the entries that\nare cached partially. The negative cache is not counted.")
dsCacheHits = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsCacheHits.setDescription(" Number of operations that were serviced from\nthe locally held cache.")
dsSlaveHits = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsSlaveHits.setDescription(" Number of operations that were serviced from\nthe locally held object replications ( copy-\nentries).")
dsApplIfOpsTable = MibTable((1, 3, 6, 1, 2, 1, 66, 2))
if mibBuilder.loadTexts: dsApplIfOpsTable.setDescription(" The table holding information related to the\nDirectory Server operations.")
dsApplIfOpsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 66, 2, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "DIRECTORY-SERVER-MIB", "dsApplIfProtocolIndex"))
if mibBuilder.loadTexts: dsApplIfOpsEntry.setDescription(" Entry containing operations related statistics\nfor a Directory Server.")
dsApplIfProtocolIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfProtocolIndex.setDescription("An index to uniquely identify an entry corresponding to a\napplication-layer protocol interface. This index is used\nfor lexicographic ordering of the table.")
dsApplIfProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfProtocol.setDescription("An identification of the protocol being used by the application\non this interface.  For an OSI Application, this will be the\nApplication Context.  For Internet applications, the IANA\nmaintains a registry[22] of the OIDs which correspond to\nwell-known applications.  If the application protocol is\nnot listed in the registry, an OID value of the form\n{applTCPProtoID port} or {applUDProtoID port} are used for\nTCP-based and UDP-based protocols, respectively. In either\ncase 'port' corresponds to the primary port number being\nused by the protocol. The OIDs applTCPProtoID and\napplUDPProtoID are defined in NETWORK-SERVICES-MIB")
dsApplIfUnauthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfUnauthBinds.setDescription(" Number of unauthenticated/anonymous bind requests\nreceived.")
dsApplIfSimpleAuthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfSimpleAuthBinds.setDescription(" Number of bind requests that were authenticated\nusing simple authentication procedures like password\nchecks. This includes the\npassword authentication using SASL mechanisms like\nCRAM-MD5.")
dsApplIfStrongAuthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfStrongAuthBinds.setDescription(" Number of bind requests that were authenticated\nusing TLS and X.500 strong authentication procedures.\nThis includes the binds that were\nauthenticated using external authentication procedures.")
dsApplIfBindSecurityErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfBindSecurityErrors.setDescription(" Number of bind requests that have been rejected\ndue to inappropriate authentication or\ninvalid credentials.")
dsApplIfInOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfInOps.setDescription(" Number of requests received from DUAs or other\nDirectory Servers.")
dsApplIfReadOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfReadOps.setDescription(" Number of read requests  received.")
dsApplIfCompareOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfCompareOps.setDescription(" Number of compare requests received.")
dsApplIfAddEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfAddEntryOps.setDescription(" Number of addEntry requests received.")
dsApplIfRemoveEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfRemoveEntryOps.setDescription(" Number of removeEntry requests received.")
dsApplIfModifyEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfModifyEntryOps.setDescription(" Number of modifyEntry requests received.")
dsApplIfModifyRDNOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfModifyRDNOps.setDescription(" Number of modifyRDN requests received.")
dsApplIfListOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfListOps.setDescription(" Number of list requests received.")
dsApplIfSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfSearchOps.setDescription(" Number of search requests- baseObject searches,\noneLevel searches and  whole subtree searches,\nreceived.")
dsApplIfOneLevelSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfOneLevelSearchOps.setDescription(" Number of oneLevel search requests received.")
dsApplIfWholeSubtreeSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfWholeSubtreeSearchOps.setDescription(" Number of whole subtree search requests received.")
dsApplIfReferrals = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfReferrals.setDescription(" Number of referrals returned in response\nto requests for operations.")
dsApplIfChainings = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfChainings.setDescription(" Number of operations forwarded by this Directory Server\nto other Directory Servers.")
dsApplIfSecurityErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfSecurityErrors.setDescription(" Number of requests received\nwhich did not meet the security requirements. ")
dsApplIfErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfErrors.setDescription(" Number of requests that could not be serviced\ndue to errors other than security errors, and\nreferrals.\nA partially serviced operation will not be counted\nas an error.\nThe errors include naming-related, update-related,\nattribute-related and service-related errors.")
dsApplIfReplicationUpdatesIn = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfReplicationUpdatesIn.setDescription(" Number of replication updates fetched or received from\nsupplier Directory Servers.")
dsApplIfReplicationUpdatesOut = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfReplicationUpdatesOut.setDescription(" Number of replication updates sent to or taken by\nconsumer Directory Servers.")
dsApplIfInBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfInBytes.setDescription(" Incoming traffic, in bytes, on the interface.\nThis will include requests from DUAs as well\nas responses from other Directory Servers.")
dsApplIfOutBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfOutBytes.setDescription(" Outgoing traffic in bytes on the interface.\nThis will include responses to DUAs and Directory\nServers as well as requests to other Directory Servers.")
dsIntTable = MibTable((1, 3, 6, 1, 2, 1, 66, 3))
if mibBuilder.loadTexts: dsIntTable.setDescription(" Each row of this table contains some details\nrelated to the history of the interaction\nof the monitored Directory Server with its\npeer Directory Servers.")
dsIntEntry = MibTableRow((1, 3, 6, 1, 2, 1, 66, 3, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "DIRECTORY-SERVER-MIB", "dsIntEntIndex"), (0, "DIRECTORY-SERVER-MIB", "dsApplIfProtocolIndex"))
if mibBuilder.loadTexts: dsIntEntry.setDescription(" Entry containing interaction details of a Directory\nServer with a peer Directory Server.")
dsIntEntIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: dsIntEntIndex.setDescription(" Together with applIndex and dsApplIfProtocolIndex, this\nobject forms the unique key to\nidentify the conceptual row which contains useful info\non the (attempted) interaction between the Directory\nServer (referred to by applIndex) and a peer Directory\nServer using a particular protocol.")
dsIntEntDirectoryName = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 2), DistinguishedName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntDirectoryName.setDescription(" Distinguished Name of the peer Directory Server to\nwhich this entry pertains.")
dsIntEntTimeOfCreation = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntTimeOfCreation.setDescription(" The value of sysUpTime when this row was created.\nIf the entry was created before the network management\nsubsystem was initialized, this object will contain\na value of zero.")
dsIntEntTimeOfLastAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntTimeOfLastAttempt.setDescription(" The value of sysUpTime when the last attempt was made\nto contact the peer Directory Server. If the last attempt\nwas made before the network management subsystem was\ninitialized, this object will contain a value of zero.")
dsIntEntTimeOfLastSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntTimeOfLastSuccess.setDescription(" The value of sysUpTime when the last attempt made to\ncontact the peer Directory Server was successful. If there\nhave been no successful attempts this entry will have a value\nof zero. If the last successful attempt was made before\nthe network management subsystem was initialized, this\nobject will contain a value of zero.")
dsIntEntFailuresSinceLastSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntFailuresSinceLastSuccess.setDescription(" The number of failures since the last time an\nattempt to contact the peer Directory Server was successful.\nIf there have been no successful attempts, this counter\nwill contain the number of failures since this entry\nwas created.")
dsIntEntFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntFailures.setDescription(" Cumulative failures in contacting the peer Directory Server\nsince the creation of this entry.")
dsIntEntSuccesses = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 8), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntSuccesses.setDescription(" Cumulative successes in contacting the peer Directory Server\nsince the creation of this entry.")
dsIntEntURL = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 9), URLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntURL.setDescription(" URL of the peer Directory Server.")
dsConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 66, 4))
dsGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 66, 4, 1))
dsCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 66, 4, 2))

# Augmentions

# Groups

dsEntryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 66, 4, 1, 1)).setObjects(("DIRECTORY-SERVER-MIB", "dsSlaveHits"), ("DIRECTORY-SERVER-MIB", "dsCacheEntries"), ("DIRECTORY-SERVER-MIB", "dsServerDescription"), ("DIRECTORY-SERVER-MIB", "dsMasterEntries"), ("DIRECTORY-SERVER-MIB", "dsCopyEntries"), ("DIRECTORY-SERVER-MIB", "dsServerType"), ("DIRECTORY-SERVER-MIB", "dsCacheHits"), )
if mibBuilder.loadTexts: dsEntryGroup.setDescription(" A collection of objects for a summary overview of the\nDirectory Servers.")
dsOpsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 66, 4, 1, 2)).setObjects(("DIRECTORY-SERVER-MIB", "dsApplIfReadOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfOutBytes"), ("DIRECTORY-SERVER-MIB", "dsApplIfWholeSubtreeSearchOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfSimpleAuthBinds"), ("DIRECTORY-SERVER-MIB", "dsApplIfReferrals"), ("DIRECTORY-SERVER-MIB", "dsApplIfInBytes"), ("DIRECTORY-SERVER-MIB", "dsApplIfChainings"), ("DIRECTORY-SERVER-MIB", "dsApplIfCompareOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfProtocolIndex"), ("DIRECTORY-SERVER-MIB", "dsApplIfSecurityErrors"), ("DIRECTORY-SERVER-MIB", "dsApplIfProtocol"), ("DIRECTORY-SERVER-MIB", "dsApplIfInOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfModifyRDNOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfErrors"), ("DIRECTORY-SERVER-MIB", "dsApplIfUnauthBinds"), ("DIRECTORY-SERVER-MIB", "dsApplIfStrongAuthBinds"), ("DIRECTORY-SERVER-MIB", "dsApplIfReplicationUpdatesOut"), ("DIRECTORY-SERVER-MIB", "dsApplIfBindSecurityErrors"), ("DIRECTORY-SERVER-MIB", "dsApplIfListOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfAddEntryOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfRemoveEntryOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfReplicationUpdatesIn"), ("DIRECTORY-SERVER-MIB", "dsApplIfSearchOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfModifyEntryOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfOneLevelSearchOps"), )
if mibBuilder.loadTexts: dsOpsGroup.setDescription(" A collection of objects for monitoring the Directory\nServer operations.")
dsIntGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 66, 4, 1, 3)).setObjects(("DIRECTORY-SERVER-MIB", "dsIntEntFailures"), ("DIRECTORY-SERVER-MIB", "dsIntEntTimeOfLastAttempt"), ("DIRECTORY-SERVER-MIB", "dsIntEntFailuresSinceLastSuccess"), ("DIRECTORY-SERVER-MIB", "dsIntEntDirectoryName"), ("DIRECTORY-SERVER-MIB", "dsIntEntURL"), ("DIRECTORY-SERVER-MIB", "dsIntEntTimeOfCreation"), ("DIRECTORY-SERVER-MIB", "dsIntEntTimeOfLastSuccess"), ("DIRECTORY-SERVER-MIB", "dsIntEntSuccesses"), )
if mibBuilder.loadTexts: dsIntGroup.setDescription(" A collection of objects for monitoring the Directory\nServer's interaction with peer Directory Servers.")

# Compliances

dsEntryCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 66, 4, 2, 1)).setObjects(("DIRECTORY-SERVER-MIB", "dsEntryGroup"), )
if mibBuilder.loadTexts: dsEntryCompliance.setDescription("The compliance statement for SNMP entities\nwhich implement the DIRECTORY-SERVER-MIB for\na summary overview of the Directory Servers .")
dsOpsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 66, 4, 2, 2)).setObjects(("DIRECTORY-SERVER-MIB", "dsEntryGroup"), ("DIRECTORY-SERVER-MIB", "dsOpsGroup"), )
if mibBuilder.loadTexts: dsOpsCompliance.setDescription("The compliance statement for SNMP entities\nwhich implement the DIRECTORY-SERVER-MIB for monitoring\nDirectory Server operations,  entry statistics and cache\nperformance.")
dsIntCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 66, 4, 2, 3)).setObjects(("DIRECTORY-SERVER-MIB", "dsIntGroup"), ("DIRECTORY-SERVER-MIB", "dsEntryGroup"), )
if mibBuilder.loadTexts: dsIntCompliance.setDescription(" The compliance statement  for SNMP  entities\nwhich implement the DIRECTORY-SERVER-MIB for\nmonitoring Directory Server operations and the\ninteraction of the Directory Server with peer\nDirectory Servers.")
dsOpsIntCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 66, 4, 2, 4)).setObjects(("DIRECTORY-SERVER-MIB", "dsIntGroup"), ("DIRECTORY-SERVER-MIB", "dsEntryGroup"), ("DIRECTORY-SERVER-MIB", "dsOpsGroup"), )
if mibBuilder.loadTexts: dsOpsIntCompliance.setDescription(" The compliance statement  for SNMP  entities\nwhich implement the DIRECTORY-SERVER-MIB for monitoring\nDirectory Server operations and the interaction of the\nDirectory Server with peer Directory Servers.")

# Exports

# Module identity
mibBuilder.exportSymbols("DIRECTORY-SERVER-MIB", PYSNMP_MODULE_ID=dsMIB)

# Objects
mibBuilder.exportSymbols("DIRECTORY-SERVER-MIB", dsMIB=dsMIB, dsTable=dsTable, dsTableEntry=dsTableEntry, dsServerType=dsServerType, dsServerDescription=dsServerDescription, dsMasterEntries=dsMasterEntries, dsCopyEntries=dsCopyEntries, dsCacheEntries=dsCacheEntries, dsCacheHits=dsCacheHits, dsSlaveHits=dsSlaveHits, dsApplIfOpsTable=dsApplIfOpsTable, dsApplIfOpsEntry=dsApplIfOpsEntry, dsApplIfProtocolIndex=dsApplIfProtocolIndex, dsApplIfProtocol=dsApplIfProtocol, dsApplIfUnauthBinds=dsApplIfUnauthBinds, dsApplIfSimpleAuthBinds=dsApplIfSimpleAuthBinds, dsApplIfStrongAuthBinds=dsApplIfStrongAuthBinds, dsApplIfBindSecurityErrors=dsApplIfBindSecurityErrors, dsApplIfInOps=dsApplIfInOps, dsApplIfReadOps=dsApplIfReadOps, dsApplIfCompareOps=dsApplIfCompareOps, dsApplIfAddEntryOps=dsApplIfAddEntryOps, dsApplIfRemoveEntryOps=dsApplIfRemoveEntryOps, dsApplIfModifyEntryOps=dsApplIfModifyEntryOps, dsApplIfModifyRDNOps=dsApplIfModifyRDNOps, dsApplIfListOps=dsApplIfListOps, dsApplIfSearchOps=dsApplIfSearchOps, dsApplIfOneLevelSearchOps=dsApplIfOneLevelSearchOps, dsApplIfWholeSubtreeSearchOps=dsApplIfWholeSubtreeSearchOps, dsApplIfReferrals=dsApplIfReferrals, dsApplIfChainings=dsApplIfChainings, dsApplIfSecurityErrors=dsApplIfSecurityErrors, dsApplIfErrors=dsApplIfErrors, dsApplIfReplicationUpdatesIn=dsApplIfReplicationUpdatesIn, dsApplIfReplicationUpdatesOut=dsApplIfReplicationUpdatesOut, dsApplIfInBytes=dsApplIfInBytes, dsApplIfOutBytes=dsApplIfOutBytes, dsIntTable=dsIntTable, dsIntEntry=dsIntEntry, dsIntEntIndex=dsIntEntIndex, dsIntEntDirectoryName=dsIntEntDirectoryName, dsIntEntTimeOfCreation=dsIntEntTimeOfCreation, dsIntEntTimeOfLastAttempt=dsIntEntTimeOfLastAttempt, dsIntEntTimeOfLastSuccess=dsIntEntTimeOfLastSuccess, dsIntEntFailuresSinceLastSuccess=dsIntEntFailuresSinceLastSuccess, dsIntEntFailures=dsIntEntFailures, dsIntEntSuccesses=dsIntEntSuccesses, dsIntEntURL=dsIntEntURL, dsConformance=dsConformance, dsGroups=dsGroups, dsCompliances=dsCompliances)

# Groups
mibBuilder.exportSymbols("DIRECTORY-SERVER-MIB", dsEntryGroup=dsEntryGroup, dsOpsGroup=dsOpsGroup, dsIntGroup=dsIntGroup)

# Compliances
mibBuilder.exportSymbols("DIRECTORY-SERVER-MIB", dsEntryCompliance=dsEntryCompliance, dsOpsCompliance=dsOpsCompliance, dsIntCompliance=dsIntCompliance, dsOpsIntCompliance=dsOpsIntCompliance)
