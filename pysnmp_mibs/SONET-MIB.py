# PySNMP SMI module. Autogenerated from smidump -f python SONET-MIB
# by libsmi2pysnmp-0.0.6-alpha at Thu Apr  6 13:19:36 2006,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( PerfCurrentCount, PerfIntervalCount, ) = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( DisplayString, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue")

# Objects

sonetMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 39)).setRevisions(("2003-08-11 00:00","1998-10-19 00:00","1994-01-03 00:00",))
sonetObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 1))
sonetMedium = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 1, 1))
sonetMediumTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1))
sonetMediumEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
sonetMediumType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("sonet", 1), ("sdh", 2), ))).setMaxAccess("readwrite")
sonetMediumTimeElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 900))).setMaxAccess("readonly")
sonetMediumValidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
sonetMediumLineCoding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,4,5,1,)).subtype(namedValues=namedval.NamedValues(("sonetMediumOther", 1), ("sonetMediumB3ZS", 2), ("sonetMediumCMI", 3), ("sonetMediumNRZ", 4), ("sonetMediumRZ", 5), ))).setMaxAccess("readwrite")
sonetMediumLineType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 5), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,4,1,5,6,3,)).subtype(namedValues=namedval.NamedValues(("sonetOther", 1), ("sonetShortSingleMode", 2), ("sonetLongSingleMode", 3), ("sonetMultiMode", 4), ("sonetCoax", 5), ("sonetUTP", 6), ))).setMaxAccess("readwrite")
sonetMediumCircuitIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
sonetMediumInvalidIntervals = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
sonetMediumLoopbackConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 1, 1, 8), Bits().subtype(namedValues=namedval.NamedValues(("sonetNoLoop", 0), ("sonetFacilityLoop", 1), ("sonetTerminalLoop", 2), ("sonetOtherLoop", 3), ))).setMaxAccess("readwrite")
sonetSESthresholdSet = MibScalar((1, 3, 6, 1, 2, 1, 10, 39, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,2,1,5,4,)).subtype(namedValues=namedval.NamedValues(("other", 1), ("bellcore1991", 2), ("ansi1993", 3), ("itu1995", 4), ("ansi1997", 5), ))).setMaxAccess("readwrite")
sonetSection = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 1, 2))
sonetSectionCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1))
sonetSectionCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
sonetSectionCurrentStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
sonetSectionCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
sonetSectionCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
sonetSectionCurrentSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
sonetSectionCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 1, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
sonetSectionIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2))
sonetSectionIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetSectionIntervalNumber"))
sonetSectionIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 96))).setMaxAccess("noaccess")
sonetSectionIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
sonetSectionIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
sonetSectionIntervalSEFSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
sonetSectionIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
sonetSectionIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 2, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
sonetLine = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 1, 3))
sonetLineCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1))
sonetLineCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
sonetLineCurrentStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
sonetLineCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
sonetLineCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
sonetLineCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
sonetLineCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 1, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
sonetLineIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2))
sonetLineIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetLineIntervalNumber"))
sonetLineIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 96))).setMaxAccess("noaccess")
sonetLineIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
sonetLineIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
sonetLineIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
sonetLineIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
sonetLineIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 3, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
sonetFarEndLine = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 1, 4))
sonetFarEndLineCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1))
sonetFarEndLineCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
sonetFarEndLineCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 1), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndLineCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndLineCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndLineCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 1, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndLineIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2))
sonetFarEndLineIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetFarEndLineIntervalNumber"))
sonetFarEndLineIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 96))).setMaxAccess("noaccess")
sonetFarEndLineIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndLineIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndLineIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndLineIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndLineIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 1, 4, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
sonetObjectsPath = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 2))
sonetPath = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 2, 1))
sonetPathCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1))
sonetPathCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
sonetPathCurrentWidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(7,2,1,6,3,5,4,)).subtype(namedValues=namedval.NamedValues(("sts1", 1), ("sts3cSTM1", 2), ("sts12cSTM4", 3), ("sts24c", 4), ("sts48cSTM16", 5), ("sts192cSTM64", 6), ("sts768cSTM256", 7), ))).setMaxAccess("readwrite")
sonetPathCurrentStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 62))).setMaxAccess("readonly")
sonetPathCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
sonetPathCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
sonetPathCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
sonetPathCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 1, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
sonetPathIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2))
sonetPathIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetPathIntervalNumber"))
sonetPathIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 96))).setMaxAccess("noaccess")
sonetPathIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
sonetPathIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
sonetPathIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
sonetPathIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
sonetPathIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
sonetFarEndPath = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 2, 2))
sonetFarEndPathCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1))
sonetFarEndPathCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
sonetFarEndPathCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 1), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndPathCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndPathCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndPathCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 1, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndPathIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2))
sonetFarEndPathIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetFarEndPathIntervalNumber"))
sonetFarEndPathIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 96))).setMaxAccess("noaccess")
sonetFarEndPathIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndPathIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndPathIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndPathIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndPathIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 2, 2, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
sonetObjectsVT = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 3))
sonetVT = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 3, 1))
sonetVTCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1))
sonetVTCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
sonetVTCurrentWidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(5,2,1,4,3,)).subtype(namedValues=namedval.NamedValues(("vtWidth15VC11", 1), ("vtWidth2VC12", 2), ("vtWidth3", 3), ("vtWidth6VC2", 4), ("vtWidth6c", 5), ))).setMaxAccess("readwrite")
sonetVTCurrentStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 126))).setMaxAccess("readonly")
sonetVTCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
sonetVTCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
sonetVTCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 5), PerfCurrentCount()).setMaxAccess("readonly")
sonetVTCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 1, 1, 6), PerfCurrentCount()).setMaxAccess("readonly")
sonetVTIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2))
sonetVTIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetVTIntervalNumber"))
sonetVTIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 96))).setMaxAccess("noaccess")
sonetVTIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
sonetVTIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
sonetVTIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
sonetVTIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
sonetVTIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
sonetFarEndVT = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 3, 2))
sonetFarEndVTCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1))
sonetFarEndVTCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
sonetFarEndVTCurrentESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 1), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndVTCurrentSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndVTCurrentCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndVTCurrentUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 1, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
sonetFarEndVTIntervalTable = MibTable((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2))
sonetFarEndVTIntervalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SONET-MIB", "sonetFarEndVTIntervalNumber"))
sonetFarEndVTIntervalNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 96))).setMaxAccess("noaccess")
sonetFarEndVTIntervalESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndVTIntervalSESs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndVTIntervalCVs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndVTIntervalUASs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
sonetFarEndVTIntervalValidData = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 39, 3, 2, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
sonetConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 4))
sonetGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 4, 1))
sonetCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 39, 4, 2))

# Augmentions

# Groups

sonetFarEndPathStuff2 = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 15)).setObjects(("SONET-MIB", "sonetFarEndPathIntervalSESs"), ("SONET-MIB", "sonetFarEndPathIntervalValidData"), ("SONET-MIB", "sonetFarEndPathIntervalESs"), ("SONET-MIB", "sonetFarEndPathCurrentUASs"), ("SONET-MIB", "sonetFarEndPathCurrentESs"), ("SONET-MIB", "sonetFarEndPathIntervalUASs"), ("SONET-MIB", "sonetFarEndPathCurrentCVs"), ("SONET-MIB", "sonetFarEndPathIntervalCVs"), ("SONET-MIB", "sonetFarEndPathCurrentSESs"), )
sonetSectionStuff2 = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 10)).setObjects(("SONET-MIB", "sonetSectionCurrentESs"), ("SONET-MIB", "sonetSectionIntervalSESs"), ("SONET-MIB", "sonetSectionIntervalESs"), ("SONET-MIB", "sonetSectionIntervalSEFSs"), ("SONET-MIB", "sonetSectionCurrentStatus"), ("SONET-MIB", "sonetSectionCurrentSESs"), ("SONET-MIB", "sonetSectionIntervalCVs"), ("SONET-MIB", "sonetSectionCurrentSEFSs"), ("SONET-MIB", "sonetSectionCurrentCVs"), ("SONET-MIB", "sonetSectionIntervalValidData"), )
sonetPathStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 5)).setObjects(("SONET-MIB", "sonetPathIntervalSESs"), ("SONET-MIB", "sonetPathIntervalESs"), ("SONET-MIB", "sonetPathCurrentStatus"), ("SONET-MIB", "sonetPathCurrentCVs"), ("SONET-MIB", "sonetPathIntervalUASs"), ("SONET-MIB", "sonetPathCurrentESs"), ("SONET-MIB", "sonetPathCurrentUASs"), ("SONET-MIB", "sonetPathCurrentWidth"), ("SONET-MIB", "sonetPathCurrentSESs"), ("SONET-MIB", "sonetPathIntervalCVs"), )
sonetFarEndVTStuff2 = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 16)).setObjects(("SONET-MIB", "sonetFarEndVTIntervalSESs"), ("SONET-MIB", "sonetFarEndVTCurrentUASs"), ("SONET-MIB", "sonetFarEndVTIntervalESs"), ("SONET-MIB", "sonetFarEndVTCurrentSESs"), ("SONET-MIB", "sonetFarEndVTIntervalCVs"), ("SONET-MIB", "sonetFarEndVTIntervalUASs"), ("SONET-MIB", "sonetFarEndVTCurrentESs"), ("SONET-MIB", "sonetFarEndVTIntervalValidData"), ("SONET-MIB", "sonetFarEndVTCurrentCVs"), )
sonetVTStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 7)).setObjects(("SONET-MIB", "sonetVTCurrentCVs"), ("SONET-MIB", "sonetVTCurrentStatus"), ("SONET-MIB", "sonetVTCurrentSESs"), ("SONET-MIB", "sonetVTCurrentWidth"), ("SONET-MIB", "sonetVTIntervalUASs"), ("SONET-MIB", "sonetVTCurrentUASs"), ("SONET-MIB", "sonetVTIntervalSESs"), ("SONET-MIB", "sonetVTIntervalESs"), ("SONET-MIB", "sonetVTIntervalCVs"), ("SONET-MIB", "sonetVTCurrentESs"), )
sonetLineStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 3)).setObjects(("SONET-MIB", "sonetLineCurrentCVs"), ("SONET-MIB", "sonetLineCurrentStatus"), ("SONET-MIB", "sonetLineIntervalESs"), ("SONET-MIB", "sonetLineCurrentSESs"), ("SONET-MIB", "sonetLineIntervalCVs"), ("SONET-MIB", "sonetLineIntervalSESs"), ("SONET-MIB", "sonetLineCurrentUASs"), ("SONET-MIB", "sonetLineIntervalUASs"), ("SONET-MIB", "sonetLineCurrentESs"), )
sonetFarEndLineStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 4)).setObjects(("SONET-MIB", "sonetFarEndLineCurrentUASs"), ("SONET-MIB", "sonetFarEndLineIntervalESs"), ("SONET-MIB", "sonetFarEndLineCurrentSESs"), ("SONET-MIB", "sonetFarEndLineIntervalCVs"), ("SONET-MIB", "sonetFarEndLineIntervalSESs"), ("SONET-MIB", "sonetFarEndLineCurrentCVs"), ("SONET-MIB", "sonetFarEndLineCurrentESs"), ("SONET-MIB", "sonetFarEndLineIntervalUASs"), )
sonetVTStuff2 = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 13)).setObjects(("SONET-MIB", "sonetVTCurrentCVs"), ("SONET-MIB", "sonetVTIntervalValidData"), ("SONET-MIB", "sonetVTCurrentStatus"), ("SONET-MIB", "sonetVTCurrentSESs"), ("SONET-MIB", "sonetVTCurrentWidth"), ("SONET-MIB", "sonetVTIntervalUASs"), ("SONET-MIB", "sonetVTCurrentUASs"), ("SONET-MIB", "sonetVTIntervalSESs"), ("SONET-MIB", "sonetVTIntervalESs"), ("SONET-MIB", "sonetVTIntervalCVs"), ("SONET-MIB", "sonetVTCurrentESs"), )
sonetFarEndVTStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 8)).setObjects(("SONET-MIB", "sonetFarEndVTIntervalSESs"), ("SONET-MIB", "sonetFarEndVTCurrentUASs"), ("SONET-MIB", "sonetFarEndVTIntervalESs"), ("SONET-MIB", "sonetFarEndVTCurrentSESs"), ("SONET-MIB", "sonetFarEndVTIntervalCVs"), ("SONET-MIB", "sonetFarEndVTIntervalUASs"), ("SONET-MIB", "sonetFarEndVTCurrentESs"), ("SONET-MIB", "sonetFarEndVTCurrentCVs"), )
sonetLineStuff2 = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 11)).setObjects(("SONET-MIB", "sonetLineCurrentCVs"), ("SONET-MIB", "sonetLineCurrentStatus"), ("SONET-MIB", "sonetLineIntervalESs"), ("SONET-MIB", "sonetLineCurrentSESs"), ("SONET-MIB", "sonetLineIntervalCVs"), ("SONET-MIB", "sonetLineIntervalSESs"), ("SONET-MIB", "sonetLineCurrentUASs"), ("SONET-MIB", "sonetLineIntervalUASs"), ("SONET-MIB", "sonetLineCurrentESs"), ("SONET-MIB", "sonetLineIntervalValidData"), )
sonetSectionStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 2)).setObjects(("SONET-MIB", "sonetSectionCurrentESs"), ("SONET-MIB", "sonetSectionIntervalSESs"), ("SONET-MIB", "sonetSectionIntervalESs"), ("SONET-MIB", "sonetSectionIntervalSEFSs"), ("SONET-MIB", "sonetSectionCurrentStatus"), ("SONET-MIB", "sonetSectionCurrentSESs"), ("SONET-MIB", "sonetSectionIntervalCVs"), ("SONET-MIB", "sonetSectionCurrentSEFSs"), ("SONET-MIB", "sonetSectionCurrentCVs"), )
sonetFarEndLineStuff2 = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 14)).setObjects(("SONET-MIB", "sonetFarEndLineCurrentUASs"), ("SONET-MIB", "sonetFarEndLineIntervalESs"), ("SONET-MIB", "sonetFarEndLineCurrentSESs"), ("SONET-MIB", "sonetFarEndLineIntervalCVs"), ("SONET-MIB", "sonetFarEndLineIntervalSESs"), ("SONET-MIB", "sonetFarEndLineIntervalValidData"), ("SONET-MIB", "sonetFarEndLineCurrentCVs"), ("SONET-MIB", "sonetFarEndLineCurrentESs"), ("SONET-MIB", "sonetFarEndLineIntervalUASs"), )
sonetFarEndPathStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 6)).setObjects(("SONET-MIB", "sonetFarEndPathIntervalSESs"), ("SONET-MIB", "sonetFarEndPathIntervalESs"), ("SONET-MIB", "sonetFarEndPathCurrentUASs"), ("SONET-MIB", "sonetFarEndPathCurrentESs"), ("SONET-MIB", "sonetFarEndPathIntervalUASs"), ("SONET-MIB", "sonetFarEndPathCurrentCVs"), ("SONET-MIB", "sonetFarEndPathIntervalCVs"), ("SONET-MIB", "sonetFarEndPathCurrentSESs"), )
sonetMediumStuff = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 1)).setObjects(("SONET-MIB", "sonetMediumTimeElapsed"), ("SONET-MIB", "sonetMediumValidIntervals"), ("SONET-MIB", "sonetMediumCircuitIdentifier"), ("SONET-MIB", "sonetMediumLineCoding"), ("SONET-MIB", "sonetMediumType"), ("SONET-MIB", "sonetMediumLineType"), )
sonetMediumStuff2 = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 9)).setObjects(("SONET-MIB", "sonetMediumTimeElapsed"), ("SONET-MIB", "sonetMediumValidIntervals"), ("SONET-MIB", "sonetSESthresholdSet"), ("SONET-MIB", "sonetMediumLoopbackConfig"), ("SONET-MIB", "sonetMediumInvalidIntervals"), ("SONET-MIB", "sonetMediumCircuitIdentifier"), ("SONET-MIB", "sonetMediumLineCoding"), ("SONET-MIB", "sonetMediumType"), ("SONET-MIB", "sonetMediumLineType"), )
sonetPathStuff2 = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 39, 4, 1, 12)).setObjects(("SONET-MIB", "sonetPathIntervalSESs"), ("SONET-MIB", "sonetPathIntervalESs"), ("SONET-MIB", "sonetPathCurrentStatus"), ("SONET-MIB", "sonetPathCurrentCVs"), ("SONET-MIB", "sonetPathIntervalValidData"), ("SONET-MIB", "sonetPathIntervalUASs"), ("SONET-MIB", "sonetPathCurrentESs"), ("SONET-MIB", "sonetPathCurrentUASs"), ("SONET-MIB", "sonetPathCurrentWidth"), ("SONET-MIB", "sonetPathCurrentSESs"), ("SONET-MIB", "sonetPathIntervalCVs"), )

# Exports

# Module identity
mibBuilder.exportSymbols("SONET-MIB", PYSNMP_MODULE_ID=sonetMIB)

# Objects
mibBuilder.exportSymbols("SONET-MIB", sonetMIB=sonetMIB, sonetObjects=sonetObjects, sonetMedium=sonetMedium, sonetMediumTable=sonetMediumTable, sonetMediumEntry=sonetMediumEntry, sonetMediumType=sonetMediumType, sonetMediumTimeElapsed=sonetMediumTimeElapsed, sonetMediumValidIntervals=sonetMediumValidIntervals, sonetMediumLineCoding=sonetMediumLineCoding, sonetMediumLineType=sonetMediumLineType, sonetMediumCircuitIdentifier=sonetMediumCircuitIdentifier, sonetMediumInvalidIntervals=sonetMediumInvalidIntervals, sonetMediumLoopbackConfig=sonetMediumLoopbackConfig, sonetSESthresholdSet=sonetSESthresholdSet, sonetSection=sonetSection, sonetSectionCurrentTable=sonetSectionCurrentTable, sonetSectionCurrentEntry=sonetSectionCurrentEntry, sonetSectionCurrentStatus=sonetSectionCurrentStatus, sonetSectionCurrentESs=sonetSectionCurrentESs, sonetSectionCurrentSESs=sonetSectionCurrentSESs, sonetSectionCurrentSEFSs=sonetSectionCurrentSEFSs, sonetSectionCurrentCVs=sonetSectionCurrentCVs, sonetSectionIntervalTable=sonetSectionIntervalTable, sonetSectionIntervalEntry=sonetSectionIntervalEntry, sonetSectionIntervalNumber=sonetSectionIntervalNumber, sonetSectionIntervalESs=sonetSectionIntervalESs, sonetSectionIntervalSESs=sonetSectionIntervalSESs, sonetSectionIntervalSEFSs=sonetSectionIntervalSEFSs, sonetSectionIntervalCVs=sonetSectionIntervalCVs, sonetSectionIntervalValidData=sonetSectionIntervalValidData, sonetLine=sonetLine, sonetLineCurrentTable=sonetLineCurrentTable, sonetLineCurrentEntry=sonetLineCurrentEntry, sonetLineCurrentStatus=sonetLineCurrentStatus, sonetLineCurrentESs=sonetLineCurrentESs, sonetLineCurrentSESs=sonetLineCurrentSESs, sonetLineCurrentCVs=sonetLineCurrentCVs, sonetLineCurrentUASs=sonetLineCurrentUASs, sonetLineIntervalTable=sonetLineIntervalTable, sonetLineIntervalEntry=sonetLineIntervalEntry, sonetLineIntervalNumber=sonetLineIntervalNumber, sonetLineIntervalESs=sonetLineIntervalESs, sonetLineIntervalSESs=sonetLineIntervalSESs, sonetLineIntervalCVs=sonetLineIntervalCVs, sonetLineIntervalUASs=sonetLineIntervalUASs, sonetLineIntervalValidData=sonetLineIntervalValidData, sonetFarEndLine=sonetFarEndLine, sonetFarEndLineCurrentTable=sonetFarEndLineCurrentTable, sonetFarEndLineCurrentEntry=sonetFarEndLineCurrentEntry, sonetFarEndLineCurrentESs=sonetFarEndLineCurrentESs, sonetFarEndLineCurrentSESs=sonetFarEndLineCurrentSESs, sonetFarEndLineCurrentCVs=sonetFarEndLineCurrentCVs, sonetFarEndLineCurrentUASs=sonetFarEndLineCurrentUASs, sonetFarEndLineIntervalTable=sonetFarEndLineIntervalTable, sonetFarEndLineIntervalEntry=sonetFarEndLineIntervalEntry, sonetFarEndLineIntervalNumber=sonetFarEndLineIntervalNumber, sonetFarEndLineIntervalESs=sonetFarEndLineIntervalESs, sonetFarEndLineIntervalSESs=sonetFarEndLineIntervalSESs, sonetFarEndLineIntervalCVs=sonetFarEndLineIntervalCVs, sonetFarEndLineIntervalUASs=sonetFarEndLineIntervalUASs, sonetFarEndLineIntervalValidData=sonetFarEndLineIntervalValidData, sonetObjectsPath=sonetObjectsPath, sonetPath=sonetPath, sonetPathCurrentTable=sonetPathCurrentTable, sonetPathCurrentEntry=sonetPathCurrentEntry, sonetPathCurrentWidth=sonetPathCurrentWidth, sonetPathCurrentStatus=sonetPathCurrentStatus, sonetPathCurrentESs=sonetPathCurrentESs, sonetPathCurrentSESs=sonetPathCurrentSESs, sonetPathCurrentCVs=sonetPathCurrentCVs, sonetPathCurrentUASs=sonetPathCurrentUASs, sonetPathIntervalTable=sonetPathIntervalTable, sonetPathIntervalEntry=sonetPathIntervalEntry, sonetPathIntervalNumber=sonetPathIntervalNumber, sonetPathIntervalESs=sonetPathIntervalESs, sonetPathIntervalSESs=sonetPathIntervalSESs, sonetPathIntervalCVs=sonetPathIntervalCVs, sonetPathIntervalUASs=sonetPathIntervalUASs, sonetPathIntervalValidData=sonetPathIntervalValidData, sonetFarEndPath=sonetFarEndPath, sonetFarEndPathCurrentTable=sonetFarEndPathCurrentTable, sonetFarEndPathCurrentEntry=sonetFarEndPathCurrentEntry, sonetFarEndPathCurrentESs=sonetFarEndPathCurrentESs, sonetFarEndPathCurrentSESs=sonetFarEndPathCurrentSESs, sonetFarEndPathCurrentCVs=sonetFarEndPathCurrentCVs, sonetFarEndPathCurrentUASs=sonetFarEndPathCurrentUASs, sonetFarEndPathIntervalTable=sonetFarEndPathIntervalTable, sonetFarEndPathIntervalEntry=sonetFarEndPathIntervalEntry, sonetFarEndPathIntervalNumber=sonetFarEndPathIntervalNumber, sonetFarEndPathIntervalESs=sonetFarEndPathIntervalESs, sonetFarEndPathIntervalSESs=sonetFarEndPathIntervalSESs, sonetFarEndPathIntervalCVs=sonetFarEndPathIntervalCVs, sonetFarEndPathIntervalUASs=sonetFarEndPathIntervalUASs, sonetFarEndPathIntervalValidData=sonetFarEndPathIntervalValidData, sonetObjectsVT=sonetObjectsVT, sonetVT=sonetVT, sonetVTCurrentTable=sonetVTCurrentTable, sonetVTCurrentEntry=sonetVTCurrentEntry, sonetVTCurrentWidth=sonetVTCurrentWidth, sonetVTCurrentStatus=sonetVTCurrentStatus, sonetVTCurrentESs=sonetVTCurrentESs, sonetVTCurrentSESs=sonetVTCurrentSESs, sonetVTCurrentCVs=sonetVTCurrentCVs, sonetVTCurrentUASs=sonetVTCurrentUASs, sonetVTIntervalTable=sonetVTIntervalTable, sonetVTIntervalEntry=sonetVTIntervalEntry, sonetVTIntervalNumber=sonetVTIntervalNumber, sonetVTIntervalESs=sonetVTIntervalESs, sonetVTIntervalSESs=sonetVTIntervalSESs, sonetVTIntervalCVs=sonetVTIntervalCVs, sonetVTIntervalUASs=sonetVTIntervalUASs, sonetVTIntervalValidData=sonetVTIntervalValidData, sonetFarEndVT=sonetFarEndVT, sonetFarEndVTCurrentTable=sonetFarEndVTCurrentTable, sonetFarEndVTCurrentEntry=sonetFarEndVTCurrentEntry, sonetFarEndVTCurrentESs=sonetFarEndVTCurrentESs, sonetFarEndVTCurrentSESs=sonetFarEndVTCurrentSESs, sonetFarEndVTCurrentCVs=sonetFarEndVTCurrentCVs, sonetFarEndVTCurrentUASs=sonetFarEndVTCurrentUASs, sonetFarEndVTIntervalTable=sonetFarEndVTIntervalTable, sonetFarEndVTIntervalEntry=sonetFarEndVTIntervalEntry, sonetFarEndVTIntervalNumber=sonetFarEndVTIntervalNumber, sonetFarEndVTIntervalESs=sonetFarEndVTIntervalESs, sonetFarEndVTIntervalSESs=sonetFarEndVTIntervalSESs, sonetFarEndVTIntervalCVs=sonetFarEndVTIntervalCVs, sonetFarEndVTIntervalUASs=sonetFarEndVTIntervalUASs)
mibBuilder.exportSymbols("SONET-MIB", sonetFarEndVTIntervalValidData=sonetFarEndVTIntervalValidData, sonetConformance=sonetConformance, sonetGroups=sonetGroups, sonetCompliances=sonetCompliances)

# Groups
mibBuilder.exportSymbols("SONET-MIB", sonetFarEndPathStuff2=sonetFarEndPathStuff2, sonetSectionStuff2=sonetSectionStuff2, sonetPathStuff=sonetPathStuff, sonetFarEndVTStuff2=sonetFarEndVTStuff2, sonetVTStuff=sonetVTStuff, sonetLineStuff=sonetLineStuff, sonetFarEndLineStuff=sonetFarEndLineStuff, sonetVTStuff2=sonetVTStuff2, sonetFarEndVTStuff=sonetFarEndVTStuff, sonetLineStuff2=sonetLineStuff2, sonetSectionStuff=sonetSectionStuff, sonetFarEndLineStuff2=sonetFarEndLineStuff2, sonetFarEndPathStuff=sonetFarEndPathStuff, sonetMediumStuff=sonetMediumStuff, sonetMediumStuff2=sonetMediumStuff2, sonetPathStuff2=sonetPathStuff2)
