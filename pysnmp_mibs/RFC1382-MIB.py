# PySNMP SMI module. Autogenerated from smidump -f python RFC1382-MIB
# by libsmi2pysnmp-0.0.6-alpha at Thu Apr  6 13:19:33 2006,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "transmission")
( EntryStatus, ) = mibBuilder.importSymbols("RFC1271-MIB", "EntryStatus")
( IfIndexType, PositiveInteger, ) = mibBuilder.importSymbols("RFC1381-MIB", "IfIndexType", "PositiveInteger")
( Bits, Counter32, Gauge32, Integer32, Integer32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Types

class X121Address(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,17)
    pass


# Objects

x25 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 5))
x25AdmnTable = MibTable((1, 3, 6, 1, 2, 1, 10, 5, 1))
x25AdmnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 5, 1, 1)).setIndexNames((0, "RFC1382-MIB", "x25AdmnIndex"))
x25AdmnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 1), IfIndexType()).setMaxAccess("readonly")
x25AdmnInterfaceMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,)).subtype(namedValues=namedval.NamedValues(("dte", 1), ("dce", 2), ("dxe", 3), ))).setMaxAccess("readwrite")
x25AdmnMaxActiveCircuits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4096))).setMaxAccess("readwrite")
x25AdmnPacketSequencing = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("modulo8", 1), ("modulo128", 2), ))).setMaxAccess("readwrite")
x25AdmnRestartTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 5), PositiveInteger()).setMaxAccess("readwrite")
x25AdmnCallTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 6), PositiveInteger()).setMaxAccess("readwrite")
x25AdmnResetTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 7), PositiveInteger()).setMaxAccess("readwrite")
x25AdmnClearTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 8), PositiveInteger()).setMaxAccess("readwrite")
x25AdmnWindowTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 9), PositiveInteger()).setMaxAccess("readwrite")
x25AdmnDataRxmtTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 10), PositiveInteger()).setMaxAccess("readwrite")
x25AdmnInterruptTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 11), PositiveInteger()).setMaxAccess("readwrite")
x25AdmnRejectTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 12), PositiveInteger()).setMaxAccess("readwrite")
x25AdmnRegistrationRequestTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 13), PositiveInteger()).setMaxAccess("readwrite")
x25AdmnMinimumRecallTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 14), PositiveInteger()).setMaxAccess("readwrite")
x25AdmnRestartCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 15), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
x25AdmnResetCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
x25AdmnClearCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
x25AdmnDataRxmtCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 18), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
x25AdmnRejectCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 19), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
x25AdmnRegistrationRequestCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 20), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
x25AdmnNumberPVCs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 21), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4096))).setMaxAccess("readwrite")
x25AdmnDefCallParamId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 22), ObjectIdentifier()).setMaxAccess("readwrite")
x25AdmnLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 23), X121Address()).setMaxAccess("readwrite")
x25AdmnProtocolVersionSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 1, 1, 24), ObjectIdentifier()).setMaxAccess("readwrite")
x25OperTable = MibTable((1, 3, 6, 1, 2, 1, 10, 5, 2))
x25OperEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 5, 2, 1)).setIndexNames((0, "RFC1382-MIB", "x25OperIndex"))
x25OperIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 1), IfIndexType()).setMaxAccess("readonly")
x25OperInterfaceMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,)).subtype(namedValues=namedval.NamedValues(("dte", 1), ("dce", 2), ("dxe", 3), ))).setMaxAccess("readonly")
x25OperMaxActiveCircuits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4096))).setMaxAccess("readonly")
x25OperPacketSequencing = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("modulo8", 1), ("modulo128", 2), ))).setMaxAccess("readonly")
x25OperRestartTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 5), PositiveInteger()).setMaxAccess("readonly")
x25OperCallTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 6), PositiveInteger()).setMaxAccess("readonly")
x25OperResetTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 7), PositiveInteger()).setMaxAccess("readonly")
x25OperClearTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 8), PositiveInteger()).setMaxAccess("readonly")
x25OperWindowTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 9), PositiveInteger()).setMaxAccess("readonly")
x25OperDataRxmtTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 10), PositiveInteger()).setMaxAccess("readonly")
x25OperInterruptTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 11), PositiveInteger()).setMaxAccess("readonly")
x25OperRejectTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 12), PositiveInteger()).setMaxAccess("readonly")
x25OperRegistrationRequestTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 13), PositiveInteger()).setMaxAccess("readonly")
x25OperMinimumRecallTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 14), PositiveInteger()).setMaxAccess("readonly")
x25OperRestartCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 15), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
x25OperResetCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 16), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
x25OperClearCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 17), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
x25OperDataRxmtCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 18), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
x25OperRejectCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 19), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
x25OperRegistrationRequestCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 20), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
x25OperNumberPVCs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 21), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4096))).setMaxAccess("readonly")
x25OperDefCallParamId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 22), ObjectIdentifier()).setMaxAccess("readonly")
x25OperLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 23), X121Address()).setMaxAccess("readonly")
x25OperDataLinkId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 24), ObjectIdentifier()).setMaxAccess("readonly")
x25OperProtocolVersionSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 2, 1, 25), ObjectIdentifier()).setMaxAccess("readonly")
x25StatTable = MibTable((1, 3, 6, 1, 2, 1, 10, 5, 3))
x25StatEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 5, 3, 1)).setIndexNames((0, "RFC1382-MIB", "x25StatIndex"))
x25StatIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 1), IfIndexType()).setMaxAccess("readonly")
x25StatInCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 2), Counter32()).setMaxAccess("readonly")
x25StatInCallRefusals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 3), Counter32()).setMaxAccess("readonly")
x25StatInProviderInitiatedClears = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 4), Counter32()).setMaxAccess("readonly")
x25StatInRemotelyInitiatedResets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 5), Counter32()).setMaxAccess("readonly")
x25StatInProviderInitiatedResets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 6), Counter32()).setMaxAccess("readonly")
x25StatInRestarts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 7), Counter32()).setMaxAccess("readonly")
x25StatInDataPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 8), Counter32()).setMaxAccess("readonly")
x25StatInAccusedOfProtocolErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 9), Counter32()).setMaxAccess("readonly")
x25StatInInterrupts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 10), Counter32()).setMaxAccess("readonly")
x25StatOutCallAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 11), Counter32()).setMaxAccess("readonly")
x25StatOutCallFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 12), Counter32()).setMaxAccess("readonly")
x25StatOutInterrupts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 13), Counter32()).setMaxAccess("readonly")
x25StatOutDataPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 14), Counter32()).setMaxAccess("readonly")
x25StatOutgoingCircuits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 15), Gauge32()).setMaxAccess("readonly")
x25StatIncomingCircuits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 16), Gauge32()).setMaxAccess("readonly")
x25StatTwowayCircuits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 17), Gauge32()).setMaxAccess("readonly")
x25StatRestartTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 18), Counter32()).setMaxAccess("readonly")
x25StatCallTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 19), Counter32()).setMaxAccess("readonly")
x25StatResetTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 20), Counter32()).setMaxAccess("readonly")
x25StatClearTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 21), Counter32()).setMaxAccess("readonly")
x25StatDataRxmtTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 22), Counter32()).setMaxAccess("readonly")
x25StatInterruptTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 23), Counter32()).setMaxAccess("readonly")
x25StatRetryCountExceededs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 24), Counter32()).setMaxAccess("readonly")
x25StatClearCountExceededs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 3, 1, 25), Counter32()).setMaxAccess("readonly")
x25ChannelTable = MibTable((1, 3, 6, 1, 2, 1, 10, 5, 4))
x25ChannelEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 5, 4, 1)).setIndexNames((0, "RFC1382-MIB", "x25ChannelIndex"))
x25ChannelIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 1), IfIndexType()).setMaxAccess("readonly")
x25ChannelLIC = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
x25ChannelHIC = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
x25ChannelLTC = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
x25ChannelHTC = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
x25ChannelLOC = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
x25ChannelHOC = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 4, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
x25CircuitTable = MibTable((1, 3, 6, 1, 2, 1, 10, 5, 5))
x25CircuitEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 5, 5, 1)).setIndexNames((0, "RFC1382-MIB", "x25CircuitIndex"), (0, "RFC1382-MIB", "x25CircuitChannel"))
x25CircuitIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 1), IfIndexType()).setMaxAccess("readonly")
x25CircuitChannel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
x25CircuitStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(7,5,9,1,3,8,6,10,2,4,)).subtype(namedValues=namedval.NamedValues(("invalid", 1), ("other", 10), ("closed", 2), ("calling", 3), ("open", 4), ("clearing", 5), ("pvc", 6), ("pvcResetting", 7), ("startClear", 8), ("startPvcResetting", 9), ))).setMaxAccess("readwrite")
x25CircuitEstablishTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 4), TimeTicks()).setMaxAccess("readonly")
x25CircuitDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("incoming", 1), ("outgoing", 2), ("pvc", 3), )).clone(3)).setMaxAccess("readwrite")
x25CircuitInOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 6), Counter32()).setMaxAccess("readonly")
x25CircuitInPdus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 7), Counter32()).setMaxAccess("readonly")
x25CircuitInRemotelyInitiatedResets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 8), Counter32()).setMaxAccess("readonly")
x25CircuitInProviderInitiatedResets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 9), Counter32()).setMaxAccess("readonly")
x25CircuitInInterrupts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 10), Counter32()).setMaxAccess("readonly")
x25CircuitOutOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 11), Counter32()).setMaxAccess("readonly")
x25CircuitOutPdus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 12), Counter32()).setMaxAccess("readonly")
x25CircuitOutInterrupts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 13), Counter32()).setMaxAccess("readonly")
x25CircuitDataRetransmissionTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 14), Counter32()).setMaxAccess("readonly")
x25CircuitResetTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 15), Counter32()).setMaxAccess("readonly")
x25CircuitInterruptTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 16), Counter32()).setMaxAccess("readonly")
x25CircuitCallParamId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 17), ObjectIdentifier().clone((0,))).setMaxAccess("readwrite")
x25CircuitCalledDteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 18), X121Address()).setMaxAccess("readwrite")
x25CircuitCallingDteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 19), X121Address()).setMaxAccess("readwrite")
x25CircuitOriginallyCalledAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 20), X121Address()).setMaxAccess("readwrite")
x25CircuitDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 5, 1, 21), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255)).clone('')).setMaxAccess("readwrite")
x25ClearedCircuitEntriesRequested = MibScalar((1, 3, 6, 1, 2, 1, 10, 5, 6), PositiveInteger()).setMaxAccess("readwrite")
x25ClearedCircuitEntriesGranted = MibScalar((1, 3, 6, 1, 2, 1, 10, 5, 7), PositiveInteger()).setMaxAccess("readonly")
x25ClearedCircuitTable = MibTable((1, 3, 6, 1, 2, 1, 10, 5, 8))
x25ClearedCircuitEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 5, 8, 1)).setIndexNames((0, "RFC1382-MIB", "x25ClearedCircuitIndex"))
x25ClearedCircuitIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 1), PositiveInteger()).setMaxAccess("readonly")
x25ClearedCircuitPleIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 2), IfIndexType()).setMaxAccess("readonly")
x25ClearedCircuitTimeEstablished = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 3), TimeTicks()).setMaxAccess("readonly")
x25ClearedCircuitTimeCleared = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 4), TimeTicks()).setMaxAccess("readonly")
x25ClearedCircuitChannel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
x25ClearedCircuitClearingCause = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
x25ClearedCircuitDiagnosticCode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
x25ClearedCircuitInPdus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 8), Counter32()).setMaxAccess("readonly")
x25ClearedCircuitOutPdus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 9), Counter32()).setMaxAccess("readonly")
x25ClearedCircuitCalledAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 10), X121Address()).setMaxAccess("readonly")
x25ClearedCircuitCallingAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 11), X121Address()).setMaxAccess("readonly")
x25ClearedCircuitClearFacilities = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 8, 1, 12), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 109))).setMaxAccess("readonly")
x25CallParmTable = MibTable((1, 3, 6, 1, 2, 1, 10, 5, 9))
x25CallParmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 5, 9, 1)).setIndexNames((0, "RFC1382-MIB", "x25CallParmIndex"))
x25CallParmIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 1), PositiveInteger()).setMaxAccess("readonly")
x25CallParmStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 2), EntryStatus()).setMaxAccess("readwrite")
x25CallParmRefCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 3), PositiveInteger()).setMaxAccess("readonly")
x25CallParmInPacketSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4096)).clone(128)).setMaxAccess("readwrite")
x25CallParmOutPacketSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 4096)).clone(128)).setMaxAccess("readwrite")
x25CallParmInWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 127)).clone(2)).setMaxAccess("readwrite")
x25CallParmOutWindowSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 127)).clone(2)).setMaxAccess("readwrite")
x25CallParmAcceptReverseCharging = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 8), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,4,2,)).subtype(namedValues=namedval.NamedValues(("default", 1), ("accept", 2), ("refuse", 3), ("neverAccept", 4), )).clone(3)).setMaxAccess("readwrite")
x25CallParmProposeReverseCharging = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 9), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("default", 1), ("reverse", 2), ("local", 3), )).clone(3)).setMaxAccess("readwrite")
x25CallParmFastSelect = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,6,3,4,5,2,)).subtype(namedValues=namedval.NamedValues(("default", 1), ("notSpecified", 2), ("fastSelect", 3), ("restrictedFastResponse", 4), ("noFastSelect", 5), ("noRestrictedFastResponse", 6), )).clone(5)).setMaxAccess("readwrite")
x25CallParmInThruPutClasSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(7,13,5,6,4,17,10,11,8,2,16,3,12,18,14,15,1,9,)).subtype(namedValues=namedval.NamedValues(("tcReserved1", 1), ("tc9600", 10), ("tc19200", 11), ("tc48000", 12), ("tc64000", 13), ("tcReserved14", 14), ("tcReserved15", 15), ("tcReserved0", 16), ("tcNone", 17), ("tcDefault", 18), ("tcReserved2", 2), ("tc75", 3), ("tc150", 4), ("tc300", 5), ("tc600", 6), ("tc1200", 7), ("tc2400", 8), ("tc4800", 9), )).clone(17)).setMaxAccess("readwrite")
x25CallParmOutThruPutClasSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(7,13,5,6,4,17,10,11,8,2,16,3,12,18,14,15,1,9,)).subtype(namedValues=namedval.NamedValues(("tcReserved1", 1), ("tc9600", 10), ("tc19200", 11), ("tc48000", 12), ("tc64000", 13), ("tcReserved14", 14), ("tcReserved15", 15), ("tcReserved0", 16), ("tcNone", 17), ("tcDefault", 18), ("tcReserved2", 2), ("tc75", 3), ("tc150", 4), ("tc300", 5), ("tc600", 6), ("tc1200", 7), ("tc2400", 8), ("tc4800", 9), )).clone(17)).setMaxAccess("readwrite")
x25CallParmCug = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 13), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 4)).clone('')).setMaxAccess("readwrite")
x25CallParmCugoa = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 14), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 4)).clone('')).setMaxAccess("readwrite")
x25CallParmBcug = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 15), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 3)).clone('')).setMaxAccess("readwrite")
x25CallParmNui = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 16), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 108)).clone('')).setMaxAccess("readwrite")
x25CallParmChargingInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 17), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,4,)).subtype(namedValues=namedval.NamedValues(("default", 1), ("noFacility", 2), ("noChargingInfo", 3), ("chargingInfo", 4), )).clone(2)).setMaxAccess("readwrite")
x25CallParmRpoa = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 18), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 108)).clone('')).setMaxAccess("readwrite")
x25CallParmTrnstDly = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 19), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65537)).clone(65536)).setMaxAccess("readwrite")
x25CallParmCallingExt = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 20), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 40)).clone('')).setMaxAccess("readwrite")
x25CallParmCalledExt = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 21), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 40)).clone('')).setMaxAccess("readwrite")
x25CallParmInMinThuPutCls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 22), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 17)).clone(17)).setMaxAccess("readwrite")
x25CallParmOutMinThuPutCls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 23), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 17)).clone(17)).setMaxAccess("readwrite")
x25CallParmEndTrnsDly = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 24), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 6)).clone('')).setMaxAccess("readwrite")
x25CallParmPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 25), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 6)).clone('')).setMaxAccess("readwrite")
x25CallParmProtection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 26), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 108)).clone('')).setMaxAccess("readwrite")
x25CallParmExptData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 27), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("default", 1), ("noExpeditedData", 2), ("expeditedData", 3), )).clone(2)).setMaxAccess("readwrite")
x25CallParmUserData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 28), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 128)).clone('')).setMaxAccess("readwrite")
x25CallParmCallingNetworkFacilities = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 29), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 108)).clone('')).setMaxAccess("readwrite")
x25CallParmCalledNetworkFacilities = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 5, 9, 1, 30), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 108)).clone('')).setMaxAccess("readwrite")
x25ProtocolVersion = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 5, 10))
x25protocolCcittV1976 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 5, 10, 1))
x25protocolCcittV1980 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 5, 10, 2))
x25protocolCcittV1984 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 5, 10, 3))
x25protocolCcittV1988 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 5, 10, 4))
x25protocolIso8208V1987 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 5, 10, 5))
x25protocolIso8208V1989 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 5, 10, 6))

# Augmentions

# Notifications

x25Restart = NotificationType((1, 3, 6, 1, 2, 1, 10, 5, 0, 1)).setObjects(("RFC1382-MIB", "x25OperIndex"), )
x25Reset = NotificationType((1, 3, 6, 1, 2, 1, 10, 5, 0, 2)).setObjects(("RFC1382-MIB", "x25CircuitChannel"), ("RFC1382-MIB", "x25CircuitIndex"), )

# Exports

# Types
mibBuilder.exportSymbols("RFC1382-MIB", X121Address=X121Address)

# Objects
mibBuilder.exportSymbols("RFC1382-MIB", x25=x25, x25AdmnTable=x25AdmnTable, x25AdmnEntry=x25AdmnEntry, x25AdmnIndex=x25AdmnIndex, x25AdmnInterfaceMode=x25AdmnInterfaceMode, x25AdmnMaxActiveCircuits=x25AdmnMaxActiveCircuits, x25AdmnPacketSequencing=x25AdmnPacketSequencing, x25AdmnRestartTimer=x25AdmnRestartTimer, x25AdmnCallTimer=x25AdmnCallTimer, x25AdmnResetTimer=x25AdmnResetTimer, x25AdmnClearTimer=x25AdmnClearTimer, x25AdmnWindowTimer=x25AdmnWindowTimer, x25AdmnDataRxmtTimer=x25AdmnDataRxmtTimer, x25AdmnInterruptTimer=x25AdmnInterruptTimer, x25AdmnRejectTimer=x25AdmnRejectTimer, x25AdmnRegistrationRequestTimer=x25AdmnRegistrationRequestTimer, x25AdmnMinimumRecallTimer=x25AdmnMinimumRecallTimer, x25AdmnRestartCount=x25AdmnRestartCount, x25AdmnResetCount=x25AdmnResetCount, x25AdmnClearCount=x25AdmnClearCount, x25AdmnDataRxmtCount=x25AdmnDataRxmtCount, x25AdmnRejectCount=x25AdmnRejectCount, x25AdmnRegistrationRequestCount=x25AdmnRegistrationRequestCount, x25AdmnNumberPVCs=x25AdmnNumberPVCs, x25AdmnDefCallParamId=x25AdmnDefCallParamId, x25AdmnLocalAddress=x25AdmnLocalAddress, x25AdmnProtocolVersionSupported=x25AdmnProtocolVersionSupported, x25OperTable=x25OperTable, x25OperEntry=x25OperEntry, x25OperIndex=x25OperIndex, x25OperInterfaceMode=x25OperInterfaceMode, x25OperMaxActiveCircuits=x25OperMaxActiveCircuits, x25OperPacketSequencing=x25OperPacketSequencing, x25OperRestartTimer=x25OperRestartTimer, x25OperCallTimer=x25OperCallTimer, x25OperResetTimer=x25OperResetTimer, x25OperClearTimer=x25OperClearTimer, x25OperWindowTimer=x25OperWindowTimer, x25OperDataRxmtTimer=x25OperDataRxmtTimer, x25OperInterruptTimer=x25OperInterruptTimer, x25OperRejectTimer=x25OperRejectTimer, x25OperRegistrationRequestTimer=x25OperRegistrationRequestTimer, x25OperMinimumRecallTimer=x25OperMinimumRecallTimer, x25OperRestartCount=x25OperRestartCount, x25OperResetCount=x25OperResetCount, x25OperClearCount=x25OperClearCount, x25OperDataRxmtCount=x25OperDataRxmtCount, x25OperRejectCount=x25OperRejectCount, x25OperRegistrationRequestCount=x25OperRegistrationRequestCount, x25OperNumberPVCs=x25OperNumberPVCs, x25OperDefCallParamId=x25OperDefCallParamId, x25OperLocalAddress=x25OperLocalAddress, x25OperDataLinkId=x25OperDataLinkId, x25OperProtocolVersionSupported=x25OperProtocolVersionSupported, x25StatTable=x25StatTable, x25StatEntry=x25StatEntry, x25StatIndex=x25StatIndex, x25StatInCalls=x25StatInCalls, x25StatInCallRefusals=x25StatInCallRefusals, x25StatInProviderInitiatedClears=x25StatInProviderInitiatedClears, x25StatInRemotelyInitiatedResets=x25StatInRemotelyInitiatedResets, x25StatInProviderInitiatedResets=x25StatInProviderInitiatedResets, x25StatInRestarts=x25StatInRestarts, x25StatInDataPackets=x25StatInDataPackets, x25StatInAccusedOfProtocolErrors=x25StatInAccusedOfProtocolErrors, x25StatInInterrupts=x25StatInInterrupts, x25StatOutCallAttempts=x25StatOutCallAttempts, x25StatOutCallFailures=x25StatOutCallFailures, x25StatOutInterrupts=x25StatOutInterrupts, x25StatOutDataPackets=x25StatOutDataPackets, x25StatOutgoingCircuits=x25StatOutgoingCircuits, x25StatIncomingCircuits=x25StatIncomingCircuits, x25StatTwowayCircuits=x25StatTwowayCircuits, x25StatRestartTimeouts=x25StatRestartTimeouts, x25StatCallTimeouts=x25StatCallTimeouts, x25StatResetTimeouts=x25StatResetTimeouts, x25StatClearTimeouts=x25StatClearTimeouts, x25StatDataRxmtTimeouts=x25StatDataRxmtTimeouts, x25StatInterruptTimeouts=x25StatInterruptTimeouts, x25StatRetryCountExceededs=x25StatRetryCountExceededs, x25StatClearCountExceededs=x25StatClearCountExceededs, x25ChannelTable=x25ChannelTable, x25ChannelEntry=x25ChannelEntry, x25ChannelIndex=x25ChannelIndex, x25ChannelLIC=x25ChannelLIC, x25ChannelHIC=x25ChannelHIC, x25ChannelLTC=x25ChannelLTC, x25ChannelHTC=x25ChannelHTC, x25ChannelLOC=x25ChannelLOC, x25ChannelHOC=x25ChannelHOC, x25CircuitTable=x25CircuitTable, x25CircuitEntry=x25CircuitEntry, x25CircuitIndex=x25CircuitIndex, x25CircuitChannel=x25CircuitChannel, x25CircuitStatus=x25CircuitStatus, x25CircuitEstablishTime=x25CircuitEstablishTime, x25CircuitDirection=x25CircuitDirection, x25CircuitInOctets=x25CircuitInOctets, x25CircuitInPdus=x25CircuitInPdus, x25CircuitInRemotelyInitiatedResets=x25CircuitInRemotelyInitiatedResets, x25CircuitInProviderInitiatedResets=x25CircuitInProviderInitiatedResets, x25CircuitInInterrupts=x25CircuitInInterrupts, x25CircuitOutOctets=x25CircuitOutOctets, x25CircuitOutPdus=x25CircuitOutPdus, x25CircuitOutInterrupts=x25CircuitOutInterrupts, x25CircuitDataRetransmissionTimeouts=x25CircuitDataRetransmissionTimeouts, x25CircuitResetTimeouts=x25CircuitResetTimeouts, x25CircuitInterruptTimeouts=x25CircuitInterruptTimeouts, x25CircuitCallParamId=x25CircuitCallParamId, x25CircuitCalledDteAddress=x25CircuitCalledDteAddress, x25CircuitCallingDteAddress=x25CircuitCallingDteAddress, x25CircuitOriginallyCalledAddress=x25CircuitOriginallyCalledAddress, x25CircuitDescr=x25CircuitDescr, x25ClearedCircuitEntriesRequested=x25ClearedCircuitEntriesRequested, x25ClearedCircuitEntriesGranted=x25ClearedCircuitEntriesGranted, x25ClearedCircuitTable=x25ClearedCircuitTable, x25ClearedCircuitEntry=x25ClearedCircuitEntry, x25ClearedCircuitIndex=x25ClearedCircuitIndex, x25ClearedCircuitPleIndex=x25ClearedCircuitPleIndex, x25ClearedCircuitTimeEstablished=x25ClearedCircuitTimeEstablished, x25ClearedCircuitTimeCleared=x25ClearedCircuitTimeCleared, x25ClearedCircuitChannel=x25ClearedCircuitChannel, x25ClearedCircuitClearingCause=x25ClearedCircuitClearingCause, x25ClearedCircuitDiagnosticCode=x25ClearedCircuitDiagnosticCode, x25ClearedCircuitInPdus=x25ClearedCircuitInPdus, x25ClearedCircuitOutPdus=x25ClearedCircuitOutPdus)
mibBuilder.exportSymbols("RFC1382-MIB", x25ClearedCircuitCalledAddress=x25ClearedCircuitCalledAddress, x25ClearedCircuitCallingAddress=x25ClearedCircuitCallingAddress, x25ClearedCircuitClearFacilities=x25ClearedCircuitClearFacilities, x25CallParmTable=x25CallParmTable, x25CallParmEntry=x25CallParmEntry, x25CallParmIndex=x25CallParmIndex, x25CallParmStatus=x25CallParmStatus, x25CallParmRefCount=x25CallParmRefCount, x25CallParmInPacketSize=x25CallParmInPacketSize, x25CallParmOutPacketSize=x25CallParmOutPacketSize, x25CallParmInWindowSize=x25CallParmInWindowSize, x25CallParmOutWindowSize=x25CallParmOutWindowSize, x25CallParmAcceptReverseCharging=x25CallParmAcceptReverseCharging, x25CallParmProposeReverseCharging=x25CallParmProposeReverseCharging, x25CallParmFastSelect=x25CallParmFastSelect, x25CallParmInThruPutClasSize=x25CallParmInThruPutClasSize, x25CallParmOutThruPutClasSize=x25CallParmOutThruPutClasSize, x25CallParmCug=x25CallParmCug, x25CallParmCugoa=x25CallParmCugoa, x25CallParmBcug=x25CallParmBcug, x25CallParmNui=x25CallParmNui, x25CallParmChargingInfo=x25CallParmChargingInfo, x25CallParmRpoa=x25CallParmRpoa, x25CallParmTrnstDly=x25CallParmTrnstDly, x25CallParmCallingExt=x25CallParmCallingExt, x25CallParmCalledExt=x25CallParmCalledExt, x25CallParmInMinThuPutCls=x25CallParmInMinThuPutCls, x25CallParmOutMinThuPutCls=x25CallParmOutMinThuPutCls, x25CallParmEndTrnsDly=x25CallParmEndTrnsDly, x25CallParmPriority=x25CallParmPriority, x25CallParmProtection=x25CallParmProtection, x25CallParmExptData=x25CallParmExptData, x25CallParmUserData=x25CallParmUserData, x25CallParmCallingNetworkFacilities=x25CallParmCallingNetworkFacilities, x25CallParmCalledNetworkFacilities=x25CallParmCalledNetworkFacilities, x25ProtocolVersion=x25ProtocolVersion, x25protocolCcittV1976=x25protocolCcittV1976, x25protocolCcittV1980=x25protocolCcittV1980, x25protocolCcittV1984=x25protocolCcittV1984, x25protocolCcittV1988=x25protocolCcittV1988, x25protocolIso8208V1987=x25protocolIso8208V1987, x25protocolIso8208V1989=x25protocolIso8208V1989)

# Notifications
mibBuilder.exportSymbols("RFC1382-MIB", x25Restart=x25Restart, x25Reset=x25Reset)

