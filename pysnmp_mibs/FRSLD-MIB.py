# PySNMP SMI module. Autogenerated from smidump -f python FRSLD-MIB
# by libsmi2pysnmp-0.0.6-alpha at Thu Apr  6 13:19:18 2006,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( DLCI, ) = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "DLCI")
( CounterBasedGauge64, ) = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2")
( RowStatus, TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeStamp")

# Types

class FrsldRxRP(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,11,9,1,5,2,6,8,10,12,3,7,)
    namedValues = namedval.NamedValues(("desLocalRP", 1), ("eqiRxRemoteRP", 10), ("eqoRxRemoteRP", 11), ("otherRxRemoteRP", 12), ("ingRxLocalRP", 2), ("tpRxLocalRP", 3), ("eqiRxLocalRP", 4), ("eqoRxLocalRP", 5), ("otherRxLocalRP", 6), ("desRemoteRP", 7), ("ingRxRemoteRP", 8), ("tpRxRemoteRP", 9), )
    pass

class FrsldTxRP(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(6,5,12,10,3,4,11,1,9,7,2,8,)
    namedValues = namedval.NamedValues(("srcLocalRP", 1), ("eqiTxRemoteRP", 10), ("eqoTxRemoteRP", 11), ("otherTxRemoteRP", 12), ("ingTxLocalRP", 2), ("tpTxLocalRP", 3), ("eqiTxLocalRP", 4), ("eqoTxLocalRP", 5), ("otherTxLocalRP", 6), ("srcRemoteRP", 7), ("ingTxRemoteRP", 8), ("tpTxRemoteRP", 9), )
    pass


# Objects

frsldMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 95)).setRevisions(("2002-01-03 00:00",))
frsldObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 95, 1))
frsldPvcCtrlTable = MibTable((1, 3, 6, 1, 2, 1, 95, 1, 1))
frsldPvcCtrlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 95, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FRSLD-MIB", "frsldPvcCtrlDlci"), (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"), (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"))
frsldPvcCtrlDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 1), DLCI()).setMaxAccess("noaccess")
frsldPvcCtrlTransmitRP = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 2), FrsldTxRP()).setMaxAccess("noaccess")
frsldPvcCtrlReceiveRP = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 3), FrsldRxRP()).setMaxAccess("noaccess")
frsldPvcCtrlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
frsldPvcCtrlPacketFreq = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 3600)).clone(60)).setMaxAccess("readwrite")
frsldPvcCtrlDelayFrSize = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 8188)).clone(128)).setMaxAccess("readwrite")
frsldPvcCtrlDelayType = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("oneWay", 1), ("roundTrip", 2), ))).setMaxAccess("readwrite")
frsldPvcCtrlDelayTimeOut = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 3600)).clone(60)).setMaxAccess("readwrite")
frsldPvcCtrlPurge = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 172800)).clone(0)).setMaxAccess("readwrite")
frsldPvcCtrlDeleteOnPurge = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,3,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("sampleContols", 2), ("all", 3), )).clone(3)).setMaxAccess("readwrite")
frsldPvcCtrlLastPurgeTime = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 1, 1, 11), TimeStamp()).setMaxAccess("readonly")
frsldSmplCtrlTable = MibTable((1, 3, 6, 1, 2, 1, 95, 1, 2))
frsldSmplCtrlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 95, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FRSLD-MIB", "frsldPvcCtrlDlci"), (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"), (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"), (0, "FRSLD-MIB", "frsldSmplCtrlIdx"))
frsldSmplCtrlIdx = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 256))).setMaxAccess("noaccess")
frsldSmplCtrlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 2), RowStatus()).setMaxAccess("readwrite")
frsldSmplCtrlColPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readwrite")
frsldSmplCtrlBuckets = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 65535)).clone(60)).setMaxAccess("readwrite")
frsldSmplCtrlBucketsGranted = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
frsldPvcDataTable = MibTable((1, 3, 6, 1, 2, 1, 95, 1, 3))
frsldPvcDataEntry = MibTableRow((1, 3, 6, 1, 2, 1, 95, 1, 3, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FRSLD-MIB", "frsldPvcCtrlDlci"), (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"), (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"))
frsldPvcDataMissedPolls = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
frsldPvcDataFrDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
frsldPvcDataFrDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
frsldPvcDataFrOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
frsldPvcDataFrOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
frsldPvcDataDataDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
frsldPvcDataDataDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
frsldPvcDataDataOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
frsldPvcDataDataOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
frsldPvcDataHCFrDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
frsldPvcDataHCFrDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 11), Counter64()).setMaxAccess("readonly")
frsldPvcDataHCFrOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 12), Counter64()).setMaxAccess("readonly")
frsldPvcDataHCFrOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 13), Counter64()).setMaxAccess("readonly")
frsldPvcDataHCDataDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 14), Counter64()).setMaxAccess("readonly")
frsldPvcDataHCDataDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 15), Counter64()).setMaxAccess("readonly")
frsldPvcDataHCDataOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 16), Counter64()).setMaxAccess("readonly")
frsldPvcDataHCDataOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 17), Counter64()).setMaxAccess("readonly")
frsldPvcDataUnavailableTime = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 18), TimeTicks()).setMaxAccess("readonly")
frsldPvcDataUnavailables = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
frsldPvcSampleTable = MibTable((1, 3, 6, 1, 2, 1, 95, 1, 4))
frsldPvcSampleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 95, 1, 4, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "FRSLD-MIB", "frsldPvcCtrlDlci"), (0, "FRSLD-MIB", "frsldPvcCtrlTransmitRP"), (0, "FRSLD-MIB", "frsldPvcCtrlReceiveRP"), (0, "FRSLD-MIB", "frsldSmplCtrlIdx"), (0, "FRSLD-MIB", "frsldPvcSmplIdx"))
frsldPvcSmplIdx = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
frsldPvcSmplDelayMin = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplDelayMax = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplDelayAvg = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplMissedPolls = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplFrDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplFrDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplFrOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 8), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplFrOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 9), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplDataDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 10), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplDataDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 11), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplDataOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 12), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplDataOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 13), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplHCFrDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 14), CounterBasedGauge64()).setMaxAccess("readonly")
frsldPvcSmplHCFrDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 15), CounterBasedGauge64()).setMaxAccess("readonly")
frsldPvcSmplHCFrOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 16), CounterBasedGauge64()).setMaxAccess("readonly")
frsldPvcSmplHCFrOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 17), CounterBasedGauge64()).setMaxAccess("readonly")
frsldPvcSmplHCDataDeliveredC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 18), CounterBasedGauge64()).setMaxAccess("readonly")
frsldPvcSmplHCDataDeliveredE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 19), CounterBasedGauge64()).setMaxAccess("readonly")
frsldPvcSmplHCDataOfferedC = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 20), CounterBasedGauge64()).setMaxAccess("readonly")
frsldPvcSmplHCDataOfferedE = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 21), CounterBasedGauge64()).setMaxAccess("readonly")
frsldPvcSmplUnavailableTime = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 22), TimeTicks()).setMaxAccess("readonly")
frsldPvcSmplUnavailables = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 23), Gauge32()).setMaxAccess("readonly")
frsldPvcSmplStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 24), TimeStamp()).setMaxAccess("readonly")
frsldPvcSmplEndTime = MibTableColumn((1, 3, 6, 1, 2, 1, 95, 1, 4, 1, 25), TimeStamp()).setMaxAccess("readonly")
frsldCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 95, 2))
frsldPvcCtrlWriteCaps = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 1), Bits().subtype(namedValues=namedval.NamedValues(("frsldPvcCtrlStatus", 0), ("frsldPvcCtrlPacketFreq", 1), ("frsldPvcCtrlDelayFrSize", 2), ("frsldPvcCtrlDelayType", 3), ("frsldPvcCtrlDelayTimeOut", 4), ("frsldPvcCtrlPurge", 5), ("frsldPvcCtrlDeleteOnPurge", 6), ))).setMaxAccess("readonly")
frsldSmplCtrlWriteCaps = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 2), Bits().subtype(namedValues=namedval.NamedValues(("frsldSmplCtrlStatus", 0), ("frsldSmplCtrlBuckets", 1), ))).setMaxAccess("readonly")
frsldRPCaps = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 3), Bits().subtype(namedValues=namedval.NamedValues(("srcLocalRP", 0), ("ingTxLocalRP", 1), ("eqoTxRemoteRP", 10), ("otherTxRemoteRP", 11), ("desLocalRP", 12), ("ingRxLocalRP", 13), ("tpRxLocalRP", 14), ("eqiRxLocalRP", 15), ("eqoRxLocalRP", 16), ("otherRxLocalRP", 17), ("desRemoteRP", 18), ("ingRxRemoteRP", 19), ("tpTxLocalRP", 2), ("tpRxRemoteRP", 20), ("eqiRxRemoteRP", 21), ("eqoRxRemoteRP", 22), ("otherRxRemoteRP", 23), ("eqiTxLocalRP", 3), ("eqoTxLocalRP", 4), ("otherTxLocalRP", 5), ("srcRemoteRP", 6), ("ingTxRemoteRP", 7), ("tpTxRemoteRP", 8), ("eqiTxRemoteRP", 9), ))).setMaxAccess("readonly")
frsldMaxPvcCtrls = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readwrite")
frsldNumPvcCtrls = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 5), Gauge32()).setMaxAccess("readonly")
frsldMaxSmplCtrls = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readwrite")
frsldNumSmplCtrls = MibScalar((1, 3, 6, 1, 2, 1, 95, 2, 7), Gauge32()).setMaxAccess("readonly")
frsldConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 95, 3))
frsldMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 95, 3, 1))
frsldMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 95, 3, 2))

# Augmentions

# Groups

frsldPvcReqCtrlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 1)).setObjects(("FRSLD-MIB", "frsldPvcCtrlLastPurgeTime"), ("FRSLD-MIB", "frsldPvcCtrlDeleteOnPurge"), ("FRSLD-MIB", "frsldPvcCtrlPurge"), ("FRSLD-MIB", "frsldPvcCtrlStatus"), )
frsldPvcDelayDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 6)).setObjects(("FRSLD-MIB", "frsldPvcDataMissedPolls"), )
frsldPvcSampleDelayGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 9)).setObjects(("FRSLD-MIB", "frsldPvcSmplDelayMin"), ("FRSLD-MIB", "frsldPvcSmplMissedPolls"), ("FRSLD-MIB", "frsldPvcSmplDelayMax"), ("FRSLD-MIB", "frsldPvcSmplDelayAvg"), )
frsldPvcPacketGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 2)).setObjects(("FRSLD-MIB", "frsldPvcCtrlPacketFreq"), )
frsldPvcHCOctetDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 8)).setObjects(("FRSLD-MIB", "frsldPvcDataHCDataDeliveredC"), ("FRSLD-MIB", "frsldPvcDataHCDataOfferedE"), ("FRSLD-MIB", "frsldPvcDataHCDataOfferedC"), ("FRSLD-MIB", "frsldPvcDataHCDataDeliveredE"), )
frsldPvcReqDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 5)).setObjects(("FRSLD-MIB", "frsldPvcDataFrOfferedE"), ("FRSLD-MIB", "frsldPvcDataDataDeliveredE"), ("FRSLD-MIB", "frsldPvcDataDataDeliveredC"), ("FRSLD-MIB", "frsldPvcDataFrOfferedC"), ("FRSLD-MIB", "frsldPvcDataFrDeliveredE"), ("FRSLD-MIB", "frsldPvcDataUnavailableTime"), ("FRSLD-MIB", "frsldPvcDataFrDeliveredC"), ("FRSLD-MIB", "frsldPvcDataDataOfferedC"), ("FRSLD-MIB", "frsldPvcDataDataOfferedE"), ("FRSLD-MIB", "frsldPvcDataUnavailables"), )
frsldPvcSampleDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 10)).setObjects(("FRSLD-MIB", "frsldPvcSmplFrDeliveredE"), ("FRSLD-MIB", "frsldPvcSmplFrDeliveredC"), ("FRSLD-MIB", "frsldPvcSmplDataOfferedC"), ("FRSLD-MIB", "frsldPvcSmplDataOfferedE"), ("FRSLD-MIB", "frsldPvcSmplFrOfferedE"), ("FRSLD-MIB", "frsldPvcSmplDataDeliveredE"), ("FRSLD-MIB", "frsldPvcSmplDataDeliveredC"), ("FRSLD-MIB", "frsldPvcSmplFrOfferedC"), )
frsldPvcSampleCtrlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 4)).setObjects(("FRSLD-MIB", "frsldSmplCtrlStatus"), ("FRSLD-MIB", "frsldSmplCtrlColPeriod"), ("FRSLD-MIB", "frsldSmplCtrlBuckets"), ("FRSLD-MIB", "frsldSmplCtrlBucketsGranted"), )
frsldPvcSampleGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 14)).setObjects(("FRSLD-MIB", "frsldPvcSmplEndTime"), ("FRSLD-MIB", "frsldPvcSmplStartTime"), )
frsldPvcDelayCtrlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 3)).setObjects(("FRSLD-MIB", "frsldPvcCtrlDelayTimeOut"), ("FRSLD-MIB", "frsldPvcCtrlDelayFrSize"), ("FRSLD-MIB", "frsldPvcCtrlDelayType"), )
frsldPvcSampleHCFrameGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 11)).setObjects(("FRSLD-MIB", "frsldPvcSmplHCFrDeliveredC"), ("FRSLD-MIB", "frsldPvcSmplHCFrOfferedC"), ("FRSLD-MIB", "frsldPvcSmplHCFrDeliveredE"), ("FRSLD-MIB", "frsldPvcSmplHCFrOfferedE"), )
frsldPvcSampleAvailGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 13)).setObjects(("FRSLD-MIB", "frsldPvcSmplUnavailables"), ("FRSLD-MIB", "frsldPvcSmplUnavailableTime"), )
frsldCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 15)).setObjects(("FRSLD-MIB", "frsldPvcCtrlWriteCaps"), ("FRSLD-MIB", "frsldNumSmplCtrls"), ("FRSLD-MIB", "frsldRPCaps"), ("FRSLD-MIB", "frsldMaxSmplCtrls"), ("FRSLD-MIB", "frsldMaxPvcCtrls"), ("FRSLD-MIB", "frsldSmplCtrlWriteCaps"), ("FRSLD-MIB", "frsldNumPvcCtrls"), )
frsldPvcHCFrameDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 7)).setObjects(("FRSLD-MIB", "frsldPvcDataHCFrDeliveredC"), ("FRSLD-MIB", "frsldPvcDataHCFrOfferedC"), ("FRSLD-MIB", "frsldPvcDataHCFrDeliveredE"), ("FRSLD-MIB", "frsldPvcDataHCFrOfferedE"), )
frsldPvcSampleHCDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 95, 3, 1, 12)).setObjects(("FRSLD-MIB", "frsldPvcSmplHCDataDeliveredC"), ("FRSLD-MIB", "frsldPvcSmplHCDataOfferedE"), ("FRSLD-MIB", "frsldPvcSmplHCDataOfferedC"), ("FRSLD-MIB", "frsldPvcSmplHCDataDeliveredE"), )

# Exports

# Module identity
mibBuilder.exportSymbols("FRSLD-MIB", PYSNMP_MODULE_ID=frsldMIB)

# Types
mibBuilder.exportSymbols("FRSLD-MIB", FrsldRxRP=FrsldRxRP, FrsldTxRP=FrsldTxRP)

# Objects
mibBuilder.exportSymbols("FRSLD-MIB", frsldMIB=frsldMIB, frsldObjects=frsldObjects, frsldPvcCtrlTable=frsldPvcCtrlTable, frsldPvcCtrlEntry=frsldPvcCtrlEntry, frsldPvcCtrlDlci=frsldPvcCtrlDlci, frsldPvcCtrlTransmitRP=frsldPvcCtrlTransmitRP, frsldPvcCtrlReceiveRP=frsldPvcCtrlReceiveRP, frsldPvcCtrlStatus=frsldPvcCtrlStatus, frsldPvcCtrlPacketFreq=frsldPvcCtrlPacketFreq, frsldPvcCtrlDelayFrSize=frsldPvcCtrlDelayFrSize, frsldPvcCtrlDelayType=frsldPvcCtrlDelayType, frsldPvcCtrlDelayTimeOut=frsldPvcCtrlDelayTimeOut, frsldPvcCtrlPurge=frsldPvcCtrlPurge, frsldPvcCtrlDeleteOnPurge=frsldPvcCtrlDeleteOnPurge, frsldPvcCtrlLastPurgeTime=frsldPvcCtrlLastPurgeTime, frsldSmplCtrlTable=frsldSmplCtrlTable, frsldSmplCtrlEntry=frsldSmplCtrlEntry, frsldSmplCtrlIdx=frsldSmplCtrlIdx, frsldSmplCtrlStatus=frsldSmplCtrlStatus, frsldSmplCtrlColPeriod=frsldSmplCtrlColPeriod, frsldSmplCtrlBuckets=frsldSmplCtrlBuckets, frsldSmplCtrlBucketsGranted=frsldSmplCtrlBucketsGranted, frsldPvcDataTable=frsldPvcDataTable, frsldPvcDataEntry=frsldPvcDataEntry, frsldPvcDataMissedPolls=frsldPvcDataMissedPolls, frsldPvcDataFrDeliveredC=frsldPvcDataFrDeliveredC, frsldPvcDataFrDeliveredE=frsldPvcDataFrDeliveredE, frsldPvcDataFrOfferedC=frsldPvcDataFrOfferedC, frsldPvcDataFrOfferedE=frsldPvcDataFrOfferedE, frsldPvcDataDataDeliveredC=frsldPvcDataDataDeliveredC, frsldPvcDataDataDeliveredE=frsldPvcDataDataDeliveredE, frsldPvcDataDataOfferedC=frsldPvcDataDataOfferedC, frsldPvcDataDataOfferedE=frsldPvcDataDataOfferedE, frsldPvcDataHCFrDeliveredC=frsldPvcDataHCFrDeliveredC, frsldPvcDataHCFrDeliveredE=frsldPvcDataHCFrDeliveredE, frsldPvcDataHCFrOfferedC=frsldPvcDataHCFrOfferedC, frsldPvcDataHCFrOfferedE=frsldPvcDataHCFrOfferedE, frsldPvcDataHCDataDeliveredC=frsldPvcDataHCDataDeliveredC, frsldPvcDataHCDataDeliveredE=frsldPvcDataHCDataDeliveredE, frsldPvcDataHCDataOfferedC=frsldPvcDataHCDataOfferedC, frsldPvcDataHCDataOfferedE=frsldPvcDataHCDataOfferedE, frsldPvcDataUnavailableTime=frsldPvcDataUnavailableTime, frsldPvcDataUnavailables=frsldPvcDataUnavailables, frsldPvcSampleTable=frsldPvcSampleTable, frsldPvcSampleEntry=frsldPvcSampleEntry, frsldPvcSmplIdx=frsldPvcSmplIdx, frsldPvcSmplDelayMin=frsldPvcSmplDelayMin, frsldPvcSmplDelayMax=frsldPvcSmplDelayMax, frsldPvcSmplDelayAvg=frsldPvcSmplDelayAvg, frsldPvcSmplMissedPolls=frsldPvcSmplMissedPolls, frsldPvcSmplFrDeliveredC=frsldPvcSmplFrDeliveredC, frsldPvcSmplFrDeliveredE=frsldPvcSmplFrDeliveredE, frsldPvcSmplFrOfferedC=frsldPvcSmplFrOfferedC, frsldPvcSmplFrOfferedE=frsldPvcSmplFrOfferedE, frsldPvcSmplDataDeliveredC=frsldPvcSmplDataDeliveredC, frsldPvcSmplDataDeliveredE=frsldPvcSmplDataDeliveredE, frsldPvcSmplDataOfferedC=frsldPvcSmplDataOfferedC, frsldPvcSmplDataOfferedE=frsldPvcSmplDataOfferedE, frsldPvcSmplHCFrDeliveredC=frsldPvcSmplHCFrDeliveredC, frsldPvcSmplHCFrDeliveredE=frsldPvcSmplHCFrDeliveredE, frsldPvcSmplHCFrOfferedC=frsldPvcSmplHCFrOfferedC, frsldPvcSmplHCFrOfferedE=frsldPvcSmplHCFrOfferedE, frsldPvcSmplHCDataDeliveredC=frsldPvcSmplHCDataDeliveredC, frsldPvcSmplHCDataDeliveredE=frsldPvcSmplHCDataDeliveredE, frsldPvcSmplHCDataOfferedC=frsldPvcSmplHCDataOfferedC, frsldPvcSmplHCDataOfferedE=frsldPvcSmplHCDataOfferedE, frsldPvcSmplUnavailableTime=frsldPvcSmplUnavailableTime, frsldPvcSmplUnavailables=frsldPvcSmplUnavailables, frsldPvcSmplStartTime=frsldPvcSmplStartTime, frsldPvcSmplEndTime=frsldPvcSmplEndTime, frsldCapabilities=frsldCapabilities, frsldPvcCtrlWriteCaps=frsldPvcCtrlWriteCaps, frsldSmplCtrlWriteCaps=frsldSmplCtrlWriteCaps, frsldRPCaps=frsldRPCaps, frsldMaxPvcCtrls=frsldMaxPvcCtrls, frsldNumPvcCtrls=frsldNumPvcCtrls, frsldMaxSmplCtrls=frsldMaxSmplCtrls, frsldNumSmplCtrls=frsldNumSmplCtrls, frsldConformance=frsldConformance, frsldMIBGroups=frsldMIBGroups, frsldMIBCompliances=frsldMIBCompliances)

# Groups
mibBuilder.exportSymbols("FRSLD-MIB", frsldPvcReqCtrlGroup=frsldPvcReqCtrlGroup, frsldPvcDelayDataGroup=frsldPvcDelayDataGroup, frsldPvcSampleDelayGroup=frsldPvcSampleDelayGroup, frsldPvcPacketGroup=frsldPvcPacketGroup, frsldPvcHCOctetDataGroup=frsldPvcHCOctetDataGroup, frsldPvcReqDataGroup=frsldPvcReqDataGroup, frsldPvcSampleDataGroup=frsldPvcSampleDataGroup, frsldPvcSampleCtrlGroup=frsldPvcSampleCtrlGroup, frsldPvcSampleGeneralGroup=frsldPvcSampleGeneralGroup, frsldPvcDelayCtrlGroup=frsldPvcDelayCtrlGroup, frsldPvcSampleHCFrameGroup=frsldPvcSampleHCFrameGroup, frsldPvcSampleAvailGroup=frsldPvcSampleAvailGroup, frsldCapabilitiesGroup=frsldCapabilitiesGroup, frsldPvcHCFrameDataGroup=frsldPvcHCFrameDataGroup, frsldPvcSampleHCDataGroup=frsldPvcSampleHCDataGroup)
