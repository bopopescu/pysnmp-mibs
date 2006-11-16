# PySNMP SMI module. Autogenerated from smidump -f python FIBRE-CHANNEL-FE-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 19:13:20 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "TruthValue")

# Types

class FcAddressId(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(3,3)
    isFixedLengthFlag = 1
    pass

class FcBbCredit(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,32767)
    pass

class FcBbCreditModel(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,1,)
    namedValues = namedval.NamedValues(("regular", 1), ("alternate", 2), )
    pass

class FcCosCap(Bits):
    namedValues = namedval.NamedValues(("classF", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4), ("class5", 5), ("class6", 6), )
    pass

class FcFeFxPortCapacity(Unsigned32):
    pass

class FcFeFxPortIndex(Unsigned32):
    pass

class FcFeModuleCapacity(Unsigned32):
    pass

class FcFeModuleIndex(Unsigned32):
    pass

class FcFeNxPortIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(1,126)
    pass

class FcNameId(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(8,8)
    isFixedLengthFlag = 1
    pass

class FcRxDataFieldSize(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(128,2112)
    pass

class FcStackedConnMode(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,1,2,)
    namedValues = namedval.NamedValues(("none", 1), ("transparent", 2), ("lockedDown", 3), )
    pass

class FcphVersion(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,255)
    pass

class MicroSeconds(Unsigned32):
    pass

class MilliSeconds(Unsigned32):
    pass


# Objects

fcFeMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 75)).setRevisions(("2000-05-18 00:00",))
fcFeMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 75, 1))
fcFeConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 75, 1, 1))
fcFeFabricName = MibScalar((1, 3, 6, 1, 2, 1, 75, 1, 1, 1), FcNameId()).setMaxAccess("readwrite")
fcFeElementName = MibScalar((1, 3, 6, 1, 2, 1, 75, 1, 1, 2), FcNameId()).setMaxAccess("readwrite")
fcFeModuleCapacity = MibScalar((1, 3, 6, 1, 2, 1, 75, 1, 1, 3), FcFeModuleCapacity()).setMaxAccess("readonly")
fcFeModuleTable = MibTable((1, 3, 6, 1, 2, 1, 75, 1, 1, 4))
fcFeModuleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1)).setIndexNames((0, "FIBRE-CHANNEL-FE-MIB", "fcFeModuleIndex"))
fcFeModuleIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 1), FcFeModuleIndex()).setMaxAccess("noaccess")
fcFeModuleDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
fcFeModuleObjectID = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
fcFeModuleOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,4,)).subtype(namedValues=namedval.NamedValues(("online", 1), ("offline", 2), ("testing", 3), ("faulty", 4), ))).setMaxAccess("readonly")
fcFeModuleLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 5), TimeStamp()).setMaxAccess("readonly")
fcFeModuleFxPortCapacity = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 6), FcFeFxPortCapacity()).setMaxAccess("readonly")
fcFeModuleName = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 7), FcNameId()).setMaxAccess("readwrite")
fcFxPortTable = MibTable((1, 3, 6, 1, 2, 1, 75, 1, 1, 5))
fcFxPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1)).setIndexNames((0, "FIBRE-CHANNEL-FE-MIB", "fcFeModuleIndex"), (0, "FIBRE-CHANNEL-FE-MIB", "fcFxPortIndex"))
fcFxPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 1), FcFeFxPortIndex()).setMaxAccess("noaccess")
fcFxPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 2), FcNameId()).setMaxAccess("readonly")
fcFxPortFcphVersionHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 3), FcphVersion()).setMaxAccess("readonly")
fcFxPortFcphVersionLow = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 4), FcphVersion()).setMaxAccess("readonly")
fcFxPortBbCredit = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 5), FcBbCredit()).setMaxAccess("readonly")
fcFxPortRxBufSize = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 6), FcRxDataFieldSize()).setMaxAccess("readonly")
fcFxPortRatov = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 7), MilliSeconds()).setMaxAccess("readonly")
fcFxPortEdtov = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 8), MilliSeconds()).setMaxAccess("readonly")
fcFxPortCosSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 9), FcCosCap()).setMaxAccess("readonly")
fcFxPortIntermixSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 10), TruthValue()).setMaxAccess("readonly")
fcFxPortStackedConnMode = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 11), FcStackedConnMode()).setMaxAccess("readonly")
fcFxPortClass2SeqDeliv = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 12), TruthValue()).setMaxAccess("readonly")
fcFxPortClass3SeqDeliv = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 13), TruthValue()).setMaxAccess("readonly")
fcFxPortHoldTime = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 14), MicroSeconds()).setMaxAccess("readonly")
fcFeStatus = MibIdentifier((1, 3, 6, 1, 2, 1, 75, 1, 2))
fcFxPortStatusTable = MibTable((1, 3, 6, 1, 2, 1, 75, 1, 2, 1))
fcFxPortStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 75, 1, 2, 1, 1))
fcFxPortID = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 1, 1, 1), FcAddressId()).setMaxAccess("readonly")
fcFxPortBbCreditAvailable = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
fcFxPortOperMode = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 1, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,3,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("fPort", 2), ("flPort", 3), ))).setMaxAccess("readonly")
fcFxPortAdminMode = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,)).subtype(namedValues=namedval.NamedValues(("fPort", 2), ("flPort", 3), ))).setMaxAccess("readwrite")
fcFxPortPhysTable = MibTable((1, 3, 6, 1, 2, 1, 75, 1, 2, 2))
fcFxPortPhysEntry = MibTableRow((1, 3, 6, 1, 2, 1, 75, 1, 2, 2, 1))
fcFxPortPhysAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 2, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("online", 1), ("offline", 2), ("testing", 3), ))).setMaxAccess("readwrite")
fcFxPortPhysOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,4,1,2,)).subtype(namedValues=namedval.NamedValues(("online", 1), ("offline", 2), ("testing", 3), ("linkFailure", 4), ))).setMaxAccess("readonly")
fcFxPortPhysLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
fcFxPortPhysRttov = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 2, 1, 4), MilliSeconds()).setMaxAccess("readwrite")
fcFxLoginTable = MibTable((1, 3, 6, 1, 2, 1, 75, 1, 2, 3))
fcFxLoginEntry = MibTableRow((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1)).setIndexNames((0, "FIBRE-CHANNEL-FE-MIB", "fcFeModuleIndex"), (0, "FIBRE-CHANNEL-FE-MIB", "fcFxPortIndex"), (0, "FIBRE-CHANNEL-FE-MIB", "fcFxPortNxLoginIndex"))
fcFxPortNxLoginIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 1), FcFeNxPortIndex()).setMaxAccess("noaccess")
fcFxPortFcphVersionAgreed = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 2), FcphVersion()).setMaxAccess("readonly")
fcFxPortNxPortBbCredit = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 3), FcBbCredit()).setMaxAccess("readonly")
fcFxPortNxPortRxDataFieldSize = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 4), FcRxDataFieldSize()).setMaxAccess("readonly")
fcFxPortCosSuppAgreed = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 5), FcCosCap()).setMaxAccess("readonly")
fcFxPortIntermixSuppAgreed = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 6), TruthValue()).setMaxAccess("readonly")
fcFxPortStackedConnModeAgreed = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 7), FcStackedConnMode()).setMaxAccess("readonly")
fcFxPortClass2SeqDelivAgreed = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 8), TruthValue()).setMaxAccess("readonly")
fcFxPortClass3SeqDelivAgreed = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 9), TruthValue()).setMaxAccess("readonly")
fcFxPortNxPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 10), FcNameId()).setMaxAccess("readonly")
fcFxPortConnectedNxPort = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 11), FcAddressId()).setMaxAccess("readonly")
fcFxPortBbCreditModel = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 12), FcBbCreditModel()).setMaxAccess("readwrite")
fcFeError = MibIdentifier((1, 3, 6, 1, 2, 1, 75, 1, 3))
fcFxPortErrorTable = MibTable((1, 3, 6, 1, 2, 1, 75, 1, 3, 1))
fcFxPortErrorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1))
fcFxPortLinkFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
fcFxPortSyncLosses = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
fcFxPortSigLosses = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
fcFxPortPrimSeqProtoErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
fcFxPortInvalidTxWords = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
fcFxPortInvalidCrcs = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
fcFxPortDelimiterErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
fcFxPortAddressIdErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
fcFxPortLinkResetIns = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
fcFxPortLinkResetOuts = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
fcFxPortOlsIns = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
fcFxPortOlsOuts = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
fcFeAccounting = MibIdentifier((1, 3, 6, 1, 2, 1, 75, 1, 4))
fcFxPortC1AccountingTable = MibTable((1, 3, 6, 1, 2, 1, 75, 1, 4, 1))
fcFxPortC1AccountingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1))
fcFxPortC1InFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 1), Counter32()).setMaxAccess("readonly")
fcFxPortC1OutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 2), Counter32()).setMaxAccess("readonly")
fcFxPortC1InOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
fcFxPortC1OutOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
fcFxPortC1Discards = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
fcFxPortC1FbsyFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
fcFxPortC1FrjtFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
fcFxPortC1InConnections = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
fcFxPortC1OutConnections = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
fcFxPortC1ConnTime = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 10), MilliSeconds()).setMaxAccess("readonly")
fcFxPortC2AccountingTable = MibTable((1, 3, 6, 1, 2, 1, 75, 1, 4, 2))
fcFxPortC2AccountingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1))
fcFxPortC2InFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 1), Counter32()).setMaxAccess("readonly")
fcFxPortC2OutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 2), Counter32()).setMaxAccess("readonly")
fcFxPortC2InOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 3), Counter32()).setMaxAccess("readonly")
fcFxPortC2OutOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 4), Counter32()).setMaxAccess("readonly")
fcFxPortC2Discards = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 5), Counter32()).setMaxAccess("readonly")
fcFxPortC2FbsyFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 6), Counter32()).setMaxAccess("readonly")
fcFxPortC2FrjtFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 7), Counter32()).setMaxAccess("readonly")
fcFxPortC3AccountingTable = MibTable((1, 3, 6, 1, 2, 1, 75, 1, 4, 3))
fcFxPortC3AccountingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1))
fcFxPortC3InFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1, 1), Counter32()).setMaxAccess("readonly")
fcFxPortC3OutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1, 2), Counter32()).setMaxAccess("readonly")
fcFxPortC3InOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1, 3), Counter32()).setMaxAccess("readonly")
fcFxPortC3OutOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1, 4), Counter32()).setMaxAccess("readonly")
fcFxPortC3Discards = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1, 5), Counter32()).setMaxAccess("readonly")
fcFeCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 75, 1, 5))
fcFxPortCapTable = MibTable((1, 3, 6, 1, 2, 1, 75, 1, 5, 1))
fcFxPortCapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1))
fcFxPortCapFcphVersionHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 1), FcphVersion()).setMaxAccess("readonly")
fcFxPortCapFcphVersionLow = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 2), FcphVersion()).setMaxAccess("readonly")
fcFxPortCapBbCreditMax = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 3), FcBbCredit()).setMaxAccess("readonly")
fcFxPortCapBbCreditMin = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 4), FcBbCredit()).setMaxAccess("readonly")
fcFxPortCapRxDataFieldSizeMax = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 5), FcRxDataFieldSize()).setMaxAccess("readonly")
fcFxPortCapRxDataFieldSizeMin = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 6), FcRxDataFieldSize()).setMaxAccess("readonly")
fcFxPortCapCos = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 7), FcCosCap()).setMaxAccess("readonly")
fcFxPortCapIntermix = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
fcFxPortCapStackedConnMode = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 9), FcStackedConnMode()).setMaxAccess("readonly")
fcFxPortCapClass2SeqDeliv = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
fcFxPortCapClass3SeqDeliv = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
fcFxPortCapHoldTimeMax = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 12), MicroSeconds()).setMaxAccess("readonly")
fcFxPortCapHoldTimeMin = MibTableColumn((1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 13), MicroSeconds()).setMaxAccess("readonly")
fcFeMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 75, 2))
fcFeMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 75, 2, 1))
fcFeMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 75, 2, 2))

# Augmentions
fcFxPortEntry.registerAugmentions(("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1AccountingEntry"))
apply(fcFxPortC1AccountingEntry.setIndexNames, fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3AccountingEntry"))
apply(fcFxPortC3AccountingEntry.setIndexNames, fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(("FIBRE-CHANNEL-FE-MIB", "fcFxPortPhysEntry"))
apply(fcFxPortPhysEntry.setIndexNames, fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(("FIBRE-CHANNEL-FE-MIB", "fcFxPortErrorEntry"))
apply(fcFxPortErrorEntry.setIndexNames, fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapEntry"))
apply(fcFxPortCapEntry.setIndexNames, fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2AccountingEntry"))
apply(fcFxPortC2AccountingEntry.setIndexNames, fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(("FIBRE-CHANNEL-FE-MIB", "fcFxPortStatusEntry"))
apply(fcFxPortStatusEntry.setIndexNames, fcFxPortEntry.getIndexNames())

# Groups

fcFeClass3AccountingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 75, 2, 2, 6)).setObjects(("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3InFrames"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3OutOctets"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3InOctets"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3OutFrames"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3Discards"), )
fcFeClass1AccountingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 75, 2, 2, 4)).setObjects(("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1OutConnections"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1InConnections"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1FbsyFrames"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1ConnTime"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1OutOctets"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1OutFrames"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1InOctets"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1FrjtFrames"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1InFrames"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1Discards"), )
fcFeConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 75, 2, 2, 1)).setObjects(("FIBRE-CHANNEL-FE-MIB", "fcFeModuleCapacity"), ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleOperStatus"), ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleName"), ("FIBRE-CHANNEL-FE-MIB", "fcFeElementName"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortRatov"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortName"), ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleDescr"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortClass3SeqDeliv"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortEdtov"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCosSupported"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortBbCredit"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortClass2SeqDeliv"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortIntermixSupported"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortRxBufSize"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortFcphVersionHigh"), ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleLastChange"), ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleFxPortCapacity"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortHoldTime"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortStackedConnMode"), ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleObjectID"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortFcphVersionLow"), ("FIBRE-CHANNEL-FE-MIB", "fcFeFabricName"), )
fcFeStatusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 75, 2, 2, 2)).setObjects(("FIBRE-CHANNEL-FE-MIB", "fcFxPortNxPortBbCredit"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortPhysRttov"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortID"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortClass2SeqDelivAgreed"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCosSuppAgreed"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortNxPortRxDataFieldSize"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortIntermixSuppAgreed"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortBbCreditAvailable"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortClass3SeqDelivAgreed"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortStackedConnModeAgreed"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortNxPortName"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortPhysLastChange"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortPhysAdminStatus"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortAdminMode"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortFcphVersionAgreed"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortBbCreditModel"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortOperMode"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortConnectedNxPort"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortPhysOperStatus"), )
fcFeCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 75, 2, 2, 7)).setObjects(("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapFcphVersionLow"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapRxDataFieldSizeMin"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapBbCreditMin"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapFcphVersionHigh"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapClass2SeqDeliv"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapBbCreditMax"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapHoldTimeMin"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapClass3SeqDeliv"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapHoldTimeMax"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapStackedConnMode"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapRxDataFieldSizeMax"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapIntermix"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapCos"), )
fcFeClass2AccountingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 75, 2, 2, 5)).setObjects(("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2FbsyFrames"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2OutFrames"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2OutOctets"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2InFrames"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2FrjtFrames"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2Discards"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2InOctets"), )
fcFeErrorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 75, 2, 2, 3)).setObjects(("FIBRE-CHANNEL-FE-MIB", "fcFxPortLinkFailures"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortInvalidTxWords"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortLinkResetIns"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortPrimSeqProtoErrors"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortAddressIdErrors"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortOlsIns"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortLinkResetOuts"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortInvalidCrcs"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortOlsOuts"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortDelimiterErrors"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortSyncLosses"), ("FIBRE-CHANNEL-FE-MIB", "fcFxPortSigLosses"), )

# Exports

# Module identity
mibBuilder.exportSymbols("FIBRE-CHANNEL-FE-MIB", PYSNMP_MODULE_ID=fcFeMIB)

# Types
mibBuilder.exportSymbols("FIBRE-CHANNEL-FE-MIB", FcAddressId=FcAddressId, FcBbCredit=FcBbCredit, FcBbCreditModel=FcBbCreditModel, FcCosCap=FcCosCap, FcFeFxPortCapacity=FcFeFxPortCapacity, FcFeFxPortIndex=FcFeFxPortIndex, FcFeModuleCapacity=FcFeModuleCapacity, FcFeModuleIndex=FcFeModuleIndex, FcFeNxPortIndex=FcFeNxPortIndex, FcNameId=FcNameId, FcRxDataFieldSize=FcRxDataFieldSize, FcStackedConnMode=FcStackedConnMode, FcphVersion=FcphVersion, MicroSeconds=MicroSeconds, MilliSeconds=MilliSeconds)

# Objects
mibBuilder.exportSymbols("FIBRE-CHANNEL-FE-MIB", fcFeMIB=fcFeMIB, fcFeMIBObjects=fcFeMIBObjects, fcFeConfig=fcFeConfig, fcFeFabricName=fcFeFabricName, fcFeElementName=fcFeElementName, fcFeModuleCapacity=fcFeModuleCapacity, fcFeModuleTable=fcFeModuleTable, fcFeModuleEntry=fcFeModuleEntry, fcFeModuleIndex=fcFeModuleIndex, fcFeModuleDescr=fcFeModuleDescr, fcFeModuleObjectID=fcFeModuleObjectID, fcFeModuleOperStatus=fcFeModuleOperStatus, fcFeModuleLastChange=fcFeModuleLastChange, fcFeModuleFxPortCapacity=fcFeModuleFxPortCapacity, fcFeModuleName=fcFeModuleName, fcFxPortTable=fcFxPortTable, fcFxPortEntry=fcFxPortEntry, fcFxPortIndex=fcFxPortIndex, fcFxPortName=fcFxPortName, fcFxPortFcphVersionHigh=fcFxPortFcphVersionHigh, fcFxPortFcphVersionLow=fcFxPortFcphVersionLow, fcFxPortBbCredit=fcFxPortBbCredit, fcFxPortRxBufSize=fcFxPortRxBufSize, fcFxPortRatov=fcFxPortRatov, fcFxPortEdtov=fcFxPortEdtov, fcFxPortCosSupported=fcFxPortCosSupported, fcFxPortIntermixSupported=fcFxPortIntermixSupported, fcFxPortStackedConnMode=fcFxPortStackedConnMode, fcFxPortClass2SeqDeliv=fcFxPortClass2SeqDeliv, fcFxPortClass3SeqDeliv=fcFxPortClass3SeqDeliv, fcFxPortHoldTime=fcFxPortHoldTime, fcFeStatus=fcFeStatus, fcFxPortStatusTable=fcFxPortStatusTable, fcFxPortStatusEntry=fcFxPortStatusEntry, fcFxPortID=fcFxPortID, fcFxPortBbCreditAvailable=fcFxPortBbCreditAvailable, fcFxPortOperMode=fcFxPortOperMode, fcFxPortAdminMode=fcFxPortAdminMode, fcFxPortPhysTable=fcFxPortPhysTable, fcFxPortPhysEntry=fcFxPortPhysEntry, fcFxPortPhysAdminStatus=fcFxPortPhysAdminStatus, fcFxPortPhysOperStatus=fcFxPortPhysOperStatus, fcFxPortPhysLastChange=fcFxPortPhysLastChange, fcFxPortPhysRttov=fcFxPortPhysRttov, fcFxLoginTable=fcFxLoginTable, fcFxLoginEntry=fcFxLoginEntry, fcFxPortNxLoginIndex=fcFxPortNxLoginIndex, fcFxPortFcphVersionAgreed=fcFxPortFcphVersionAgreed, fcFxPortNxPortBbCredit=fcFxPortNxPortBbCredit, fcFxPortNxPortRxDataFieldSize=fcFxPortNxPortRxDataFieldSize, fcFxPortCosSuppAgreed=fcFxPortCosSuppAgreed, fcFxPortIntermixSuppAgreed=fcFxPortIntermixSuppAgreed, fcFxPortStackedConnModeAgreed=fcFxPortStackedConnModeAgreed, fcFxPortClass2SeqDelivAgreed=fcFxPortClass2SeqDelivAgreed, fcFxPortClass3SeqDelivAgreed=fcFxPortClass3SeqDelivAgreed, fcFxPortNxPortName=fcFxPortNxPortName, fcFxPortConnectedNxPort=fcFxPortConnectedNxPort, fcFxPortBbCreditModel=fcFxPortBbCreditModel, fcFeError=fcFeError, fcFxPortErrorTable=fcFxPortErrorTable, fcFxPortErrorEntry=fcFxPortErrorEntry, fcFxPortLinkFailures=fcFxPortLinkFailures, fcFxPortSyncLosses=fcFxPortSyncLosses, fcFxPortSigLosses=fcFxPortSigLosses, fcFxPortPrimSeqProtoErrors=fcFxPortPrimSeqProtoErrors, fcFxPortInvalidTxWords=fcFxPortInvalidTxWords, fcFxPortInvalidCrcs=fcFxPortInvalidCrcs, fcFxPortDelimiterErrors=fcFxPortDelimiterErrors, fcFxPortAddressIdErrors=fcFxPortAddressIdErrors, fcFxPortLinkResetIns=fcFxPortLinkResetIns, fcFxPortLinkResetOuts=fcFxPortLinkResetOuts, fcFxPortOlsIns=fcFxPortOlsIns, fcFxPortOlsOuts=fcFxPortOlsOuts, fcFeAccounting=fcFeAccounting, fcFxPortC1AccountingTable=fcFxPortC1AccountingTable, fcFxPortC1AccountingEntry=fcFxPortC1AccountingEntry, fcFxPortC1InFrames=fcFxPortC1InFrames, fcFxPortC1OutFrames=fcFxPortC1OutFrames, fcFxPortC1InOctets=fcFxPortC1InOctets, fcFxPortC1OutOctets=fcFxPortC1OutOctets, fcFxPortC1Discards=fcFxPortC1Discards, fcFxPortC1FbsyFrames=fcFxPortC1FbsyFrames, fcFxPortC1FrjtFrames=fcFxPortC1FrjtFrames, fcFxPortC1InConnections=fcFxPortC1InConnections, fcFxPortC1OutConnections=fcFxPortC1OutConnections, fcFxPortC1ConnTime=fcFxPortC1ConnTime, fcFxPortC2AccountingTable=fcFxPortC2AccountingTable, fcFxPortC2AccountingEntry=fcFxPortC2AccountingEntry, fcFxPortC2InFrames=fcFxPortC2InFrames, fcFxPortC2OutFrames=fcFxPortC2OutFrames, fcFxPortC2InOctets=fcFxPortC2InOctets, fcFxPortC2OutOctets=fcFxPortC2OutOctets, fcFxPortC2Discards=fcFxPortC2Discards, fcFxPortC2FbsyFrames=fcFxPortC2FbsyFrames, fcFxPortC2FrjtFrames=fcFxPortC2FrjtFrames, fcFxPortC3AccountingTable=fcFxPortC3AccountingTable, fcFxPortC3AccountingEntry=fcFxPortC3AccountingEntry, fcFxPortC3InFrames=fcFxPortC3InFrames, fcFxPortC3OutFrames=fcFxPortC3OutFrames, fcFxPortC3InOctets=fcFxPortC3InOctets, fcFxPortC3OutOctets=fcFxPortC3OutOctets, fcFxPortC3Discards=fcFxPortC3Discards, fcFeCapabilities=fcFeCapabilities, fcFxPortCapTable=fcFxPortCapTable, fcFxPortCapEntry=fcFxPortCapEntry, fcFxPortCapFcphVersionHigh=fcFxPortCapFcphVersionHigh, fcFxPortCapFcphVersionLow=fcFxPortCapFcphVersionLow, fcFxPortCapBbCreditMax=fcFxPortCapBbCreditMax, fcFxPortCapBbCreditMin=fcFxPortCapBbCreditMin, fcFxPortCapRxDataFieldSizeMax=fcFxPortCapRxDataFieldSizeMax, fcFxPortCapRxDataFieldSizeMin=fcFxPortCapRxDataFieldSizeMin, fcFxPortCapCos=fcFxPortCapCos, fcFxPortCapIntermix=fcFxPortCapIntermix, fcFxPortCapStackedConnMode=fcFxPortCapStackedConnMode, fcFxPortCapClass2SeqDeliv=fcFxPortCapClass2SeqDeliv, fcFxPortCapClass3SeqDeliv=fcFxPortCapClass3SeqDeliv, fcFxPortCapHoldTimeMax=fcFxPortCapHoldTimeMax, fcFxPortCapHoldTimeMin=fcFxPortCapHoldTimeMin, fcFeMIBConformance=fcFeMIBConformance, fcFeMIBCompliances=fcFeMIBCompliances, fcFeMIBGroups=fcFeMIBGroups)

# Groups
mibBuilder.exportSymbols("FIBRE-CHANNEL-FE-MIB", fcFeClass3AccountingGroup=fcFeClass3AccountingGroup, fcFeClass1AccountingGroup=fcFeClass1AccountingGroup, fcFeConfigGroup=fcFeConfigGroup, fcFeStatusGroup=fcFeStatusGroup, fcFeCapabilitiesGroup=fcFeCapabilitiesGroup, fcFeClass2AccountingGroup=fcFeClass2AccountingGroup, fcFeErrorGroup=fcFeErrorGroup)
