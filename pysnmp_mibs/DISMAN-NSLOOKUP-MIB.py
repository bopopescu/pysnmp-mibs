# PySNMP SMI module. Autogenerated from smidump -f python DISMAN-NSLOOKUP-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:28:48 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( RowStatus, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus")

# Objects

lookupMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 82)).setRevisions(("2006-06-13 00:00","2000-09-21 00:00",))
if mibBuilder.loadTexts: lookupMIB.setOrganization("IETF Distributed Management Working Group")
if mibBuilder.loadTexts: lookupMIB.setContactInfo("Juergen Quittek\n\n\n\nNEC Europe Ltd.\nNetwork Laboratories\nKurfuersten-Anlage 36\n69115 Heidelberg\nGermany\n\nPhone: +49 6221 4342-115\nEmail: quittek@netlab.nec.de")
if mibBuilder.loadTexts: lookupMIB.setDescription("The Lookup MIB (DISMAN-NSLOOKUP-MIB) enables determination\nof either the name(s) corresponding to a host address or of\nthe address(es) associated with a host name at a remote\nhost.\n\nCopyright (C) The Internet Society (2006).  This version of\nthis MIB module is part of RFC 4560; see the RFC itself for\nfull legal notices.")
lookupObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 82, 1))
lookupMaxConcurrentRequests = MibScalar((1, 3, 6, 1, 2, 1, 82, 1, 1), Unsigned32().clone(10)).setMaxAccess("readwrite").setUnits("requests")
if mibBuilder.loadTexts: lookupMaxConcurrentRequests.setDescription("The maximum number of concurrent active lookup requests\nthat are allowed within an agent implementation.  A value\nof 0 for this object implies that there is no limit for\nthe number of concurrent active requests in effect.\n\nThe limit applies only to new requests being activated.\nWhen a new value is set, the agent will continue processing\nall the requests already active, even if their number\nexceed the limit just imposed.")
lookupPurgeTime = MibScalar((1, 3, 6, 1, 2, 1, 82, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(900)).setMaxAccess("readwrite").setUnits("seconds")
if mibBuilder.loadTexts: lookupPurgeTime.setDescription("The amount of time to wait before automatically\ndeleting an entry in the lookupCtlTable and any\ndependent lookupResultsTable entries\nafter the lookup operation represented by a\nlookupCtlEntry has been completed.\nA lookupCtEntry is considered complete\nwhen its lookupCtlOperStatus object has a\nvalue of completed(3).\n\nA value of 0 indicates that automatic deletion\nof entries is disabled.")
lookupCtlTable = MibTable((1, 3, 6, 1, 2, 1, 82, 1, 3))
if mibBuilder.loadTexts: lookupCtlTable.setDescription("Defines the Lookup Control Table for providing\nthe capability of performing a lookup operation\nfor a symbolic host name or for a host address\nfrom a remote host.")
lookupCtlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 82, 1, 3, 1)).setIndexNames((0, "DISMAN-NSLOOKUP-MIB", "lookupCtlOwnerIndex"), (0, "DISMAN-NSLOOKUP-MIB", "lookupCtlOperationName"))
if mibBuilder.loadTexts: lookupCtlEntry.setDescription("Defines an entry in the lookupCtlTable.  A\nlookupCtlEntry is initially indexed by\nlookupCtlOwnerIndex, which is a type of SnmpAdminString,\na textual convention that allows for the use of the SNMPv3\nView-Based Access Control Model (RFC 3415, VACM)\nand that also allows a management application to identify\nits entries.  The second index element,\nlookupCtlOperationName, enables the same\nlookupCtlOwnerIndex entity to have multiple outstanding\nrequests.  The value of lookupCtlTargetAddressType\ndetermines which lookup function to perform.")
lookupCtlOwnerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: lookupCtlOwnerIndex.setDescription("To facilitate the provisioning of access control by a\nsecurity administrator using the View-Based Access\nControl Model (RFC 2575, VACM) for tables in which\nmultiple users may need to create or\nmodify entries independently, the initial index is used as\nan 'owner index'.  Such an initial index has a syntax of\nSnmpAdminString and can thus be trivially mapped to a\n\n\nsecurityName or groupName defined in VACM, in\naccordance with a security policy.\n\nWhen used in conjunction with such a security policy all\nentries in the table belonging to a particular user (or\ngroup) will have the same value for this initial index.\nFor a given user's entries in a particular table, the\nobject identifiers for the information in these entries\nwill have the same subidentifiers (except for the\n'column' subidentifier) up to the end of the encoded\nowner index.  To configure VACM to permit access to this\nportion of the table, one would create\nvacmViewTreeFamilyTable entries with the value of\nvacmViewTreeFamilySubtree including the owner index\nportion, and vacmViewTreeFamilyMask 'wildcarding' the\ncolumn subidentifier.  More elaborate configurations\nare possible.")
lookupCtlOperationName = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: lookupCtlOperationName.setDescription("The name of a lookup operation.  This is locally unique,\nwithin the scope of an lookupCtlOwnerIndex.")
lookupCtlTargetAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 3), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lookupCtlTargetAddressType.setDescription("Specifies the type of address for performing a\nlookup operation for a symbolic host name or for a host\naddress from a remote host.\n\nSpecification of dns(16) as the value for this object\nmeans that a function such as, for example, getaddrinfo()\nor gethostbyname() should be performed to return one or\nmore numeric addresses.  Use of a value of either ipv4(1)\nor ipv6(2) means that a functions such as, for example,\ngetnameinfo() or gethostbyaddr() should be used to return\nthe symbolic names associated with a host.")
lookupCtlTargetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lookupCtlTargetAddress.setDescription("Specifies the address used for a resolver lookup at a\nremote host.  The corresponding lookupCtlTargetAddressType\nobjects determines its type, as well as the function\nthat can be requested.\n\nA value for this object MUST be set prior to\ntransitioning its corresponding lookupCtlEntry to\nactive(1) via lookupCtlRowStatus.")
lookupCtlOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(2,3,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("notStarted", 2), ("completed", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lookupCtlOperStatus.setDescription("Reflects the operational state of an lookupCtlEntry:\n\nenabled(1)    - Operation is active.\nnotStarted(2) - Operation has not been enabled.\ncompleted(3)  - Operation has been completed.\n\nAn operation is automatically enabled(1) when its\nlookupCtlRowStatus object is transitioned to active(1)\nstatus.  Until this occurs, lookupCtlOperStatus MUST\nreport a value of notStarted(2).  After the lookup\noperation is completed (success or failure), the value\nfor lookupCtlOperStatus MUST be transitioned to\ncompleted(3).")
lookupCtlTime = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lookupCtlTime.setDescription("Reports the number of milliseconds that a lookup\noperation required to be completed at a remote host.\nCompleted means operation failure as well as\n\n\nsuccess.")
lookupCtlRc = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lookupCtlRc.setDescription("The system-specific return code from a lookup\noperation.  All implementations MUST return a value\nof 0 for this object when the remote lookup\noperation succeeds.  A non-zero value for this\nobjects indicates failure.  It is recommended that\nimplementations return the error codes that are\ngenerated by the lookup function used.")
lookupCtlRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lookupCtlRowStatus.setDescription("This object allows entries to be created and deleted\nin the lookupCtlTable.\n\nA remote lookup operation is started when an\nentry in this table is created via an SNMP set\nrequest and the entry is activated.  This\noccurs by setting the value of this object\nto CreateAndGo(4) during row creation or\nby setting this object to active(1) after\nthe row is created.\n\nA value MUST be specified for lookupCtlTargetAddress\nprior to the acceptance of a transition to active(1) state.\nA remote lookup operation starts when its entry\nfirst becomes active(1).  Transitions in and\nout of active(1) state have no effect on the\noperational behavior of a remote lookup\noperation, with the exception that deletion of\nan entry in this table by setting its RowStatus\nobject to destroy(6) will stop an active\nremote lookup operation.\n\nThe operational state of a remote lookup operation\ncan be determined by examination of its\nlookupCtlOperStatus object.")
lookupResultsTable = MibTable((1, 3, 6, 1, 2, 1, 82, 1, 4))
if mibBuilder.loadTexts: lookupResultsTable.setDescription("Defines the Lookup Results Table for providing\nthe capability of determining the results of a\noperation at a remote host.\n\nOne or more entries are added to the\nlookupResultsTable when a lookup operation,\nas reflected by an lookupCtlEntry, is completed\nsuccessfully.  All entries related to a\nsuccessful lookup operation MUST be added\nto the lookupResultsTable at the same time\nthat the associating lookupCtlOperStatus\nobject is transitioned to completed(2).\n\nThe number of entries added depends on the\nresults determined for a particular lookup\noperation.  All entries associated with an\nlookupCtlEntry are removed when the\nlookupCtlEntry is deleted.\n\nA remote host can be multi-homed and have more than one IP\naddress associated with it (returned by lookup function),\nor it can have more than one symbolic name (returned\nby lookup function).\n\nA function such as, for example, getnameinfo() or\ngethostbyaddr() is called with a host address as its\nparameter and is used primarily to determine a symbolic\nname to associate with the host address.  Entries in the\nlookupResultsTable MUST be made for each host name\nreturned.  If the function identifies an 'official host\nname,' then this symbolic name MUST be assigned a\nlookupResultsIndex of 1.\n\nA function such as, for example, getaddrinfo() or\ngethostbyname() is called with a symbolic host name and is\nused primarily to retrieve a host address.  The entries\n\n\nMUST be stored in the order that they are retrieved from\nthe lookup function.  lookupResultsIndex 1 MUST be\nassigned to the first entry.")
lookupResultsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 82, 1, 4, 1)).setIndexNames((0, "DISMAN-NSLOOKUP-MIB", "lookupCtlOwnerIndex"), (0, "DISMAN-NSLOOKUP-MIB", "lookupCtlOperationName"), (0, "DISMAN-NSLOOKUP-MIB", "lookupResultsIndex"))
if mibBuilder.loadTexts: lookupResultsEntry.setDescription("Defines an entry in the lookupResultsTable.  The\nfirst two index elements identify the\nlookupCtlEntry that a lookupResultsEntry belongs\nto.  The third index element selects a single\nlookup operation result.")
lookupResultsIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: lookupResultsIndex.setDescription("Entries in the lookupResultsTable are created when\nthe result of a lookup operation is determined.\n\nEntries MUST be stored in the lookupResultsTable in\nthe order that they are retrieved.  Values assigned\nto lookupResultsIndex MUST start at 1 and increase\nconsecutively.")
lookupResultsAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 4, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lookupResultsAddressType.setDescription("Indicates the type of result of a remote lookup\noperation.  A value of unknown(0) implies either that\nthe operation hasn't been started or that\nit has failed.")
lookupResultsAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 82, 1, 4, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lookupResultsAddress.setDescription("Reflects a result for a remote lookup operation\nas per the value of lookupResultsAddressType.\n\nThe address type (InetAddressType) that relates to\nthis object is specified by the corresponding value\nof lookupResultsAddress.")
lookupConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 82, 2))
lookupCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 82, 2, 1))
lookupGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 82, 2, 2))

# Augmentions

# Groups

lookupGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 82, 2, 2, 1)).setObjects(("DISMAN-NSLOOKUP-MIB", "lookupCtlOperStatus"), ("DISMAN-NSLOOKUP-MIB", "lookupCtlTargetAddress"), ("DISMAN-NSLOOKUP-MIB", "lookupCtlRowStatus"), ("DISMAN-NSLOOKUP-MIB", "lookupMaxConcurrentRequests"), ("DISMAN-NSLOOKUP-MIB", "lookupCtlRc"), ("DISMAN-NSLOOKUP-MIB", "lookupResultsAddress"), ("DISMAN-NSLOOKUP-MIB", "lookupResultsAddressType"), ("DISMAN-NSLOOKUP-MIB", "lookupCtlTime"), ("DISMAN-NSLOOKUP-MIB", "lookupCtlTargetAddressType"), ("DISMAN-NSLOOKUP-MIB", "lookupPurgeTime"), )
if mibBuilder.loadTexts: lookupGroup.setDescription("The group of objects that constitute the remote\nLookup operation.")

# Compliances

lookupCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 82, 2, 1, 1)).setObjects(("DISMAN-NSLOOKUP-MIB", "lookupGroup"), )
if mibBuilder.loadTexts: lookupCompliance.setDescription("The compliance statement for SNMP entities that\nfully implement the DISMAN-NSLOOKUP-MIB.")
lookupMinimumCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 82, 2, 1, 2)).setObjects(("DISMAN-NSLOOKUP-MIB", "lookupGroup"), )
if mibBuilder.loadTexts: lookupMinimumCompliance.setDescription("The minimum compliance statement for SNMP entities\nthat implement the minimal subset of the\nDISMAN-NSLOOKUP-MIB.  Implementors might choose this\nsubset for small devices with limited resources.")

# Exports

# Module identity
mibBuilder.exportSymbols("DISMAN-NSLOOKUP-MIB", PYSNMP_MODULE_ID=lookupMIB)

# Objects
mibBuilder.exportSymbols("DISMAN-NSLOOKUP-MIB", lookupMIB=lookupMIB, lookupObjects=lookupObjects, lookupMaxConcurrentRequests=lookupMaxConcurrentRequests, lookupPurgeTime=lookupPurgeTime, lookupCtlTable=lookupCtlTable, lookupCtlEntry=lookupCtlEntry, lookupCtlOwnerIndex=lookupCtlOwnerIndex, lookupCtlOperationName=lookupCtlOperationName, lookupCtlTargetAddressType=lookupCtlTargetAddressType, lookupCtlTargetAddress=lookupCtlTargetAddress, lookupCtlOperStatus=lookupCtlOperStatus, lookupCtlTime=lookupCtlTime, lookupCtlRc=lookupCtlRc, lookupCtlRowStatus=lookupCtlRowStatus, lookupResultsTable=lookupResultsTable, lookupResultsEntry=lookupResultsEntry, lookupResultsIndex=lookupResultsIndex, lookupResultsAddressType=lookupResultsAddressType, lookupResultsAddress=lookupResultsAddress, lookupConformance=lookupConformance, lookupCompliances=lookupCompliances, lookupGroups=lookupGroups)

# Groups
mibBuilder.exportSymbols("DISMAN-NSLOOKUP-MIB", lookupGroup=lookupGroup)

# Compliances
mibBuilder.exportSymbols("DISMAN-NSLOOKUP-MIB", lookupCompliance=lookupCompliance, lookupMinimumCompliance=lookupMinimumCompliance)
