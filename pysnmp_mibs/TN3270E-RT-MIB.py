#
# PySNMP MIB module TN3270E-RT-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/TN3270E-RT-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:32:48 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( IANATn3270eAddrType, IANATn3270eAddress, ) = mibBuilder.importSymbols("IANATn3270eTC-MIB", "IANATn3270eAddrType", "IANATn3270eAddress")
( snanauMIB, ) = mibBuilder.importSymbols("SNA-NAU-MIB", "snanauMIB")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( TextualConvention, DateAndTime, TimeStamp, TestAndIncr, RowStatus, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "TimeStamp", "TestAndIncr", "RowStatus", "DisplayString")
( tn3270eSrvrConfIndex, tn3270eResMapElementType, tn3270eClientGroupName, ) = mibBuilder.importSymbols("TN3270E-MIB", "tn3270eSrvrConfIndex", "tn3270eResMapElementType", "tn3270eClientGroupName")
tn3270eRtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 9)).setRevisions(("1998-07-27 00:00",))
if mibBuilder.loadTexts: tn3270eRtMIB.setOrganization('TN3270E Working Group')
if mibBuilder.loadTexts: tn3270eRtMIB.setContactInfo('Kenneth White (kennethw@vnet.ibm.com)\n           IBM Corp. - Dept. BRQA/Bldg. 501/G114\n           P.O. Box 12195\n           3039 Cornwallis\n           RTP, NC 27709-2195\n\n           Robert Moore (remoore@us.ibm.com)\n           IBM Corp. - Dept. BRQA/Bldg. 501/G114\n           P.O. Box 12195\n           3039 Cornwallis\n           RTP, NC 27709-2195\n           (919) 254-4436')
if mibBuilder.loadTexts: tn3270eRtMIB.setDescription("This module defines a portion of the management\n          information base (MIB) that enables monitoring of\n          TN3270 and TN3270E clients' response times by a\n          TN3270E server.")
tn3270eRtNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 0))
tn3270eRtObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 1))
tn3270eRtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3))
tn3270eRtCollCtlTable = MibTable((1, 3, 6, 1, 2, 1, 34, 9, 1, 1), )
if mibBuilder.loadTexts: tn3270eRtCollCtlTable.setDescription('The response time monitoring collection control table,\n        which allows a management application to control the\n        types of response time data being collected, and the\n        clients for which it is being collected.\n\n        This table is indexed by tn3270eSrvrConfIndex and\n        tn3270eClientGroupName imported from the\n        TN3270E-MIB.  tn3270eSrvrConfIndex indicates within\n        a host which TN3270E server an entry applies to.\n        tn3270eClientGroupName it identifies the set of IP\n        clients for which response time data is being collected.\n        The particular IP clients making up the set are identified\n        in the tn3270eClientGroupTable in the TN3270E-MIB.')
tn3270eRtCollCtlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1), ).setIndexNames((0, "TN3270E-RT-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-RT-MIB", "tn3270eClientGroupName"))
if mibBuilder.loadTexts: tn3270eRtCollCtlEntry.setDescription('An entry in the TN3270E response time monitoring collection\n        control table.  To handle the case of multiple TN3270E\n        servers on the same host, the first index of this table is\n        the tn3270eSrvrConfIndex from the TN3270E-MIB.')
tn3270eRtCollCtlType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("aggregate", 0), ("excludeIpComponent", 1), ("ddr", 2), ("average", 3), ("buckets", 4), ("traps", 5),))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlType.setDescription('This object controls what types of response time data to\n         collect, whether to summarize the data across the members\n         of a client group or keep it individually, whether to\n         introduce dynamic definite responses, and whether to\n         generate traps.\n         aggregate(0)          - Aggregate response time data for the\n                                 client group as a whole.  If this bit\n                                 is set to 0, then maintain response\n                                 time data separately for each member\n                                 of the client group.\n         excludeIpComponent(1) - Do not include the IP-network\n                                 component in any response times.\n         ddr(2)                - Enable dynamic definite response.\n         average(3)            - Produce an average response time\n                                 based on a specified collection\n                                 interval.\n         buckets(4)            - Maintain tn3270eRtDataBucket values in\n                                 a corresponding tn3270eRtDataEntry,\n                                 based on the bucket boundaries specified\n                                 in the tn3270eRtCollCtlBucketBndry\n                                 objects          .\n         traps(5)              - generate the notifications specified\n                                 in this MIB module.  The\n                                 tn3270eRtExceeded and tn3270eRtOkay\n                                 notifications are generated only if\n                                 average(3) is also specified.')
tn3270eRtCollCtlSPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15,86400)).clone(20)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlSPeriod.setDescription('The number of seconds that defines the sample period.\n         The actual interval is defined as tn3270eRtCollCtlSPeriod\n         times tn3270eRtCollCtlSPMult.\n\n         The value of this object is used only if the corresponding\n         tn3270eRtCollCtlType has the average(3) setting.')
tn3270eRtCollCtlSPMult = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,5760)).clone(30)).setUnits('period').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlSPMult.setDescription('The sample period multiplier; this value is multiplied by\n        the sample period, tn3270eRtCollCtlSPeriod, to determine\n        the collection interval.\n        Sliding-window average calculation can, if necessary, be\n        disabled, by setting the sample period multiplier,\n        tn3270eRtCollCtlSPMult, to 1, and setting the sample\n        period, tn3270eRtCollCtlSPeriod, to the required\n        collection interval.\n\n        The value of this object is used only if the corresponding\n        tn3270eRtCollCtlType has the average(3) setting.')
tn3270eRtCollCtlThreshHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlThreshHigh.setDescription('The threshold for generating a tn3270eRtExceeded\n        notification, signalling that a monitored total response\n        time has exceeded the specified limit.  A value of zero\n        for this object suppresses generation of this notification.\n        The value of this object is used only if the corresponding\n        tn3270eRtCollCtlType has average(3) and traps(5) selected.\n\n        A tn3270eRtExceeded notification is not generated again for a\n        tn3270eRtDataEntry until an average response time falling below\n        the low threshold tn3270eRtCollCtlThreshLow specified for the\n        client group has occurred for the entry.')
tn3270eRtCollCtlThreshLow = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 6), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlThreshLow.setDescription('The threshold for generating a tn3270eRtOkay notification,\n        signalling that a monitored total response time has fallen\n        below the specified limit.  A value of zero for this object\n        suppresses generation of this notification.  The value of\n        this object is used only if the corresponding\n        tn3270eRtCollCtlType has average(3) and traps(5) selected.\n\n        A tn3270eRtOkay notification is not generated again for a\n        tn3270eRtDataEntry until an average response time\n        exceeding the high threshold tn3270eRtCollCtlThreshHigh\n        specified for the client group has occurred for the entry.')
tn3270eRtCollCtlIdleCount = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 7), Unsigned32().clone(1)).setUnits('transactions').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlIdleCount.setDescription('The value of this object is used to determine whether a\n        sample that yields an average response time exceeding the\n        value of tn3270eRtCollCtlThreshHigh was a statistically\n        valid one.  If the following statement is true, then the\n        sample was statistically valid, and so a tn3270eRtExceeded\n        notification should be generated:\n\n          AvgCountTrans * ((AvgRt/ThreshHigh - 1) ** 2) >=  IdleCount\n\n        This comparison is done only if the corresponding\n        tn3270eRtCollCtlType has average(3) and traps(5) selected.')
tn3270eRtCollCtlBucketBndry1 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 8), Unsigned32().clone(10)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry1.setDescription('The value of this object defines the range of transaction\n         response times counted in the Tn3270eRtDataBucket1Rts\n         object: those less than or equal to this value.')
tn3270eRtCollCtlBucketBndry2 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 9), Unsigned32().clone(20)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry2.setDescription('The value of this object, together with that of the\n        tn3270eRtCollCtlBucketBndry1 object, defines the range\n        of transaction response times counted in the\n        Tn3270eRtDataBucket2Rts object: those greater than the\n        value of the tn3270eRtCollCtlBucketBndry1 object, and\n        less than or equal to the value of this object.')
tn3270eRtCollCtlBucketBndry3 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 10), Unsigned32().clone(50)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry3.setDescription('The value of this object, together with that of the\n        tn3270eRtCollCtlBucketBndry2 object, defines the range of\n        transaction response times counted in the\n        Tn3270eRtDataBucket3Rts object:  those greater than the\n        value of the tn3270eRtCollCtlBucketBndry2 object, and less\n        than or equal to the value of this object.')
tn3270eRtCollCtlBucketBndry4 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 11), Unsigned32().clone(100)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry4.setDescription('The value of this object, together with that of the\n        tn3270eRtCollCtlBucketBndry3 object, defines the range\n        of transaction response times counted in the\n        Tn3270eRtDataBucket4Rts object: those greater than the\n        value of the tn3270eRtCollCtlBucketBndry3 object, and\n        less than or equal to the value of this object.\n\n        The value of this object also defines the range of\n        transaction response times counted in the\n        Tn3270eRtDataBucket5Rts object: those greater than the\n        value of this object.')
tn3270eRtCollCtlRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlRowStatus.setDescription('This object allows entries to be created and deleted\n         in the tn3270eRtCollCtlTable.  An entry in this table\n         is deleted by setting this object to destroy(6).\n         Deleting an entry in this table has the side-effect\n         of removing all entries from the tn3270eRtDataTable\n         that are associated with the entry being deleted.')
tn3270eRtDataTable = MibTable((1, 3, 6, 1, 2, 1, 34, 9, 1, 2), )
if mibBuilder.loadTexts: tn3270eRtDataTable.setDescription('The response time data table.  Entries in this table are\n         created based on entries in the tn3270eRtCollCtlTable.')
tn3270eRtDataEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1), ).setIndexNames((0, "TN3270E-RT-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-RT-MIB", "tn3270eClientGroupName"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddrType"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddress"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientPort"))
if mibBuilder.loadTexts: tn3270eRtDataEntry.setDescription('Entries in this table are created based upon the\n        tn3270eRtCollCtlTable.  When the corresponding\n        tn3270eRtCollCtlType has aggregate(0) specified, a single\n        entry is created in this table, with a tn3270eRtDataClientAddrType\n        of unknown(0), a zero-length octet string value for\n        tn3270eRtDataClientAddress, and a tn3270eRtDataClientPort value of\n        0.  When aggregate(0) is not specified, a separate entry is\n        created for each client in the group.\n\n        Note that the following objects defined within an entry in this\n        table can  wrap:\n            tn3270eRtDataTotalRts\n            tn3270eRtDataTotalIpRts\n            tn3270eRtDataCountTrans\n            tn3270eRtDataCountDrs\n            tn3270eRtDataElapsRnTrpSq\n            tn3270eRtDataElapsIpRtSq\n            tn3270eRtDataBucket1Rts\n            tn3270eRtDataBucket2Rts\n            tn3270eRtDataBucket3Rts\n            tn3270eRtDataBucket4Rts\n            tn3270eRtDataBucket5Rts')
tn3270eRtDataClientAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 1), IANATn3270eAddrType())
if mibBuilder.loadTexts: tn3270eRtDataClientAddrType.setDescription('Indicates the type of address represented by the value\n        of tn3270eRtDataClientAddress.  The value unknown(0) is\n        used if aggregate data is being collected for the client\n        group.')
tn3270eRtDataClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 2), IANATn3270eAddress())
if mibBuilder.loadTexts: tn3270eRtDataClientAddress.setDescription('Contains the IP address of the TN3270 client being\n        monitored.  A zero-length octet string is used if\n        aggregate data is being collected for the client group.')
tn3270eRtDataClientPort = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0,65535)))
if mibBuilder.loadTexts: tn3270eRtDataClientPort.setDescription('Contains the client port number of the TN3270 client being\n        monitored.  The value 0 is used if aggregate data is being\n        collected for the client group, or if the\n        tn3270eRtDataClientAddrType identifies an address type that\n        does not support ports.')
tn3270eRtDataAvgRt = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 4), Gauge32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgRt.setDescription('The average total response time measured over the last\n        collection interval.')
tn3270eRtDataAvgIpRt = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 5), Gauge32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgIpRt.setDescription('The average IP response time measured over the last\n        collection interval.')
tn3270eRtDataAvgCountTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 6), Gauge32()).setUnits('transactions').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgCountTrans.setDescription('The sliding transaction count used for calculating the\n        values of the tn3270eRtDataAvgRt and tn3270eRtDataAvgIpRt\n        objects.  The actual transaction count is available in\n        the tn3270eRtDataCountTrans object.\n\n        The initial value of this object, before any averages have\n        been calculated, is 0.')
tn3270eRtDataIntTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataIntTimeStamp.setDescription('The date and time of the last interval that\n        tn3270eRtDataAvgRt, tn3270eRtDataAvgIpRt, and\n        tn3270eRtDataAvgCountTrans were calculated.\n\n        Prior to the calculation of the first interval\n        averages, this object returns the value\n        0x0000000000000000000000.  When this value is\n        returned, the remaining objects in the entry have\n        no significance.')
tn3270eRtDataTotalRts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 8), Counter32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataTotalRts.setDescription('The count of the total response times collected.\n\n        A management application can detect discontinuities in this\n        counter by monitoring the tn3270eRtDataDiscontinuityTime\n        object.')
tn3270eRtDataTotalIpRts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 9), Counter32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataTotalIpRts.setDescription('The count of the total IP-network response times\n        collected.\n\n        A management application can detect discontinuities in this\n        counter by monitoring the tn3270eRtDataDiscontinuityTime\n        object.')
tn3270eRtDataCountTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 10), Counter32()).setUnits('transactions').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataCountTrans.setDescription('The count of the total number of transactions detected.\n\n        A management application can detect discontinuities in this\n        counter by monitoring the tn3270eRtDataDiscontinuityTime\n        object.')
tn3270eRtDataCountDrs = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 11), Counter32()).setUnits('definite responses').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataCountDrs.setDescription('The count of the total number of definite responses\n        detected.\n\n        A management application can detect discontinuities in this\n        counter by monitoring the tn3270eRtDataDiscontinuityTime\n        object.')
tn3270eRtDataElapsRndTrpSq = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 12), Unsigned32()).setUnits('tenths of seconds squared').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataElapsRndTrpSq.setDescription('The sum of the elapsed round trip time squared.  The sum\n        of the squares is kept in order to enable calculation of\n        a variance.')
tn3270eRtDataElapsIpRtSq = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 13), Unsigned32()).setUnits('tenths of seconds squared').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataElapsIpRtSq.setDescription('The sum of the elapsed IP round trip time squared.\n        The sum of the squares is kept in order to enable\n        calculation of a variance.')
tn3270eRtDataBucket1Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket1Rts.setDescription('The count of the response times falling into bucket 1.\n\n        A management application can detect discontinuities in this\n        counter by monitoring the tn3270eRtDataDiscontinuityTime\n        object.')
tn3270eRtDataBucket2Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket2Rts.setDescription('The count of the response times falling into bucket 2.\n\n        A management application can detect discontinuities in this\n        counter by monitoring the tn3270eRtDataDiscontinuityTime\n        object.')
tn3270eRtDataBucket3Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket3Rts.setDescription('The count of the response times falling into bucket 3.\n\n        A management application can detect discontinuities in this\n        counter by monitoring the tn3270eRtDataDiscontinuityTime\n        object.')
tn3270eRtDataBucket4Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket4Rts.setDescription('The count of the response times falling into bucket 4.\n\n        A management application can detect discontinuities in this\n        counter by monitoring the tn3270eRtDataDiscontinuityTime\n        object.')
tn3270eRtDataBucket5Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket5Rts.setDescription('The count of the response times falling into bucket 5.\n\n        A management application can detect discontinuities in this\n        counter by monitoring the tn3270eRtDataDiscontinuityTime\n        object.')
tn3270eRtDataRtMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2,)).clone(namedValues=NamedValues(("none", 0), ("responses", 1), ("timingMark", 2),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataRtMethod.setDescription("The value of this object indicates the method that was\n        used in calculating the IP network time.\n\n        The value 'none(0) indicates that response times were not\n        calculated for the IP network.")
tn3270eRtDataDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 20), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at\n          which one or more of this entry's counter objects\n          suffered a discontinuity.  This may happen if a TN3270E\n          server is stopped and then restarted, and local methods\n          are used to set up collection policy\n          (tn3270eRtCollCtlTable entries).")
tn3270eRtSpinLock = MibScalar((1, 3, 6, 1, 2, 1, 34, 9, 1, 3), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tn3270eRtSpinLock.setDescription('An advisory lock used to allow cooperating TN3270E-RT-MIB\n        applications to coordinate their use of the\n        tn3270eRtCollCtlTable.\n        When creating a new entry or altering an existing entry\n        in the tn3270eRtCollCtlTable, an application should make\n        use of tn3270eRtSpinLock to serialize application changes\n        or additions.\n\n        Since this is an advisory lock, the use of this lock is\n        not enforced.')
tn3270eRtExceeded = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 1)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"),))
if mibBuilder.loadTexts: tn3270eRtExceeded.setDescription('This notification is generated when the average response\n        time, tn3270eRtDataAvgRt, exceeds\n        tn3270eRtCollCtlThresholdHigh at the end of a collection\n        interval specified by tn3270eCollCtlSPeriod\n        times tn3270eCollCtlSPMult.  Note that the corresponding\n        tn3270eCollCtlType must have traps(5) and average(3) set\n        for this notification to be generated.  In addition,\n        tn3270eRtDataAvgCountTrans, tn3270eRtCollCtlThreshHigh, and\n        tn3270eRtDataAvgRt are algorithmically compared to\n        tn3270eRtCollCtlIdleCount for determination if this\n        notification will be suppressed.')
tn3270eRtOkay = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 2)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"),))
if mibBuilder.loadTexts: tn3270eRtOkay.setDescription('This notification is generated when the average response\n        time, tn3270eRtDataAvgRt, falls below\n        tn3270eRtCollCtlThresholdLow at the end of a collection\n        interval specified by tn3270eCollCtlSPeriod times\n        tn3270eCollCtlSPMult, after a tn3270eRtExceeded\n        notification was generated.  Note that the corresponding\n        tn3270eCollCtlType must have traps(5) and average(3)\n        set for this notification to be generated.')
tn3270eRtCollStart = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 3)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eResMapElementType"),))
if mibBuilder.loadTexts: tn3270eRtCollStart.setDescription('This notification is generated when response time data\n        collection is enabled for a member of a client group.\n        In order for this notification to occur the corresponding\n        tn3270eRtCollCtlType must have traps(5) selected.\n\n        tn3270eResMapElementType contains a valid value only if\n        tn3270eRtDataClientAddress contains a valid address\n        (rather than a zero-length octet string).')
tn3270eRtCollEnd = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 4)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"),))
if mibBuilder.loadTexts: tn3270eRtCollEnd.setDescription("This notification is generated when an tn3270eRtDataEntry\n        is deleted after being active (actual data collected), in\n        order to enable a management application monitoring an\n        tn3270eRtDataEntry to get the entry's final values.  Note\n        that the corresponding tn3270eCollCtlType must have traps(5)\n        set for this notification to be generated.")
tn3270eRtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3, 1))
tn3270eRtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3, 2))
tn3270eRtCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 9, 3, 2, 1)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtGroup"), ("TN3270E-RT-MIB", "tn3270eRtNotGroup"),))
if mibBuilder.loadTexts: tn3270eRtCompliance.setDescription('The compliance statement for agents that support the\n        TN327E-RT-MIB.')
tn3270eRtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 1)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtCollCtlType"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPeriod"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPMult"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshHigh"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshLow"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlIdleCount"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry1"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry2"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry3"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry4"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlRowStatus"), ("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtSpinLock"),))
if mibBuilder.loadTexts: tn3270eRtGroup.setDescription('This group is mandatory for all implementations that\n        support the TN3270E-RT-MIB. ')
tn3270eRtNotGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 2)).setObjects(*(("TN3270E-RT-MIB", "tn3270eRtExceeded"), ("TN3270E-RT-MIB", "tn3270eRtOkay"), ("TN3270E-RT-MIB", "tn3270eRtCollStart"), ("TN3270E-RT-MIB", "tn3270eRtCollEnd"),))
if mibBuilder.loadTexts: tn3270eRtNotGroup.setDescription('The notifications that must be supported when the\n        TN3270E-RT-MIB is implemented. ')
mibBuilder.exportSymbols("TN3270E-RT-MIB", tn3270eRtCollCtlBucketBndry3=tn3270eRtCollCtlBucketBndry3, tn3270eRtDataAvgCountTrans=tn3270eRtDataAvgCountTrans, tn3270eRtNotGroup=tn3270eRtNotGroup, tn3270eRtCollEnd=tn3270eRtCollEnd, tn3270eRtOkay=tn3270eRtOkay, tn3270eRtDataTotalIpRts=tn3270eRtDataTotalIpRts, tn3270eRtDataClientPort=tn3270eRtDataClientPort, tn3270eRtDataElapsIpRtSq=tn3270eRtDataElapsIpRtSq, tn3270eRtDataClientAddress=tn3270eRtDataClientAddress, tn3270eRtCollCtlSPeriod=tn3270eRtCollCtlSPeriod, tn3270eRtCollCtlTable=tn3270eRtCollCtlTable, tn3270eRtDataCountDrs=tn3270eRtDataCountDrs, tn3270eRtDataTable=tn3270eRtDataTable, tn3270eRtGroup=tn3270eRtGroup, tn3270eRtCompliances=tn3270eRtCompliances, tn3270eRtDataBucket3Rts=tn3270eRtDataBucket3Rts, tn3270eRtDataCountTrans=tn3270eRtDataCountTrans, tn3270eRtCollCtlBucketBndry4=tn3270eRtCollCtlBucketBndry4, tn3270eRtDataClientAddrType=tn3270eRtDataClientAddrType, tn3270eRtDataBucket1Rts=tn3270eRtDataBucket1Rts, tn3270eRtCollStart=tn3270eRtCollStart, tn3270eRtMIB=tn3270eRtMIB, tn3270eRtDataTotalRts=tn3270eRtDataTotalRts, tn3270eRtCollCtlThreshLow=tn3270eRtCollCtlThreshLow, tn3270eRtCollCtlType=tn3270eRtCollCtlType, tn3270eRtDataDiscontinuityTime=tn3270eRtDataDiscontinuityTime, tn3270eRtSpinLock=tn3270eRtSpinLock, tn3270eRtCollCtlRowStatus=tn3270eRtCollCtlRowStatus, tn3270eRtObjects=tn3270eRtObjects, tn3270eRtConformance=tn3270eRtConformance, tn3270eRtDataRtMethod=tn3270eRtDataRtMethod, PYSNMP_MODULE_ID=tn3270eRtMIB, tn3270eRtDataEntry=tn3270eRtDataEntry, tn3270eRtCollCtlSPMult=tn3270eRtCollCtlSPMult, tn3270eRtDataElapsRndTrpSq=tn3270eRtDataElapsRndTrpSq, tn3270eRtGroups=tn3270eRtGroups, tn3270eRtCompliance=tn3270eRtCompliance, tn3270eRtDataAvgIpRt=tn3270eRtDataAvgIpRt, tn3270eRtCollCtlThreshHigh=tn3270eRtCollCtlThreshHigh, tn3270eRtExceeded=tn3270eRtExceeded, tn3270eRtDataBucket5Rts=tn3270eRtDataBucket5Rts, tn3270eRtCollCtlIdleCount=tn3270eRtCollCtlIdleCount, tn3270eRtCollCtlBucketBndry1=tn3270eRtCollCtlBucketBndry1, tn3270eRtDataBucket2Rts=tn3270eRtDataBucket2Rts, tn3270eRtNotifications=tn3270eRtNotifications, tn3270eRtDataAvgRt=tn3270eRtDataAvgRt, tn3270eRtDataBucket4Rts=tn3270eRtDataBucket4Rts, tn3270eRtCollCtlEntry=tn3270eRtCollCtlEntry, tn3270eRtDataIntTimeStamp=tn3270eRtDataIntTimeStamp, tn3270eRtCollCtlBucketBndry2=tn3270eRtCollCtlBucketBndry2)
