# PySNMP SMI module. Autogenerated from smidump -f python ROHC-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:34 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( DateAndTime, TextualConvention, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "TimeInterval", "TruthValue")

# Types

class RohcChannelIdentifier(TextualConvention, Unsigned32):
    subtypeConstraints = Unsigned32.subtypeConstraints + ( subtypes.ValueRangeConstraint(1, 4294967295L), )
    pass

class RohcChannelIdentifierOrZero(TextualConvention, Unsigned32):
    subtypeConstraints = Unsigned32.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 4294967295L), )
    pass

class RohcCompressionRatio(TextualConvention, Unsigned32):
    pass


# Objects

rohcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 112))
rohcObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 112, 1))
rohcInstanceObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 112, 1, 1))
rohcChannelTable = MibTable((1, 3, 6, 1, 2, 1, 112, 1, 1, 1))
rohcChannelEntry = MibTableRow((1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ROHC-MIB", "rohcChannelID"))
rohcChannelID = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), RohcChannelIdentifier()).setMaxAccess("noaccess"))
rohcChannelType = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(3,1,2,)).addNamedValues(("notInUse", 1), ("rohc", 2), ("dedicatedFeedback", 3), )).setMaxAccess("readonly"))
rohcChannelFeedbackFor = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1, 4)).setColumnInitializer(MibVariable((), RohcChannelIdentifierOrZero()).setMaxAccess("readonly"))
rohcChannelDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1, 5)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readonly"))
rohcChannelStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("enabled", 1), ("disabled", 2), )).setMaxAccess("readonly"))
rohcInstanceTable = MibTable((1, 3, 6, 1, 2, 1, 112, 1, 1, 2))
rohcInstanceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1)).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ROHC-MIB", "rohcInstanceType"), (0, "ROHC-MIB", "rohcChannelID"))
rohcInstanceType = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(1,2,)).addNamedValues(("compressor", 1), ("decompressor", 2), )).setMaxAccess("noaccess"))
rohcInstanceFBChannelID = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), RohcChannelIdentifierOrZero()).setMaxAccess("readonly"))
rohcInstanceVendor = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 5)).setColumnInitializer(MibVariable((), ObjectIdentifier()).setMaxAccess("readonly"))
rohcInstanceVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 6)).setColumnInitializer(MibVariable((), SnmpAdminString().addConstraints(subtypes.ValueRangeConstraint(0, 32))).setMaxAccess("readonly"))
rohcInstanceDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 7)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readonly"))
rohcInstanceClockRes = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 8)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
rohcInstanceMaxCID = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 9)).setColumnInitializer(MibVariable((), Unsigned32().addConstraints(subtypes.ValueRangeConstraint(1, 16383))).setMaxAccess("readonly"))
rohcInstanceLargeCIDs = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 10)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
rohcInstanceMRRU = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 11)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
rohcInstanceContextStorageTime = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 12)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readwrite"))
rohcInstanceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 13)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("enabled", 1), ("disabled", 2), )).setMaxAccess("readonly"))
rohcInstanceContextsTotal = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 14)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcInstanceContextsCurrent = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 15)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
rohcInstancePackets = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 16)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcInstanceIRs = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 17)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcInstanceIRDYNs = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 18)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcInstanceFeedbacks = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 19)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcInstanceCompressionRatio = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 2, 1, 20)).setColumnInitializer(MibVariable((), RohcCompressionRatio()).setMaxAccess("readonly"))
rohcProfileTable = MibTable((1, 3, 6, 1, 2, 1, 112, 1, 1, 3))
rohcProfileEntry = MibTableRow((1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1)).setIndexNames((0, "ROHC-MIB", "rohcChannelID"), (0, "ROHC-MIB", "rohcProfile"))
rohcProfile = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1, 2)).setColumnInitializer(MibVariable((), Unsigned32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess"))
rohcProfileVendor = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1, 3)).setColumnInitializer(MibVariable((), ObjectIdentifier()).setMaxAccess("readonly"))
rohcProfileVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1, 4)).setColumnInitializer(MibVariable((), SnmpAdminString().addConstraints(subtypes.ValueRangeConstraint(0, 32))).setMaxAccess("readonly"))
rohcProfileDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1, 5)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readonly"))
rohcProfileNegotiated = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 1, 3, 1, 6)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
rohcContextTable = MibTable((1, 3, 6, 1, 2, 1, 112, 1, 2))
rohcContextEntry = MibTableRow((1, 3, 6, 1, 2, 1, 112, 1, 2, 1)).setIndexNames((0, "ROHC-MIB", "rohcChannelID"), (0, "ROHC-MIB", "rohcContextCID"))
rohcContextCID = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), Unsigned32().addConstraints(subtypes.ValueRangeConstraint(0, 16383))).setMaxAccess("noaccess"))
rohcContextCIDState = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(1,2,3,4,)).addNamedValues(("unused", 1), ("active", 2), ("expired", 3), ("terminated", 4), )).setMaxAccess("readonly"))
rohcContextProfile = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), Unsigned32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
rohcContextDecompressorDepth = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 5)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
rohcContextStorageTime = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 6)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readwrite"))
rohcContextActivationTime = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 7)).setColumnInitializer(MibVariable((), DateAndTime()).setMaxAccess("readonly"))
rohcContextDeactivationTime = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 8)).setColumnInitializer(MibVariable((), DateAndTime()).setMaxAccess("readonly"))
rohcContextPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 9)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcContextIRs = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 10)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcContextIRDYNs = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcContextFeedbacks = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 12)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcContextDecompressorFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 13)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcContextDecompressorRepairs = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 14)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
rohcContextAllPacketsRatio = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 15)).setColumnInitializer(MibVariable((), RohcCompressionRatio()).setMaxAccess("readonly"))
rohcContextAllHeadersRatio = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 16)).setColumnInitializer(MibVariable((), RohcCompressionRatio()).setMaxAccess("readonly"))
rohcContextAllPacketsMeanSize = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 17)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
rohcContextAllHeadersMeanSize = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 18)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
rohcContextLastPacketsRatio = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 19)).setColumnInitializer(MibVariable((), RohcCompressionRatio()).setMaxAccess("readonly"))
rohcContextLastHeadersRatio = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 20)).setColumnInitializer(MibVariable((), RohcCompressionRatio()).setMaxAccess("readonly"))
rohcContextLastPacketsMeanSize = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 21)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
rohcContextLastHeadersMeanSize = MibTableColumn((1, 3, 6, 1, 2, 1, 112, 1, 2, 1, 22)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readonly"))
rohcConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 112, 2))
rohcCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 112, 2, 1))
rohcGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 112, 2, 2))

# Augmentions

# Groups

rohcContextGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 112, 2, 2, 5)).setObjects(("ROHC-MIB", "rohcContextDecompressorDepth"), ("ROHC-MIB", "rohcContextProfile"), ("ROHC-MIB", "rohcContextCIDState"), )
rohcInstanceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 112, 2, 2, 2)).setObjects(("ROHC-MIB", "rohcChannelType"), ("ROHC-MIB", "rohcInstanceDescr"), ("ROHC-MIB", "rohcProfileDescr"), ("ROHC-MIB", "rohcInstanceStatus"), ("ROHC-MIB", "rohcInstanceFBChannelID"), ("ROHC-MIB", "rohcInstanceLargeCIDs"), ("ROHC-MIB", "rohcInstanceMRRU"), ("ROHC-MIB", "rohcProfileNegotiated"), ("ROHC-MIB", "rohcInstanceVersion"), ("ROHC-MIB", "rohcChannelDescr"), ("ROHC-MIB", "rohcInstanceVendor"), ("ROHC-MIB", "rohcChannelStatus"), ("ROHC-MIB", "rohcChannelFeedbackFor"), ("ROHC-MIB", "rohcProfileVendor"), ("ROHC-MIB", "rohcInstanceClockRes"), ("ROHC-MIB", "rohcProfileVersion"), ("ROHC-MIB", "rohcInstanceMaxCID"), )
rohcStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 112, 2, 2, 4)).setObjects(("ROHC-MIB", "rohcInstanceFeedbacks"), ("ROHC-MIB", "rohcInstancePackets"), ("ROHC-MIB", "rohcInstanceIRDYNs"), ("ROHC-MIB", "rohcInstanceContextsCurrent"), ("ROHC-MIB", "rohcInstanceContextsTotal"), ("ROHC-MIB", "rohcInstanceCompressionRatio"), ("ROHC-MIB", "rohcInstanceIRs"), )
rohcTimerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 112, 2, 2, 6)).setObjects(("ROHC-MIB", "rohcContextActivationTime"), ("ROHC-MIB", "rohcContextDeactivationTime"), ("ROHC-MIB", "rohcInstanceContextStorageTime"), ("ROHC-MIB", "rohcContextStorageTime"), )
rohcContextStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 112, 2, 2, 7)).setObjects(("ROHC-MIB", "rohcContextIRs"), ("ROHC-MIB", "rohcContextAllHeadersRatio"), ("ROHC-MIB", "rohcContextIRDYNs"), ("ROHC-MIB", "rohcContextAllPacketsMeanSize"), ("ROHC-MIB", "rohcContextAllHeadersMeanSize"), ("ROHC-MIB", "rohcContextFeedbacks"), ("ROHC-MIB", "rohcContextAllPacketsRatio"), ("ROHC-MIB", "rohcContextLastHeadersRatio"), ("ROHC-MIB", "rohcContextPackets"), ("ROHC-MIB", "rohcContextLastPacketsMeanSize"), ("ROHC-MIB", "rohcContextDecompressorRepairs"), ("ROHC-MIB", "rohcContextLastPacketsRatio"), ("ROHC-MIB", "rohcContextLastHeadersMeanSize"), ("ROHC-MIB", "rohcContextDecompressorFailures"), )

# Exports

# Types
mibBuilder.exportSymbols("ROHC-MIB", RohcChannelIdentifier=RohcChannelIdentifier, RohcChannelIdentifierOrZero=RohcChannelIdentifierOrZero, RohcCompressionRatio=RohcCompressionRatio)

# Objects
mibBuilder.exportSymbols("ROHC-MIB", rohcMIB=rohcMIB, rohcObjects=rohcObjects, rohcInstanceObjects=rohcInstanceObjects, rohcChannelTable=rohcChannelTable, rohcChannelEntry=rohcChannelEntry, rohcChannelID=rohcChannelID, rohcChannelType=rohcChannelType, rohcChannelFeedbackFor=rohcChannelFeedbackFor, rohcChannelDescr=rohcChannelDescr, rohcChannelStatus=rohcChannelStatus, rohcInstanceTable=rohcInstanceTable, rohcInstanceEntry=rohcInstanceEntry, rohcInstanceType=rohcInstanceType, rohcInstanceFBChannelID=rohcInstanceFBChannelID, rohcInstanceVendor=rohcInstanceVendor, rohcInstanceVersion=rohcInstanceVersion, rohcInstanceDescr=rohcInstanceDescr, rohcInstanceClockRes=rohcInstanceClockRes, rohcInstanceMaxCID=rohcInstanceMaxCID, rohcInstanceLargeCIDs=rohcInstanceLargeCIDs, rohcInstanceMRRU=rohcInstanceMRRU, rohcInstanceContextStorageTime=rohcInstanceContextStorageTime, rohcInstanceStatus=rohcInstanceStatus, rohcInstanceContextsTotal=rohcInstanceContextsTotal, rohcInstanceContextsCurrent=rohcInstanceContextsCurrent, rohcInstancePackets=rohcInstancePackets, rohcInstanceIRs=rohcInstanceIRs, rohcInstanceIRDYNs=rohcInstanceIRDYNs, rohcInstanceFeedbacks=rohcInstanceFeedbacks, rohcInstanceCompressionRatio=rohcInstanceCompressionRatio, rohcProfileTable=rohcProfileTable, rohcProfileEntry=rohcProfileEntry, rohcProfile=rohcProfile, rohcProfileVendor=rohcProfileVendor, rohcProfileVersion=rohcProfileVersion, rohcProfileDescr=rohcProfileDescr, rohcProfileNegotiated=rohcProfileNegotiated, rohcContextTable=rohcContextTable, rohcContextEntry=rohcContextEntry, rohcContextCID=rohcContextCID, rohcContextCIDState=rohcContextCIDState, rohcContextProfile=rohcContextProfile, rohcContextDecompressorDepth=rohcContextDecompressorDepth, rohcContextStorageTime=rohcContextStorageTime, rohcContextActivationTime=rohcContextActivationTime, rohcContextDeactivationTime=rohcContextDeactivationTime, rohcContextPackets=rohcContextPackets, rohcContextIRs=rohcContextIRs, rohcContextIRDYNs=rohcContextIRDYNs, rohcContextFeedbacks=rohcContextFeedbacks, rohcContextDecompressorFailures=rohcContextDecompressorFailures, rohcContextDecompressorRepairs=rohcContextDecompressorRepairs, rohcContextAllPacketsRatio=rohcContextAllPacketsRatio, rohcContextAllHeadersRatio=rohcContextAllHeadersRatio, rohcContextAllPacketsMeanSize=rohcContextAllPacketsMeanSize, rohcContextAllHeadersMeanSize=rohcContextAllHeadersMeanSize, rohcContextLastPacketsRatio=rohcContextLastPacketsRatio, rohcContextLastHeadersRatio=rohcContextLastHeadersRatio, rohcContextLastPacketsMeanSize=rohcContextLastPacketsMeanSize, rohcContextLastHeadersMeanSize=rohcContextLastHeadersMeanSize, rohcConformance=rohcConformance, rohcCompliances=rohcCompliances, rohcGroups=rohcGroups)

# Groups
mibBuilder.exportSymbols("ROHC-MIB", rohcContextGroup=rohcContextGroup, rohcInstanceGroup=rohcInstanceGroup, rohcStatisticsGroup=rohcStatisticsGroup, rohcTimerGroup=rohcTimerGroup, rohcContextStatisticsGroup=rohcContextStatisticsGroup)
