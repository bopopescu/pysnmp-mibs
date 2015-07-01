#
# PySNMP MIB module APPN-TRAP-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/APPN-TRAP-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:26:13 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( dlurDlusSessnStatus, ) = mibBuilder.importSymbols("APPN-DLUR-MIB", "dlurDlusSessnStatus")
( appnLocalTgOperational, appnPortOperState, appnIsInS2PNonFmdPius, appnCompliances, appnIsInP2SNonFmdPius, appnIsInP2SFmdBytes, appnIsInS2PFmdPius, appnIsInP2SNonFmdBytes, appnGroups, appnIsInSessUpTime, appnLsOperState, appnObjects, appnLocalTgCpCpSession, appnMIB, appnIsInP2SFmdPius, appnIsInS2PNonFmdBytes, appnIsInS2PFmdBytes, ) = mibBuilder.importSymbols("APPN-MIB", "appnLocalTgOperational", "appnPortOperState", "appnIsInS2PNonFmdPius", "appnCompliances", "appnIsInP2SNonFmdPius", "appnIsInP2SFmdBytes", "appnIsInS2PFmdPius", "appnIsInP2SNonFmdBytes", "appnGroups", "appnIsInSessUpTime", "appnLsOperState", "appnObjects", "appnLocalTgCpCpSession", "appnMIB", "appnIsInP2SFmdPius", "appnIsInS2PNonFmdBytes", "appnIsInS2PFmdBytes")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
appnTrapMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 4, 0))
if mibBuilder.loadTexts: appnTrapMIB.setOrganization('IETF SNA NAU MIB WG / AIW APPN MIBs SIG')
if mibBuilder.loadTexts: appnTrapMIB.setContactInfo('\n                        Bob Clouston\n                        Cisco Systems\n                        7025 Kit Creek Road\n                        P.O. Box 14987\n                        Research Triangle Park, NC 27709, USA\n                        Tel:    1 919 472 2333\n                        E-mail: clouston@cisco.com\n\n                        Bob Moore\n                        IBM Corporation\n                        4205 S. Miami Boulevard\n                        BRQA/501\n                        P.O. Box 12195\n                        Research Triangle Park, NC 27709, USA\n                        Tel:    1 919 254 4436\n                        E-mail: remoore@us.ibm.com\n                ')
if mibBuilder.loadTexts: appnTrapMIB.setDescription('This MIB module defines notifications to be generated by\n                network devices with APPN capabilities.  It presupposes\n                support for the APPN MIB.  It also presupposes\n                support for the DLUR MIB for implementations\n                that support the DLUR-related groups.')
appnIsrAccountingDataTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 1)).setObjects(*(("APPN-TRAP-MIB", "appnIsInP2SFmdPius"), ("APPN-TRAP-MIB", "appnIsInS2PFmdPius"), ("APPN-TRAP-MIB", "appnIsInP2SNonFmdPius"), ("APPN-TRAP-MIB", "appnIsInS2PNonFmdPius"), ("APPN-TRAP-MIB", "appnIsInP2SFmdBytes"), ("APPN-TRAP-MIB", "appnIsInS2PFmdBytes"), ("APPN-TRAP-MIB", "appnIsInP2SNonFmdBytes"), ("APPN-TRAP-MIB", "appnIsInS2PNonFmdBytes"), ("APPN-TRAP-MIB", "appnIsInSessUpTime"),))
if mibBuilder.loadTexts: appnIsrAccountingDataTrap.setDescription('When it has been enabled, this notification is generated by an\n          APPN node whenever an ISR session passing through the node is\n          taken down, regardless of whether the session went down\n          normally or abnormally.  Its purpose is to allow a management\n          application (primarily an accounting application) that is\n          monitoring the ISR counts to receive the final values of these\n          counts, so that the application can properly account for the\n          amounts the counts were incremented since the last time the\n          application polled them.  The appnIsInSessUpTime object\n          provides the total amount of time that the session was active.\n\n          This notification is not a substitute for polling the ISR\n          counts.  In particular, the count values reported in this\n          notification cannot be assumed to be the complete totals for\n          the life of the session, since they may have wrapped while the\n          session was up.\n\n          The session to which the objects in this notification apply is\n          identified by the fully qualified CP name and PCID that make up\n          the table index.  An instance of this notification will contain\n          exactly one instance of each of its objects, and these objects\n          will all belong to the same conceptual row of the\n          appnIsInTable.\n\n          Generation of this notification is controlled by the same\n          object in the APPN MIB, appnIsInGlobeCtrAdminStatus, that\n          controls whether the count objects themselves are being\n          incremented.')
appnLocalTgOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 2)).setObjects(*(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-TRAP-MIB", "appnLocalTgOperational"),))
if mibBuilder.loadTexts: appnLocalTgOperStateChangeTrap.setDescription("When it has been enabled, this notification makes it possible\n          for an APPN topology application to get asynchronous\n          notifications of local TG operational state changes,\n          and thus to reduce the frequency with which it polls\n          for these changes.\n\n          This notification is sent whenever there is a change to\n          the appnLocalTgOperational object in a row of the\n          appnLocalTgTable.  This notification is only sent for row\n          creation if the row is created with a value of 'true' for\n          appnLocalTgOperational.  This notification is only sent for\n          row deletion if the last value of appnLocalTgOperational was\n          'true'.  In this case, the value of appnLocalTgOperational\n          in the notification shall be 'false', since the deletion of\n          a row indicates that the TG is no longer operational.\n\n          The notification is more than a simple 'poll me now' indication.\n          It carries both a count of local TG topology changes, and the\n          current operational state itself.  The count of changes allows an\n          application to detect lost notifications, either when polling\n          or upon receiving a subsequent notification, at which point it\n          knows it must retrieve the entire appnLocalTgTable again.\n          This is the same count as used in the appnLocalCpCpStateChangeTrap.\n          A lost notification could indicate a local TG CP-CP session state\n          change or an operational state change.\n\n          Generation of this notification is controlled by the\n          appnTrapControl object.")
appnLocalTgCpCpChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 3)).setObjects(*(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-TRAP-MIB", "appnLocalTgCpCpSession"),))
if mibBuilder.loadTexts: appnLocalTgCpCpChangeTrap.setDescription("When it has been enabled, this notification makes it possible\n          for an APPN topology application to get asynchronous\n          notifications of local TG control-point to control-point (CP-CP)\n          session state changes, and thus to reduce the\n          frequency with which it polls for these changes.\n\n          This notification is sent whenever there is a change to\n          the appnLocalTgCpCpSession object but NOT the\n          appnLocalTgOperational object in a row of the appnLocalTgTable.\n          This notification is never sent for appnLocalTgTable row\n          creation or deletion.\n\n          The notification is more than a simple 'poll me now' indication.\n          It carries both a count of local TG topology changes, and the\n          current CP-CP session state itself.  The count of changes allows\n          an application to detect lost notifications, either when polling\n          or upon receiving a subsequent notification, at which point it\n          knows it must retrieve the entire appnLocalTgTable again.  This\n          is the same count as used in the appnLocalTgOperStateChangeTrap.\n          A lost notification could indicate a local TG CP-CP session\n          state change or an operational state change.\n\n          Generation of this notification is controlled by the\n          appnTrapControl object.")
appnPortOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 4)).setObjects(*(("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-TRAP-MIB", "appnPortOperState"),))
if mibBuilder.loadTexts: appnPortOperStateChangeTrap.setDescription("When it has been enabled, this notification makes it possible\n          for an APPN topology application to get asynchronous\n          notifications of port operational state changes, and thus to\n          reduce the frequency with which it polls for these changes.\n          This notification is only sent when a appnPortOperState has\n          transitioned to a value of 'active' or 'inactive'.\n\n          This notification is sent whenever there is a appnPortOperState\n          object transition to 'inactive' or 'active' state in the\n          appnPortTable.  This notification is only sent for row creation\n          if the row is created with a value of 'active' for\n          appnPortOperState.  This notification is only sent for\n          row deletion if the last value of appnPortOperState was\n          'active'.  In this case, the value of appnPortOperState\n          in the notification shall be 'inactive', since the deletion of\n          a row indicates that the port is no longer active.\n\n          The notification is more than a simple 'poll me now' indication.\n          It carries both a count of port table changes, and the\n          operational state itself.  The count of changes allows an\n          application to detect lost notifications, either when polling\n          or upon receiving a subsequent notification, at which point\n          it knows it must retrieve the entire appnPortTable again.\n\n          Generation of this notification is controlled by the\n          appnTrapControl object.")
appnLsOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 5)).setObjects(*(("APPN-TRAP-MIB", "appnLsTableChanges"), ("APPN-TRAP-MIB", "appnLsOperState"),))
if mibBuilder.loadTexts: appnLsOperStateChangeTrap.setDescription("When it has been enabled, this notification makes it possible\n          for an APPN topology application to get asynchronous\n          notifications of link station operational state changes, and\n          thus to reduce the frequency with which it polls for these\n          changes.  This notification is only sent when a appnLsOperState\n          has transitioned to a value of 'active' or 'inactive'.\n\n          This notification is sent whenever there is a appnLsOperState\n          object transition to 'inactive' or 'active' state in the\n          appnLsTable.  This notification is only sent for row creation\n          if the row is created with a value of 'active' for\n          appnLsOperState.  This notification is only sent for\n          row deletion if the last value of appnLsOperState was\n          'active'.  In this case, the value of appnLsOperState\n          in the notification shall be 'inactive', since the deletion of\n          a row indicates that the link station is no longer active.\n\n          The notification is more than a simple 'poll me now' indication.\n          It carries both a count of link station table changes, and the\n          operational state itself.  The count of changes allows an\n          application to detect lost notifications, either when polling\n          or upon receiving a subsequent notification, at which point it\n          knows it must retrieve the entire appnLsTable again.\n\n          Generation of this notification is controlled by the\n          appnTrapControl object.")
dlurDlusStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 6)).setObjects(*(("APPN-TRAP-MIB", "dlurDlusTableChanges"), ("APPN-TRAP-MIB", "dlurDlusSessnStatus"),))
if mibBuilder.loadTexts: dlurDlusStateChangeTrap.setDescription("When it has been enabled, this notification makes it possible\n          for an APPN topology application to get asynchronous\n          notifications of DLUR-DLUS session changes, and thus to reduce\n          the frequency with which it polls for these changes.\n\n          This notification is sent whenever there is a dlurDlusSessnStatus\n          object transition to 'inactive' or 'active' state in the\n          dlurDlusTable.  This notification is only sent for row creation\n          if the row is created with a value of 'active' for\n          dlurDlusSessnStatus.  This notification is only sent for\n          row deletion if the last value of dlurDlusSessnStatus was\n          'active'.  In this case, the value of dlurDlusSessnStatus\n          in the notification shall be 'inactive', since the deletion of\n          a row indicates that the session is no longer active.\n\n          The notification is more than a simple 'poll me now' indication.\n          It carries both a count of DLUR-DLUS table changes, and the\n          session status itself.  The count of changes allows an\n          application to detect lost notifications, either when polling\n          or upon receiving a subsequent notification, at which point it\n          knows it must retrieve the entire dlurDlusTable again.\n\n          Generation of this notification is controlled by the\n          appnTrapControl object.")
appnTrapObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 4, 1, 7))
appnTrapControl = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 1), Bits().clone(namedValues=NamedValues(("appnLocalTgOperStateChangeTrap", 0), ("appnLocalTgCpCpChangeTrap", 1), ("appnPortOperStateChangeTrap", 2), ("appnLsOperStateChangeTrap", 3), ("dlurDlusStateChangeTrap", 4),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appnTrapControl.setDescription("An object to turn APPN notification generation on and off.\n          Setting a notification type's bit to 1 enables generation of\n          notifications of that type, subject to further filtering\n          resulting from entries in the snmpNotificationMIB.  Setting\n          this bit to 0 disables generation of notifications of that\n          type.\n\n          Note that generation of the appnIsrAccountingDataTrap is\n          controlled by the appnIsInGlobeCtrAdminStatus object in\n          the APPN MIB:  if counts of intermediate session traffic\n          are being kept at all, then the notification is also enabled.")
appnLocalTgTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnLocalTgTableChanges.setDescription('A count of the number of times a row in the appnLocalTgTable\n          has changed status since the APPN node was last reinitialized.\n          This counter is incremented whenever a condition is detected\n          that would cause a appnLocalTgOperStateChangeTrap or\n          appnLocalTgCpCpChangeTrap notification to be sent, whether\n          or not those notifications are enabled.')
appnPortTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnPortTableChanges.setDescription('A count of the number of times a row in the appnPortTable\n          has changed status since the APPN node was last reinitialized.\n          This counter is incremented whenever a condition is detected\n          that would cause a appnPortOperStateChangeTrap notification\n          to be sent, whether or not this notification is enabled.')
appnLsTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnLsTableChanges.setDescription('A count of the number of times a row in the appnLsTable\n          has changed status since the APPN node was last reinitialized.\n          This counter is incremented whenever a condition is detected\n          that would cause a appnLsOperStateChangeTrap notification\n          to be sent, whether or not this notification is enabled.')
dlurDlusTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlurDlusTableChanges.setDescription('A count of the number of times a row in the dlurDlusTable\n          has changed status since the APPN node was last reinitialized.\n          This counter is incremented whenever a condition is detected\n          that would cause a dlurDlusStateChangeTrap notification\n          to be sent, whether or not this notification is enabled.')
appnTrapMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 4, 3, 1, 2)).setObjects(*(("APPN-TRAP-MIB", "appnTrapMibIsrNotifGroup"), ("APPN-TRAP-MIB", "appnTrapMibTopoConfGroup"), ("APPN-TRAP-MIB", "appnTrapMibTopoNotifGroup"), ("APPN-TRAP-MIB", "appnTrapMibDlurConfGroup"), ("APPN-TRAP-MIB", "appnTrapMibDlurNotifGroup"),))
if mibBuilder.loadTexts: appnTrapMibCompliance.setDescription('The compliance statement for the SNMP entities that\n           implement the APPN-TRAP-MIB.')
appnTrapMibIsrNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 21)).setObjects(*(("APPN-TRAP-MIB", "appnIsrAccountingDataTrap"),))
if mibBuilder.loadTexts: appnTrapMibIsrNotifGroup.setDescription("A notification for reporting the final values of the\n            APPN MIB's ISR counters.")
appnTrapMibTopoConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 22)).setObjects(*(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-TRAP-MIB", "appnLsTableChanges"),))
if mibBuilder.loadTexts: appnTrapMibTopoConfGroup.setDescription('A collection of objects for reducing the polling\n            associated with the local topology tables in the\n            APPN MIB.  Nodes that implement this group SHALL\n            also implement the appnTrapMibTopoNotifGroup.')
appnTrapMibTopoNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 23)).setObjects(*(("APPN-TRAP-MIB", "appnLocalTgOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLocalTgCpCpChangeTrap"), ("APPN-TRAP-MIB", "appnPortOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLsOperStateChangeTrap"),))
if mibBuilder.loadTexts: appnTrapMibTopoNotifGroup.setDescription('A collection of notifications for reducing the polling\n            associated with the local topology tables in the\n            APPN MIB.  Nodes that implement this group SHALL\n            also implement the appnTrapMibTopoConfGroup.')
appnTrapMibDlurConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 24)).setObjects(*(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "dlurDlusTableChanges"),))
if mibBuilder.loadTexts: appnTrapMibDlurConfGroup.setDescription('A collection of objects for reducing the polling\n            associated with the dlurDlusTable in the DLUR\n            MIB.  Nodes that implement this group SHALL also\n            implement the appnTrapMibDlurNotifGroup.')
appnTrapMibDlurNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 25)).setObjects(*(("APPN-TRAP-MIB", "dlurDlusStateChangeTrap"),))
if mibBuilder.loadTexts: appnTrapMibDlurNotifGroup.setDescription('A notification for reducing the polling associated\n            with the dlurDlusTable in the DLUR MIB.  Nodes that\n            implement this group SHALL also implement the\n            appnTrapMibDlurConfGroup.')
mibBuilder.exportSymbols("APPN-TRAP-MIB", appnTrapControl=appnTrapControl, appnTrapMibIsrNotifGroup=appnTrapMibIsrNotifGroup, appnTrapMibDlurConfGroup=appnTrapMibDlurConfGroup, appnTrapObjects=appnTrapObjects, appnLsTableChanges=appnLsTableChanges, appnLsOperStateChangeTrap=appnLsOperStateChangeTrap, appnIsrAccountingDataTrap=appnIsrAccountingDataTrap, PYSNMP_MODULE_ID=appnTrapMIB, appnLocalTgCpCpChangeTrap=appnLocalTgCpCpChangeTrap, dlurDlusTableChanges=dlurDlusTableChanges, appnTrapMibTopoConfGroup=appnTrapMibTopoConfGroup, appnTrapMibCompliance=appnTrapMibCompliance, appnTrapMibDlurNotifGroup=appnTrapMibDlurNotifGroup, dlurDlusStateChangeTrap=dlurDlusStateChangeTrap, appnPortOperStateChangeTrap=appnPortOperStateChangeTrap, appnPortTableChanges=appnPortTableChanges, appnTrapMIB=appnTrapMIB, appnLocalTgTableChanges=appnLocalTgTableChanges, appnTrapMibTopoNotifGroup=appnTrapMibTopoNotifGroup, appnLocalTgOperStateChangeTrap=appnLocalTgOperStateChangeTrap)
