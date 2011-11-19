# PySNMP SMI module. Autogenerated from smidump -f python ACCOUNTING-CONTROL-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:28:29 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( DisplayString, RowStatus, TextualConvention, TestAndIncr, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TestAndIncr", "TruthValue")

# Types

class DataCollectionList(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,8)
    
class DataCollectionSubtree(ObjectIdentifier):
    pass

class FileIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,65535)
    

# Objects

accountingControlMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 60)).setRevisions(("1998-09-28 10:00",))
if mibBuilder.loadTexts: accountingControlMIB.setOrganization("IETF AToM MIB Working Group")
if mibBuilder.loadTexts: accountingControlMIB.setContactInfo("Keith McCloghrie\nCisco Systems, Inc.\n170 West Tasman Drive,\nSan Jose CA 95134-1706.\nPhone: +1 408 526 5260\nEmail: kzm@cisco.com")
if mibBuilder.loadTexts: accountingControlMIB.setDescription("The MIB module for managing the collection and storage of\naccounting information for connections in a connection-\noriented network such as ATM.")
acctngMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 60, 1))
acctngSelectionControl = MibIdentifier((1, 3, 6, 1, 2, 1, 60, 1, 1))
acctngSelectionTable = MibTable((1, 3, 6, 1, 2, 1, 60, 1, 1, 1))
if mibBuilder.loadTexts: acctngSelectionTable.setDescription("A list of accounting information selection entries.\n\nNote that additions, modifications and deletions of entries\nin this table can occur at any time, but such changes only\ntake effect on the next occasion when collection begins into\na new file.  Thus, between modification and the next 'swap',\nthe content of this table does not reflect the current\nselection.")
acctngSelectionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1)).setIndexNames((0, "ACCOUNTING-CONTROL-MIB", "acctngSelectionIndex"))
if mibBuilder.loadTexts: acctngSelectionEntry.setDescription("An entry identifying an (subtree, list) tuple used to\nselect a set of accounting information which is to be\ncollected.")
acctngSelectionIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: acctngSelectionIndex.setDescription("An arbitrary integer value which uniquely identifies a\ntuple stored in this table.  This value is required to be\nthe permanent 'handle' for an entry in this table for as\nlong as that entry exists, including across restarts and\npower outages.")
acctngSelectionSubtree = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 2), DataCollectionSubtree()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngSelectionSubtree.setDescription("The combination of acctngSelectionSubtree and\nacctngSelectionList specifies one (subtree, list) tuple\nwhich is to be collected.")
acctngSelectionList = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 3), DataCollectionList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngSelectionList.setDescription("The combination of acctngSelectionSubtree and\nacctngSelectionList specifies one (subtree, list) tuple\nwhich is to be collected.")
acctngSelectionFile = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 4), FileIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngSelectionFile.setDescription("An indication of the file into which the accounting\ninformation identified by this entry is to be stored.  If\nthere is no conceptual row in the acctngFileTable for which\nthe value of acctngFileIndex has the same value as this\nobject, then the information selected by this entry is not\ncollected.")
acctngSelectionType = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 5), Bits().subtype(namedValues=NamedValues(("svcIncoming", 0), ("svcOutgoing", 1), ("svpIncoming", 2), ("svpOutgoing", 3), ("pvc", 4), ("pvp", 5), ("spvcOriginator", 6), ("spvcTarget", 7), ("spvpOriginator", 8), ("spvpTarget", 9), )).clone(("svcIncoming","svcOutgoing","svpIncoming","svpOutgoing",))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngSelectionType.setDescription("Indicates the types of connections for which the\ninformation selected by this entry are to be collected.")
acctngSelectionRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngSelectionRowStatus.setDescription("The status of this conceptual row.  An agent may refuse to\ncreate new conceptual rows and/or modify existing conceptual\nrows, if such creation/modification would cause multiple\nrows to have the same values of acctngSelectionSubtree and\nacctngSelectionList.\n\nA conceptual row can not have the status of 'active' until\nvalues have been assigned to the acctngSelectionSubtree,\nacctngSelectionList and acctngSelectionFile columnar objects\nwithin that row.\n\nAn agent must not refuse to change the values of the\nacctngSelectionSubtree, acctngSelectionList and\nacctngSelectionFile columnar objects within a conceptual row\neven while that row's status is 'active'.  Similarly, an\nagent must not refuse to destroy an existing conceptual row\nwhile the file referenced by that row's instance of\nacctngSelectionFile is in active use, i.e., while the\ncorresponding instance of acctngFileRowStatus has the value\n'active'.  However, such changes only take effect upon the\nnext occasion when collection begins into a new (version of\nthe) file.")
acctngFileControl = MibIdentifier((1, 3, 6, 1, 2, 1, 60, 1, 2))
acctngFileTable = MibTable((1, 3, 6, 1, 2, 1, 60, 1, 2, 1))
if mibBuilder.loadTexts: acctngFileTable.setDescription("A list of files into which accounting information is to be\nstored.")
acctngFileEntry = MibTableRow((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1)).setIndexNames((0, "ACCOUNTING-CONTROL-MIB", "acctngFileIndex"))
if mibBuilder.loadTexts: acctngFileEntry.setDescription("An entry identifying a file into which accounting\ninformation is to be collected.")
acctngFileIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 1), FileIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: acctngFileIndex.setDescription("A unique value identifying a file into which accounting\ndata is to be stored.  This value is required to be the\npermanent 'handle' for an entry in this table for as long as\nthat entry exists, including across restarts and power\noutages.")
acctngFileName = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngFileName.setDescription("The name of the file into which accounting data is to be\nstored.  If files are named using suffixes, then the name of\nthe current file is the concatenation of acctngFileName and\nacctngFileNameSuffix.\n\nAn agent will respond with an error (e.g., 'wrongValue') to\na management set operation which attempts to modify the\nvalue of this object to the same value as already held by\nanother instance of acctngFileName.  An agent will also\nrespond with an error (e.g., 'wrongValue') if the new value\nis invalid for use as a file name on the local file system\n(e.g., many file systems do not support white space embedded\nin file names).\n\nThe value of this object can not be modified while the\ncorresponding instance of acctngFileRowStatus is 'active'.")
acctngFileNameSuffix = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctngFileNameSuffix.setDescription("The suffix, if any, of the name of a file into which\naccounting data is currently being stored.  If suffixes are\nnot used, then the value of this object is the zero-length\nstring.  Note that if a separator, such as a period, is used\nin appending the suffix to the file name, then that\nseparator appears as the first character of this value.")
acctngFileDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 4), DisplayString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngFileDescription.setDescription("The textual description of the accounting data which will\nbe stored (on the next occasion) when header information is\nstored in the file.  The value of this object may be\nmodified at any time.")
acctngFileCommand = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,4,2,)).subtype(namedValues=NamedValues(("idle", 1), ("cmdInProgress", 2), ("swapToNewFile", 3), ("collectNow", 4), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngFileCommand.setDescription("A control object for the collection of accounting data.\nWhen read the value is either 'idle' or 'cmdInProgress'.\nWriting a value is only allowed when the current value is\n'idle'.  When a value is successfully written, the value\nchanges to 'cmdInProgress' until completion of the action,\nat which time the value reverts to 'idle'.  Actions are\ninvoked by writing the following values:\n\n   'swapToNewFile' - the collection of data into the current\n          file is terminated, and collection continues into\n          a new (version of the) file.\n\n   'collectNow' - the agent creates and stores a connection\n          record into the current file for each active\n          connection having a type matching\n          acctngSelectionType and an age greater than\n          acctngFileMinAge.")
acctngFileMaximumSize = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 2147483647)).clone(5000000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngFileMaximumSize.setDescription("The maximum size of the file (including header\ninformation).  When the file of collected data reaches this\nsize, either the agent automatically swaps to a new version\n(i.e., a new value acctngFileNameSuffix) of the file, or new\nrecords are discarded.  Since a file must contain an\nintegral number of connection records, the actual maximum\nsize of the file may be just less OR Just greater than the\nvalue of this object.\n\nThe value of this object can not be modified while the\ncorresponding instance of acctngFileRowStatus is 'active'.\nThe largest value of the maximum file size in some agents\nwill be less than 2147483647 bytes.")
acctngFileCurrentSize = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctngFileCurrentSize.setDescription("The current size of the file into which data is currently\nbeing collected, including header information.")
acctngFileFormat = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("other", 1), ("ber", 2), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngFileFormat.setDescription("An indication of the format in which the accounting data is\nto be stored in the file.  If the value is modified, the new\nvalue takes effect after the next 'swap' to a new file.  The\nvalue ber(2) indicates the standard format.")
acctngFileCollectMode = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 9), Bits().subtype(namedValues=NamedValues(("onRelease", 0), ("periodically", 1), )).clone(("onRelease",))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngFileCollectMode.setDescription("An indication of when accounting data is to be written into\nthis file.  Note that in addition to the occasions indicated\nby the value of this object, an agent always writes\ninformation on appropriate connections to the file when the\ncorresponding instance of acctngFileCommand is set to\n'collectNow'.\n\n  - 'onRelease' - whenever a connection (or possibly,\n          connection attempt) is terminated, either through\n          a Release message or through management removal,\n          information on that connection is written.\n\n  - 'periodically' - information on appropriate connections\n          is written on the expiry of a periodic timer,\n\nThis value may be modified at any time.")
acctngFileCollectFailedAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 10), Bits().subtype(namedValues=NamedValues(("soft", 0), ("regular", 1), )).clone(("soft","regular",))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngFileCollectFailedAttempts.setDescription("An indication of whether connection data is to be collected\nfor failed connection attempts when the value of the\ncorresponding instance of acctngFileCollectMode includes\n'onRelease'.  The individual values have the following\nmeaning:\n\n  'soft' - indicates that connection data is to be collected\nfor failed Soft PVCs/PVPs which originate or terminate at\nthe relevant interface.\n\n  'regular' - indicates that connection data is to be\ncollected for failed SVCs, including Soft PVCs/PVPs not\noriginating or terminating at the relevant interface.\n\nThis value may be modified at any time.")
acctngFileInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 86400)).clone(3600)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngFileInterval.setDescription("The number of seconds between the periodic collections of\naccounting data when the value of the corresponding instance\nof acctngFileCollectMode includes 'periodically'.  Some\nagents may impose restrictions on the range of this\ninterval.  This value may be modified at any time.")
acctngFileMinAge = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 86400)).clone(3600)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngFileMinAge.setDescription("The minimum age of a connection, as used to determine the\nset of connections for which data is to be collected at the\nperiodic intervals and/or when acctngFileCommand is set to\n'collectNow'.  The age of a connection is the elapsed time\nsince it was last installed.\n\nWhen the periodic interval expires for a file or when\nacctngFileCommand is set to 'collectNow', accounting data is\ncollected and stored in the file for each connection having\na type matching acctngSelectionType and whose age at that\ntime is greater than the value of acctngFileMinAge\nassociated with the file.  This value may be modified at any\ntime.")
acctngFileRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acctngFileRowStatus.setDescription("The status of this conceptual row.\n\nThis object can not be set to 'active' until a value has\nbeen assigned to the corresponding instance of\nacctngFileName.  Collection of data into the file does not\nbegin until this object has the value 'active' and one or\nmore (active) instances of acctngSelectionFile refer to it.\nIf this value is modified after a collection has begun,\ncollection into this file terminates and a new (or new\nversion of the) file is immediately made ready for future\ncollection (as if acctngFileCommand had been set to\n'swapToNewFile'), but collection into the new (or new\nversion of the) file does not begin until the value is\nsubsequently set back to active.")
acctngInterfaceControl = MibIdentifier((1, 3, 6, 1, 2, 1, 60, 1, 3))
acctngAdminStatus = MibScalar((1, 3, 6, 1, 2, 1, 60, 1, 3, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctngAdminStatus.setDescription("A control object to indicate the administratively desired\nstate of the collection of accounting records across all\ninterfaces.\n\nModifying the value of acctngAdminStatus to 'disabled' does\nnot remove or change the current configuration as\nrepresented by the active rows in the acctngSelectionTable,\nacctngFileTable and acctngInterfaceTable tables.")
acctngOperStatus = MibScalar((1, 3, 6, 1, 2, 1, 60, 1, 3, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctngOperStatus.setDescription("A status object to indicate the operational state of the\ncollection of accounting records across all interfaces.\n\nWhen the value of acctngAdminStatus is modified to be\n'enabled', the value of this object will change to 'enabled'\nproviding it is possible to begin collecting accounting\nrecords.\n\nWhen the value of acctngAdminStatus is modified to be\n'disabled', the value of this object will change to\n'disabled' as soon as the collection of accounting records\nhas terminated.")
acctngProtection = MibScalar((1, 3, 6, 1, 2, 1, 60, 1, 3, 3), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctngProtection.setDescription("A control object to protect against duplication of control\ncommands.  Over some transport/network protocols, it is\npossible for SNMP messages to get duplicated.  Such\nduplication, if it occurred at just the wrong time could\ncause serious disruption to the collection and retrieval of\naccounting data, e.g., if a SNMP message setting\nacctngFileCommand to 'swapToNewFile' were to be duplicated,\na whole file of accounting data could be lost.\n\nTo protect against such duplication, a management\napplication should retrieve the value of this object, and\ninclude in the Set operation needing protection, a variable\nbinding which sets this object to the retrieved value.")
acctngAgentMode = MibScalar((1, 3, 6, 1, 2, 1, 60, 1, 3, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("swapOnCommand", 1), ("swapOnFull", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctngAgentMode.setDescription("An indication of the behaviour mode of the agent when a\nfile becomes full:\n\n   'swapOnCommand' - the agent does not automatically swap\n          to a new file; rather, it discards newly collected\n          data until a management application subsequently\n          instructs it to swap to a new file.\n\n   'swapOnFull' - the agent terminates collection into the\n          current file as and when that file becomes full.")
acctngInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 60, 1, 3, 5))
if mibBuilder.loadTexts: acctngInterfaceTable.setDescription("A table controlling the collection of accounting data on\nspecific interfaces of the switch.")
acctngInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 60, 1, 3, 5, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: acctngInterfaceEntry.setDescription("An entry which controls whether accounting data is to be\ncollected on an interface.  The types of interfaces which\nare represented in this table is implementation-specific.")
acctngInterfaceEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 60, 1, 3, 5, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctngInterfaceEnable.setDescription("Indicates whether the collection of accounting data is\nenabled on this interface.")
acctngTrapControl = MibIdentifier((1, 3, 6, 1, 2, 1, 60, 1, 4))
acctngControlTrapThreshold = MibScalar((1, 3, 6, 1, 2, 1, 60, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctngControlTrapThreshold.setDescription("A percentage of the maximum file size at which a 'nearly-\nfull' trap is generated.  The value of 0 indicates that no\n'nearly-full' trap is to be generated.")
acctngControlTrapEnable = MibScalar((1, 3, 6, 1, 2, 1, 60, 1, 4, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctngControlTrapEnable.setDescription("An indication of whether the acctngFileNearlyFull and\nacctngFileFull traps are enabled.")
acctngNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 60, 2))
acctngNotifyPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 60, 2, 0))
acctngConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 60, 3))
acctngGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 60, 3, 1))
acctngCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 60, 3, 2))

# Augmentions

# Notifications

acctngFileNearlyFull = NotificationType((1, 3, 6, 1, 2, 1, 60, 2, 0, 1)).setObjects(("ACCOUNTING-CONTROL-MIB", "acctngControlTrapThreshold"), ("ACCOUNTING-CONTROL-MIB", "acctngFileMaximumSize"), ("ACCOUNTING-CONTROL-MIB", "acctngFileNameSuffix"), ("ACCOUNTING-CONTROL-MIB", "acctngFileName"), )
if mibBuilder.loadTexts: acctngFileNearlyFull.setDescription("An indication that the size of the file into which\naccounting information is currently being collected has\nexceeded the threshold percentage of its maximum file size.\nThis notification is generated only at the time of the\ntransition from not-exceeding to exceeding.")
acctngFileFull = NotificationType((1, 3, 6, 1, 2, 1, 60, 2, 0, 2)).setObjects(("ACCOUNTING-CONTROL-MIB", "acctngFileMaximumSize"), ("ACCOUNTING-CONTROL-MIB", "acctngFileNameSuffix"), ("ACCOUNTING-CONTROL-MIB", "acctngFileName"), )
if mibBuilder.loadTexts: acctngFileFull.setDescription("An indication that the size of the file into which\naccounting information is currently being collected has\ntransistioned to its maximum file size.  This notification\nis generated (for all values of acctngAgentMode) at the time\nof the transition from not-full to full.  If acctngAgentMode\nhas the value 'swapOnCommand', it is also generated\nperiodically thereafter until such time as collection of\ndata is no longer inhibited by the file full condition.")

# Groups

acctngBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 60, 3, 1, 1)).setObjects(("ACCOUNTING-CONTROL-MIB", "acctngAdminStatus"), ("ACCOUNTING-CONTROL-MIB", "acctngProtection"), ("ACCOUNTING-CONTROL-MIB", "acctngFileName"), ("ACCOUNTING-CONTROL-MIB", "acctngSelectionSubtree"), ("ACCOUNTING-CONTROL-MIB", "acctngFileCollectMode"), ("ACCOUNTING-CONTROL-MIB", "acctngControlTrapThreshold"), ("ACCOUNTING-CONTROL-MIB", "acctngFileRowStatus"), ("ACCOUNTING-CONTROL-MIB", "acctngSelectionRowStatus"), ("ACCOUNTING-CONTROL-MIB", "acctngOperStatus"), ("ACCOUNTING-CONTROL-MIB", "acctngSelectionFile"), ("ACCOUNTING-CONTROL-MIB", "acctngFileFormat"), ("ACCOUNTING-CONTROL-MIB", "acctngSelectionType"), ("ACCOUNTING-CONTROL-MIB", "acctngSelectionList"), ("ACCOUNTING-CONTROL-MIB", "acctngFileCurrentSize"), ("ACCOUNTING-CONTROL-MIB", "acctngFileDescription"), ("ACCOUNTING-CONTROL-MIB", "acctngFileInterval"), ("ACCOUNTING-CONTROL-MIB", "acctngAgentMode"), ("ACCOUNTING-CONTROL-MIB", "acctngControlTrapEnable"), ("ACCOUNTING-CONTROL-MIB", "acctngFileMaximumSize"), ("ACCOUNTING-CONTROL-MIB", "acctngFileCollectFailedAttempts"), ("ACCOUNTING-CONTROL-MIB", "acctngFileCommand"), ("ACCOUNTING-CONTROL-MIB", "acctngFileMinAge"), ("ACCOUNTING-CONTROL-MIB", "acctngInterfaceEnable"), ("ACCOUNTING-CONTROL-MIB", "acctngFileNameSuffix"), )
if mibBuilder.loadTexts: acctngBasicGroup.setDescription("A collection of objects providing control of the basic\ncollection of accounting data for connection-oriented\nnetworks.")
acctngNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 60, 3, 1, 2)).setObjects(("ACCOUNTING-CONTROL-MIB", "acctngFileNearlyFull"), ("ACCOUNTING-CONTROL-MIB", "acctngFileFull"), )
if mibBuilder.loadTexts: acctngNotificationsGroup.setDescription("The notifications of events relating to controlling the\ncollection of accounting data.")

# Compliances

acctngCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 60, 3, 2, 1)).setObjects(("ACCOUNTING-CONTROL-MIB", "acctngNotificationsGroup"), ("ACCOUNTING-CONTROL-MIB", "acctngBasicGroup"), )
if mibBuilder.loadTexts: acctngCompliance.setDescription("The compliance statement for switches which implement the\nAccounting Control MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("ACCOUNTING-CONTROL-MIB", PYSNMP_MODULE_ID=accountingControlMIB)

# Types
mibBuilder.exportSymbols("ACCOUNTING-CONTROL-MIB", DataCollectionList=DataCollectionList, DataCollectionSubtree=DataCollectionSubtree, FileIndex=FileIndex)

# Objects
mibBuilder.exportSymbols("ACCOUNTING-CONTROL-MIB", accountingControlMIB=accountingControlMIB, acctngMIBObjects=acctngMIBObjects, acctngSelectionControl=acctngSelectionControl, acctngSelectionTable=acctngSelectionTable, acctngSelectionEntry=acctngSelectionEntry, acctngSelectionIndex=acctngSelectionIndex, acctngSelectionSubtree=acctngSelectionSubtree, acctngSelectionList=acctngSelectionList, acctngSelectionFile=acctngSelectionFile, acctngSelectionType=acctngSelectionType, acctngSelectionRowStatus=acctngSelectionRowStatus, acctngFileControl=acctngFileControl, acctngFileTable=acctngFileTable, acctngFileEntry=acctngFileEntry, acctngFileIndex=acctngFileIndex, acctngFileName=acctngFileName, acctngFileNameSuffix=acctngFileNameSuffix, acctngFileDescription=acctngFileDescription, acctngFileCommand=acctngFileCommand, acctngFileMaximumSize=acctngFileMaximumSize, acctngFileCurrentSize=acctngFileCurrentSize, acctngFileFormat=acctngFileFormat, acctngFileCollectMode=acctngFileCollectMode, acctngFileCollectFailedAttempts=acctngFileCollectFailedAttempts, acctngFileInterval=acctngFileInterval, acctngFileMinAge=acctngFileMinAge, acctngFileRowStatus=acctngFileRowStatus, acctngInterfaceControl=acctngInterfaceControl, acctngAdminStatus=acctngAdminStatus, acctngOperStatus=acctngOperStatus, acctngProtection=acctngProtection, acctngAgentMode=acctngAgentMode, acctngInterfaceTable=acctngInterfaceTable, acctngInterfaceEntry=acctngInterfaceEntry, acctngInterfaceEnable=acctngInterfaceEnable, acctngTrapControl=acctngTrapControl, acctngControlTrapThreshold=acctngControlTrapThreshold, acctngControlTrapEnable=acctngControlTrapEnable, acctngNotifications=acctngNotifications, acctngNotifyPrefix=acctngNotifyPrefix, acctngConformance=acctngConformance, acctngGroups=acctngGroups, acctngCompliances=acctngCompliances)

# Notifications
mibBuilder.exportSymbols("ACCOUNTING-CONTROL-MIB", acctngFileNearlyFull=acctngFileNearlyFull, acctngFileFull=acctngFileFull)

# Groups
mibBuilder.exportSymbols("ACCOUNTING-CONTROL-MIB", acctngBasicGroup=acctngBasicGroup, acctngNotificationsGroup=acctngNotificationsGroup)

# Compliances
mibBuilder.exportSymbols("ACCOUNTING-CONTROL-MIB", acctngCompliance=acctngCompliance)
