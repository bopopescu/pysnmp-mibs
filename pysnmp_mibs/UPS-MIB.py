# PySNMP SMI module. Autogenerated from smidump -f python UPS-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 19:13:42 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( AutonomousType, DisplayString, TextualConvention, TestAndIncr, TimeInterval, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "DisplayString", "TextualConvention", "TestAndIncr", "TimeInterval", "TimeStamp")

# Types

class NonNegativeInteger(TextualConvention, Integer32):
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class PositiveInteger(TextualConvention, Integer32):
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(1,2147483647L)
    pass


# Objects

upsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 33)).setRevisions(("1994-02-23 00:00",))
upsObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1))
upsIdent = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 1))
upsIdentManufacturer = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
upsIdentModel = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 2), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
upsIdentUPSSoftwareVersion = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
upsIdentAgentSoftwareVersion = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
upsIdentName = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 5), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
upsIdentAttachedDevices = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 1, 6), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
upsBattery = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 2))
upsBatteryStatus = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,4,2,3,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("batteryNormal", 2), ("batteryLow", 3), ("batteryDepleted", 4), ))).setMaxAccess("readonly")
upsSecondsOnBattery = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 2), NonNegativeInteger()).setMaxAccess("readonly").setUnits("seconds")
upsEstimatedMinutesRemaining = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 3), PositiveInteger()).setMaxAccess("readonly").setUnits("minutes")
upsEstimatedChargeRemaining = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 100))).setMaxAccess("readonly").setUnits("percent")
upsBatteryVoltage = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 5), NonNegativeInteger()).setMaxAccess("readonly").setUnits("0.1 Volt DC")
upsBatteryCurrent = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 6), Integer32()).setMaxAccess("readonly").setUnits("0.1 Amp DC")
upsBatteryTemperature = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 2, 7), Integer32()).setMaxAccess("readonly").setUnits("degrees Centigrade")
upsInput = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 3))
upsInputLineBads = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 3, 1), Counter32()).setMaxAccess("readonly")
upsInputNumLines = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 3, 2), NonNegativeInteger()).setMaxAccess("readonly")
upsInputTable = MibTable((1, 3, 6, 1, 2, 1, 33, 1, 3, 3))
upsInputEntry = MibTableRow((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1)).setIndexNames((0, "UPS-MIB", "upsInputLineIndex"))
upsInputLineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 1), PositiveInteger()).setMaxAccess("noaccess")
upsInputFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 2), NonNegativeInteger()).setMaxAccess("readonly")
upsInputVoltage = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 3), NonNegativeInteger()).setMaxAccess("readonly")
upsInputCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 4), NonNegativeInteger()).setMaxAccess("readonly")
upsInputTruePower = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 5), NonNegativeInteger()).setMaxAccess("readonly")
upsOutput = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 4))
upsOutputSource = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 4, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,7,3,5,1,4,6,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("none", 2), ("normal", 3), ("bypass", 4), ("battery", 5), ("booster", 6), ("reducer", 7), ))).setMaxAccess("readonly")
upsOutputFrequency = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 4, 2), NonNegativeInteger()).setMaxAccess("readonly").setUnits("0.1 Hertz")
upsOutputNumLines = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 4, 3), NonNegativeInteger()).setMaxAccess("readonly")
upsOutputTable = MibTable((1, 3, 6, 1, 2, 1, 33, 1, 4, 4))
upsOutputEntry = MibTableRow((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1)).setIndexNames((0, "UPS-MIB", "upsOutputLineIndex"))
upsOutputLineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 1), PositiveInteger()).setMaxAccess("noaccess")
upsOutputVoltage = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 2), NonNegativeInteger()).setMaxAccess("readonly")
upsOutputCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 3), NonNegativeInteger()).setMaxAccess("readonly")
upsOutputPower = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 4), NonNegativeInteger()).setMaxAccess("readonly")
upsOutputPercentLoad = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 200))).setMaxAccess("readonly")
upsBypass = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 5))
upsBypassFrequency = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 5, 1), NonNegativeInteger()).setMaxAccess("readonly").setUnits("0.1 Hertz")
upsBypassNumLines = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 5, 2), NonNegativeInteger()).setMaxAccess("readonly")
upsBypassTable = MibTable((1, 3, 6, 1, 2, 1, 33, 1, 5, 3))
upsBypassEntry = MibTableRow((1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1)).setIndexNames((0, "UPS-MIB", "upsBypassLineIndex"))
upsBypassLineIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 1), PositiveInteger()).setMaxAccess("noaccess")
upsBypassVoltage = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 2), NonNegativeInteger()).setMaxAccess("readonly")
upsBypassCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 3), NonNegativeInteger()).setMaxAccess("readonly")
upsBypassPower = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 4), NonNegativeInteger()).setMaxAccess("readonly")
upsAlarm = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6))
upsAlarmsPresent = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 6, 1), Gauge32()).setMaxAccess("readonly")
upsAlarmTable = MibTable((1, 3, 6, 1, 2, 1, 33, 1, 6, 2))
upsAlarmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1)).setIndexNames((0, "UPS-MIB", "upsAlarmId"))
upsAlarmId = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1, 1), PositiveInteger()).setMaxAccess("noaccess")
upsAlarmDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1, 2), AutonomousType()).setMaxAccess("readonly")
upsAlarmTime = MibTableColumn((1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
upsWellKnownAlarms = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3))
upsAlarmBatteryBad = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 1))
upsAlarmOnBattery = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 2))
upsAlarmLowBattery = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 3))
upsAlarmDepletedBattery = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 4))
upsAlarmTempBad = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 5))
upsAlarmInputBad = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 6))
upsAlarmOutputBad = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 7))
upsAlarmOutputOverload = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 8))
upsAlarmOnBypass = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 9))
upsAlarmBypassBad = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 10))
upsAlarmOutputOffAsRequested = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 11))
upsAlarmUpsOffAsRequested = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 12))
upsAlarmChargerFailed = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 13))
upsAlarmUpsOutputOff = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 14))
upsAlarmUpsSystemOff = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 15))
upsAlarmFanFailure = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 16))
upsAlarmFuseFailure = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 17))
upsAlarmGeneralFault = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 18))
upsAlarmDiagnosticTestFailed = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 19))
upsAlarmCommunicationsLost = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 20))
upsAlarmAwaitingPower = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 21))
upsAlarmShutdownPending = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 22))
upsAlarmShutdownImminent = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 23))
upsAlarmTestInProgress = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 24))
upsTest = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 7))
upsTestId = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 1), ObjectIdentifier()).setMaxAccess("readwrite")
upsTestSpinLock = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 2), TestAndIncr()).setMaxAccess("readwrite")
upsTestResultsSummary = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,4,5,6,)).subtype(namedValues=namedval.NamedValues(("donePass", 1), ("doneWarning", 2), ("doneError", 3), ("aborted", 4), ("inProgress", 5), ("noTestsInitiated", 6), ))).setMaxAccess("readonly")
upsTestResultsDetail = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
upsTestStartTime = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 5), TimeStamp()).setMaxAccess("readonly")
upsTestElapsedTime = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 7, 6), TimeInterval()).setMaxAccess("readonly")
upsWellKnownTests = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 7, 7))
upsTestNoTestsInitiated = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 1))
upsTestAbortTestInProgress = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 2))
upsTestGeneralSystemsTest = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 3))
upsTestQuickBatteryTest = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 4))
upsTestDeepBatteryCalibration = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 5))
upsControl = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 8))
upsShutdownType = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 8, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("output", 1), ("system", 2), ))).setMaxAccess("readwrite")
upsShutdownAfterDelay = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 8, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L))).setMaxAccess("readwrite").setUnits("seconds")
upsStartupAfterDelay = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 8, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 2147483647L))).setMaxAccess("readwrite").setUnits("seconds")
upsRebootWithDuration = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 8, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-1, 300))).setMaxAccess("readwrite").setUnits("seconds")
upsAutoRestart = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 8, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("on", 1), ("off", 2), ))).setMaxAccess("readwrite")
upsConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 1, 9))
upsConfigInputVoltage = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 1), NonNegativeInteger()).setMaxAccess("readwrite").setUnits("RMS Volts")
upsConfigInputFreq = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 2), NonNegativeInteger()).setMaxAccess("readwrite").setUnits("0.1 Hertz")
upsConfigOutputVoltage = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 3), NonNegativeInteger()).setMaxAccess("readwrite").setUnits("RMS Volts")
upsConfigOutputFreq = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 4), NonNegativeInteger()).setMaxAccess("readwrite").setUnits("0.1 Hertz")
upsConfigOutputVA = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 5), NonNegativeInteger()).setMaxAccess("readonly").setUnits("Volt-Amps")
upsConfigOutputPower = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 6), NonNegativeInteger()).setMaxAccess("readonly").setUnits("Watts")
upsConfigLowBattTime = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 7), NonNegativeInteger()).setMaxAccess("readwrite").setUnits("minutes")
upsConfigAudibleStatus = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("disabled", 1), ("enabled", 2), ("muted", 3), ))).setMaxAccess("readwrite")
upsConfigLowVoltageTransferPoint = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 9), NonNegativeInteger()).setMaxAccess("readwrite").setUnits("RMS Volts")
upsConfigHighVoltageTransferPoint = MibScalar((1, 3, 6, 1, 2, 1, 33, 1, 9, 10), NonNegativeInteger()).setMaxAccess("readwrite").setUnits("RMS Volts")
upsTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 2))
upsConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3))
upsCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3, 1))
upsGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3, 2))
upsSubsetGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3, 2, 1))
upsBasicGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3, 2, 2))
upsFullGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 33, 3, 2, 3))

# Augmentions

# Notifications

upsTrapAlarmEntryAdded = NotificationType((1, 3, 6, 1, 2, 1, 33, 2, 3)).setObjects(("UPS-MIB", "upsAlarmId"), ("UPS-MIB", "upsAlarmDescr"), )
upsTrapOnBattery = NotificationType((1, 3, 6, 1, 2, 1, 33, 2, 1)).setObjects(("UPS-MIB", "upsEstimatedMinutesRemaining"), ("UPS-MIB", "upsSecondsOnBattery"), ("UPS-MIB", "upsConfigLowBattTime"), )
upsTrapAlarmEntryRemoved = NotificationType((1, 3, 6, 1, 2, 1, 33, 2, 4)).setObjects(("UPS-MIB", "upsAlarmId"), ("UPS-MIB", "upsAlarmDescr"), )
upsTrapTestCompleted = NotificationType((1, 3, 6, 1, 2, 1, 33, 2, 2)).setObjects(("UPS-MIB", "upsTestStartTime"), ("UPS-MIB", "upsTestElapsedTime"), ("UPS-MIB", "upsTestId"), ("UPS-MIB", "upsTestSpinLock"), ("UPS-MIB", "upsTestResultsSummary"), ("UPS-MIB", "upsTestResultsDetail"), )

# Groups

upsSubsetConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 9)).setObjects(("UPS-MIB", "upsConfigInputFreq"), ("UPS-MIB", "upsConfigOutputFreq"), ("UPS-MIB", "upsConfigOutputVA"), ("UPS-MIB", "upsConfigOutputVoltage"), ("UPS-MIB", "upsConfigOutputPower"), ("UPS-MIB", "upsConfigInputVoltage"), )
upsFullConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 9)).setObjects(("UPS-MIB", "upsConfigInputFreq"), ("UPS-MIB", "upsConfigLowBattTime"), ("UPS-MIB", "upsConfigOutputFreq"), ("UPS-MIB", "upsConfigOutputVA"), ("UPS-MIB", "upsConfigOutputVoltage"), ("UPS-MIB", "upsConfigOutputPower"), ("UPS-MIB", "upsConfigInputVoltage"), ("UPS-MIB", "upsConfigAudibleStatus"), )
upsBasicTestGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 7)).setObjects(("UPS-MIB", "upsTestStartTime"), ("UPS-MIB", "upsTestElapsedTime"), ("UPS-MIB", "upsTestId"), ("UPS-MIB", "upsTestSpinLock"), ("UPS-MIB", "upsTestResultsSummary"), ("UPS-MIB", "upsTestResultsDetail"), )
upsFullControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 8)).setObjects(("UPS-MIB", "upsRebootWithDuration"), ("UPS-MIB", "upsAutoRestart"), ("UPS-MIB", "upsShutdownType"), ("UPS-MIB", "upsStartupAfterDelay"), ("UPS-MIB", "upsShutdownAfterDelay"), )
upsSubsetBatteryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 2)).setObjects(("UPS-MIB", "upsSecondsOnBattery"), ("UPS-MIB", "upsBatteryStatus"), )
upsBasicIdentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 1)).setObjects(("UPS-MIB", "upsIdentAgentSoftwareVersion"), ("UPS-MIB", "upsIdentUPSSoftwareVersion"), ("UPS-MIB", "upsIdentManufacturer"), ("UPS-MIB", "upsIdentModel"), ("UPS-MIB", "upsIdentName"), )
upsBasicOutputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 4)).setObjects(("UPS-MIB", "upsOutputNumLines"), ("UPS-MIB", "upsOutputFrequency"), ("UPS-MIB", "upsOutputSource"), ("UPS-MIB", "upsOutputVoltage"), )
upsBasicInputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 3)).setObjects(("UPS-MIB", "upsInputFrequency"), ("UPS-MIB", "upsInputVoltage"), ("UPS-MIB", "upsInputLineBads"), ("UPS-MIB", "upsInputNumLines"), )
upsSubsetOutputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 4)).setObjects(("UPS-MIB", "upsOutputSource"), )
upsBasicBypassGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 5)).setObjects(("UPS-MIB", "upsBypassFrequency"), ("UPS-MIB", "upsBypassVoltage"), ("UPS-MIB", "upsBypassNumLines"), )
upsFullBypassGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 5)).setObjects(("UPS-MIB", "upsBypassFrequency"), ("UPS-MIB", "upsBypassVoltage"), ("UPS-MIB", "upsBypassNumLines"), )
upsSubsetInputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 3)).setObjects(("UPS-MIB", "upsInputLineBads"), )
upsBasicBatteryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 2)).setObjects(("UPS-MIB", "upsSecondsOnBattery"), ("UPS-MIB", "upsBatteryStatus"), )
upsBasicAlarmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 6)).setObjects(("UPS-MIB", "upsAlarmsPresent"), ("UPS-MIB", "upsAlarmTime"), ("UPS-MIB", "upsAlarmDescr"), )
upsFullAlarmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 6)).setObjects(("UPS-MIB", "upsAlarmsPresent"), ("UPS-MIB", "upsAlarmTime"), ("UPS-MIB", "upsAlarmDescr"), )
upsFullIdentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 1)).setObjects(("UPS-MIB", "upsIdentAgentSoftwareVersion"), ("UPS-MIB", "upsIdentName"), ("UPS-MIB", "upsIdentUPSSoftwareVersion"), ("UPS-MIB", "upsIdentManufacturer"), ("UPS-MIB", "upsIdentModel"), ("UPS-MIB", "upsIdentAttachedDevices"), )
upsSubsetControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 8)).setObjects(("UPS-MIB", "upsAutoRestart"), ("UPS-MIB", "upsShutdownType"), ("UPS-MIB", "upsShutdownAfterDelay"), )
upsFullBatteryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 2)).setObjects(("UPS-MIB", "upsEstimatedMinutesRemaining"), ("UPS-MIB", "upsSecondsOnBattery"), ("UPS-MIB", "upsEstimatedChargeRemaining"), ("UPS-MIB", "upsBatteryStatus"), )
upsBasicControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 8)).setObjects(("UPS-MIB", "upsRebootWithDuration"), ("UPS-MIB", "upsAutoRestart"), ("UPS-MIB", "upsShutdownType"), ("UPS-MIB", "upsStartupAfterDelay"), ("UPS-MIB", "upsShutdownAfterDelay"), )
upsSubsetAlarmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 6)).setObjects(("UPS-MIB", "upsAlarmsPresent"), ("UPS-MIB", "upsAlarmTime"), ("UPS-MIB", "upsAlarmDescr"), )
upsBasicConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 9)).setObjects(("UPS-MIB", "upsConfigInputFreq"), ("UPS-MIB", "upsConfigLowBattTime"), ("UPS-MIB", "upsConfigOutputFreq"), ("UPS-MIB", "upsConfigOutputVA"), ("UPS-MIB", "upsConfigOutputVoltage"), ("UPS-MIB", "upsConfigOutputPower"), ("UPS-MIB", "upsConfigInputVoltage"), ("UPS-MIB", "upsConfigAudibleStatus"), )
upsFullInputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 3)).setObjects(("UPS-MIB", "upsInputFrequency"), ("UPS-MIB", "upsInputVoltage"), ("UPS-MIB", "upsInputLineBads"), ("UPS-MIB", "upsInputNumLines"), )
upsSubsetIdentGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 1)).setObjects(("UPS-MIB", "upsIdentAgentSoftwareVersion"), ("UPS-MIB", "upsIdentName"), ("UPS-MIB", "upsIdentManufacturer"), ("UPS-MIB", "upsIdentAttachedDevices"), ("UPS-MIB", "upsIdentModel"), )
upsFullOutputGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 4)).setObjects(("UPS-MIB", "upsOutputNumLines"), ("UPS-MIB", "upsOutputFrequency"), ("UPS-MIB", "upsOutputSource"), ("UPS-MIB", "upsOutputPercentLoad"), ("UPS-MIB", "upsOutputPower"), ("UPS-MIB", "upsOutputCurrent"), ("UPS-MIB", "upsOutputVoltage"), )
upsFullTestGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 7)).setObjects(("UPS-MIB", "upsTestStartTime"), ("UPS-MIB", "upsTestElapsedTime"), ("UPS-MIB", "upsTestId"), ("UPS-MIB", "upsTestSpinLock"), ("UPS-MIB", "upsTestResultsSummary"), ("UPS-MIB", "upsTestResultsDetail"), )

# Exports

# Module identity
mibBuilder.exportSymbols("UPS-MIB", PYSNMP_MODULE_ID=upsMIB)

# Types
mibBuilder.exportSymbols("UPS-MIB", NonNegativeInteger=NonNegativeInteger, PositiveInteger=PositiveInteger)

# Objects
mibBuilder.exportSymbols("UPS-MIB", upsMIB=upsMIB, upsObjects=upsObjects, upsIdent=upsIdent, upsIdentManufacturer=upsIdentManufacturer, upsIdentModel=upsIdentModel, upsIdentUPSSoftwareVersion=upsIdentUPSSoftwareVersion, upsIdentAgentSoftwareVersion=upsIdentAgentSoftwareVersion, upsIdentName=upsIdentName, upsIdentAttachedDevices=upsIdentAttachedDevices, upsBattery=upsBattery, upsBatteryStatus=upsBatteryStatus, upsSecondsOnBattery=upsSecondsOnBattery, upsEstimatedMinutesRemaining=upsEstimatedMinutesRemaining, upsEstimatedChargeRemaining=upsEstimatedChargeRemaining, upsBatteryVoltage=upsBatteryVoltage, upsBatteryCurrent=upsBatteryCurrent, upsBatteryTemperature=upsBatteryTemperature, upsInput=upsInput, upsInputLineBads=upsInputLineBads, upsInputNumLines=upsInputNumLines, upsInputTable=upsInputTable, upsInputEntry=upsInputEntry, upsInputLineIndex=upsInputLineIndex, upsInputFrequency=upsInputFrequency, upsInputVoltage=upsInputVoltage, upsInputCurrent=upsInputCurrent, upsInputTruePower=upsInputTruePower, upsOutput=upsOutput, upsOutputSource=upsOutputSource, upsOutputFrequency=upsOutputFrequency, upsOutputNumLines=upsOutputNumLines, upsOutputTable=upsOutputTable, upsOutputEntry=upsOutputEntry, upsOutputLineIndex=upsOutputLineIndex, upsOutputVoltage=upsOutputVoltage, upsOutputCurrent=upsOutputCurrent, upsOutputPower=upsOutputPower, upsOutputPercentLoad=upsOutputPercentLoad, upsBypass=upsBypass, upsBypassFrequency=upsBypassFrequency, upsBypassNumLines=upsBypassNumLines, upsBypassTable=upsBypassTable, upsBypassEntry=upsBypassEntry, upsBypassLineIndex=upsBypassLineIndex, upsBypassVoltage=upsBypassVoltage, upsBypassCurrent=upsBypassCurrent, upsBypassPower=upsBypassPower, upsAlarm=upsAlarm, upsAlarmsPresent=upsAlarmsPresent, upsAlarmTable=upsAlarmTable, upsAlarmEntry=upsAlarmEntry, upsAlarmId=upsAlarmId, upsAlarmDescr=upsAlarmDescr, upsAlarmTime=upsAlarmTime, upsWellKnownAlarms=upsWellKnownAlarms, upsAlarmBatteryBad=upsAlarmBatteryBad, upsAlarmOnBattery=upsAlarmOnBattery, upsAlarmLowBattery=upsAlarmLowBattery, upsAlarmDepletedBattery=upsAlarmDepletedBattery, upsAlarmTempBad=upsAlarmTempBad, upsAlarmInputBad=upsAlarmInputBad, upsAlarmOutputBad=upsAlarmOutputBad, upsAlarmOutputOverload=upsAlarmOutputOverload, upsAlarmOnBypass=upsAlarmOnBypass, upsAlarmBypassBad=upsAlarmBypassBad, upsAlarmOutputOffAsRequested=upsAlarmOutputOffAsRequested, upsAlarmUpsOffAsRequested=upsAlarmUpsOffAsRequested, upsAlarmChargerFailed=upsAlarmChargerFailed, upsAlarmUpsOutputOff=upsAlarmUpsOutputOff, upsAlarmUpsSystemOff=upsAlarmUpsSystemOff, upsAlarmFanFailure=upsAlarmFanFailure, upsAlarmFuseFailure=upsAlarmFuseFailure, upsAlarmGeneralFault=upsAlarmGeneralFault, upsAlarmDiagnosticTestFailed=upsAlarmDiagnosticTestFailed, upsAlarmCommunicationsLost=upsAlarmCommunicationsLost, upsAlarmAwaitingPower=upsAlarmAwaitingPower, upsAlarmShutdownPending=upsAlarmShutdownPending, upsAlarmShutdownImminent=upsAlarmShutdownImminent, upsAlarmTestInProgress=upsAlarmTestInProgress, upsTest=upsTest, upsTestId=upsTestId, upsTestSpinLock=upsTestSpinLock, upsTestResultsSummary=upsTestResultsSummary, upsTestResultsDetail=upsTestResultsDetail, upsTestStartTime=upsTestStartTime, upsTestElapsedTime=upsTestElapsedTime, upsWellKnownTests=upsWellKnownTests, upsTestNoTestsInitiated=upsTestNoTestsInitiated, upsTestAbortTestInProgress=upsTestAbortTestInProgress, upsTestGeneralSystemsTest=upsTestGeneralSystemsTest, upsTestQuickBatteryTest=upsTestQuickBatteryTest, upsTestDeepBatteryCalibration=upsTestDeepBatteryCalibration, upsControl=upsControl, upsShutdownType=upsShutdownType, upsShutdownAfterDelay=upsShutdownAfterDelay, upsStartupAfterDelay=upsStartupAfterDelay, upsRebootWithDuration=upsRebootWithDuration, upsAutoRestart=upsAutoRestart, upsConfig=upsConfig, upsConfigInputVoltage=upsConfigInputVoltage, upsConfigInputFreq=upsConfigInputFreq, upsConfigOutputVoltage=upsConfigOutputVoltage, upsConfigOutputFreq=upsConfigOutputFreq, upsConfigOutputVA=upsConfigOutputVA, upsConfigOutputPower=upsConfigOutputPower, upsConfigLowBattTime=upsConfigLowBattTime, upsConfigAudibleStatus=upsConfigAudibleStatus, upsConfigLowVoltageTransferPoint=upsConfigLowVoltageTransferPoint, upsConfigHighVoltageTransferPoint=upsConfigHighVoltageTransferPoint, upsTraps=upsTraps, upsConformance=upsConformance, upsCompliances=upsCompliances, upsGroups=upsGroups, upsSubsetGroups=upsSubsetGroups, upsBasicGroups=upsBasicGroups, upsFullGroups=upsFullGroups)

# Notifications
mibBuilder.exportSymbols("UPS-MIB", upsTrapAlarmEntryAdded=upsTrapAlarmEntryAdded, upsTrapOnBattery=upsTrapOnBattery, upsTrapAlarmEntryRemoved=upsTrapAlarmEntryRemoved, upsTrapTestCompleted=upsTrapTestCompleted)

# Groups
mibBuilder.exportSymbols("UPS-MIB", upsSubsetConfigGroup=upsSubsetConfigGroup, upsFullConfigGroup=upsFullConfigGroup, upsBasicTestGroup=upsBasicTestGroup, upsFullControlGroup=upsFullControlGroup, upsSubsetBatteryGroup=upsSubsetBatteryGroup, upsBasicIdentGroup=upsBasicIdentGroup, upsBasicOutputGroup=upsBasicOutputGroup, upsBasicInputGroup=upsBasicInputGroup, upsSubsetOutputGroup=upsSubsetOutputGroup, upsBasicBypassGroup=upsBasicBypassGroup, upsFullBypassGroup=upsFullBypassGroup, upsSubsetInputGroup=upsSubsetInputGroup, upsBasicBatteryGroup=upsBasicBatteryGroup, upsBasicAlarmGroup=upsBasicAlarmGroup, upsFullAlarmGroup=upsFullAlarmGroup, upsFullIdentGroup=upsFullIdentGroup, upsSubsetControlGroup=upsSubsetControlGroup, upsFullBatteryGroup=upsFullBatteryGroup, upsBasicControlGroup=upsBasicControlGroup, upsSubsetAlarmGroup=upsSubsetAlarmGroup, upsBasicConfigGroup=upsBasicConfigGroup, upsFullInputGroup=upsFullInputGroup, upsSubsetIdentGroup=upsSubsetIdentGroup, upsFullOutputGroup=upsFullOutputGroup, upsFullTestGroup=upsFullTestGroup)
