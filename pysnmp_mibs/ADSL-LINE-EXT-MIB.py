# PySNMP SMI module. Autogenerated from smidump -f python ADSL-LINE-EXT-MIB
# by libsmi2pysnmp-0.0.6-alpha at Thu Apr  6 13:19:05 2006,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( adslAtucIntervalEntry, adslAtucPerfDataEntry, adslAturIntervalEntry, adslAturPerfDataEntry, adslLineAlarmConfProfileEntry, adslLineConfProfileEntry, adslLineEntry, adslMIB, ) = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAtucIntervalEntry", "adslAtucPerfDataEntry", "adslAturIntervalEntry", "adslAturPerfDataEntry", "adslLineAlarmConfProfileEntry", "adslLineConfProfileEntry", "adslLineEntry", "adslMIB")
( AdslPerfCurrDayCount, AdslPerfPrevDayCount, ) = mibBuilder.importSymbols("ADSL-TC-MIB", "AdslPerfCurrDayCount", "AdslPerfPrevDayCount")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( PerfCurrentCount, PerfIntervalCount, ) = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class AdslTransmissionModeType(Bits):
    namedValues = namedval.NamedValues(("ansit1413", 0), ("etsi", 1), ("q9922tcmIsdnNonOverlapped", 10), ("q9922tcmIsdnOverlapped", 11), ("q9921tcmIsdnSymmetric", 12), ("q9921PotsNonOverlapped", 2), ("q9921PotsOverlapped", 3), ("q9921IsdnNonOverlapped", 4), ("q9921isdnOverlapped", 5), ("q9921tcmIsdnNonOverlapped", 6), ("q9921tcmIsdnOverlapped", 7), ("q9922potsNonOverlapeed", 8), ("q9922potsOverlapped", 9), )
    pass


# Objects

adslExtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 94, 3)).setRevisions(("2002-12-10 00:00",))
adslExtMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1))
adslLineExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17))
adslLineExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1))
adslLineTransAtucCap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 1), AdslTransmissionModeType()).setMaxAccess("readonly")
adslLineTransAtucConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 2), AdslTransmissionModeType()).setMaxAccess("readwrite")
adslLineTransAtucActual = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 3), AdslTransmissionModeType()).setMaxAccess("readonly")
adslLineGlitePowerState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,4,2,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("l0", 2), ("l1", 3), ("l3", 4), ))).setMaxAccess("readonly")
adslLineConfProfileDualLite = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 5), SnmpAdminString()).setMaxAccess("readwrite")
adslAtucPerfDataExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18))
adslAtucPerfDataExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1))
adslAtucPerfStatFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 1), Counter32()).setMaxAccess("readonly")
adslAtucPerfStatFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 2), Counter32()).setMaxAccess("readonly")
adslAtucPerfStatSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 3), Counter32()).setMaxAccess("readonly")
adslAtucPerfStatUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 4), Counter32()).setMaxAccess("readonly")
adslAtucPerfCurr15MinFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
adslAtucPerfCurr15MinFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
adslAtucPerfCurr15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 7), PerfCurrentCount()).setMaxAccess("readonly")
adslAtucPerfCurr15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 8), PerfCurrentCount()).setMaxAccess("readonly")
adslAtucPerfCurr1DayFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 9), AdslPerfCurrDayCount()).setMaxAccess("readonly")
adslAtucPerfCurr1DayFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 10), AdslPerfCurrDayCount()).setMaxAccess("readonly")
adslAtucPerfCurr1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 11), AdslPerfCurrDayCount()).setMaxAccess("readonly")
adslAtucPerfCurr1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 12), AdslPerfCurrDayCount()).setMaxAccess("readonly")
adslAtucPerfPrev1DayFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 13), AdslPerfPrevDayCount()).setMaxAccess("readonly")
adslAtucPerfPrev1DayFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 14), AdslPerfPrevDayCount()).setMaxAccess("readonly")
adslAtucPerfPrev1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 15), AdslPerfPrevDayCount()).setMaxAccess("readonly")
adslAtucPerfPrev1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 16), AdslPerfPrevDayCount()).setMaxAccess("readonly")
adslAtucIntervalExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19))
adslAtucIntervalExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1))
adslAtucIntervalFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
adslAtucIntervalFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
adslAtucIntervalSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
adslAtucIntervalUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
adslAturPerfDataExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20))
adslAturPerfDataExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1))
adslAturPerfStatSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 1), Counter32()).setMaxAccess("readonly")
adslAturPerfStatUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 2), Counter32()).setMaxAccess("readonly")
adslAturPerfCurr15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
adslAturPerfCurr15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
adslAturPerfCurr1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 5), AdslPerfCurrDayCount()).setMaxAccess("readonly")
adslAturPerfCurr1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 6), AdslPerfCurrDayCount()).setMaxAccess("readonly")
adslAturPerfPrev1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 7), AdslPerfPrevDayCount()).setMaxAccess("readonly")
adslAturPerfPrev1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 8), AdslPerfPrevDayCount()).setMaxAccess("readonly")
adslAturIntervalExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21))
adslAturIntervalExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1))
adslAturIntervalSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
adslAturIntervalUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
adslConfProfileExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22))
adslConfProfileExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22, 1))
adslConfProfileLineType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,4,5,)).subtype(namedValues=namedval.NamedValues(("noChannel", 1), ("fastOnly", 2), ("interleavedOnly", 3), ("fastOrInterleaved", 4), ("fastAndInterleaved", 5), )).clone(2)).setMaxAccess("readwrite")
adslAlarmConfProfileExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23))
adslAlarmConfProfileExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1))
adslAtucThreshold15MinFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 900)).clone(0)).setMaxAccess("readwrite")
adslAtucThreshold15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 900)).clone(0)).setMaxAccess("readwrite")
adslAtucThreshold15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 900)).clone(0)).setMaxAccess("readwrite")
adslAturThreshold15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 900)).clone(0)).setMaxAccess("readwrite")
adslAturThreshold15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 900)).clone(0)).setMaxAccess("readwrite")
adslExtTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24))
adslExtAtucTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1))
adslExtAtucTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0))
adslExtAturTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2))
adslExtAturTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0))
adslExtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 2))
adslExtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1))
adslExtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 2))

# Augmentions
adslLineConfProfileEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslLineConfProfileEntry")
adslLineConfProfileEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslConfProfileExtEntry"))
apply(adslConfProfileExtEntry.setIndexNames, adslLineConfProfileEntry.getIndexNames())
adslLineEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslLineEntry")
adslLineEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslLineExtEntry"))
apply(adslLineExtEntry.setIndexNames, adslLineEntry.getIndexNames())
adslAtucPerfDataEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAtucPerfDataEntry")
adslAtucPerfDataEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAtucPerfDataExtEntry"))
apply(adslAtucPerfDataExtEntry.setIndexNames, adslAtucPerfDataEntry.getIndexNames())
adslAturIntervalEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAturIntervalEntry")
adslAturIntervalEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAturIntervalExtEntry"))
apply(adslAturIntervalExtEntry.setIndexNames, adslAturIntervalEntry.getIndexNames())
adslAturPerfDataEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAturPerfDataEntry")
adslAturPerfDataEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAturPerfDataExtEntry"))
apply(adslAturPerfDataExtEntry.setIndexNames, adslAturPerfDataEntry.getIndexNames())
adslLineAlarmConfProfileEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslLineAlarmConfProfileEntry")
adslLineAlarmConfProfileEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAlarmConfProfileExtEntry"))
apply(adslAlarmConfProfileExtEntry.setIndexNames, adslLineAlarmConfProfileEntry.getIndexNames())
adslAtucIntervalEntry, = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAtucIntervalEntry")
adslAtucIntervalEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAtucIntervalExtEntry"))
apply(adslAtucIntervalExtEntry.setIndexNames, adslAtucIntervalEntry.getIndexNames())

# Notifications

adslAtucFailedFastRThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 1)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFailedFastR"), )
adslAturUasLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0, 2)).setObjects(("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinUasL"), )
adslAturSesLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0, 1)).setObjects(("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinSesL"), )
adslAtucSesLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 2)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinSesL"), )
adslAtucUasLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 3)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinUasL"), )

# Groups

adslExtAturPhysPerfCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 3)).setObjects(("ADSL-LINE-EXT-MIB", "adslAturPerfStatUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfPrev1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAturIntervalUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfStatSesL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfPrev1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinSesL"), ("ADSL-LINE-EXT-MIB", "adslAturIntervalSesL"), )
adslExtLineConfProfileControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 4)).setObjects(("ADSL-LINE-EXT-MIB", "adslConfProfileLineType"), )
adslExtLineAlarmConfProfileGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 5)).setObjects(("ADSL-LINE-EXT-MIB", "adslAturThreshold15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAturThreshold15MinSesL"), )
adslExtAtucPhysPerfCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 2)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatFastR"), )
adslExtLineGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 1)).setObjects(("ADSL-LINE-EXT-MIB", "adslLineConfProfileDualLite"), ("ADSL-LINE-EXT-MIB", "adslLineTransAtucConfig"), ("ADSL-LINE-EXT-MIB", "adslLineGlitePowerState"), ("ADSL-LINE-EXT-MIB", "adslLineTransAtucCap"), ("ADSL-LINE-EXT-MIB", "adslLineTransAtucActual"), )
adslExtNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 6)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucFailedFastRThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAturUasLThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAturSesLThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAtucSesLThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAtucUasLThreshTrap"), )

# Exports

# Module identity
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", PYSNMP_MODULE_ID=adslExtMIB)

# Types
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", AdslTransmissionModeType=AdslTransmissionModeType)

# Objects
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", adslExtMIB=adslExtMIB, adslExtMibObjects=adslExtMibObjects, adslLineExtTable=adslLineExtTable, adslLineExtEntry=adslLineExtEntry, adslLineTransAtucCap=adslLineTransAtucCap, adslLineTransAtucConfig=adslLineTransAtucConfig, adslLineTransAtucActual=adslLineTransAtucActual, adslLineGlitePowerState=adslLineGlitePowerState, adslLineConfProfileDualLite=adslLineConfProfileDualLite, adslAtucPerfDataExtTable=adslAtucPerfDataExtTable, adslAtucPerfDataExtEntry=adslAtucPerfDataExtEntry, adslAtucPerfStatFastR=adslAtucPerfStatFastR, adslAtucPerfStatFailedFastR=adslAtucPerfStatFailedFastR, adslAtucPerfStatSesL=adslAtucPerfStatSesL, adslAtucPerfStatUasL=adslAtucPerfStatUasL, adslAtucPerfCurr15MinFastR=adslAtucPerfCurr15MinFastR, adslAtucPerfCurr15MinFailedFastR=adslAtucPerfCurr15MinFailedFastR, adslAtucPerfCurr15MinSesL=adslAtucPerfCurr15MinSesL, adslAtucPerfCurr15MinUasL=adslAtucPerfCurr15MinUasL, adslAtucPerfCurr1DayFastR=adslAtucPerfCurr1DayFastR, adslAtucPerfCurr1DayFailedFastR=adslAtucPerfCurr1DayFailedFastR, adslAtucPerfCurr1DaySesL=adslAtucPerfCurr1DaySesL, adslAtucPerfCurr1DayUasL=adslAtucPerfCurr1DayUasL, adslAtucPerfPrev1DayFastR=adslAtucPerfPrev1DayFastR, adslAtucPerfPrev1DayFailedFastR=adslAtucPerfPrev1DayFailedFastR, adslAtucPerfPrev1DaySesL=adslAtucPerfPrev1DaySesL, adslAtucPerfPrev1DayUasL=adslAtucPerfPrev1DayUasL, adslAtucIntervalExtTable=adslAtucIntervalExtTable, adslAtucIntervalExtEntry=adslAtucIntervalExtEntry, adslAtucIntervalFastR=adslAtucIntervalFastR, adslAtucIntervalFailedFastR=adslAtucIntervalFailedFastR, adslAtucIntervalSesL=adslAtucIntervalSesL, adslAtucIntervalUasL=adslAtucIntervalUasL, adslAturPerfDataExtTable=adslAturPerfDataExtTable, adslAturPerfDataExtEntry=adslAturPerfDataExtEntry, adslAturPerfStatSesL=adslAturPerfStatSesL, adslAturPerfStatUasL=adslAturPerfStatUasL, adslAturPerfCurr15MinSesL=adslAturPerfCurr15MinSesL, adslAturPerfCurr15MinUasL=adslAturPerfCurr15MinUasL, adslAturPerfCurr1DaySesL=adslAturPerfCurr1DaySesL, adslAturPerfCurr1DayUasL=adslAturPerfCurr1DayUasL, adslAturPerfPrev1DaySesL=adslAturPerfPrev1DaySesL, adslAturPerfPrev1DayUasL=adslAturPerfPrev1DayUasL, adslAturIntervalExtTable=adslAturIntervalExtTable, adslAturIntervalExtEntry=adslAturIntervalExtEntry, adslAturIntervalSesL=adslAturIntervalSesL, adslAturIntervalUasL=adslAturIntervalUasL, adslConfProfileExtTable=adslConfProfileExtTable, adslConfProfileExtEntry=adslConfProfileExtEntry, adslConfProfileLineType=adslConfProfileLineType, adslAlarmConfProfileExtTable=adslAlarmConfProfileExtTable, adslAlarmConfProfileExtEntry=adslAlarmConfProfileExtEntry, adslAtucThreshold15MinFailedFastR=adslAtucThreshold15MinFailedFastR, adslAtucThreshold15MinSesL=adslAtucThreshold15MinSesL, adslAtucThreshold15MinUasL=adslAtucThreshold15MinUasL, adslAturThreshold15MinSesL=adslAturThreshold15MinSesL, adslAturThreshold15MinUasL=adslAturThreshold15MinUasL, adslExtTraps=adslExtTraps, adslExtAtucTraps=adslExtAtucTraps, adslExtAtucTrapsPrefix=adslExtAtucTrapsPrefix, adslExtAturTraps=adslExtAturTraps, adslExtAturTrapsPrefix=adslExtAturTrapsPrefix, adslExtConformance=adslExtConformance, adslExtGroups=adslExtGroups, adslExtCompliances=adslExtCompliances)

# Notifications
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", adslAtucFailedFastRThreshTrap=adslAtucFailedFastRThreshTrap, adslAturUasLThreshTrap=adslAturUasLThreshTrap, adslAturSesLThreshTrap=adslAturSesLThreshTrap, adslAtucSesLThreshTrap=adslAtucSesLThreshTrap, adslAtucUasLThreshTrap=adslAtucUasLThreshTrap)

# Groups
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", adslExtAturPhysPerfCounterGroup=adslExtAturPhysPerfCounterGroup, adslExtLineConfProfileControlGroup=adslExtLineConfProfileControlGroup, adslExtLineAlarmConfProfileGroup=adslExtLineAlarmConfProfileGroup, adslExtAtucPhysPerfCounterGroup=adslExtAtucPhysPerfCounterGroup, adslExtLineGroup=adslExtLineGroup, adslExtNotificationsGroup=adslExtNotificationsGroup)
