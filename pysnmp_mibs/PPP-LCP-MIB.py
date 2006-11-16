# PySNMP SMI module. Autogenerated from smidump -f python PPP-LCP-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 19:13:34 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ifIndex, transmission, ) = mibBuilder.importSymbols("RFC1213-MIB", "ifIndex", "transmission")
( Bits, Counter32, Integer32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

ppp = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23))
pppLcp = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1))
pppLink = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 1))
pppLinkStatusTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1))
pppLinkStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppLinkStatusPhysicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
pppLinkStatusBadAddresses = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
pppLinkStatusBadControls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
pppLinkStatusPacketTooLongs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
pppLinkStatusBadFCSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
pppLinkStatusLocalMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
pppLinkStatusRemoteMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
pppLinkStatusLocalToPeerACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 4)).setFixedLength()).setMaxAccess("readonly")
pppLinkStatusPeerToLocalACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 4)).setFixedLength()).setMaxAccess("readonly")
pppLinkStatusLocalToRemoteProtocolCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 10), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readonly")
pppLinkStatusRemoteToLocalProtocolCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 11), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readonly")
pppLinkStatusLocalToRemoteACCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 12), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readonly")
pppLinkStatusRemoteToLocalACCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 13), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readonly")
pppLinkStatusTransmitFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
pppLinkStatusReceiveFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
pppLinkConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2))
pppLinkConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppLinkConfigInitialMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(1500)).setMaxAccess("readwrite")
pppLinkConfigReceiveACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 4)).setFixedLength().clone('\xff\xff\xff\xff')).setMaxAccess("readwrite")
pppLinkConfigTransmitACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 4)).setFixedLength().clone('\xff\xff\xff\xff')).setMaxAccess("readwrite")
pppLinkConfigMagicNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("false", 1), ("true", 2), )).clone(1)).setMaxAccess("readwrite")
pppLinkConfigFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 128)).clone(16)).setMaxAccess("readwrite")
pppLqr = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 2))
pppLqrTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1))
pppLqrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppLqrQuality = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("good", 1), ("bad", 2), ("not-determined", 3), ))).setMaxAccess("readonly")
pppLqrInGoodOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
pppLqrLocalPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
pppLqrRemotePeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("readonly")
pppLqrOutLQRs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
pppLqrInLQRs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
pppLqrConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2))
pppLqrConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppLqrConfigPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readwrite")
pppLqrConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("disabled", 1), ("enabled", 2), )).clone(2)).setMaxAccess("readwrite")
pppLqrExtnsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3))
pppLqrExtnsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3, 1)).setIndexNames((0, "RFC1213-MIB", "ifIndex"))
pppLqrExtnsLastReceivedLqrPacket = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(68, 68)).setFixedLength()).setMaxAccess("readonly")
pppTests = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3))
pppEchoTest = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3, 1))
pppDiscardTest = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3, 2))

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("PPP-LCP-MIB", ppp=ppp, pppLcp=pppLcp, pppLink=pppLink, pppLinkStatusTable=pppLinkStatusTable, pppLinkStatusEntry=pppLinkStatusEntry, pppLinkStatusPhysicalIndex=pppLinkStatusPhysicalIndex, pppLinkStatusBadAddresses=pppLinkStatusBadAddresses, pppLinkStatusBadControls=pppLinkStatusBadControls, pppLinkStatusPacketTooLongs=pppLinkStatusPacketTooLongs, pppLinkStatusBadFCSs=pppLinkStatusBadFCSs, pppLinkStatusLocalMRU=pppLinkStatusLocalMRU, pppLinkStatusRemoteMRU=pppLinkStatusRemoteMRU, pppLinkStatusLocalToPeerACCMap=pppLinkStatusLocalToPeerACCMap, pppLinkStatusPeerToLocalACCMap=pppLinkStatusPeerToLocalACCMap, pppLinkStatusLocalToRemoteProtocolCompression=pppLinkStatusLocalToRemoteProtocolCompression, pppLinkStatusRemoteToLocalProtocolCompression=pppLinkStatusRemoteToLocalProtocolCompression, pppLinkStatusLocalToRemoteACCompression=pppLinkStatusLocalToRemoteACCompression, pppLinkStatusRemoteToLocalACCompression=pppLinkStatusRemoteToLocalACCompression, pppLinkStatusTransmitFcsSize=pppLinkStatusTransmitFcsSize, pppLinkStatusReceiveFcsSize=pppLinkStatusReceiveFcsSize, pppLinkConfigTable=pppLinkConfigTable, pppLinkConfigEntry=pppLinkConfigEntry, pppLinkConfigInitialMRU=pppLinkConfigInitialMRU, pppLinkConfigReceiveACCMap=pppLinkConfigReceiveACCMap, pppLinkConfigTransmitACCMap=pppLinkConfigTransmitACCMap, pppLinkConfigMagicNumber=pppLinkConfigMagicNumber, pppLinkConfigFcsSize=pppLinkConfigFcsSize, pppLqr=pppLqr, pppLqrTable=pppLqrTable, pppLqrEntry=pppLqrEntry, pppLqrQuality=pppLqrQuality, pppLqrInGoodOctets=pppLqrInGoodOctets, pppLqrLocalPeriod=pppLqrLocalPeriod, pppLqrRemotePeriod=pppLqrRemotePeriod, pppLqrOutLQRs=pppLqrOutLQRs, pppLqrInLQRs=pppLqrInLQRs, pppLqrConfigTable=pppLqrConfigTable, pppLqrConfigEntry=pppLqrConfigEntry, pppLqrConfigPeriod=pppLqrConfigPeriod, pppLqrConfigStatus=pppLqrConfigStatus, pppLqrExtnsTable=pppLqrExtnsTable, pppLqrExtnsEntry=pppLqrExtnsEntry, pppLqrExtnsLastReceivedLqrPacket=pppLqrExtnsLastReceivedLqrPacket, pppTests=pppTests, pppEchoTest=pppEchoTest, pppDiscardTest=pppDiscardTest)

