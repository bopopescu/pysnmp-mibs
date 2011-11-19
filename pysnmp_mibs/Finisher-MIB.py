# PySNMP SMI module. Autogenerated from smidump -f python Finisher-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:29:07 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( hrDeviceIndex, ) = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrDeviceIndex")
( FinAttributeTypeTC, FinDeviceTypeTC, ) = mibBuilder.importSymbols("IANA-FINISHER-MIB", "FinAttributeTypeTC", "FinDeviceTypeTC")
( PrtInputTypeTC, PrtMarkerSuppliesTypeTC, ) = mibBuilder.importSymbols("IANA-PRINTER-MIB", "PrtInputTypeTC", "PrtMarkerSuppliesTypeTC")
( PresentOnOff, PrtCapacityUnitTC, PrtLocalizedDescriptionStringTC, PrtMarkerSuppliesClassTC, PrtMarkerSuppliesSupplyUnitTC, PrtMediaUnitTC, PrtSubUnitStatusTC, printmib, prtMIBConformance, ) = mibBuilder.importSymbols("Printer-MIB", "PresentOnOff", "PrtCapacityUnitTC", "PrtLocalizedDescriptionStringTC", "PrtMarkerSuppliesClassTC", "PrtMarkerSuppliesSupplyUnitTC", "PrtMediaUnitTC", "PrtSubUnitStatusTC", "printmib", "prtMIBConformance")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")

# Objects

finMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 2, 6))
finDevice = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 30))
finDeviceTable = MibTable((1, 3, 6, 1, 2, 1, 43, 30, 1))
if mibBuilder.loadTexts: finDeviceTable.setDescription("This table defines the finishing device subunits,\nincluding information regarding possible configuration\noptions and the status for each finisher device subunit.")
finDeviceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 30, 1, 1)).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finDeviceIndex"))
if mibBuilder.loadTexts: finDeviceEntry.setDescription("There is an entry in the finishing device table for each\npossible finisher process.  Each individual finisher process is\nimplemented by a finishing device represented in this table.")
finDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: finDeviceIndex.setDescription("A unique value used to identify a finisher process.\nAlthough these values may change due to a major\nreconfiguration of the printer system (e.g., the addition\nof new finishing processes), the values are normally\nexpected to remain stable across successive power cycles.")
finDeviceType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 2), FinDeviceTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceType.setDescription("Defines the type of finishing process associated with this\ntable row entry.")
finDevicePresentOnOff = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 3), PresentOnOff().clone('notPresent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDevicePresentOnOff.setDescription("Indicates if this finishing device subunit is available\nand whether the device subunit is enabled.")
finDeviceCapacityUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 4), PrtCapacityUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceCapacityUnit.setDescription("The unit of measure for specifying the capacity of this\nfinisher device subunit.")
finDeviceMaxCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceMaxCapacity.setDescription("The maximum capacity of this finisher device subunit in\nfinDeviceCapacityUnits.  If the device can reliably sense\nthis value, the value is sensed by the finisher device\n\n\nand is read-only: otherwise the value may be written by a\nmanagement or control console application.  The value (-1)\nmeans other and specifically indicates that the device\nplaces no restrictions on this parameter.  The value (-2)\nmeans unknown.")
finDeviceCurrentCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceCurrentCapacity.setDescription("The current capacity of this finisher device subunit in\nfinDeviceCapacityUnits.  If the device can reliably sense\nthis value, the value is sensed by the finisher and is\nread-only: otherwise the value may be written by a\nmanagement or control console application.  The value (-1)\nmeans other and specifically indicates that the device\nplaces no restrictions on this parameter.  The value (-2)\nmeans unknown.")
finDeviceAssociatedMediaPaths = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceAssociatedMediaPaths.setDescription("Indicates the media paths which can supply media for this\nfinisher device.  The value of this object is a bit map in an\noctet string with each position representing the value of a\nprtMediaPathIndex.  For a media path that can be a source\nfor this finisher device subunit, the bit position equal\nto one less than the value of prtMediaPathIndex will be set.\nThe bits are numbered starting with the most significant bit of\nthe first byte being bit 0, the least significant bit of the\nfirst byte being bit 7, the most significant of the second byte\nbeing bit 8, and so on.")
finDeviceAssociatedOutputs = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceAssociatedOutputs.setDescription("Indicates the printer output subunits this finisher device\nsubunit services.  The value of this object is a bit map in an\n\n\noctet string with each position representing the value of a\nprtOutputIndex.  For an output subunit that is serviced\nby this finisher device subunit, the bit position equal\nto one less than the value of prtOutputIndex will be set.\nThe bits are numbered starting with the most significant bit of\nthe first byte being bit 0, the least significant bit of the\nfirst byte being bit 7, the most significant of the second byte\nbeing bit 8, and so on.")
finDeviceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 9), PrtSubUnitStatusTC().clone('5')).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceStatus.setDescription("Indicates the current status of this finisher device\nsubunit.")
finDeviceDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 30, 1, 1, 10), PrtLocalizedDescriptionStringTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finDeviceDescription.setDescription("A free form text description of this device subunit in the\nlocalization specified by prtGeneralCurrentLocalization.")
finSupply = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 31))
finSupplyTable = MibTable((1, 3, 6, 1, 2, 1, 43, 31, 1))
if mibBuilder.loadTexts: finSupplyTable.setDescription("Each unique source of supply is an entry in the finisher\nsupply table. Each supply entry has its own\ncharacteristics associated with it such as colorant and\n\n\ncurrent supply level.")
finSupplyEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 31, 1, 1)).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finSupplyIndex"))
if mibBuilder.loadTexts: finSupplyEntry.setDescription("A list of finisher devices, with their associated\nsupplies and supplies characteristics.")
finSupplyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: finSupplyIndex.setDescription("A unique value used by a finisher to identify this supply\ncontainer/receptacle.  Although these values may change\ndue to a major reconfiguration of the finisher (e.g., the\naddition of new supply sources to the finisher), values\nare normally expected to remain stable across successive\npower cycles.")
finSupplyDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyDeviceIndex.setDescription("The value of finDeviceIndex corresponding to the finishing\ndevice subunit with which this finisher supply is associated.\nThe value zero indicates the associated finishing device is\nUnknown.")
finSupplyClass = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 3), PrtMarkerSuppliesClassTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyClass.setDescription("This value indicates whether this supply entity\nrepresents a supply that is consumed or a container that\nis filled.")
finSupplyType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 4), PrtMarkerSuppliesTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyType.setDescription("The type of this supply.")
finSupplyDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 5), PrtLocalizedDescriptionStringTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyDescription.setDescription("The description of this supply/receptacle in text useful\nfor operators and management applications and in the\nlocalization specified by prtGeneralCurrentLocalization.")
finSupplyUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 6), PrtMarkerSuppliesSupplyUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyUnit.setDescription("Unit of measure of this finisher supply container or\nreceptacle.")
finSupplyMaxCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMaxCapacity.setDescription("The maximum capacity of this supply container/receptacle\nexpressed in Supply Units.  If this supply container/\nreceptacle can reliably sense this value, the value is\nsensed  and is read-only; otherwise the value may be\nwritten by a control panel or management application.  The\nvalue (-1) means other and places no restrictions on this\n\n\n\nparameter.  The value (-2) means unknown.")
finSupplyCurrentLevel = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-3, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyCurrentLevel.setDescription("The current level if this supply is a container; the\nremaining space if this supply is a receptacle. If this\nsupply container/receptacle can reliably sense this value,\nthe value is sensed and is read-only; otherwise the value\nmay be written by a control panel or management\napplication.  The value (-1) means other and places no\nrestrictions on this parameter. The value (-2) means\nunknown.  A value of (-3) means that the printer knows there\nis some supply or remaining space.")
finSupplyColorName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 31, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyColorName.setDescription("The name of the color associated with this supply.")
finSupplyMediaInput = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 32))
finSupplyMediaInputTable = MibTable((1, 3, 6, 1, 2, 1, 43, 32, 1))
if mibBuilder.loadTexts: finSupplyMediaInputTable.setDescription("The input subunits associated with a finisher supply media\nare each represented by an entry in this table.")
finSupplyMediaInputEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 32, 1, 1)).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finSupplyMediaInputIndex"))
if mibBuilder.loadTexts: finSupplyMediaInputEntry.setDescription("A list of finisher supply media input subunit features and\ncharacteristics.")
finSupplyMediaInputIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: finSupplyMediaInputIndex.setDescription("A unique value used by a finisher to identify this supply\nmedia input subunit.  Although these values may change\ndue to a major reconfiguration of the finisher (e.g., the\naddition of new supply media input sources to the\nfinisher), values are normally expected to remain stable\nacross successive power cycles.")
finSupplyMediaInputDeviceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputDeviceIndex.setDescription("The value of finDeviceIndex corresponding to the finishing\ndevice subunit with which this finisher media supply is\nassociated.  The value zero indicates the associated device\nis unknown.")
finSupplyMediaInputSupplyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputSupplyIndex.setDescription("The value of finSupplyIndex corresponding to the finishing\nsupply subunit with which this finisher media supply is\nassociated.  The value zero indicates the associated finishing\nsupply is unknown or there is no applicable finisher supply\ntable entry.")
finSupplyMediaInputType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 4), PrtInputTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputType.setDescription("The type of technology (discriminated primarily according\nto the feeder mechanism type) employed by the input\nsubunit.")
finSupplyMediaInputDimUnit = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 5), PrtMediaUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputDimUnit.setDescription("The unit of measure for specifying dimensional values for\nthis input device.")
finSupplyMediaInputMediaDimFeedDir = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaDimFeedDir.setDescription("This object provides the value of the dimension in the\nfeed direction of the media that is placed or will be\nplaced in this input device.  Feed dimension measurements\nare taken parallel to the feed direction of the device and\nmeasured in finSupplyMediaInputDimUnits.  If this input\ndevice can reliably sense this value, the value is sensed\nand is read-only access. Otherwise the value is read-write\naccess and may be written by management or control panel\napplications. The value (-1) means other and specifically\nindicates that this device places no restrictions on this\nparameter. The value (-2) indicates unknown. ")
finSupplyMediaInputMediaDimXFeedDir = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaDimXFeedDir.setDescription("This object provides the value of the dimension across the\nfeed direction of the media that is placed or will be\nplaced in this input device.  The cross feed direction is\nninety degrees relative to the feed direction on this\ndevice and measured in finSupplyMediaInputDimUnits.  If\nthis input device can reliably sense this value, the value\nis sensed and is read-only access. Otherwise the value is\nread-write access and may be written by management or\ncontrol panel applications. The value (-1) means other and\nspecifically indicates that this device places no\n\n\n\nrestrictions on this parameter. The value (-2) indicates\nunknown. ")
finSupplyMediaInputStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 8), PrtSubUnitStatusTC().clone('5')).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputStatus.setDescription("This value indicates the current status of this input\ndevice.")
finSupplyMediaInputMediaName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaName.setDescription("The name of the current media contained in this input\ndevice. Examples are Engineering Manual Cover, Section A Tab\nDivider or any ISO standard names.")
finSupplyMediaInputName = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputName.setDescription("The name assigned to this input subunit.")
finSupplyMediaInputDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 11), PrtLocalizedDescriptionStringTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: finSupplyMediaInputDescription.setDescription("A free form text description of this input subunit in the\nlocalization specified by prtGeneralCurrentLocalization.")
finSupplyMediaInputSecurity = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 12), PresentOnOff()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputSecurity.setDescription("Indicates if this subunit has some security associated\nwith it.")
finSupplyMediaInputMediaWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaWeight.setDescription("The weight of the media associated with this Input device\nin grams per meter squared.  The value (-1) means other\nand specifically indicates that the device places no\nrestriction on this parameter.  The value (-2) means\nunknown.  This object can be used to calculate the weight\nof individual pages processed by the document finisher.\nThis value, when multiplied by the number of pages in a\nfinished set, can be used to calculate the weight of a set\nbefore it is inserted into a mailing envelope.")
finSupplyMediaInputMediaThickness = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaThickness.setDescription("This object identifies the thickness of the input media\nprocessed by this document input subunit measured in\nmicrometers.  This value may be used by devices (or\noperators) to set up proper machine tolerances for the\nfeeder operation.  The value (-2) indicates that the media\nthickness is unknown or not used in the setup for this\ninput subunit.")
finSupplyMediaInputMediaType = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 32, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finSupplyMediaInputMediaType.setDescription("The name of the type of medium associated with this input\nsubunit. ")
finDeviceAttribute = MibIdentifier((1, 3, 6, 1, 2, 1, 43, 33))
finDeviceAttributeTable = MibTable((1, 3, 6, 1, 2, 1, 43, 33, 1))
if mibBuilder.loadTexts: finDeviceAttributeTable.setDescription("The attribute table defines special parameters that are\napplicable only to a minority of the finisher devices.\nAn attribute table entry is used, rather than unique\nobjects, to minimize the number of MIB objects and to\nallow for expansion without the addition of MIB objects.\nEach finisher device is represented by a separate row\nin the device subunit attribute table.")
finDeviceAttributeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 43, 33, 1, 1)).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "Finisher-MIB", "finDeviceIndex"), (0, "Finisher-MIB", "finDeviceAttributeTypeIndex"), (0, "Finisher-MIB", "finDeviceAttributeInstanceIndex"))
if mibBuilder.loadTexts: finDeviceAttributeEntry.setDescription("Each entry defines a finisher function parameter that\ncannot be represented by an object in the finisher\ndevice subunit table.")
finDeviceAttributeTypeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 1), FinAttributeTypeTC()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: finDeviceAttributeTypeIndex.setDescription("Defines the attribute type represented by this row.")
finDeviceAttributeInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: finDeviceAttributeInstanceIndex.setDescription("An index that allows the discrimination of an attribute\ninstance when the same attribute occurs multiple times for\na specific instance of a finisher function.  The value of\nthis index shall be 1 if only a single instance of the\nattribute occurs for the specific finisher function.\nAdditional values shall be assigned in a contiguous manner.")
finDeviceAttributeValueAsInteger = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceAttributeValueAsInteger.setDescription("Defines the integer value of the attribute.  The value of\nthe attribute is represented as an integer if the\nfinAttributeTypeTC description for the attribute has the\ntag 'INTEGER:'.\n\nDepending upon the attribute enum definition, this object\nmay be either an integer, a counter, an index, or an enum.\nAttributes for which the concept of an integer value is\nnot meaningful SHALL return a value of -1 for this\nattribute.")
finDeviceAttributeValueAsOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 43, 33, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)).clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: finDeviceAttributeValueAsOctets.setDescription("Contains the octet string value of the attribute.  The\nvalue of the attribute is represented as a string if the\nfinAttributeTypeTC description for the attribute has the\ntag 'OCTETS:'.\n\n\n\nDepending upon the attribute enum definition, this object\nmay be either a coded character set string (text) or a\nbinary octet string.  Attributes for which the concept of\nan octet string value is not meaningful SHALL contain a\nzero length string.")
finisherMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 111)).setRevisions(("2004-06-02 00:00",))
if mibBuilder.loadTexts: finisherMIB.setOrganization("PWG IEEE/ISTO Printer Working Group")
if mibBuilder.loadTexts: finisherMIB.setContactInfo("Harry Lewis\nIBM\nPhone (303) 924-5337\nEmail: harryl@us.ibm.com\n\nSend comments to the printmib WG using the Finisher MIB\nProject (FIN) Mailing List:  fin@pwg.org\n\nFor further information, access the PWG web page under 'Finisher\nMIB':      http://www.pwg.org/\n\nImplementers of this specification are encouraged to join the\nfin mailing list in order to participate in discussions on any\nclarifications needed and registration proposals being reviewed\nin order to achieve consensus.")
if mibBuilder.loadTexts: finisherMIB.setDescription("The MIB module for management of printers.\nCopyright (C) The Internet Society (2004). This\nversion of this MIB module was published\n\n\n\nin RFC 3806. For full legal notices see the RFC itself.")

# Augmentions

# Groups

finDeviceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 6, 1)).setObjects(("Finisher-MIB", "finDeviceStatus"), ("Finisher-MIB", "finDeviceDescription"), ("Finisher-MIB", "finDevicePresentOnOff"), ("Finisher-MIB", "finDeviceAssociatedOutputs"), ("Finisher-MIB", "finDeviceCurrentCapacity"), ("Finisher-MIB", "finDeviceMaxCapacity"), ("Finisher-MIB", "finDeviceCapacityUnit"), ("Finisher-MIB", "finDeviceType"), ("Finisher-MIB", "finDeviceAssociatedMediaPaths"), )
if mibBuilder.loadTexts: finDeviceGroup.setDescription("The finisher device group.")
finSupplyGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 6, 2)).setObjects(("Finisher-MIB", "finSupplyMaxCapacity"), ("Finisher-MIB", "finSupplyCurrentLevel"), ("Finisher-MIB", "finSupplyColorName"), ("Finisher-MIB", "finSupplyDeviceIndex"), ("Finisher-MIB", "finSupplyDescription"), ("Finisher-MIB", "finSupplyClass"), ("Finisher-MIB", "finSupplyUnit"), ("Finisher-MIB", "finSupplyType"), )
if mibBuilder.loadTexts: finSupplyGroup.setDescription("The finisher supply group.")
finSupplyMediaInputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 6, 3)).setObjects(("Finisher-MIB", "finSupplyMediaInputDeviceIndex"), ("Finisher-MIB", "finSupplyMediaInputMediaName"), ("Finisher-MIB", "finSupplyMediaInputType"), ("Finisher-MIB", "finSupplyMediaInputMediaDimFeedDir"), ("Finisher-MIB", "finSupplyMediaInputMediaWeight"), ("Finisher-MIB", "finSupplyMediaInputMediaThickness"), ("Finisher-MIB", "finSupplyMediaInputStatus"), ("Finisher-MIB", "finSupplyMediaInputMediaDimXFeedDir"), ("Finisher-MIB", "finSupplyMediaInputDescription"), ("Finisher-MIB", "finSupplyMediaInputDimUnit"), ("Finisher-MIB", "finSupplyMediaInputMediaType"), ("Finisher-MIB", "finSupplyMediaInputSupplyIndex"), ("Finisher-MIB", "finSupplyMediaInputSecurity"), ("Finisher-MIB", "finSupplyMediaInputName"), )
if mibBuilder.loadTexts: finSupplyMediaInputGroup.setDescription("The finisher supply, media input group.")
finDeviceAttributeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 43, 2, 6, 4)).setObjects(("Finisher-MIB", "finDeviceAttributeValueAsInteger"), ("Finisher-MIB", "finDeviceAttributeValueAsOctets"), )
if mibBuilder.loadTexts: finDeviceAttributeGroup.setDescription("The finisher device attribute group.  This group is mandatory\nfor a finisher device that contains an inserter subunit.")

# Compliances

finMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 43, 2, 5)).setObjects(("Finisher-MIB", "finDeviceGroup"), ("Finisher-MIB", "finSupplyMediaInputGroup"), ("Finisher-MIB", "finSupplyGroup"), ("Finisher-MIB", "finDeviceAttributeGroup"), )
if mibBuilder.loadTexts: finMIBCompliance.setDescription("The compliance statement for agents that implement the\nfinisher MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("Finisher-MIB", PYSNMP_MODULE_ID=finisherMIB)

# Objects
mibBuilder.exportSymbols("Finisher-MIB", finMIBGroups=finMIBGroups, finDevice=finDevice, finDeviceTable=finDeviceTable, finDeviceEntry=finDeviceEntry, finDeviceIndex=finDeviceIndex, finDeviceType=finDeviceType, finDevicePresentOnOff=finDevicePresentOnOff, finDeviceCapacityUnit=finDeviceCapacityUnit, finDeviceMaxCapacity=finDeviceMaxCapacity, finDeviceCurrentCapacity=finDeviceCurrentCapacity, finDeviceAssociatedMediaPaths=finDeviceAssociatedMediaPaths, finDeviceAssociatedOutputs=finDeviceAssociatedOutputs, finDeviceStatus=finDeviceStatus, finDeviceDescription=finDeviceDescription, finSupply=finSupply, finSupplyTable=finSupplyTable, finSupplyEntry=finSupplyEntry, finSupplyIndex=finSupplyIndex, finSupplyDeviceIndex=finSupplyDeviceIndex, finSupplyClass=finSupplyClass, finSupplyType=finSupplyType, finSupplyDescription=finSupplyDescription, finSupplyUnit=finSupplyUnit, finSupplyMaxCapacity=finSupplyMaxCapacity, finSupplyCurrentLevel=finSupplyCurrentLevel, finSupplyColorName=finSupplyColorName, finSupplyMediaInput=finSupplyMediaInput, finSupplyMediaInputTable=finSupplyMediaInputTable, finSupplyMediaInputEntry=finSupplyMediaInputEntry, finSupplyMediaInputIndex=finSupplyMediaInputIndex, finSupplyMediaInputDeviceIndex=finSupplyMediaInputDeviceIndex, finSupplyMediaInputSupplyIndex=finSupplyMediaInputSupplyIndex, finSupplyMediaInputType=finSupplyMediaInputType, finSupplyMediaInputDimUnit=finSupplyMediaInputDimUnit, finSupplyMediaInputMediaDimFeedDir=finSupplyMediaInputMediaDimFeedDir, finSupplyMediaInputMediaDimXFeedDir=finSupplyMediaInputMediaDimXFeedDir, finSupplyMediaInputStatus=finSupplyMediaInputStatus, finSupplyMediaInputMediaName=finSupplyMediaInputMediaName, finSupplyMediaInputName=finSupplyMediaInputName, finSupplyMediaInputDescription=finSupplyMediaInputDescription, finSupplyMediaInputSecurity=finSupplyMediaInputSecurity, finSupplyMediaInputMediaWeight=finSupplyMediaInputMediaWeight, finSupplyMediaInputMediaThickness=finSupplyMediaInputMediaThickness, finSupplyMediaInputMediaType=finSupplyMediaInputMediaType, finDeviceAttribute=finDeviceAttribute, finDeviceAttributeTable=finDeviceAttributeTable, finDeviceAttributeEntry=finDeviceAttributeEntry, finDeviceAttributeTypeIndex=finDeviceAttributeTypeIndex, finDeviceAttributeInstanceIndex=finDeviceAttributeInstanceIndex, finDeviceAttributeValueAsInteger=finDeviceAttributeValueAsInteger, finDeviceAttributeValueAsOctets=finDeviceAttributeValueAsOctets, finisherMIB=finisherMIB)

# Groups
mibBuilder.exportSymbols("Finisher-MIB", finDeviceGroup=finDeviceGroup, finSupplyGroup=finSupplyGroup, finSupplyMediaInputGroup=finSupplyMediaInputGroup, finDeviceAttributeGroup=finDeviceAttributeGroup)

# Compliances
mibBuilder.exportSymbols("Finisher-MIB", finMIBCompliance=finMIBCompliance)
