# PySNMP SMI module. Autogenerated from smidump -f python DS1-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:15 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( PerfCurrentCount, PerfIntervalCount, PerfTotalCount, ) = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( DisplayString, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TruthValue")

# Objects

ds1 = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 18))
dsx1ConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 6))
dsx1ConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 6, 1)).setIndexNames((0, "DS1-MIB", "dsx1LineIndex"))
dsx1LineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
dsx1IfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 2)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
dsx1TimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 3)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 899))).setMaxAccess("readonly"))
dsx1ValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 4)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 96))).setMaxAccess("readonly"))
dsx1LineType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 5)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(7,10,8,9,3,4,2,11,1,6,5,)).addNamedValues(("other", 1), ("dsx1DS2M12", 10), ("dsx2E2", 11), ("dsx1ESF", 2), ("dsx1D4", 3), ("dsx1E1", 4), ("dsx1E1CRC", 5), ("dsx1E1MF", 6), ("dsx1E1CRCMF", 7), ("dsx1Unframed", 8), ("dsx1E1Unframed", 9), )).setMaxAccess("readwrite"))
dsx1LineCoding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 6)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(6,2,3,7,5,1,4,)).addNamedValues(("dsx1JBZS", 1), ("dsx1B8ZS", 2), ("dsx1HDB3", 3), ("dsx1ZBTSI", 4), ("dsx1AMI", 5), ("other", 6), ("dsx1B6ZS", 7), )).setMaxAccess("readwrite"))
dsx1SendCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 7)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(5,2,4,8,3,1,7,6,)).addNamedValues(("dsx1SendNoCode", 1), ("dsx1SendLineCode", 2), ("dsx1SendPayloadCode", 3), ("dsx1SendResetCode", 4), ("dsx1SendQRS", 5), ("dsx1Send511Pattern", 6), ("dsx1Send3in24Pattern", 7), ("dsx1SendOtherTestPattern", 8), )).setMaxAccess("readwrite"))
dsx1CircuitIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 8)).setColumnInitializer(MibVariable((), DisplayString().addConstraints(subtypes.ValueRangeConstraint(0, 255))).setMaxAccess("readwrite"))
dsx1LoopbackConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 9)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(6,5,1,2,3,4,)).addNamedValues(("dsx1NoLoop", 1), ("dsx1PayloadLoop", 2), ("dsx1LineLoop", 3), ("dsx1OtherLoop", 4), ("dsx1InwardLoop", 5), ("dsx1DualLoop", 6), )).setMaxAccess("readwrite"))
dsx1LineStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 10)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 131071))).setMaxAccess("readonly"))
dsx1SignalMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 11)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(1,5,2,4,3,)).addNamedValues(("none", 1), ("robbedBit", 2), ("bitOriented", 3), ("messageOriented", 4), ("other", 5), )).setMaxAccess("readwrite"))
dsx1TransmitClockSource = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 12)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(3,1,2,)).addNamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3), )).setMaxAccess("readwrite"))
dsx1Fdl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 13)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 15))).setMaxAccess("readwrite"))
dsx1InvalidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 14)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 96))).setMaxAccess("readonly"))
dsx1LineLength = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 15)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 64000))).setMaxAccess("readwrite"))
dsx1LineStatusLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 16)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
dsx1LineStatusChangeTrapEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 17)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("enabled", 1), ("disabled", 2), ).set(2)).setMaxAccess("readwrite"))
dsx1LoopbackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 18)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 127))).setMaxAccess("readonly"))
dsx1Ds1ChannelNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 19)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 28))).setMaxAccess("readonly"))
dsx1Channelization = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 6, 1, 20)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(1,3,2,)).addNamedValues(("disabled", 1), ("enabledDs0", 2), ("enabledDs1", 3), )).setMaxAccess("readwrite"))
dsx1CurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 7))
dsx1CurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 7, 1)).setIndexNames((0, "DS1-MIB", "dsx1CurrentIndex"))
dsx1CurrentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
dsx1CurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 2)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1CurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 3)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1CurrentSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 4)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1CurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 5)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1CurrentCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 6)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1CurrentPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 7)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1CurrentLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 8)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1CurrentBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 9)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1CurrentDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 10)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1CurrentLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 7, 1, 11)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1IntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 8))
dsx1IntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 8, 1)).setIndexNames((0, "DS1-MIB", "dsx1IntervalIndex"), (0, "DS1-MIB", "dsx1IntervalNumber"))
dsx1IntervalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
dsx1IntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 2)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 96))).setMaxAccess("readonly"))
dsx1IntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 3)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1IntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 4)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1IntervalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 5)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1IntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 6)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1IntervalCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 7)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1IntervalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 8)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1IntervalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 9)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1IntervalBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 10)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1IntervalDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 11)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1IntervalLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 12)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1IntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 8, 1, 13)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
dsx1TotalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 9))
dsx1TotalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 9, 1)).setIndexNames((0, "DS1-MIB", "dsx1TotalIndex"))
dsx1TotalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
dsx1TotalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 2)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1TotalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 3)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1TotalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 4)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1TotalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 5)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1TotalCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 6)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1TotalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 7)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1TotalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 8)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1TotalBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 9)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1TotalDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 10)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1TotalLCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 9, 1, 11)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1FarEndCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 10))
dsx1FarEndCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 10, 1)).setIndexNames((0, "DS1-MIB", "dsx1FarEndCurrentIndex"))
dsx1FarEndCurrentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
dsx1FarEndTimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 2)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 899))).setMaxAccess("readonly"))
dsx1FarEndValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 3)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 96))).setMaxAccess("readonly"))
dsx1FarEndCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 4)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1FarEndCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 5)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1FarEndCurrentSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 6)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1FarEndCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 7)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1FarEndCurrentCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 8)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1FarEndCurrentLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 9)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1FarEndCurrentPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 10)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1FarEndCurrentBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 11)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1FarEndCurrentDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 12)).setColumnInitializer(MibVariable((), PerfCurrentCount()).setMaxAccess("readonly"))
dsx1FarEndInvalidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 10, 1, 13)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 96))).setMaxAccess("readonly"))
dsx1FarEndIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 11))
dsx1FarEndIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 11, 1)).setIndexNames((0, "DS1-MIB", "dsx1FarEndIntervalIndex"), (0, "DS1-MIB", "dsx1FarEndIntervalNumber"))
dsx1FarEndIntervalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
dsx1FarEndIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 2)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 96))).setMaxAccess("readonly"))
dsx1FarEndIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 3)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1FarEndIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 4)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1FarEndIntervalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 5)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1FarEndIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 6)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1FarEndIntervalCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 7)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1FarEndIntervalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 8)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1FarEndIntervalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 9)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1FarEndIntervalBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 10)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1FarEndIntervalDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 11)).setColumnInitializer(MibVariable((), PerfIntervalCount()).setMaxAccess("readonly"))
dsx1FarEndIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 11, 1, 12)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
dsx1FarEndTotalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 12))
dsx1FarEndTotalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 12, 1)).setIndexNames((0, "DS1-MIB", "dsx1FarEndTotalIndex"))
dsx1FarEndTotalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))
dsx1FarEndTotalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 2)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1FarEndTotalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 3)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1FarEndTotalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 4)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1FarEndTotalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 5)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1FarEndTotalCSSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 6)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1FarEndTotalLESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 7)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1FarEndTotalPCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 8)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1FarEndTotalBESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 9)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1FarEndTotalDMs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 12, 1, 10)).setColumnInitializer(MibVariable((), PerfTotalCount()).setMaxAccess("readonly"))
dsx1FracTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 13))
dsx1FracEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 13, 1)).setIndexNames((0, "DS1-MIB", "dsx1FracIndex"), (0, "DS1-MIB", "dsx1FracNumber"))
dsx1FracIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 13, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly"))
dsx1FracNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 13, 1, 2)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 31))).setMaxAccess("readonly"))
dsx1FracIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 13, 1, 3)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readwrite"))
ds1Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 18, 14))
ds1Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 18, 14, 1))
ds1Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 18, 14, 2))
ds1Traps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 18, 15))
dsx1ChanMappingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 18, 16))
dsx1ChanMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 18, 16, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DS1-MIB", "dsx1Ds1ChannelNumber"))
dsx1ChanMappedIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 18, 16, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("readonly"))

# Augmentions

# Notifications

dsx1LineStatusChange = NotificationType((1, 3, 6, 1, 2, 1, 10, 18, 15, 0, 1)).setObjects(("DS1-MIB", "dsx1LineStatus"), ("DS1-MIB", "dsx1LineStatusLastChange"), )

# Groups

ds1NearEndStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 18, 14, 1, 2)).setObjects(("DS1-MIB", "dsx1TotalUASs"), ("DS1-MIB", "dsx1CurrentSEFSs"), ("DS1-MIB", "dsx1CurrentLESs"), ("DS1-MIB", "dsx1IntervalNumber"), ("DS1-MIB", "dsx1IntervalUASs"), ("DS1-MIB", "dsx1CurrentUASs"), ("DS1-MIB", "dsx1CurrentIndex"), ("DS1-MIB", "dsx1IntervalBESs"), ("DS1-MIB", "dsx1CurrentDMs"), ("DS1-MIB", "dsx1TotalCSSs"), ("DS1-MIB", "dsx1IntervalValidData"), ("DS1-MIB", "dsx1TotalSEFSs"), ("DS1-MIB", "dsx1IntervalLESs"), ("DS1-MIB", "dsx1CurrentBESs"), ("DS1-MIB", "dsx1IntervalLCVs"), ("DS1-MIB", "dsx1TotalDMs"), ("DS1-MIB", "dsx1TotalPCVs"), ("DS1-MIB", "dsx1TotalESs"), ("DS1-MIB", "dsx1CurrentSESs"), ("DS1-MIB", "dsx1TotalLESs"), ("DS1-MIB", "dsx1TotalLCVs"), ("DS1-MIB", "dsx1TotalSESs"), ("DS1-MIB", "dsx1IntervalIndex"), ("DS1-MIB", "dsx1CurrentESs"), ("DS1-MIB", "dsx1IntervalDMs"), ("DS1-MIB", "dsx1TotalBESs"), ("DS1-MIB", "dsx1IntervalESs"), ("DS1-MIB", "dsx1CurrentPCVs"), ("DS1-MIB", "dsx1TotalIndex"), ("DS1-MIB", "dsx1CurrentLCVs"), ("DS1-MIB", "dsx1IntervalCSSs"), ("DS1-MIB", "dsx1IntervalSESs"), ("DS1-MIB", "dsx1IntervalSEFSs"), ("DS1-MIB", "dsx1IntervalPCVs"), ("DS1-MIB", "dsx1CurrentCSSs"), )
ds1FarEndGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 18, 14, 1, 3)).setObjects(("DS1-MIB", "dsx1FarEndTotalESs"), ("DS1-MIB", "dsx1FarEndValidIntervals"), ("DS1-MIB", "dsx1FarEndIntervalUASs"), ("DS1-MIB", "dsx1FarEndTotalSESs"), ("DS1-MIB", "dsx1FarEndIntervalNumber"), ("DS1-MIB", "dsx1FarEndCurrentLESs"), ("DS1-MIB", "dsx1FarEndTimeElapsed"), ("DS1-MIB", "dsx1FarEndTotalUASs"), ("DS1-MIB", "dsx1FarEndTotalPCVs"), ("DS1-MIB", "dsx1FarEndTotalDMs"), ("DS1-MIB", "dsx1FarEndCurrentCSSs"), ("DS1-MIB", "dsx1FarEndCurrentBESs"), ("DS1-MIB", "dsx1FarEndIntervalSESs"), ("DS1-MIB", "dsx1FarEndTotalIndex"), ("DS1-MIB", "dsx1FarEndCurrentIndex"), ("DS1-MIB", "dsx1FarEndIntervalSEFSs"), ("DS1-MIB", "dsx1FarEndIntervalLESs"), ("DS1-MIB", "dsx1FarEndCurrentSEFSs"), ("DS1-MIB", "dsx1FarEndIntervalValidData"), ("DS1-MIB", "dsx1FarEndIntervalPCVs"), ("DS1-MIB", "dsx1FarEndCurrentPCVs"), ("DS1-MIB", "dsx1FarEndTotalCSSs"), ("DS1-MIB", "dsx1FarEndTotalBESs"), ("DS1-MIB", "dsx1FarEndCurrentSESs"), ("DS1-MIB", "dsx1FarEndCurrentESs"), ("DS1-MIB", "dsx1FarEndIntervalBESs"), ("DS1-MIB", "dsx1FarEndIntervalIndex"), ("DS1-MIB", "dsx1FarEndInvalidIntervals"), ("DS1-MIB", "dsx1FarEndCurrentDMs"), ("DS1-MIB", "dsx1FarEndIntervalCSSs"), ("DS1-MIB", "dsx1FarEndTotalSEFSs"), ("DS1-MIB", "dsx1FarEndCurrentUASs"), ("DS1-MIB", "dsx1FarEndIntervalDMs"), ("DS1-MIB", "dsx1FarEndTotalLESs"), ("DS1-MIB", "dsx1FarEndIntervalESs"), )
ds1DS2Group = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 18, 14, 1, 6)).setObjects(("DS1-MIB", "dsx1LineStatus"), ("DS1-MIB", "dsx1LineIndex"), ("DS1-MIB", "dsx1SendCode"), ("DS1-MIB", "dsx1SignalMode"), ("DS1-MIB", "dsx1Channelization"), ("DS1-MIB", "dsx1TransmitClockSource"), ("DS1-MIB", "dsx1LineType"), ("DS1-MIB", "dsx1LineCoding"), )
ds1ChanMappingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 18, 14, 1, 9)).setObjects(("DS1-MIB", "dsx1ChanMappedIfIndex"), )
ds1NearEndOptionalConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 18, 14, 1, 5)).setObjects(("DS1-MIB", "dsx1LineStatusChangeTrapEnable"), ("DS1-MIB", "dsx1LineStatusLastChange"), )
ds1NearEndOptionalTrapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 18, 14, 1, 8)).setObjects(("DS1-MIB", "dsx1LineStatusChange"), )
ds1TransStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 18, 14, 1, 7)).setObjects(("DS1-MIB", "dsx1CurrentSESs"), ("DS1-MIB", "dsx1TotalUASs"), ("DS1-MIB", "dsx1IntervalSESs"), ("DS1-MIB", "dsx1CurrentESs"), ("DS1-MIB", "dsx1TotalSESs"), ("DS1-MIB", "dsx1IntervalUASs"), ("DS1-MIB", "dsx1CurrentUASs"), ("DS1-MIB", "dsx1IntervalESs"), ("DS1-MIB", "dsx1TotalESs"), )
ds1NearEndConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 18, 14, 1, 1)).setObjects(("DS1-MIB", "dsx1LineStatus"), ("DS1-MIB", "dsx1LineIndex"), ("DS1-MIB", "dsx1LineLength"), ("DS1-MIB", "dsx1SendCode"), ("DS1-MIB", "dsx1LoopbackStatus"), ("DS1-MIB", "dsx1TransmitClockSource"), ("DS1-MIB", "dsx1TimeElapsed"), ("DS1-MIB", "dsx1LineCoding"), ("DS1-MIB", "dsx1InvalidIntervals"), ("DS1-MIB", "dsx1CircuitIdentifier"), ("DS1-MIB", "dsx1Channelization"), ("DS1-MIB", "dsx1ValidIntervals"), ("DS1-MIB", "dsx1SignalMode"), ("DS1-MIB", "dsx1Ds1ChannelNumber"), ("DS1-MIB", "dsx1LoopbackConfig"), ("DS1-MIB", "dsx1Fdl"), ("DS1-MIB", "dsx1LineType"), )
ds1DeprecatedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 18, 14, 1, 4)).setObjects(("DS1-MIB", "dsx1IfIndex"), ("DS1-MIB", "dsx1FracIndex"), ("DS1-MIB", "dsx1FracIfIndex"), ("DS1-MIB", "dsx1FracNumber"), )

# Exports

# Objects
mibBuilder.exportSymbols("DS1-MIB", ds1=ds1, dsx1ConfigTable=dsx1ConfigTable, dsx1ConfigEntry=dsx1ConfigEntry, dsx1LineIndex=dsx1LineIndex, dsx1IfIndex=dsx1IfIndex, dsx1TimeElapsed=dsx1TimeElapsed, dsx1ValidIntervals=dsx1ValidIntervals, dsx1LineType=dsx1LineType, dsx1LineCoding=dsx1LineCoding, dsx1SendCode=dsx1SendCode, dsx1CircuitIdentifier=dsx1CircuitIdentifier, dsx1LoopbackConfig=dsx1LoopbackConfig, dsx1LineStatus=dsx1LineStatus, dsx1SignalMode=dsx1SignalMode, dsx1TransmitClockSource=dsx1TransmitClockSource, dsx1Fdl=dsx1Fdl, dsx1InvalidIntervals=dsx1InvalidIntervals, dsx1LineLength=dsx1LineLength, dsx1LineStatusLastChange=dsx1LineStatusLastChange, dsx1LineStatusChangeTrapEnable=dsx1LineStatusChangeTrapEnable, dsx1LoopbackStatus=dsx1LoopbackStatus, dsx1Ds1ChannelNumber=dsx1Ds1ChannelNumber, dsx1Channelization=dsx1Channelization, dsx1CurrentTable=dsx1CurrentTable, dsx1CurrentEntry=dsx1CurrentEntry, dsx1CurrentIndex=dsx1CurrentIndex, dsx1CurrentESs=dsx1CurrentESs, dsx1CurrentSESs=dsx1CurrentSESs, dsx1CurrentSEFSs=dsx1CurrentSEFSs, dsx1CurrentUASs=dsx1CurrentUASs, dsx1CurrentCSSs=dsx1CurrentCSSs, dsx1CurrentPCVs=dsx1CurrentPCVs, dsx1CurrentLESs=dsx1CurrentLESs, dsx1CurrentBESs=dsx1CurrentBESs, dsx1CurrentDMs=dsx1CurrentDMs, dsx1CurrentLCVs=dsx1CurrentLCVs, dsx1IntervalTable=dsx1IntervalTable, dsx1IntervalEntry=dsx1IntervalEntry, dsx1IntervalIndex=dsx1IntervalIndex, dsx1IntervalNumber=dsx1IntervalNumber, dsx1IntervalESs=dsx1IntervalESs, dsx1IntervalSESs=dsx1IntervalSESs, dsx1IntervalSEFSs=dsx1IntervalSEFSs, dsx1IntervalUASs=dsx1IntervalUASs, dsx1IntervalCSSs=dsx1IntervalCSSs, dsx1IntervalPCVs=dsx1IntervalPCVs, dsx1IntervalLESs=dsx1IntervalLESs, dsx1IntervalBESs=dsx1IntervalBESs, dsx1IntervalDMs=dsx1IntervalDMs, dsx1IntervalLCVs=dsx1IntervalLCVs, dsx1IntervalValidData=dsx1IntervalValidData, dsx1TotalTable=dsx1TotalTable, dsx1TotalEntry=dsx1TotalEntry, dsx1TotalIndex=dsx1TotalIndex, dsx1TotalESs=dsx1TotalESs, dsx1TotalSESs=dsx1TotalSESs, dsx1TotalSEFSs=dsx1TotalSEFSs, dsx1TotalUASs=dsx1TotalUASs, dsx1TotalCSSs=dsx1TotalCSSs, dsx1TotalPCVs=dsx1TotalPCVs, dsx1TotalLESs=dsx1TotalLESs, dsx1TotalBESs=dsx1TotalBESs, dsx1TotalDMs=dsx1TotalDMs, dsx1TotalLCVs=dsx1TotalLCVs, dsx1FarEndCurrentTable=dsx1FarEndCurrentTable, dsx1FarEndCurrentEntry=dsx1FarEndCurrentEntry, dsx1FarEndCurrentIndex=dsx1FarEndCurrentIndex, dsx1FarEndTimeElapsed=dsx1FarEndTimeElapsed, dsx1FarEndValidIntervals=dsx1FarEndValidIntervals, dsx1FarEndCurrentESs=dsx1FarEndCurrentESs, dsx1FarEndCurrentSESs=dsx1FarEndCurrentSESs, dsx1FarEndCurrentSEFSs=dsx1FarEndCurrentSEFSs, dsx1FarEndCurrentUASs=dsx1FarEndCurrentUASs, dsx1FarEndCurrentCSSs=dsx1FarEndCurrentCSSs, dsx1FarEndCurrentLESs=dsx1FarEndCurrentLESs, dsx1FarEndCurrentPCVs=dsx1FarEndCurrentPCVs, dsx1FarEndCurrentBESs=dsx1FarEndCurrentBESs, dsx1FarEndCurrentDMs=dsx1FarEndCurrentDMs, dsx1FarEndInvalidIntervals=dsx1FarEndInvalidIntervals, dsx1FarEndIntervalTable=dsx1FarEndIntervalTable, dsx1FarEndIntervalEntry=dsx1FarEndIntervalEntry, dsx1FarEndIntervalIndex=dsx1FarEndIntervalIndex, dsx1FarEndIntervalNumber=dsx1FarEndIntervalNumber, dsx1FarEndIntervalESs=dsx1FarEndIntervalESs, dsx1FarEndIntervalSESs=dsx1FarEndIntervalSESs, dsx1FarEndIntervalSEFSs=dsx1FarEndIntervalSEFSs, dsx1FarEndIntervalUASs=dsx1FarEndIntervalUASs, dsx1FarEndIntervalCSSs=dsx1FarEndIntervalCSSs, dsx1FarEndIntervalLESs=dsx1FarEndIntervalLESs, dsx1FarEndIntervalPCVs=dsx1FarEndIntervalPCVs, dsx1FarEndIntervalBESs=dsx1FarEndIntervalBESs, dsx1FarEndIntervalDMs=dsx1FarEndIntervalDMs, dsx1FarEndIntervalValidData=dsx1FarEndIntervalValidData, dsx1FarEndTotalTable=dsx1FarEndTotalTable, dsx1FarEndTotalEntry=dsx1FarEndTotalEntry, dsx1FarEndTotalIndex=dsx1FarEndTotalIndex, dsx1FarEndTotalESs=dsx1FarEndTotalESs, dsx1FarEndTotalSESs=dsx1FarEndTotalSESs, dsx1FarEndTotalSEFSs=dsx1FarEndTotalSEFSs, dsx1FarEndTotalUASs=dsx1FarEndTotalUASs, dsx1FarEndTotalCSSs=dsx1FarEndTotalCSSs, dsx1FarEndTotalLESs=dsx1FarEndTotalLESs, dsx1FarEndTotalPCVs=dsx1FarEndTotalPCVs, dsx1FarEndTotalBESs=dsx1FarEndTotalBESs, dsx1FarEndTotalDMs=dsx1FarEndTotalDMs, dsx1FracTable=dsx1FracTable, dsx1FracEntry=dsx1FracEntry, dsx1FracIndex=dsx1FracIndex, dsx1FracNumber=dsx1FracNumber, dsx1FracIfIndex=dsx1FracIfIndex, ds1Conformance=ds1Conformance, ds1Groups=ds1Groups, ds1Compliances=ds1Compliances, ds1Traps=ds1Traps, dsx1ChanMappingTable=dsx1ChanMappingTable, dsx1ChanMappingEntry=dsx1ChanMappingEntry, dsx1ChanMappedIfIndex=dsx1ChanMappedIfIndex)

# Notifications
mibBuilder.exportSymbols("DS1-MIB", dsx1LineStatusChange=dsx1LineStatusChange)

# Groups
mibBuilder.exportSymbols("DS1-MIB", ds1NearEndStatisticsGroup=ds1NearEndStatisticsGroup, ds1FarEndGroup=ds1FarEndGroup, ds1DS2Group=ds1DS2Group, ds1ChanMappingGroup=ds1ChanMappingGroup, ds1NearEndOptionalConfigGroup=ds1NearEndOptionalConfigGroup, ds1NearEndOptionalTrapGroup=ds1NearEndOptionalTrapGroup, ds1TransStatsGroup=ds1TransStatsGroup, ds1NearEndConfigGroup=ds1NearEndConfigGroup, ds1DeprecatedGroup=ds1DeprecatedGroup)
