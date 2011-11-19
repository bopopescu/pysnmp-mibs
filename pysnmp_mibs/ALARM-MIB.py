# PySNMP SMI module. Autogenerated from smidump -f python ALARM-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:28:33 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( ZeroBasedCounter32, ) = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Counter64, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Opaque, TimeTicks, TimeTicks, Unsigned32, mib_2, zeroDotZero, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Opaque", "TimeTicks", "TimeTicks", "Unsigned32", "mib-2", "zeroDotZero")
( DateAndTime, RowPointer, RowStatus, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowPointer", "RowStatus", "TextualConvention")

# Types

class LocalSnmpEngineOrZeroLenStr(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(5,32),)
    
class ResourceId(ObjectIdentifier):
    pass


# Objects

alarmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 118)).setRevisions(("2004-09-09 00:00",))
if mibBuilder.loadTexts: alarmMIB.setOrganization("IETF Distributed Management Working Group")
if mibBuilder.loadTexts: alarmMIB.setContactInfo("WG EMail: disman@ietf.org\nSubscribe: disman-request@ietf.org\nhttp://www.ietf.org/html.charters/disman-charter.html\n\n\n\nChair:     Randy Presuhn\n           randy_presuhn@mindspring.com\n\nEditors:   Sharon Chisholm\n           Nortel Networks\n           PO Box 3511 Station C\n           Ottawa, Ont.  K1Y 4H7\n           Canada\n           schishol@nortelnetworks.com\n\n           Dan Romascanu\n           Avaya\n           Atidim Technology Park, Bldg. #3\n           Tel Aviv, 61131\n           Israel\n           Tel: +972-3-645-8414\n           Email: dromasca@avaya.com")
if mibBuilder.loadTexts: alarmMIB.setDescription("The MIB module describes a generic solution\nto model alarms and to store the current list\nof active alarms.\n\nCopyright (C) The Internet Society (2004).  The\ninitial version of this MIB module was published\nin RFC 3877.  For full legal notices see the RFC\nitself.  Supplementary information may be available on:\nhttp://www.ietf.org/copyrights/ianamib.html")
alarmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 118, 0))
alarmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 118, 1))
alarmModel = MibIdentifier((1, 3, 6, 1, 2, 1, 118, 1, 1))
alarmModelLastChanged = MibScalar((1, 3, 6, 1, 2, 1, 118, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmModelLastChanged.setDescription("The value of sysUpTime at the time of the last\ncreation, deletion or modification of an entry in\nthe alarmModelTable.\n\nIf the number and content of entries has been unchanged\nsince the last re-initialization of the local network\nmanagement subsystem, then the value of this object\nMUST be zero.")
alarmModelTable = MibTable((1, 3, 6, 1, 2, 1, 118, 1, 1, 2))
if mibBuilder.loadTexts: alarmModelTable.setDescription("A table of information about possible alarms on the system,\nand how they have been modelled.")
alarmModelEntry = MibTableRow((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1)).setIndexNames((0, "ALARM-MIB", "alarmListName"), (0, "ALARM-MIB", "alarmModelIndex"), (0, "ALARM-MIB", "alarmModelState"))
if mibBuilder.loadTexts: alarmModelEntry.setDescription("Entries appear in this table for each possible alarm state.\nThis table MUST be persistent across system reboots.")
alarmModelIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: alarmModelIndex.setDescription("An integer that acts as an alarm Id\nto uniquely identify each alarm\nwithin the named alarm list. ")
alarmModelState = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: alarmModelState.setDescription("A value of 1 MUST indicate a clear alarm state.\nThe value of this object MUST be less than the\nalarmModelState of more severe alarm states for\nthis alarm.  The value of this object MUST be more\nthan the alarmModelState of less severe alarm states\nfor this alarm.")
alarmModelNotificationId = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 3), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmModelNotificationId.setDescription("The NOTIFICATION-TYPE object identifier of this alarm\nstate transition.  If there is no notification associated\nwith this alarm state, the value of this object MUST be\n'0.0'")
alarmModelVarbindIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 4), Unsigned32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmModelVarbindIndex.setDescription("The index into the varbind listing of the notification\nindicated by alarmModelNotificationId which helps\nsignal that the given alarm has changed state.\nIf there is no applicable varbind, the value of this\nobject MUST be zero.\n\nNote that the value of alarmModelVarbindIndex acknowledges\nthe existence of the first two obligatory varbinds in\nthe InformRequest-PDU and SNMPv2-Trap-PDU (sysUpTime.0\nand snmpTrapOID.0).  That is, a value of 2 refers to\nthe snmpTrapOID.0.\n\nIf the incoming notification is instead an SNMPv1 Trap-PDU,\nthen an appropriate value for sysUpTime.0 or snmpTrapOID.0\nshall be determined by using the rules in section 3.1 of\n[RFC3584]")
alarmModelVarbindValue = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 5), Integer32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmModelVarbindValue.setDescription("The value that the varbind indicated by\nalarmModelVarbindIndex takes to indicate\nthat the alarm has entered this state.\n\nIf alarmModelVarbindIndex has a value of 0, so\nMUST alarmModelVarbindValue.")
alarmModelDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 6), SnmpAdminString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmModelDescription.setDescription("A brief description of this alarm and state suitable\nto display to operators.")
alarmModelSpecificPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 7), RowPointer().clone('0.0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmModelSpecificPointer.setDescription("If no additional, model-specific Alarm MIB is supported by\nthe system the value of this object is `0.0'and attempts\nto set it to any other value MUST be rejected appropriately.\n\nWhen a model-specific Alarm MIB is supported, this object\nMUST refer to the first accessible object in a corresponding\nrow of the model definition in one of these model-specific\nMIB and attempts to set this object to { 0 0 } or any other\nvalue MUST be rejected appropriately.")
alarmModelVarbindSubtree = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 8), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmModelVarbindSubtree.setDescription("The name portion of each VarBind in the notification,\nin order, is compared to the value of this object.\nIf the name is equal to or a subtree of the value\nof this object, for purposes of computing the value\n\n\n\nof AlarmActiveResourceID the 'prefix' will be the\nmatching portion, and the 'indexes' will be any\nremainder.  The examination of varbinds ends with\nthe first match.  If the value of this object is 0.0,\nthen the first varbind, or in the case of v2, the\nfirst varbind after the timestamp and the trap\nOID, will always be matched.")
alarmModelResourcePrefix = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 9), ObjectIdentifier().clone((0, 0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmModelResourcePrefix.setDescription("The value of AlarmActiveResourceId is computed\nby appending any indexes extracted in accordance\nwith the description of alarmModelVarbindSubtree\nonto the value of this object.  If this object's\nvalue is 0.0, then the 'prefix' extracted is used\ninstead.")
alarmModelRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alarmModelRowStatus.setDescription("Control for creating and deleting entries.  Entries may be\nmodified while active.  Alarms whose alarmModelRowStatus is\nnot active will not appear in either the alarmActiveTable\nor the alarmClearTable.  Setting this object to notInService\ncannot be used as an alarm suppression mechanism.  Entries\nthat are notInService will disappear as described in RFC2579.\n\nThis row can not be modified while it is being\nreferenced by a value of alarmActiveModelPointer.  In these\ncases, an error of `inconsistentValue' will be returned to\nthe manager.\n\nThis entry may be deleted while it is being\nreferenced by a value of alarmActiveModelPointer.  This results\nin the deletion of this entry and entries in the active alarms\nreferencing this entry via an alarmActiveModelPointer.\n\n\n\n\nAs all read-create objects in this table have a DEFVAL clause,\nthere is no requirement that any object be explicitly set\nbefore this row can become active.  Note that a row consisting\nonly of default values is not very meaningful.")
alarmActive = MibIdentifier((1, 3, 6, 1, 2, 1, 118, 1, 2))
alarmActiveLastChanged = MibScalar((1, 3, 6, 1, 2, 1, 118, 1, 2, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveLastChanged.setDescription("The value of sysUpTime at the time of the last\ncreation or deletion of an entry in the alarmActiveTable.\nIf the number of entries has been unchanged since the\nlast re-initialization of the local network management\nsubsystem, then this object contains a zero value.")
alarmActiveTable = MibTable((1, 3, 6, 1, 2, 1, 118, 1, 2, 2))
if mibBuilder.loadTexts: alarmActiveTable.setDescription("A table of Active Alarms entries.")
alarmActiveEntry = MibTableRow((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1)).setIndexNames((0, "ALARM-MIB", "alarmListName"), (0, "ALARM-MIB", "alarmActiveDateAndTime"), (0, "ALARM-MIB", "alarmActiveIndex"))
if mibBuilder.loadTexts: alarmActiveEntry.setDescription("Entries appear in this table when alarms are raised.  They\nare removed when the alarm is cleared.\n\nIf under extreme resource constraint the system is unable to\n\n\n\nadd any more entries into this table, then the\nalarmActiveOverflow statistic will be increased by one.")
alarmListName = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: alarmListName.setDescription("The name of the list of alarms.  This SHOULD be the same as\nnlmLogName if the Notification Log MIB [RFC3014] is supported.\nThis SHOULD be the same as, or contain as a prefix, the\napplicable snmpNotifyFilterProfileName if the\nSNMP-NOTIFICATION-MIB DEFINITIONS [RFC3413] is supported.\n\nAn implementation may allow multiple named alarm lists, up to\nsome implementation-specific limit (which may be none).  A\nzero-length list name is reserved for creation and deletion\nby the managed system, and MUST be used as the default log\nname by systems that do not support named alarm lists.")
alarmActiveDateAndTime = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 2), DateAndTime()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: alarmActiveDateAndTime.setDescription("The local date and time when the error occurred.\n\nThis object facilitates retrieving all instances of\n\n\n\nalarms that have been raised or have changed state\nsince a given point in time.\n\nImplementations MUST include the offset from UTC,\nif available.  Implementation in environments in which\nthe UTC offset is not available is NOT RECOMMENDED.")
alarmActiveIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: alarmActiveIndex.setDescription("A strictly monotonically increasing integer which\nacts as the index of entries within the named alarm\nlist.  It wraps back to 1 after it reaches its\nmaximum value.")
alarmActiveEngineID = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 4), LocalSnmpEngineOrZeroLenStr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveEngineID.setDescription("The identification of the SNMP engine at which the alarm\noriginated.  If the alarm is from an SNMPv1 system this\nobject is a zero length string.")
alarmActiveEngineAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveEngineAddressType.setDescription("This object indicates what type of address is stored in\nthe alarmActiveEngineAddress object - IPv4, IPv6, DNS, etc.")
alarmActiveEngineAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveEngineAddress.setDescription("The address of the SNMP engine on which the alarm is\noccurring.\n\nThis object MUST always be instantiated, even if the list\ncan contain alarms from only one engine.")
alarmActiveContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveContextName.setDescription("The name of the SNMP MIB context from which the alarm came.\nFor SNMPv1 alarms this is the community string from the Trap.\nNote that care MUST be taken when selecting community\nstrings to ensure that these can be represented as a\nwell-formed SnmpAdminString.  Community or Context names\nthat are not well-formed SnmpAdminStrings will be mapped\nto zero length strings.\n\nIf the alarm's source SNMP engine is known not to support\nmultiple contexts, this object is a zero length string.")
alarmActiveVariables = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariables.setDescription("The number of variables in alarmActiveVariableTable for this\nalarm.")
alarmActiveNotificationID = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 9), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveNotificationID.setDescription("The NOTIFICATION-TYPE object identifier of the alarm\nstate transition that is occurring.")
alarmActiveResourceId = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 10), ResourceId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveResourceId.setDescription("This object identifies the resource under alarm.\n\nIf there is no corresponding resource, then\nthe value of this object MUST be 0.0.")
alarmActiveDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveDescription.setDescription("This object provides a textual description of the\nactive alarm.  This text is generated dynamically by the\nnotification generator to provide useful information\nto the human operator.  This information SHOULD\nprovide information allowing the operator to locate\nthe resource for which this alarm is being generated.\nThis information is not intended for consumption by\nautomated tools.")
alarmActiveLogPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 12), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveLogPointer.setDescription("A pointer to the corresponding row in a\nnotification logging MIB where the state change\nnotification for this active alarm is logged.\nIf no log entry applies to this active alarm,\nthen this object MUST have the value of 0.0")
alarmActiveModelPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 13), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveModelPointer.setDescription("A pointer to the corresponding row in the\nalarmModelTable for this active alarm.  This\npoints not only to the alarm model being\ninstantiated, but also to the specific alarm\nstate that is active.")
alarmActiveSpecificPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 14), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveSpecificPointer.setDescription("If no additional, model-specific, Alarm MIB is supported by\nthe system this object is `0.0'.  When a model-specific Alarm\nMIB is supported, this object is the instance pointer to the\nspecific model-specific active alarm list.")
alarmActiveVariableTable = MibTable((1, 3, 6, 1, 2, 1, 118, 1, 2, 3))
if mibBuilder.loadTexts: alarmActiveVariableTable.setDescription("A table of variables to go with active alarm entries.")
alarmActiveVariableEntry = MibTableRow((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1)).setIndexNames((0, "ALARM-MIB", "alarmListName"), (0, "ALARM-MIB", "alarmActiveIndex"), (0, "ALARM-MIB", "alarmActiveVariableIndex"))
if mibBuilder.loadTexts: alarmActiveVariableEntry.setDescription("Entries appear in this table when there are variables in\nthe varbind list of a corresponding alarm in\nalarmActiveTable.\n\nEntries appear in this table as though\nthe trap/notification had been transported using a\nSNMPv2-Trap-PDU, as defined in [RFC3416] - i.e., the\nalarmActiveVariableIndex 1 will always be sysUpTime\nand alarmActiveVariableIndex 2 will always be\nsnmpTrapOID.\n\nIf the incoming notification is instead an SNMPv1 Trap-PDU and\nthe value of alarmModelVarbindIndex is 1 or 2, an appropriate\nvalue for sysUpTime.0 or snmpTrapOID.0 shall be determined\nby using the rules in section 3.1 of [RFC3584].")
alarmActiveVariableIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: alarmActiveVariableIndex.setDescription("A strictly monotonically increasing integer, starting at\n1 for a given alarmActiveIndex, for indexing variables\nwithin the active alarm variable list. ")
alarmActiveVariableID = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableID.setDescription("The alarm variable's object identifier.")
alarmActiveVariableValueType = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(4,6,7,5,3,8,2,9,1,)).subtype(namedValues=NamedValues(("counter32", 1), ("unsigned32", 2), ("timeTicks", 3), ("integer32", 4), ("ipAddress", 5), ("octetString", 6), ("objectId", 7), ("counter64", 8), ("opaque", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableValueType.setDescription("The type of the value.  One and only one of the value\nobjects that follow is used for a given row in this table,\nbased on this type.")
alarmActiveVariableCounter32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableCounter32Val.setDescription("The value when alarmActiveVariableType is 'counter32'.")
alarmActiveVariableUnsigned32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableUnsigned32Val.setDescription("The value when alarmActiveVariableType is 'unsigned32'.")
alarmActiveVariableTimeTicksVal = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableTimeTicksVal.setDescription("The value when alarmActiveVariableType is 'timeTicks'.")
alarmActiveVariableInteger32Val = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableInteger32Val.setDescription("The value when alarmActiveVariableType is 'integer32'.")
alarmActiveVariableOctetStringVal = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableOctetStringVal.setDescription("The value when alarmActiveVariableType is 'octetString'.")
alarmActiveVariableIpAddressVal = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableIpAddressVal.setDescription("The value when alarmActiveVariableType is 'ipAddress'.")
alarmActiveVariableOidVal = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 10), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableOidVal.setDescription("The value when alarmActiveVariableType is 'objectId'.")
alarmActiveVariableCounter64Val = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableCounter64Val.setDescription("The value when alarmActiveVariableType is 'counter64'.")
alarmActiveVariableOpaqueVal = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 12), Opaque().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveVariableOpaqueVal.setDescription("The value when alarmActiveVariableType is 'opaque'.\n\nNote that although RFC2578 [RFC2578] forbids the use\nof Opaque in 'standard' MIB modules, this particular\nusage is driven by the need to be able to accurately\nrepresent any well-formed notification, and justified\nby the need for backward compatibility.")
alarmActiveStatsTable = MibTable((1, 3, 6, 1, 2, 1, 118, 1, 2, 4))
if mibBuilder.loadTexts: alarmActiveStatsTable.setDescription("This table represents the alarm statistics\ninformation.")
alarmActiveStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1)).setIndexNames((0, "ALARM-MIB", "alarmListName"))
if mibBuilder.loadTexts: alarmActiveStatsEntry.setDescription("Statistics on the current active alarms.")
alarmActiveStatsActiveCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveStatsActiveCurrent.setDescription("The total number of currently active alarms on the system.")
alarmActiveStatsActives = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 2), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveStatsActives.setDescription("The total number of active alarms since system restarted.")
alarmActiveStatsLastRaise = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveStatsLastRaise.setDescription("The value of sysUpTime at the time of the last\nalarm raise for this alarm list.\nIf no alarm raises have occurred since the\nlast re-initialization of the local network management\nsubsystem, then this object contains a zero value.")
alarmActiveStatsLastClear = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveStatsLastClear.setDescription("The value of sysUpTime at the time of the last\nalarm clear for this alarm list.\nIf no alarm clears have occurred since the\nlast re-initialization of the local network management\nsubsystem, then this object contains a zero value.")
alarmActiveOverflow = MibScalar((1, 3, 6, 1, 2, 1, 118, 1, 2, 5), Counter32()).setMaxAccess("readonly").setUnits("active alarms")
if mibBuilder.loadTexts: alarmActiveOverflow.setDescription("The number of active alarms that have not been put into\nthe alarmActiveTable since system restart as a result\nof extreme resource constraints.")
alarmClear = MibIdentifier((1, 3, 6, 1, 2, 1, 118, 1, 3))
alarmClearMaximum = MibScalar((1, 3, 6, 1, 2, 1, 118, 1, 3, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmClearMaximum.setDescription("This object specifies the maximum number of cleared\nalarms to store in the alarmClearTable.  When this\nnumber is reached, the cleared alarms with the\nearliest clear time will be removed from the table.")
alarmClearTable = MibTable((1, 3, 6, 1, 2, 1, 118, 1, 3, 2))
if mibBuilder.loadTexts: alarmClearTable.setDescription("This table contains information on\ncleared alarms.")
alarmClearEntry = MibTableRow((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1)).setIndexNames((0, "ALARM-MIB", "alarmListName"), (0, "ALARM-MIB", "alarmClearDateAndTime"), (0, "ALARM-MIB", "alarmClearIndex"))
if mibBuilder.loadTexts: alarmClearEntry.setDescription("Information on a cleared alarm.")
alarmClearIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: alarmClearIndex.setDescription("An integer which acts as the index of entries within\n\n\n\nthe named alarm list.  It wraps back to 1 after it\nreaches its maximum value.\n\nThis object has the same value as the alarmActiveIndex that\nthis alarm instance had when it was active.")
alarmClearDateAndTime = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 2), DateAndTime()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: alarmClearDateAndTime.setDescription("The local date and time when the alarm cleared.\n\nThis object facilitates retrieving all instances of\nalarms that have been cleared since a given point in time.\n\nImplementations MUST include the offset from UTC,\nif available.  Implementation in environments in which\nthe UTC offset is not available is NOT RECOMMENDED.")
alarmClearEngineID = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 3), LocalSnmpEngineOrZeroLenStr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmClearEngineID.setDescription("The identification of the SNMP engine at which the alarm\noriginated.  If the alarm is from an SNMPv1 system this\nobject is a zero length string.")
alarmClearEngineAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmClearEngineAddressType.setDescription("This object indicates what type of address is stored in\nthe alarmActiveEngineAddress object - IPv4, IPv6, DNS, etc.")
alarmClearEngineAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmClearEngineAddress.setDescription("The Address of the SNMP engine on which the alarm was\noccurring.  This is used to identify the source of an SNMPv1\n\n\n\ntrap, since an alarmActiveEngineId cannot be extracted from the\nSNMPv1 trap PDU.\n\nThis object MUST always be instantiated, even if the list\ncan contain alarms from only one engine.")
alarmClearContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmClearContextName.setDescription("The name of the SNMP MIB context from which the alarm came.\nFor SNMPv1 traps this is the community string from the Trap.\nNote that care needs to be taken when selecting community\nstrings to ensure that these can be represented as a\nwell-formed SnmpAdminString.  Community or Context names\nthat are not well-formed SnmpAdminStrings will be mapped\nto zero length strings.\n\nIf the alarm's source SNMP engine is known not to support\nmultiple contexts, this object is a zero length string.")
alarmClearNotificationID = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmClearNotificationID.setDescription("The NOTIFICATION-TYPE object identifier of the alarm\nclear.")
alarmClearResourceId = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 8), ResourceId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmClearResourceId.setDescription("This object identifies the resource that was under alarm.\n\nIf there is no corresponding resource, then\nthe value of this object MUST be 0.0.")
alarmClearLogIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmClearLogIndex.setDescription("This number MUST be the same as the log index of the\napplicable row in the notification log MIB, if it exists.\nIf no log index applies to the trap, then this object\nMUST have the value of 0.")
alarmClearModelPointer = MibTableColumn((1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 10), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmClearModelPointer.setDescription("A pointer to the corresponding row in the\nalarmModelTable for this cleared alarm.")
alarmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 118, 2))
alarmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 118, 2, 1))
alarmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 118, 2, 2))

# Augmentions

# Notifications

alarmActiveState = NotificationType((1, 3, 6, 1, 2, 1, 118, 0, 2)).setObjects(("ALARM-MIB", "alarmActiveModelPointer"), ("ALARM-MIB", "alarmActiveResourceId"), )
if mibBuilder.loadTexts: alarmActiveState.setDescription("An instance of the alarm indicated by\nalarmActiveModelPointer has been raised\nagainst the entity indicated by\nalarmActiveResourceId.\n\nThe agent must throttle the generation of\nconsecutive alarmActiveState traps so that there is at\nleast a two-second gap between traps of this\ntype against the same alarmActiveModelPointer and\nalarmActiveResourceId.  When traps are throttled,\nthey are dropped, not queued for sending at a future time.\n\nA management application should periodically check\nthe value of alarmActiveLastChanged to detect any\nmissed alarmActiveState notification-events, e.g.,\ndue to throttling or transmission loss.")
alarmClearState = NotificationType((1, 3, 6, 1, 2, 1, 118, 0, 3)).setObjects(("ALARM-MIB", "alarmActiveModelPointer"), ("ALARM-MIB", "alarmActiveResourceId"), )
if mibBuilder.loadTexts: alarmClearState.setDescription("An instance of the alarm indicated by\nalarmActiveModelPointer has been cleared against\n\n\n\nthe entity indicated by alarmActiveResourceId.\n\nThe agent must throttle the generation of\nconsecutive alarmActiveClear traps so that there is at\nleast a two-second gap between traps of this\ntype against the same alarmActiveModelPointer and\nalarmActiveResourceId.  When traps are throttled,\nthey are dropped, not queued for sending at a future time.\n\nA management application should periodically check\nthe value of alarmActiveLastChanged to detect any\nmissed alarmClearState notification-events, e.g.,\ndue to throttling or transmission loss.")

# Groups

alarmModelGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 118, 2, 2, 1)).setObjects(("ALARM-MIB", "alarmModelSpecificPointer"), ("ALARM-MIB", "alarmModelResourcePrefix"), ("ALARM-MIB", "alarmModelLastChanged"), ("ALARM-MIB", "alarmModelNotificationId"), ("ALARM-MIB", "alarmModelVarbindValue"), ("ALARM-MIB", "alarmModelDescription"), ("ALARM-MIB", "alarmModelVarbindIndex"), ("ALARM-MIB", "alarmModelRowStatus"), ("ALARM-MIB", "alarmModelVarbindSubtree"), )
if mibBuilder.loadTexts: alarmModelGroup.setDescription("Alarm model group.")
alarmActiveGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 118, 2, 2, 2)).setObjects(("ALARM-MIB", "alarmActiveEngineAddress"), ("ALARM-MIB", "alarmActiveVariableID"), ("ALARM-MIB", "alarmActiveVariableOidVal"), ("ALARM-MIB", "alarmActiveDescription"), ("ALARM-MIB", "alarmActiveEngineAddressType"), ("ALARM-MIB", "alarmActiveResourceId"), ("ALARM-MIB", "alarmActiveVariableOpaqueVal"), ("ALARM-MIB", "alarmActiveOverflow"), ("ALARM-MIB", "alarmActiveVariableValueType"), ("ALARM-MIB", "alarmActiveVariableCounter64Val"), ("ALARM-MIB", "alarmActiveNotificationID"), ("ALARM-MIB", "alarmActiveVariableCounter32Val"), ("ALARM-MIB", "alarmActiveVariableOctetStringVal"), ("ALARM-MIB", "alarmActiveContextName"), ("ALARM-MIB", "alarmActiveVariableTimeTicksVal"), ("ALARM-MIB", "alarmActiveVariableInteger32Val"), ("ALARM-MIB", "alarmActiveEngineID"), ("ALARM-MIB", "alarmActiveVariableIpAddressVal"), ("ALARM-MIB", "alarmActiveModelPointer"), ("ALARM-MIB", "alarmActiveLogPointer"), ("ALARM-MIB", "alarmActiveVariables"), ("ALARM-MIB", "alarmActiveVariableUnsigned32Val"), ("ALARM-MIB", "alarmActiveLastChanged"), ("ALARM-MIB", "alarmActiveSpecificPointer"), )
if mibBuilder.loadTexts: alarmActiveGroup.setDescription("Active Alarm list group.")
alarmActiveStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 118, 2, 2, 3)).setObjects(("ALARM-MIB", "alarmActiveStatsActives"), ("ALARM-MIB", "alarmActiveStatsLastClear"), ("ALARM-MIB", "alarmActiveStatsActiveCurrent"), ("ALARM-MIB", "alarmActiveStatsLastRaise"), )
if mibBuilder.loadTexts: alarmActiveStatsGroup.setDescription("Active alarm summary group.")
alarmClearGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 118, 2, 2, 4)).setObjects(("ALARM-MIB", "alarmClearResourceId"), ("ALARM-MIB", "alarmClearEngineAddressType"), ("ALARM-MIB", "alarmClearMaximum"), ("ALARM-MIB", "alarmClearLogIndex"), ("ALARM-MIB", "alarmClearEngineAddress"), ("ALARM-MIB", "alarmClearModelPointer"), ("ALARM-MIB", "alarmClearContextName"), ("ALARM-MIB", "alarmClearNotificationID"), ("ALARM-MIB", "alarmClearEngineID"), )
if mibBuilder.loadTexts: alarmClearGroup.setDescription("Cleared alarm group.")
alarmNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 118, 2, 2, 6)).setObjects(("ALARM-MIB", "alarmActiveState"), ("ALARM-MIB", "alarmClearState"), )
if mibBuilder.loadTexts: alarmNotificationsGroup.setDescription("The collection of notifications that can be used to\nmodel alarms for faults lacking pre-existing\nnotification definitions.")

# Compliances

alarmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 118, 2, 1, 1)).setObjects(("ALARM-MIB", "alarmModelGroup"), ("ALARM-MIB", "alarmClearGroup"), ("ALARM-MIB", "alarmActiveGroup"), ("ALARM-MIB", "alarmActiveStatsGroup"), ("ALARM-MIB", "alarmNotificationsGroup"), )
if mibBuilder.loadTexts: alarmCompliance.setDescription("The compliance statement for systems supporting\nthe Alarm MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("ALARM-MIB", PYSNMP_MODULE_ID=alarmMIB)

# Types
mibBuilder.exportSymbols("ALARM-MIB", LocalSnmpEngineOrZeroLenStr=LocalSnmpEngineOrZeroLenStr, ResourceId=ResourceId)

# Objects
mibBuilder.exportSymbols("ALARM-MIB", alarmMIB=alarmMIB, alarmNotifications=alarmNotifications, alarmObjects=alarmObjects, alarmModel=alarmModel, alarmModelLastChanged=alarmModelLastChanged, alarmModelTable=alarmModelTable, alarmModelEntry=alarmModelEntry, alarmModelIndex=alarmModelIndex, alarmModelState=alarmModelState, alarmModelNotificationId=alarmModelNotificationId, alarmModelVarbindIndex=alarmModelVarbindIndex, alarmModelVarbindValue=alarmModelVarbindValue, alarmModelDescription=alarmModelDescription, alarmModelSpecificPointer=alarmModelSpecificPointer, alarmModelVarbindSubtree=alarmModelVarbindSubtree, alarmModelResourcePrefix=alarmModelResourcePrefix, alarmModelRowStatus=alarmModelRowStatus, alarmActive=alarmActive, alarmActiveLastChanged=alarmActiveLastChanged, alarmActiveTable=alarmActiveTable, alarmActiveEntry=alarmActiveEntry, alarmListName=alarmListName, alarmActiveDateAndTime=alarmActiveDateAndTime, alarmActiveIndex=alarmActiveIndex, alarmActiveEngineID=alarmActiveEngineID, alarmActiveEngineAddressType=alarmActiveEngineAddressType, alarmActiveEngineAddress=alarmActiveEngineAddress, alarmActiveContextName=alarmActiveContextName, alarmActiveVariables=alarmActiveVariables, alarmActiveNotificationID=alarmActiveNotificationID, alarmActiveResourceId=alarmActiveResourceId, alarmActiveDescription=alarmActiveDescription, alarmActiveLogPointer=alarmActiveLogPointer, alarmActiveModelPointer=alarmActiveModelPointer, alarmActiveSpecificPointer=alarmActiveSpecificPointer, alarmActiveVariableTable=alarmActiveVariableTable, alarmActiveVariableEntry=alarmActiveVariableEntry, alarmActiveVariableIndex=alarmActiveVariableIndex, alarmActiveVariableID=alarmActiveVariableID, alarmActiveVariableValueType=alarmActiveVariableValueType, alarmActiveVariableCounter32Val=alarmActiveVariableCounter32Val, alarmActiveVariableUnsigned32Val=alarmActiveVariableUnsigned32Val, alarmActiveVariableTimeTicksVal=alarmActiveVariableTimeTicksVal, alarmActiveVariableInteger32Val=alarmActiveVariableInteger32Val, alarmActiveVariableOctetStringVal=alarmActiveVariableOctetStringVal, alarmActiveVariableIpAddressVal=alarmActiveVariableIpAddressVal, alarmActiveVariableOidVal=alarmActiveVariableOidVal, alarmActiveVariableCounter64Val=alarmActiveVariableCounter64Val, alarmActiveVariableOpaqueVal=alarmActiveVariableOpaqueVal, alarmActiveStatsTable=alarmActiveStatsTable, alarmActiveStatsEntry=alarmActiveStatsEntry, alarmActiveStatsActiveCurrent=alarmActiveStatsActiveCurrent, alarmActiveStatsActives=alarmActiveStatsActives, alarmActiveStatsLastRaise=alarmActiveStatsLastRaise, alarmActiveStatsLastClear=alarmActiveStatsLastClear, alarmActiveOverflow=alarmActiveOverflow, alarmClear=alarmClear, alarmClearMaximum=alarmClearMaximum, alarmClearTable=alarmClearTable, alarmClearEntry=alarmClearEntry, alarmClearIndex=alarmClearIndex, alarmClearDateAndTime=alarmClearDateAndTime, alarmClearEngineID=alarmClearEngineID, alarmClearEngineAddressType=alarmClearEngineAddressType, alarmClearEngineAddress=alarmClearEngineAddress, alarmClearContextName=alarmClearContextName, alarmClearNotificationID=alarmClearNotificationID, alarmClearResourceId=alarmClearResourceId, alarmClearLogIndex=alarmClearLogIndex, alarmClearModelPointer=alarmClearModelPointer, alarmConformance=alarmConformance, alarmCompliances=alarmCompliances, alarmGroups=alarmGroups)

# Notifications
mibBuilder.exportSymbols("ALARM-MIB", alarmActiveState=alarmActiveState, alarmClearState=alarmClearState)

# Groups
mibBuilder.exportSymbols("ALARM-MIB", alarmModelGroup=alarmModelGroup, alarmActiveGroup=alarmActiveGroup, alarmActiveStatsGroup=alarmActiveStatsGroup, alarmClearGroup=alarmClearGroup, alarmNotificationsGroup=alarmNotificationsGroup)

# Compliances
mibBuilder.exportSymbols("ALARM-MIB", alarmCompliance=alarmCompliance)
