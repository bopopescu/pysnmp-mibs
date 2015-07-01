#
# PySNMP MIB module POWER-ETHERNET-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/POWER-ETHERNET-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:30:56 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( softentIND1InLinePower, ) = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1InLinePower")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( TruthValue, DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
powerEthernetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999)).setRevisions(("2002-12-02 00:00",))
if mibBuilder.loadTexts: powerEthernetMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB\n                         Working Group')
if mibBuilder.loadTexts: powerEthernetMIB.setContactInfo('\n\n                       Chair: Dan Romascanu\n                                  Avaya Inc.\n                                  Tel:  +972-3-645-8414\n                                  Email: dromasca@avaya.com\n\n                       Editor: Avi Berger\n                                 PowerDsine Inc.\n                                   Tel:    972-9-7755100 Ext 307\n                                  Fax:    972-9-7755120\n                                   E-mail: avib@PowerDsine.com\n           ')
if mibBuilder.loadTexts: powerEthernetMIB.setDescription('The MIB module for for managing Powered Devices (PD) or\n                   Power Source Equipment (PSE) working according to the IEEE\n                   802.af Powered Ethernet (DTE Power via MDI) standard.\n                  The following terms are used throughout this\n                  MIB module.  For complete formal definitions,\n                  the IEEE 802.3 standards should be consulted\n                  wherever possible:\n\n                  Group - A recommended, but optional, entity\n                  defined by the IEEE 802.3 management standard,\n                  in order to support a modular numbering scheme.\n                  The classical example allows an implementor to\n                  represent field-replaceable units as groups of\n                  ports, with the port numbering matching the\n                  modular hardware implementation.\n\n                   Port - This entity identifies the port within the group\n                   for which this entry contains information. The numbering\n                   scheme for ports is implementation specific.')
pethNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 0))
pethObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1))
pethConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2))
pethPsePortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1), )
if mibBuilder.loadTexts: pethPsePortTable.setDescription('A table of objects that display and control the power\n               characteristics power Ethernet ports on a Power Source\n               Entity (PSE) device. This group will be implemented in\n               managed power Ethernet switches and mid-span devices.')
pethPsePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"), (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"))
if mibBuilder.loadTexts: pethPsePortEntry.setDescription('A set of objects that display and control the power\n                  characteristics of a power Ethernet PSE port.')
pethPsePortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: pethPsePortGroupIndex.setDescription('This variable uniquely identifies the group\n               containing the port to which a power Ethernet PSE is connected.\n               Group means box in the stack, module in a rack and the value 1\n               MUST be used for non-modular devices .\n               pethPseMidSpanGroupCapacity is the number of Mid-Span PSE\n               groups that can be contained within the Mid-Span PSE.')
pethPsePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: pethPsePortIndex.setDescription('This variable uniquely identifies the power Ethernet PSE\n               port within group pethPseGroupIndex to which the\n               power Ethernet PSE entry is connected.')
pethPsePortAdminEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("enable", 1), ("disable", 2),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortAdminEnable.setDescription('Enables power supply on this port.\n            Setting this object at a value enable(1) enables power\n            and detection mechanism for this port.\n            Setting this object at a value disable(2) disables power\n            for this port.')
pethPsePortPowerPairsControlAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerPairsControlAbility.setDescription('Describes the capability of controlling the power pairs\n            functionality to switch pins for sourcing power.\n            The value true indicate that the device has the capability\n            to control the power pairs')
pethPsePortPowerPairs = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("signal", 1), ("spare", 2),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPairs.setDescription('Describes or controls the pairs in use. If the value of\n            pethPsePortPowerPairsControl is true, this object is\n            writable.\n            A value of signal(1) means that the signal pairs\n            only are in use.\n            A value of spare(2) means that the spare pairs\n            only are in use.')
pethPsePortPowerDetectionControl = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("auto", 1), ("test", 2),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerDetectionControl.setDescription('Controls the power detection mechanism of the port.\n            Setting the value auto(1) enables the power detection\n            mechanism of the port.\n            Setting the value test(2) puts the port in a\n            testmode: force continuous discovery without applying\n            power regardless of whether PD detected.')
pethPsePortDetectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 4, 5, 7, 8,)).clone(namedValues=NamedValues(("disabled", 1), ("searching", 2), ("deliveringPower", 4), ("fault", 5), ("test", 7), ("denyLowPriority", 8),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortDetectionStatus.setDescription('Describes the operational status of the port PD detection.\n            A value of disabled(1)- indicates that the PSE State diagram is in\n            the state IDLE\n            A value of searching(2)- indicates that the PSE State diagram is in\n            the state DETECTION, CLASSIFICATION, SIGNATURE_INVALID or BACKOFF.\n            A value of deliveringPower(4) - indicates that the PSE State diagram\n            is in the state POWER_UP, POWER_ON or POWER_OFF.\n            A value of fault(5) - indicates that the PSE State diagram is in the\n            state TEST_ERROR or the state IDLE due to the variable error\n            condition.\n            Faults detected are vendor specific.\n            A value of test(7) - indicates that the PSE State diagram is in the\n            state TEST_MODE.\n            A value of denyLowPriority(8) indicates that the port was\n            disabled by the power management system, in order to keep\n            active higher priority ports.\n             ')
pethPsePortPowerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3,)).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPriority.setDescription('This object controls the priority of the port from the point\n            of view of a power management algorithm. The priority that\n            is set by this variable could be used by a control mechanism\n            that prevents over current situations by disconnecting first\n            ports with lower power priority. Ports that connect devices\n            critical to the operation of the network - like the E911\n            telephones ports - should be set to higher priority.')
pethPsePortPowerMaintenanceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3,)).clone(namedValues=NamedValues(("ok", 1), ("underCurrent", 2), ("mPSAbsent", 3),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerMaintenanceStatus.setDescription('The value ok(1) indicates the Power Maintenance\n            Signature is present and the overcurrent condition has not been\n            detected.\n            The value overCurrent (2) indicates an overcurrent condition\n            has been detected.\n            The value mPSAbsent(3) indicates that the Power Maintenance\n            Signature is absent.')
pethPsePortMPSAbsentCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortMPSAbsentCounter.setDescription('Counts the number of times that the\n                pethPsePortPowerMaintenanceStatus attribute changes from any\n                value to the value mPSAbsent(3).')
pethPsePortOverCurrentCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortOverCurrentCounter.setDescription('Counts the number of times that the aPSEPowerCurrentStatus\n                 attribute changes from any value to the value overCurrent(2).')
pethPsePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4,)).clone(namedValues=NamedValues(("other", 1), ("telephone", 2), ("webcam", 3), ("wireless", 4),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortType.setDescription('A manager will set the value of this variable to a value\n            that indicates the type of the device that is connected\n            to theport. This value can be the result of the mapping\n            the address of the station connected to the port and of\n            the value of the pethPdPortType of the respective PD port.')
pethPsePortPowerClassifications = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5,)).clone(namedValues=NamedValues(("class0", 1), ("class1", 2), ("class2", 3), ("class3", 4), ("class4", 5),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerClassifications.setDescription('Classification is a way to tag different terminals on the\n           Power over LAN network according to their power consumption.\n           Devices such as IP telephones, WLAN access points and others,\n           will be classified according to their power requirements.\n\n          The value is only valid while a valid PD is being detected as\n          indicated by the attribute pethPsePortDetectionStatus reporting\n          the value or deliveringPower(4).')
pethPdPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 2), )
if mibBuilder.loadTexts: pethPdPortTable.setDescription('A table of objects that display and control the power\n               characteristics power Ethernet ports on a Powered\n               Device(PD) device. This group will be implemented in\n               managed powered and mid-span devices.')
pethPdPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 2, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethPdPortIndex"))
if mibBuilder.loadTexts: pethPdPortEntry.setDescription('A set of objects that display and control the power\n               characteristics of a Powered Device port.')
pethPdPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: pethPdPortIndex.setDescription('An index value that uniquely identifies an\n               interface to a PD device.  The\n               interface identified by a particular value of\n               this index is the same interface as identified\n               by the same value of ifIndex. The mapping\n               between the ifIndex values and the numbering of\n               the port on the device is an implementation\n               issue.')
pethPdPortAdminEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("enable", 1), ("disable", 2),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPdPortAdminEnable.setDescription('This value  identifies the operational state of the PD functions.\n                 An interface which can provide the PD functions will be enabled\n                 to do so when this attribute has the value enable. When this\n                 attribute has the value disable the interface will act\n                 as it would if it had no PD function.')
pethMainPseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 3))
pethMainPseTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 3, 1), )
if mibBuilder.loadTexts: pethMainPseTable.setDescription("A table of objects that display and control the Main power\n             on a PSE  device. Example - an Ethernet switch midspan device can\n               control an Ethnternet port and the Main Power supply unit's.")
pethMainPseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 3, 1, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"))
if mibBuilder.loadTexts: pethMainPseEntry.setDescription('A set of objects that display and control the Main power\n                of a PSE. ')
pethMainPseGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: pethMainPseGroupIndex.setDescription('This variable uniquely identifies the group to which\n              power Ethernet PSE is connected.Group means (box in the stack,\n              module in a rack) and  the value 1 MUST be  used for non-modular\n              devices ')
pethMainPsePower = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 3, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1,65535))).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPsePower.setDescription('The nominal power of the PSE expressed in Watts.')
pethMainPseOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3,)).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("faulty", 3),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseOperStatus.setDescription('The operational status of the main PSE.')
pethMainPseConsumptionPower = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 3, 1, 1, 4), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseConsumptionPower.setDescription('Measured usage power expressed in Watts.')
pethMainPseUsageThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,99))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethMainPseUsageThreshold.setDescription('The usage threshold expressed in percents for\n                   comparing the measured power and initiating\n                   an alarm if the threshold is exceeded.')
pethNotificationControl = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 4))
pethNotificationControlTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 4, 1), )
if mibBuilder.loadTexts: pethNotificationControlTable.setDescription('A table of objects that display and control the Notification\n             on a PSE  device.')
pethNotificationControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 4, 1, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethNotificationControlGroupIndex"))
if mibBuilder.loadTexts: pethNotificationControlEntry.setDescription('A set of objects that control the Notification events.')
pethNotificationControlGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: pethNotificationControlGroupIndex.setDescription('This variable uniquely identifies the group. Group means\n              box in the stack, module in a rack and it is RECOMENDED\n              that the value 1 be used for non-modular devices ')
pethNotificationControlEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("enable", 1), ("disable", 2),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethNotificationControlEnable.setDescription('Enable Notification from Agent')
pethPsePortOnOffNotification = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 0, 1)).setObjects(*(("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"),))
if mibBuilder.loadTexts: pethPsePortOnOffNotification.setDescription(' This Notification indicates if Pse Port is  delivering  or\n                       not power to the PD. This Notification SHOULD be sent on\n                       every status change except in the searching mode.')
pethPsePortPowerMaintenanceStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 0, 2)).setObjects(*(("POWER-ETHERNET-MIB", "pethPsePortPowerMaintenanceStatus"),))
if mibBuilder.loadTexts: pethPsePortPowerMaintenanceStatusNotification.setDescription(' This Notification indicates a Port Change Status and it\n                        SHOULD be sent on every status change.')
pethMainPowerUsageOnNotification = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 0, 4)).setObjects(*(("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"),))
if mibBuilder.loadTexts: pethMainPowerUsageOnNotification.setDescription(' This Notification indicate PSE Threshold usage indication is\n                       on, the usage power is above the threshold.')
pethMainPowerUsageOffNotification = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 0, 5)).setObjects(*(("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"),))
if mibBuilder.loadTexts: pethMainPowerUsageOffNotification.setDescription(' This Notification indicate PSE Threshold usage indication\n                       off, the usage power is below the threshold.')
pethCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 1))
pethGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 2))
pethCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 1, 1)).setObjects(*(("POWER-ETHERNET-MIB", "pethPsePortGroup"), ("POWER-ETHERNET-MIB", "pethPdPortGroup"), ("POWER-ETHERNET-MIB", "pethMainPseGroup"), ("POWER-ETHERNET-MIB", "pethNotificationControlGroup"),))
if mibBuilder.loadTexts: pethCompliance.setDescription('Describes the requirements for conformance to the\n               Power Ethernet MIB.')
pethPseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 1, 2)).setObjects(*(("POWER-ETHERNET-MIB", "pethPsePortGroup"), ("POWER-ETHERNET-MIB", "pethMainPseGroup"), ("POWER-ETHERNET-MIB", "pethNotificationControlGroup"),))
if mibBuilder.loadTexts: pethPseCompliance.setDescription('Describes the requirements for conformance to the PSE and MID-\n                Span.')
pethPdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 1, 3)).setObjects(*(("POWER-ETHERNET-MIB", "pethPdPortGroup"),))
if mibBuilder.loadTexts: pethPdCompliance.setDescription('Describes the requirements for conformance to the PD.')
pethPsePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 2, 1)).setObjects(*(("POWER-ETHERNET-MIB", "pethPsePortAdminEnable"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPairsControlAbility"), ("POWER-ETHERNET-MIB", "pethPsePortPowerDetectionControl"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPairs"), ("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPriority"), ("POWER-ETHERNET-MIB", "pethPsePortPowerMaintenanceStatus"), ("POWER-ETHERNET-MIB", "pethPsePortMPSAbsentCounter"), ("POWER-ETHERNET-MIB", "pethPsePortOverCurrentCounter"), ("POWER-ETHERNET-MIB", "pethPsePortType"), ("POWER-ETHERNET-MIB", "pethPsePortPowerClassifications"),))
if mibBuilder.loadTexts: pethPsePortGroup.setDescription('The pethPsePortGroup is mandatory for systems which\n             implement PSE ports.')
pethPdPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 2, 2)).setObjects(*(("POWER-ETHERNET-MIB", "pethPdPortAdminEnable"),))
if mibBuilder.loadTexts: pethPdPortGroup.setDescription('The pethPdPortGroup is mandatory for systems which\n        implement PD Ports.')
pethMainPseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 2, 3)).setObjects(*(("POWER-ETHERNET-MIB", "pethMainPsePower"), ("POWER-ETHERNET-MIB", "pethMainPseOperStatus"), ("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"), ("POWER-ETHERNET-MIB", "pethMainPseUsageThreshold"),))
if mibBuilder.loadTexts: pethMainPseGroup.setDescription('Main PSE Objects. ')
pethNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 2, 4)).setObjects(*(("POWER-ETHERNET-MIB", "pethNotificationControlEnable"),))
if mibBuilder.loadTexts: pethNotificationControlGroup.setDescription('Notification Control  Objects. ')
pethPsePortNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 1, 4)).setObjects(*(("POWER-ETHERNET-MIB", "pethPsePortOnOffNotification"), ("POWER-ETHERNET-MIB", "pethPsePortPowerMaintenanceStatusNotification"),))
if mibBuilder.loadTexts: pethPsePortNotificationGroup.setDescription('Pse Notification indications')
pethMainPowerNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 27, 999, 2, 1, 5)).setObjects(*(("POWER-ETHERNET-MIB", "pethMainPowerUsageOnNotification"), ("POWER-ETHERNET-MIB", "pethMainPowerUsageOffNotification"),))
if mibBuilder.loadTexts: pethMainPowerNotificationGroup.setDescription('Pse Notification indications')
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", pethPsePortOverCurrentCounter=pethPsePortOverCurrentCounter, pethMainPowerUsageOnNotification=pethMainPowerUsageOnNotification, pethNotificationControlEntry=pethNotificationControlEntry, pethPsePortEntry=pethPsePortEntry, pethMainPseOperStatus=pethMainPseOperStatus, pethPsePortPowerMaintenanceStatusNotification=pethPsePortPowerMaintenanceStatusNotification, pethPdPortEntry=pethPdPortEntry, pethPdPortGroup=pethPdPortGroup, pethPsePortIndex=pethPsePortIndex, pethMainPseEntry=pethMainPseEntry, pethMainPsePower=pethMainPsePower, pethPsePortType=pethPsePortType, pethMainPseGroup=pethMainPseGroup, pethPsePortMPSAbsentCounter=pethPsePortMPSAbsentCounter, pethGroups=pethGroups, pethMainPowerNotificationGroup=pethMainPowerNotificationGroup, pethObjects=pethObjects, pethMainPseTable=pethMainPseTable, pethPdCompliance=pethPdCompliance, pethPsePortPowerDetectionControl=pethPsePortPowerDetectionControl, pethPsePortPowerClassifications=pethPsePortPowerClassifications, pethPseCompliance=pethPseCompliance, pethNotificationControlTable=pethNotificationControlTable, powerEthernetMIB=powerEthernetMIB, pethCompliance=pethCompliance, pethPdPortAdminEnable=pethPdPortAdminEnable, pethNotificationControlGroup=pethNotificationControlGroup, pethPsePortAdminEnable=pethPsePortAdminEnable, pethPdPortIndex=pethPdPortIndex, pethPsePortPowerPairs=pethPsePortPowerPairs, pethMainPseUsageThreshold=pethMainPseUsageThreshold, pethPsePortDetectionStatus=pethPsePortDetectionStatus, pethConformance=pethConformance, pethPsePortGroupIndex=pethPsePortGroupIndex, pethMainPseGroupIndex=pethMainPseGroupIndex, pethPsePortPowerPairsControlAbility=pethPsePortPowerPairsControlAbility, pethPsePortPowerMaintenanceStatus=pethPsePortPowerMaintenanceStatus, pethPsePortPowerPriority=pethPsePortPowerPriority, pethMainPseConsumptionPower=pethMainPseConsumptionPower, pethMainPseObjects=pethMainPseObjects, PYSNMP_MODULE_ID=powerEthernetMIB, pethPsePortTable=pethPsePortTable, pethNotificationControlEnable=pethNotificationControlEnable, pethNotificationControlGroupIndex=pethNotificationControlGroupIndex, pethPdPortTable=pethPdPortTable, pethPsePortOnOffNotification=pethPsePortOnOffNotification, pethCompliances=pethCompliances, pethPsePortNotificationGroup=pethPsePortNotificationGroup, pethMainPowerUsageOffNotification=pethMainPowerUsageOffNotification, pethNotificationControl=pethNotificationControl, pethNotifications=pethNotifications, pethPsePortGroup=pethPsePortGroup)
