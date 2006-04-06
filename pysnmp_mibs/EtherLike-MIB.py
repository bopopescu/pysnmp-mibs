# PySNMP SMI module. Autogenerated from smidump -f python EtherLike-MIB
# by libsmi2pysnmp-0.0.6-alpha at Thu Apr  6 13:19:16 2006,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2", "transmission")
( TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue")

# Objects

dot3 = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7))
dot3StatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 2))
dot3StatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 2, 1)).setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
dot3StatsIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
dot3StatsAlignmentErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 2), Counter32()).setMaxAccess("readonly")
dot3StatsFCSErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 3), Counter32()).setMaxAccess("readonly")
dot3StatsSingleCollisionFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 4), Counter32()).setMaxAccess("readonly")
dot3StatsMultipleCollisionFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 5), Counter32()).setMaxAccess("readonly")
dot3StatsSQETestErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 6), Counter32()).setMaxAccess("readonly")
dot3StatsDeferredTransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 7), Counter32()).setMaxAccess("readonly")
dot3StatsLateCollisions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 8), Counter32()).setMaxAccess("readonly")
dot3StatsExcessiveCollisions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 9), Counter32()).setMaxAccess("readonly")
dot3StatsInternalMacTransmitErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 10), Counter32()).setMaxAccess("readonly")
dot3StatsCarrierSenseErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 11), Counter32()).setMaxAccess("readonly")
dot3StatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 13), Counter32()).setMaxAccess("readonly")
dot3StatsInternalMacReceiveErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 16), Counter32()).setMaxAccess("readonly")
dot3StatsEtherChipSet = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 17), ObjectIdentifier()).setMaxAccess("readonly")
dot3StatsSymbolErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 18), Counter32()).setMaxAccess("readonly")
dot3StatsDuplexStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 19), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("unknown", 1), ("halfDuplex", 2), ("fullDuplex", 3), ))).setMaxAccess("readonly")
dot3StatsRateControlAbility = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 20), TruthValue()).setMaxAccess("readonly")
dot3StatsRateControlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 2, 1, 21), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,2,)).subtype(namedValues=namedval.NamedValues(("rateControlOff", 1), ("rateControlOn", 2), ("unknown", 3), ))).setMaxAccess("readonly")
dot3CollTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 5))
dot3CollEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 5, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "EtherLike-MIB", "dot3CollCount"))
dot3CollCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 16))).setMaxAccess("noaccess")
dot3CollFrequencies = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 5, 1, 3), Counter32()).setMaxAccess("readonly")
dot3Tests = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 6))
dot3TestTdr = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 6, 1))
dot3TestLoopBack = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 6, 2))
dot3Errors = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 7))
dot3ErrorInitError = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 7, 1))
dot3ErrorLoopbackError = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 7, 7, 2))
dot3ControlTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 9))
dot3ControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 9, 1)).setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
dot3ControlFunctionsSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 1), Bits().subtype(namedValues=namedval.NamedValues(("pause", 0), ))).setMaxAccess("readonly")
dot3ControlInUnknownOpcodes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 2), Counter32()).setMaxAccess("readonly")
dot3HCControlInUnknownOpcodes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 9, 1, 3), Counter64()).setMaxAccess("readonly")
dot3PauseTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 10))
dot3PauseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 10, 1)).setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
dot3PauseAdminMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,4,3,2,)).subtype(namedValues=namedval.NamedValues(("disabled", 1), ("enabledXmit", 2), ("enabledRcv", 3), ("enabledXmitAndRcv", 4), ))).setMaxAccess("readwrite")
dot3PauseOperMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,4,3,2,)).subtype(namedValues=namedval.NamedValues(("disabled", 1), ("enabledXmit", 2), ("enabledRcv", 3), ("enabledXmitAndRcv", 4), ))).setMaxAccess("readonly")
dot3InPauseFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 3), Counter32()).setMaxAccess("readonly")
dot3OutPauseFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 4), Counter32()).setMaxAccess("readonly")
dot3HCInPauseFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 5), Counter64()).setMaxAccess("readonly")
dot3HCOutPauseFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 10, 1, 6), Counter64()).setMaxAccess("readonly")
dot3HCStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 7, 11))
dot3HCStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 7, 11, 1)).setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
dot3HCStatsAlignmentErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 1), Counter64()).setMaxAccess("readonly")
dot3HCStatsFCSErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 2), Counter64()).setMaxAccess("readonly")
dot3HCStatsInternalMacTransmitErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 3), Counter64()).setMaxAccess("readonly")
dot3HCStatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 4), Counter64()).setMaxAccess("readonly")
dot3HCStatsInternalMacReceiveErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 5), Counter64()).setMaxAccess("readonly")
dot3HCStatsSymbolErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 7, 11, 1, 6), Counter64()).setMaxAccess("readonly")
etherMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 35)).setRevisions(("2003-09-19 00:00","1999-08-24 04:00","1998-06-03 21:50","1994-02-03 04:00",))
etherMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 35, 1))
etherConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 35, 2))
etherGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 35, 2, 1))
etherCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 35, 2, 2))

# Augmentions

# Groups

etherStatsBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 4)).setObjects(("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"), ("EtherLike-MIB", "dot3StatsExcessiveCollisions"), ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"), ("EtherLike-MIB", "dot3StatsDeferredTransmissions"), ("EtherLike-MIB", "dot3StatsFCSErrors"), ("EtherLike-MIB", "dot3StatsFrameTooLongs"), ("EtherLike-MIB", "dot3StatsSingleCollisionFrames"), ("EtherLike-MIB", "dot3StatsIndex"), ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"), ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"), ("EtherLike-MIB", "dot3StatsLateCollisions"), ("EtherLike-MIB", "dot3StatsAlignmentErrors"), )
etherHCControlPauseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 14)).setObjects(("EtherLike-MIB", "dot3HCOutPauseFrames"), ("EtherLike-MIB", "dot3HCInPauseFrames"), )
etherCollisionTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 2)).setObjects(("EtherLike-MIB", "dot3CollFrequencies"), )
etherDuplexGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 7)).setObjects(("EtherLike-MIB", "dot3StatsDuplexStatus"), )
etherHCStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 12)).setObjects(("EtherLike-MIB", "dot3HCStatsInternalMacTransmitErrors"), ("EtherLike-MIB", "dot3HCStatsSymbolErrors"), ("EtherLike-MIB", "dot3HCStatsAlignmentErrors"), ("EtherLike-MIB", "dot3HCStatsFrameTooLongs"), ("EtherLike-MIB", "dot3HCStatsFCSErrors"), ("EtherLike-MIB", "dot3HCStatsInternalMacReceiveErrors"), )
etherRateControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 15)).setObjects(("EtherLike-MIB", "dot3StatsRateControlStatus"), ("EtherLike-MIB", "dot3StatsRateControlAbility"), )
etherControlPauseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 9)).setObjects(("EtherLike-MIB", "dot3PauseOperMode"), ("EtherLike-MIB", "dot3OutPauseFrames"), ("EtherLike-MIB", "dot3PauseAdminMode"), ("EtherLike-MIB", "dot3InPauseFrames"), )
etherStatsLowSpeedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 5)).setObjects(("EtherLike-MIB", "dot3StatsSQETestErrors"), )
etherHCControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 13)).setObjects(("EtherLike-MIB", "dot3HCControlInUnknownOpcodes"), )
etherStats100MbsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 3)).setObjects(("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"), ("EtherLike-MIB", "dot3StatsExcessiveCollisions"), ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"), ("EtherLike-MIB", "dot3StatsDeferredTransmissions"), ("EtherLike-MIB", "dot3StatsSymbolErrors"), ("EtherLike-MIB", "dot3StatsEtherChipSet"), ("EtherLike-MIB", "dot3StatsFCSErrors"), ("EtherLike-MIB", "dot3StatsFrameTooLongs"), ("EtherLike-MIB", "dot3StatsSingleCollisionFrames"), ("EtherLike-MIB", "dot3StatsIndex"), ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"), ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"), ("EtherLike-MIB", "dot3StatsLateCollisions"), ("EtherLike-MIB", "dot3StatsAlignmentErrors"), )
etherStatsHalfDuplexGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 11)).setObjects(("EtherLike-MIB", "dot3StatsExcessiveCollisions"), ("EtherLike-MIB", "dot3StatsSingleCollisionFrames"), ("EtherLike-MIB", "dot3StatsDeferredTransmissions"), ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"), ("EtherLike-MIB", "dot3StatsLateCollisions"), ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"), )
etherStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 1)).setObjects(("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"), ("EtherLike-MIB", "dot3StatsExcessiveCollisions"), ("EtherLike-MIB", "dot3StatsCarrierSenseErrors"), ("EtherLike-MIB", "dot3StatsDeferredTransmissions"), ("EtherLike-MIB", "dot3StatsEtherChipSet"), ("EtherLike-MIB", "dot3StatsFCSErrors"), ("EtherLike-MIB", "dot3StatsSQETestErrors"), ("EtherLike-MIB", "dot3StatsSingleCollisionFrames"), ("EtherLike-MIB", "dot3StatsIndex"), ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"), ("EtherLike-MIB", "dot3StatsMultipleCollisionFrames"), ("EtherLike-MIB", "dot3StatsLateCollisions"), ("EtherLike-MIB", "dot3StatsAlignmentErrors"), ("EtherLike-MIB", "dot3StatsFrameTooLongs"), )
etherStatsBaseGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 10)).setObjects(("EtherLike-MIB", "dot3StatsInternalMacTransmitErrors"), ("EtherLike-MIB", "dot3StatsFCSErrors"), ("EtherLike-MIB", "dot3StatsFrameTooLongs"), ("EtherLike-MIB", "dot3StatsIndex"), ("EtherLike-MIB", "dot3StatsInternalMacReceiveErrors"), ("EtherLike-MIB", "dot3StatsAlignmentErrors"), )
etherControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 8)).setObjects(("EtherLike-MIB", "dot3ControlFunctionsSupported"), ("EtherLike-MIB", "dot3ControlInUnknownOpcodes"), )
etherStatsHighSpeedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 35, 2, 1, 6)).setObjects(("EtherLike-MIB", "dot3StatsSymbolErrors"), )

# Exports

# Module identity
mibBuilder.exportSymbols("EtherLike-MIB", PYSNMP_MODULE_ID=etherMIB)

# Objects
mibBuilder.exportSymbols("EtherLike-MIB", dot3=dot3, dot3StatsTable=dot3StatsTable, dot3StatsEntry=dot3StatsEntry, dot3StatsIndex=dot3StatsIndex, dot3StatsAlignmentErrors=dot3StatsAlignmentErrors, dot3StatsFCSErrors=dot3StatsFCSErrors, dot3StatsSingleCollisionFrames=dot3StatsSingleCollisionFrames, dot3StatsMultipleCollisionFrames=dot3StatsMultipleCollisionFrames, dot3StatsSQETestErrors=dot3StatsSQETestErrors, dot3StatsDeferredTransmissions=dot3StatsDeferredTransmissions, dot3StatsLateCollisions=dot3StatsLateCollisions, dot3StatsExcessiveCollisions=dot3StatsExcessiveCollisions, dot3StatsInternalMacTransmitErrors=dot3StatsInternalMacTransmitErrors, dot3StatsCarrierSenseErrors=dot3StatsCarrierSenseErrors, dot3StatsFrameTooLongs=dot3StatsFrameTooLongs, dot3StatsInternalMacReceiveErrors=dot3StatsInternalMacReceiveErrors, dot3StatsEtherChipSet=dot3StatsEtherChipSet, dot3StatsSymbolErrors=dot3StatsSymbolErrors, dot3StatsDuplexStatus=dot3StatsDuplexStatus, dot3StatsRateControlAbility=dot3StatsRateControlAbility, dot3StatsRateControlStatus=dot3StatsRateControlStatus, dot3CollTable=dot3CollTable, dot3CollEntry=dot3CollEntry, dot3CollCount=dot3CollCount, dot3CollFrequencies=dot3CollFrequencies, dot3Tests=dot3Tests, dot3TestTdr=dot3TestTdr, dot3TestLoopBack=dot3TestLoopBack, dot3Errors=dot3Errors, dot3ErrorInitError=dot3ErrorInitError, dot3ErrorLoopbackError=dot3ErrorLoopbackError, dot3ControlTable=dot3ControlTable, dot3ControlEntry=dot3ControlEntry, dot3ControlFunctionsSupported=dot3ControlFunctionsSupported, dot3ControlInUnknownOpcodes=dot3ControlInUnknownOpcodes, dot3HCControlInUnknownOpcodes=dot3HCControlInUnknownOpcodes, dot3PauseTable=dot3PauseTable, dot3PauseEntry=dot3PauseEntry, dot3PauseAdminMode=dot3PauseAdminMode, dot3PauseOperMode=dot3PauseOperMode, dot3InPauseFrames=dot3InPauseFrames, dot3OutPauseFrames=dot3OutPauseFrames, dot3HCInPauseFrames=dot3HCInPauseFrames, dot3HCOutPauseFrames=dot3HCOutPauseFrames, dot3HCStatsTable=dot3HCStatsTable, dot3HCStatsEntry=dot3HCStatsEntry, dot3HCStatsAlignmentErrors=dot3HCStatsAlignmentErrors, dot3HCStatsFCSErrors=dot3HCStatsFCSErrors, dot3HCStatsInternalMacTransmitErrors=dot3HCStatsInternalMacTransmitErrors, dot3HCStatsFrameTooLongs=dot3HCStatsFrameTooLongs, dot3HCStatsInternalMacReceiveErrors=dot3HCStatsInternalMacReceiveErrors, dot3HCStatsSymbolErrors=dot3HCStatsSymbolErrors, etherMIB=etherMIB, etherMIBObjects=etherMIBObjects, etherConformance=etherConformance, etherGroups=etherGroups, etherCompliances=etherCompliances)

# Groups
mibBuilder.exportSymbols("EtherLike-MIB", etherStatsBaseGroup=etherStatsBaseGroup, etherHCControlPauseGroup=etherHCControlPauseGroup, etherCollisionTableGroup=etherCollisionTableGroup, etherDuplexGroup=etherDuplexGroup, etherHCStatsGroup=etherHCStatsGroup, etherRateControlGroup=etherRateControlGroup, etherControlPauseGroup=etherControlPauseGroup, etherStatsLowSpeedGroup=etherStatsLowSpeedGroup, etherHCControlGroup=etherHCControlGroup, etherStats100MbsGroup=etherStats100MbsGroup, etherStatsHalfDuplexGroup=etherStatsHalfDuplexGroup, etherStatsGroup=etherStatsGroup, etherStatsBaseGroup2=etherStatsBaseGroup2, etherControlGroup=etherControlGroup, etherStatsHighSpeedGroup=etherStatsHighSpeedGroup)
