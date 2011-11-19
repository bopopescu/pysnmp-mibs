# PySNMP SMI module. Autogenerated from smidump -f python FR-ATM-PVC-SERVICE-IWF-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:29:08 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( atmVclEntry, ) = mibBuilder.importSymbols("ATM-MIB", "atmVclEntry")
( AtmVcIdentifier, AtmVpIdentifier, ) = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVcIdentifier", "AtmVpIdentifier")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( RowStatus, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp")

# Objects

frAtmIwfMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 86)).setRevisions(("2000-09-28 00:00",))
if mibBuilder.loadTexts: frAtmIwfMIB.setOrganization("IETF Frame Relay Service MIB Working Group")
if mibBuilder.loadTexts: frAtmIwfMIB.setContactInfo("WG Charter:\nhttp://www.ietf.org/html.charters/frnetmib-charter\nWG-email:\nfrnetmib@sunroof.eng.sun.com\nSubscribe:\nfrnetmib-request@sunroof.eng.sun.com\nEmail Archive:\nftp://ftp.ietf.org/ietf-mail-archive/frnetmib\n\nChair:      Andy Malis\n          Vivace Networks, Inc.\nEmail:      Andy.Malis@vivacenetworks.com\n\nWG editor:  Kenneth Rehbehn\n          Megisto Systems, Inc.\nEmail:      krehbehn@megisto.com\n\nCo-author:  Orly Nicklass\n          RAD Data Communications Ltd.\nEMail:      orly_n@rad.co.il\n\nCo-author:  George Mouradian\n          AT&T Labs\nEMail:      gvm@att.com")
if mibBuilder.loadTexts: frAtmIwfMIB.setDescription("The MIB module for monitoring and controlling the\nFrame Relay/ATM PVC Service Interworking\nFunction.")
frAtmIwfMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 1))
frAtmIwfConnIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 86, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnIndexNext.setDescription("This object contains an appropriate value to be\nused for frAtmIwfConnIndex  when creating entries\nin the frAtmIwfConnectionTable. The value 0\nindicates that no unassigned entries are\navailable. To obtain the frAtmIwfConnIndexNext\nvalue for a new entry, the manager issues a\nmanagement protocol retrieval operation to obtain\nthe current value of this object.  After each\nretrieval, the agent should modify the value to\nthe next unassigned index.")
frAtmIwfConnectionTable = MibTable((1, 3, 6, 1, 2, 1, 86, 1, 2))
if mibBuilder.loadTexts: frAtmIwfConnectionTable.setDescription("A table in which each row represents a Frame\nRelay/ATM interworking connection.")
frAtmIwfConnectionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 86, 1, 2, 1)).setIndexNames((0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnIndex"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtmPort"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnVpi"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnVci"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFrPort"), (0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDlci"))
if mibBuilder.loadTexts: frAtmIwfConnectionEntry.setDescription("The FrAtmIwfConnectionEntry provides an entry for\nan interworking connection between a frame relay\nPVC and one or more ATM PVCs, or an ATM PVC and\none or more frame relay PVCs.  A single frame\nrelay PVC connected to a single ATM PVC is\nreferred to as a `point-to-point' connection and\nis represented by a single row in the FR/ATM IWF\nConnection Table.  The case of a single frame\nrelay PVC connected to multiple ATM PVCs (or\nsingle ATM PVC connected to multiple frame relay\nPVCs) is referred to as a `point-to-multipoint'\nconnection and is represented by multiple rows in\nthe FR/ATM IWF Connection Table.\n\nThe object frAtmIwfConnIndex uniquely identifies\neach point-to-point or point-to-multipoint\nconnection.  The manager obtains the\nfrAtmIwfConnIndex value by reading the\nfrAtmIwfConnIndexNext object.\n\nAfter a frAtmIwfConnIndex is assigned for the\nconnection, the manager creates one or more rows\nin the Cross Connect Table; one for each cross-\nconnection between the frame relay PVC and an ATM\nPVC. In the case of `point-to-multipoint'\nconnections, all rows are indexed by the same\nfrAtmIwfConnIndex value and MUST refer to the same\nframe relay PVC or ATM PVC respectively.  An entry\ncan be created only when at least one pair of\nframe relay and ATM PVCs exist.\n\nA row can be established by one-step set-request\nwith all required parameter values and\nfrAtmIwfConnRowStatus set to createAndGo(4). The\n\n\nAgent should perform all error checking as needed.\nA pair of cross-connected PVCs, as identified by a\nparticular value of the indexes, is released by\nsetting frAtmIwfConnRowStatus to destroy(6). The\nAgent may release all associated resources. The\nmanager may remove the related PVCs thereafter.\nIndexes are persistent across reboots of the\nsystem.")
frAtmIwfConnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: frAtmIwfConnIndex.setDescription("A unique value for each point-to-point or point-\nto-multipoint connection.  The manager obtains the\nfrAtmIwfConnIndex value by reading the\n\n\nfrAtmIwfConnIndexNext object.  A point-to-\nmultipoint connection will be represented in the\nfrAtmIwfConnectionTable with multiple entries that\nshare the same frAtmIwfConnIndex value.")
frAtmIwfConnAtmPort = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: frAtmIwfConnAtmPort.setDescription("The index in the ifTable that identifies the ATM\nport for this interworking connection.")
frAtmIwfConnVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 3), AtmVpIdentifier()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: frAtmIwfConnVpi.setDescription("The VPI of the ATM PVC end point for this\ninterworking connection.")
frAtmIwfConnVci = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 4), AtmVcIdentifier()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: frAtmIwfConnVci.setDescription("The VCI of the ATM PVC end point for this\ninterworking\n connection.")
frAtmIwfConnFrPort = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 5), InterfaceIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: frAtmIwfConnFrPort.setDescription("The index in the ifTable that identifies the\nframe relay port for this interworking\nconnection.")
frAtmIwfConnDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 4194303))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: frAtmIwfConnDlci.setDescription("The DLCI that identifies the frame relay PVC end\npoint for this interworking connection.")
frAtmIwfConnRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnRowStatus.setDescription("The table row may be created with\n'createAndWait(5)' or 'createAndGo(4)'.\nTo activate a connection entry, a valid connection\ndescriptor MUST be established in the\nfrAtmIwfConnectionDescriptor object.\n\nThis object is set to 'destroy(6)' to delete the\ntable row.  Before the table row is destroyed, the\nOperStatus/AdminStatus of the corresponding\nendpoints MUST be 'down(2)'.  The deactivation of\nthe ATM endpoint MAY occur as a side-effect of\ndeleting the FR/ATM IWF cross-connection table\nrow.  Otherwise, 'destroy(6)' operation MUST fail\n(error code 'inconsistentValue').")
frAtmIwfConnAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnAdminStatus.setDescription("The desired operational state for this FR/ATM\ninterworked connection.\n\nup(1)       = Activate the connection. Before the\n              activation can be completed, the\n              OperStatus/AdminStatus of the\n              corresponding endpoints MUST be\n              'up(1)'.  The activation of the\n              corresponding endpoints MAY occur as\n              a side-effect of activating the\n              FR/ATM IWF cross-connection.\n\ndown(2)     = Deactivate the connection. Before\n              the deactivation can be completed,\n              the atmVclAdminStatus of the\n              corresponding ATM endpoint MUST be\n              'down(2)'.  The deactivation of the\n\n\n              ATM endpoint MAY occur as a\n              side-effect of deactivating the\n              FR/ATM IWF cross-connection.")
frAtmIwfConnAtm2FrOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnAtm2FrOperStatus.setDescription("The current operational state of this\ninterworking connection in the ATM to frame\nrelay direction.")
frAtmIwfConnAtm2FrLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnAtm2FrLastChange.setDescription("The value of sysUpTime at the time this\ninterworking connection entered its current\noperational state in the ATM to FR direction.  If\nthe current state was entered prior to the last\nre-initialization of the local network management\nsubsystem, then this object contains a zero\nvalue.")
frAtmIwfConnFr2AtmOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 11), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnFr2AtmOperStatus.setDescription("The current operational state of this\ninterworking connection in the frame relay\nto ATM direction.")
frAtmIwfConnFr2AtmLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnFr2AtmLastChange.setDescription("The value of sysUpTime at the time this\ninterworking connection entered its current\noperational state in the FR to ATM direction.  If\nthe current state was entered prior to the last\n\n\nre-initialization of the local network management\nsubsystem, then this object contains a zero\nvalue.")
frAtmIwfConnectionDescriptor = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptor.setDescription("The value represents a pointer to the relevant\ndescriptor in the IWF descriptor table.  An\nattempt to set this value to an inactive or non-\nexistent row in the Connection Descriptor Table\nMUST fail (error code 'inconsistentValue').")
frAtmIwfConnFailedFrameTranslate = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnFailedFrameTranslate.setDescription("This object counts the number of frames discarded\nby the IWF because, while operating in Translation\nMode, the IWF is unable to decode the incoming\nframe payload header according to the mapping\nrules. (i.e., payload header not recognized by the\nIWF).\n\nFrame relay frames are received in the frame relay\nto ATM direction of the PVC.\n\nWhen operating in Transparent Mode, the IWF MUST\nreturn noSuchInstance.")
frAtmIwfConnOverSizedFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnOverSizedFrames.setDescription("Count of frames discarded by the IWF because the\nframe is too large to be processed by the AAL5\nsegmentation procedure.  Specifically, the frame\n\n\ndoes not conform to the size specified in the\natmVccAal5CpcsTransmitSduSize object associated\nwith the atmVclEntry at the ATM endpoint.\nFrame relay frames are received in the frame relay\nto ATM direction of the PVC.")
frAtmIwfConnFailedAal5PduTranslate = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnFailedAal5PduTranslate.setDescription("This attribute counts the number of AAL5 PDUs\ndiscarded by the IWF because, while operating in\nTranslation Mode, the IWF is unable to decode the\nincoming AAL5 PDU payload header according to the\nmapping rules. (i.e., payload header not\nrecognized by the IWF).\n\nAAL5 PDUs are received in the ATM to frame relay\ndirection of the PVC.\n\nWhen operating in Transparent Mode, the IWF MUST\nreturn noSuchInstance.")
frAtmIwfConnOverSizedSDUs = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnOverSizedSDUs.setDescription("Count of AAL5 SDUs discarded by the IWF because\nthe SDU is too large to be forwarded on the frame\nrelay segment of the connection.  Specifically,\nthe frame does not conform to the size specified\nin the frLportFragSize object of the FRS MIB [19].\n\nAAL5 PDUs are received in the ATM to frame relay\ndirection of the PVC.")
frAtmIwfConnCrcErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnCrcErrors.setDescription("The number of AAL5 CPCS PDUs received with CRC-32\nerrors on this AAL5 VCC at the IWF.\n\nAAL5 PDUs are received in the ATM to frame relay\ndirection of the PVC.")
frAtmIwfConnSarTimeOuts = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnSarTimeOuts.setDescription("The number of partially re-assembled AAL5 CPCS\nPDUs which were discarded on this AAL5 VCC at the\nIWF because they were not fully re-assembled\nwithin the required time period.  If the re-\nassembly timer is not supported, then this object\ncontains a zero value.\n\nAAL5 PDUs are received in the ATM to frame relay\ndirection of the PVC.")
frAtmIwfConnectionDescriptorIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 86, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorIndexNext.setDescription("This object contains an appropriate value to be\nused for frAtmIwfConnectionDescriptorIndex  when\ncreating entries in the\nfrAtmIwfConnectionDescriptorTable. The value 0\nindicates that no unassigned entries are\navailable. To obtain the\nfrAtmIwfConnectionDescriptorIndexNext value for a\nnew entry, the manager issues a management\nprotocol retrieval operation to obtain the current\nvalue of this object.  After each retrieval, the\nagent should modify the value to the next\nunassigned index.")
frAtmIwfConnectionDescriptorTable = MibTable((1, 3, 6, 1, 2, 1, 86, 1, 4))
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorTable.setDescription("A table in which each row represents a descriptor\nfor one type of Frame Relay/ATM interworking\nconnection.  A descriptor may be assigned to zero\nor more FR/ATM PVC service IWF connections.")
frAtmIwfConnectionDescriptorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 86, 1, 4, 1)).setIndexNames((0, "FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorIndex"))
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorEntry.setDescription("An entry for a descriptor in an interworking\nconnection between a frame relay PVC and an ATM\nPVC.")
frAtmIwfConnectionDescriptorIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorIndex.setDescription("A unique value to identify a descriptor in the\ntable ")
frAtmIwfConnDescriptorRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnDescriptorRowStatus.setDescription("The status of this table row.  This object is\nused to create or delete an entry in the\ndescriptor table.\n\nCreation of the row requires a row index (see\nfrAtmIwfConnectionDescriptorIndexNext).  If not\nexplicitly set or in existence, all other columns\nof the row will be created and initialized to the\ndefault value.  During creation, this object MAY\nbe set to 'createAndGo(4)' or 'createAndWait(5)'.\nThe object MUST contain the value 'active(1)'\nbefore any connection table entry references the\nrow.\n\nTo destroy a row in this table, this object is set\nto the 'destroy(6)' action.  Row destruction MUST\nfail (error code 'inconsistentValue') if any\nconnection references the row.")
frAtmIwfConnDeToClpMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,2,)).subtype(namedValues=NamedValues(("mode1", 1), ("mode2Const0", 2), ("mode2Const1", 3), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnDeToClpMappingMode.setDescription("This object describes which mode of translation\nis in use for loss priority mapping in the frame\n\n\nrelay to ATM direction.\n\nmode1(1)        = the DE field in the Q.922 core\n                  frame shall be mapped to the ATM\n                  CLP field of every cell\n                  generated by the segmentation\n                  process of the AAL5 PDU\n                  containing the information of\n                  that frame.\n\nmode2Contst0(2) = the ATM CLP field of every cell\n                  generated by the segmentation\n                  process of the AAL5 PDU\n                  containing the information of\n                  that frame shall be set to\n                  constant 0.\n\nmode2Contst1(3) = the ATM CLP field of every cell\n                  generated by the segmentation\n                  process of the AAL5 PDU\n                  containing the information of\n                  that frame shall be set to\n                  constant 1.")
frAtmIwfConnClpToDeMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,2,)).subtype(namedValues=NamedValues(("mode1", 1), ("mode2Const0", 2), ("mode2Const1", 3), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnClpToDeMappingMode.setDescription("This object describes which mode of translation\nis in use for loss priority mapping in the ATM to\nframe relay direction.\n\nmode1(1)       = if one or more cells in a frame\n                 has its CLP field set, the DE\n                 field of the Q.922 core frame\n                 should be set.\n\nmode2Const0(2) = the DE field of the Q.922 core\n                 frame should be set to the\n\n\n                 constant 0.\n\nmode2Const1(3) = the DE field of the Q.922 core\n                 frame should be set to the\n                 constant 1.")
frAtmIwfConnCongestionMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("mode1", 1), ("mode2", 2), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnCongestionMappingMode.setDescription("This object describes which mode of translation\nis in use for forward congestion indication\nmapping in the frame relay to ATM direction.\n\nmode1(1) = The FECN field in the Q.922 core frame\n           shall be mapped to the ATM EFCI field\n           of every cell generated by the\n           segmentation process of the AAL5 PDU\n           containing the information of that\n           frame.\n\nmode2(2) = The FECN field in the Q.922 core frame\n           shall not be mapped to the ATM EFCI\n           field of cells generated by the\n           segmentation process of the AAL5 PDU\n           containing the information of that\n           frame. The EFCI field is always set to\n           'congestion not experienced'.\n\nIn both of the modes above, if there is congestion\nin the forward direction in the ATM layer within\nthe IWF, then the IWF can set the EFCI field to\n'congestion experienced'.")
frAtmIwfConnEncapsulationMappingMode = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,1,)).subtype(namedValues=NamedValues(("transparentMode", 1), ("translationMode", 2), ("translationModeAll", 3), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnEncapsulationMappingMode.setDescription("This object indicates whether the mapping of\nupper layer protocol encapsulation is enabled on\nthis interworking connection.\n\ntransparentMode(1) = Forward the encapsulations\n                     unaltered.\n\ntranslationMode(2) = Perform mapping between the\n                     two encapsulations due to the\n                     incompatibilities of the two\n                     methods. Mapping is provided\n                     for a subset of the potential\n                     encapsulations as itemized in\n                     frAtmIwfConnEncapsulationMapp\n                     ings.\n\ntranslationModeAll(3) = Perform mapping between\n                     the two encapsulations due to\n                     the incompatibilities of the\n                     two methods. All\n                     encapsulations are\n                     translated.")
frAtmIwfConnEncapsulationMappings = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 7), Bits().subtype(namedValues=NamedValues(("none", 0), ("bridgedPdus", 1), ("bridged802dot6", 2), ("bPdus", 3), ("routedIp", 4), ("routedOsi", 5), ("otherRouted", 6), ("x25Iso8202", 7), ("q933q2931", 8), )).clone(("none",))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnEncapsulationMappings.setDescription("If upper layer protocol encapsulation mapping is\nenabled on this interworking connection, then this\nattribute enumerates which of the encapsulation\nmappings are supported.\n\nnone(0)           = Transparent mode operation\nbridgedPdus(1)    = PID: 0x00-01,-07,-02 or -08\nbridged802dot6(2) = PID: 0x00-0B\nbPdus(3)          = PID: 0x00-0E or -0F\nroutedIp(4)       = NLPID: OxCC\nroutedOsi(5)      = NLPID: Ox81, 0x82 or 0x83\notherRouted(6)    = Other routed protocols\nx25Iso8202(7)     = X25\nq933q2931(8)      = Q.933 and Q.2931")
frAtmIwfConnFragAndReassEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnFragAndReassEnabled.setDescription("The attribute indicates whether fragmentation and\nreassembly is enabled for this connection.")
frAtmIwfConnArpTranslationEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 4, 1, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: frAtmIwfConnArpTranslationEnabled.setDescription("The attribute indicates whether ARP translation\nis enabled for this connection.")
frAtmIwfVclTable = MibTable((1, 3, 6, 1, 2, 1, 86, 1, 5))
if mibBuilder.loadTexts: frAtmIwfVclTable.setDescription("The FR/ATM IWF VCL Table augments the ATM MIB VCL\nEndpoint table.")
frAtmIwfVclEntry = MibTableRow((1, 3, 6, 1, 2, 1, 86, 1, 5, 1))
if mibBuilder.loadTexts: frAtmIwfVclEntry.setDescription("Entries in this table are created only by the\nagent. One entry exists for each ATM VCL managed\nby the agent.")
frAtmIwfVclCrossConnectIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 86, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frAtmIwfVclCrossConnectIdentifier.setDescription("This object contains the index value of the\nFR/ATM cross-connect table entry used to link the\nATM VCL with a frame relay PVC.\n\nEach row of the atmVclTable that is not cross-\nconnected with a frame relay PVC MUST return the\nvalue zero when this object is read.\n\nIn the case of (frame relay) point to (ATM)\nmultipoint, multiple ATM VCLs will have the same\nvalue of this object, and all their cross-\nconnections are identified by entries that are\nindexed by the same value of\nfrAtmIwfVclCrossConnectIdentifier in the\nfrAtmIwfConnectionTable of this MIB module.\n\nThe value of this object is initialized by the\nagent after the associated entries in the\nfrAtmIwfConnectionTable have been created.")
frAtmIwfTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 2))
frAtmIwfTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 2, 0))
frAtmIwfConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 3))
frAtmIwfGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 3, 1))
frAtmIwfCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 86, 3, 2))

# Augmentions
atmVclEntry, = mibBuilder.importSymbols("ATM-MIB", "atmVclEntry")
atmVclEntry.registerAugmentions(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfVclEntry"))
frAtmIwfVclEntry.setIndexNames(*atmVclEntry.getIndexNames())

# Notifications

frAtmIwfConnStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 86, 2, 0, 1)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAdminStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmOperStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrOperStatus"), )
if mibBuilder.loadTexts: frAtmIwfConnStatusChange.setDescription("An indication that the status of this\ninterworking connection has changed.")

# Groups

frAtmIwfBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 1)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnCrcErrors"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnOverSizedSDUs"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrLastChange"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmLastChange"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFailedFrameTranslate"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnSarTimeOuts"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFailedAal5PduTranslate"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFr2AtmOperStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnOverSizedFrames"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptor"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAtm2FrOperStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnRowStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnAdminStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnIndexNext"), )
if mibBuilder.loadTexts: frAtmIwfBasicGroup.setDescription("The collection of basic objects for configuration\nand control of FR/ATM interworking connections.")
frAtmIwfConnectionDescriptorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 2)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDescriptorRowStatus"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnCongestionMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnEncapsulationMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnClpToDeMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnDeToClpMappingMode"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnEncapsulationMappings"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorIndexNext"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnArpTranslationEnabled"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnFragAndReassEnabled"), )
if mibBuilder.loadTexts: frAtmIwfConnectionDescriptorGroup.setDescription("The collection of basic objects for specification\nof FR/ATM interworking connection descriptors.")
frAtmIwfAtmVclTableAugmentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 3)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfVclCrossConnectIdentifier"), )
if mibBuilder.loadTexts: frAtmIwfAtmVclTableAugmentGroup.setDescription("The ATM MIB VCL Endpoint Table AUGMENT object\ncontained in the FR/ATM PVC Service Interworking\nMIB.")
frAtmIwfNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 86, 3, 1, 4)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnStatusChange"), )
if mibBuilder.loadTexts: frAtmIwfNotificationsGroup.setDescription("The notification for FR/ATM interworking status\nchange.")

# Compliances

frAtmIwfEquipmentCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 86, 3, 2, 1)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfNotificationsGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfAtmVclTableAugmentGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfBasicGroup"), )
if mibBuilder.loadTexts: frAtmIwfEquipmentCompliance.setDescription("The compliance statement for equipment that\nimplements the FR/ATM Interworking MIB.")
frAtmIwfServiceCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 86, 3, 2, 2)).setObjects(("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfConnectionDescriptorGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfNotificationsGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfAtmVclTableAugmentGroup"), ("FR-ATM-PVC-SERVICE-IWF-MIB", "frAtmIwfBasicGroup"), )
if mibBuilder.loadTexts: frAtmIwfServiceCompliance.setDescription("The compliance statement for a CNM interface that\nimplements the FR/ATM Interworking MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("FR-ATM-PVC-SERVICE-IWF-MIB", PYSNMP_MODULE_ID=frAtmIwfMIB)

# Objects
mibBuilder.exportSymbols("FR-ATM-PVC-SERVICE-IWF-MIB", frAtmIwfMIB=frAtmIwfMIB, frAtmIwfMIBObjects=frAtmIwfMIBObjects, frAtmIwfConnIndexNext=frAtmIwfConnIndexNext, frAtmIwfConnectionTable=frAtmIwfConnectionTable, frAtmIwfConnectionEntry=frAtmIwfConnectionEntry, frAtmIwfConnIndex=frAtmIwfConnIndex, frAtmIwfConnAtmPort=frAtmIwfConnAtmPort, frAtmIwfConnVpi=frAtmIwfConnVpi, frAtmIwfConnVci=frAtmIwfConnVci, frAtmIwfConnFrPort=frAtmIwfConnFrPort, frAtmIwfConnDlci=frAtmIwfConnDlci, frAtmIwfConnRowStatus=frAtmIwfConnRowStatus, frAtmIwfConnAdminStatus=frAtmIwfConnAdminStatus, frAtmIwfConnAtm2FrOperStatus=frAtmIwfConnAtm2FrOperStatus, frAtmIwfConnAtm2FrLastChange=frAtmIwfConnAtm2FrLastChange, frAtmIwfConnFr2AtmOperStatus=frAtmIwfConnFr2AtmOperStatus, frAtmIwfConnFr2AtmLastChange=frAtmIwfConnFr2AtmLastChange, frAtmIwfConnectionDescriptor=frAtmIwfConnectionDescriptor, frAtmIwfConnFailedFrameTranslate=frAtmIwfConnFailedFrameTranslate, frAtmIwfConnOverSizedFrames=frAtmIwfConnOverSizedFrames, frAtmIwfConnFailedAal5PduTranslate=frAtmIwfConnFailedAal5PduTranslate, frAtmIwfConnOverSizedSDUs=frAtmIwfConnOverSizedSDUs, frAtmIwfConnCrcErrors=frAtmIwfConnCrcErrors, frAtmIwfConnSarTimeOuts=frAtmIwfConnSarTimeOuts, frAtmIwfConnectionDescriptorIndexNext=frAtmIwfConnectionDescriptorIndexNext, frAtmIwfConnectionDescriptorTable=frAtmIwfConnectionDescriptorTable, frAtmIwfConnectionDescriptorEntry=frAtmIwfConnectionDescriptorEntry, frAtmIwfConnectionDescriptorIndex=frAtmIwfConnectionDescriptorIndex, frAtmIwfConnDescriptorRowStatus=frAtmIwfConnDescriptorRowStatus, frAtmIwfConnDeToClpMappingMode=frAtmIwfConnDeToClpMappingMode, frAtmIwfConnClpToDeMappingMode=frAtmIwfConnClpToDeMappingMode, frAtmIwfConnCongestionMappingMode=frAtmIwfConnCongestionMappingMode, frAtmIwfConnEncapsulationMappingMode=frAtmIwfConnEncapsulationMappingMode, frAtmIwfConnEncapsulationMappings=frAtmIwfConnEncapsulationMappings, frAtmIwfConnFragAndReassEnabled=frAtmIwfConnFragAndReassEnabled, frAtmIwfConnArpTranslationEnabled=frAtmIwfConnArpTranslationEnabled, frAtmIwfVclTable=frAtmIwfVclTable, frAtmIwfVclEntry=frAtmIwfVclEntry, frAtmIwfVclCrossConnectIdentifier=frAtmIwfVclCrossConnectIdentifier, frAtmIwfTraps=frAtmIwfTraps, frAtmIwfTrapsPrefix=frAtmIwfTrapsPrefix, frAtmIwfConformance=frAtmIwfConformance, frAtmIwfGroups=frAtmIwfGroups, frAtmIwfCompliances=frAtmIwfCompliances)

# Notifications
mibBuilder.exportSymbols("FR-ATM-PVC-SERVICE-IWF-MIB", frAtmIwfConnStatusChange=frAtmIwfConnStatusChange)

# Groups
mibBuilder.exportSymbols("FR-ATM-PVC-SERVICE-IWF-MIB", frAtmIwfBasicGroup=frAtmIwfBasicGroup, frAtmIwfConnectionDescriptorGroup=frAtmIwfConnectionDescriptorGroup, frAtmIwfAtmVclTableAugmentGroup=frAtmIwfAtmVclTableAugmentGroup, frAtmIwfNotificationsGroup=frAtmIwfNotificationsGroup)

# Compliances
mibBuilder.exportSymbols("FR-ATM-PVC-SERVICE-IWF-MIB", frAtmIwfEquipmentCompliance=frAtmIwfEquipmentCompliance, frAtmIwfServiceCompliance=frAtmIwfServiceCompliance)
