# PySNMP SMI module. Autogenerated from smidump -f python P-BRIDGE-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 19:13:33 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( dot1dBasePort, dot1dBasePortEntry, dot1dBridge, dot1dTp, dot1dTpPort, ) = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort", "dot1dBasePortEntry", "dot1dBridge", "dot1dTp", "dot1dTpPort")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( MacAddress, TextualConvention, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "TimeInterval", "TruthValue")

# Types

class EnabledStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,1,)
    namedValues = namedval.NamedValues(("enabled", 1), ("disabled", 2), )
    pass


# Objects

dot1dTpHCPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 4, 5))
dot1dTpHCPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 4, 5, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dTpPort"))
dot1dTpHCPortInFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 1), Counter64()).setMaxAccess("readonly")
dot1dTpHCPortOutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 2), Counter64()).setMaxAccess("readonly")
dot1dTpHCPortInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 3), Counter64()).setMaxAccess("readonly")
dot1dTpPortOverflowTable = MibTable((1, 3, 6, 1, 2, 1, 17, 4, 6))
dot1dTpPortOverflowEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 4, 6, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dTpPort"))
dot1dTpPortInOverflowFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 1), Counter32()).setMaxAccess("readonly")
dot1dTpPortOutOverflowFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 2), Counter32()).setMaxAccess("readonly")
dot1dTpPortInOverflowDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 3), Counter32()).setMaxAccess("readonly")
pBridgeMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 17, 6)).setRevisions(("2006-01-09 00:00","1999-08-25 00:00",))
pBridgeMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 1))
dot1dExtBase = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 1, 1))
dot1dDeviceCapabilities = MibScalar((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 1), Bits().subtype(namedValues=namedval.NamedValues(("dot1dExtendedFilteringServices", 0), ("dot1dTrafficClasses", 1), ("dot1qStaticEntryIndividualPort", 2), ("dot1qIVLCapable", 3), ("dot1qSVLCapable", 4), ("dot1qHybridCapable", 5), ("dot1qConfigurablePvidTagging", 6), ("dot1dLocalVlanCapable", 7), ))).setMaxAccess("readonly")
dot1dTrafficClassesEnabled = MibScalar((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
dot1dGmrpStatus = MibScalar((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 3), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
dot1dPortCapabilitiesTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4))
dot1dPortCapabilitiesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4, 1))
dot1dPortCapabilities = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4, 1, 1), Bits().subtype(namedValues=namedval.NamedValues(("dot1qDot1qTagging", 0), ("dot1qConfigurableAcceptableFrameTypes", 1), ("dot1qIngressFiltering", 2), ))).setMaxAccess("readonly")
dot1dPriority = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 1, 2))
dot1dPortPriorityTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1))
dot1dPortPriorityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1))
dot1dPortDefaultUserPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
dot1dPortNumTrafficClasses = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
dot1dUserPriorityRegenTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2))
dot1dUserPriorityRegenEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "P-BRIDGE-MIB", "dot1dUserPriority"))
dot1dUserPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("noaccess")
dot1dRegenUserPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
dot1dTrafficClassTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3))
dot1dTrafficClassEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "P-BRIDGE-MIB", "dot1dTrafficClassPriority"))
dot1dTrafficClassPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("noaccess")
dot1dTrafficClass = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
dot1dPortOutboundAccessPriorityTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4))
dot1dPortOutboundAccessPriorityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4, 1)).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "P-BRIDGE-MIB", "dot1dRegenUserPriority"))
dot1dPortOutboundAccessPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
dot1dGarp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 1, 3))
dot1dPortGarpTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1))
dot1dPortGarpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1))
dot1dPortGarpJoinTime = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 1), TimeInterval().clone(20)).setMaxAccess("readwrite")
dot1dPortGarpLeaveTime = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 2), TimeInterval().clone(60)).setMaxAccess("readwrite")
dot1dPortGarpLeaveAllTime = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 3), TimeInterval().clone(1000)).setMaxAccess("readwrite")
dot1dGmrp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 1, 4))
dot1dPortGmrpTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1))
dot1dPortGmrpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1))
dot1dPortGmrpStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 1), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
dot1dPortGmrpFailedRegistrations = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 2), Counter32()).setMaxAccess("readonly")
dot1dPortGmrpLastPduOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
dot1dPortRestrictedGroupRegistration = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
pBridgeConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 2))
pBridgeGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 2, 1))
pBridgeCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 2, 2))

# Augmentions
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
dot1dBasePortEntry.registerAugmentions(("P-BRIDGE-MIB", "dot1dPortGarpEntry"))
apply(dot1dPortGarpEntry.setIndexNames, dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
dot1dBasePortEntry.registerAugmentions(("P-BRIDGE-MIB", "dot1dPortCapabilitiesEntry"))
apply(dot1dPortCapabilitiesEntry.setIndexNames, dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
dot1dBasePortEntry.registerAugmentions(("P-BRIDGE-MIB", "dot1dPortPriorityEntry"))
apply(dot1dPortPriorityEntry.setIndexNames, dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
dot1dBasePortEntry.registerAugmentions(("P-BRIDGE-MIB", "dot1dPortGmrpEntry"))
apply(dot1dPortGmrpEntry.setIndexNames, dot1dBasePortEntry.getIndexNames())

# Groups

pBridgeRegenPriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 5)).setObjects(("P-BRIDGE-MIB", "dot1dRegenUserPriority"), )
pBridgeAccessPriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 7)).setObjects(("P-BRIDGE-MIB", "dot1dPortOutboundAccessPriority"), )
pBridgeDeviceGmrpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 2)).setObjects(("P-BRIDGE-MIB", "dot1dGmrpStatus"), )
pBridgeHCPortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 10)).setObjects(("P-BRIDGE-MIB", "dot1dTpHCPortOutFrames"), ("P-BRIDGE-MIB", "dot1dTpHCPortInDiscards"), ("P-BRIDGE-MIB", "dot1dTpHCPortInFrames"), )
pBridgeDevicePriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 3)).setObjects(("P-BRIDGE-MIB", "dot1dTrafficClassesEnabled"), )
pBridgeDefaultPriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 4)).setObjects(("P-BRIDGE-MIB", "dot1dPortDefaultUserPriority"), )
pBridgePriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 6)).setObjects(("P-BRIDGE-MIB", "dot1dTrafficClass"), ("P-BRIDGE-MIB", "dot1dPortNumTrafficClasses"), )
pBridgePortOverflowGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 11)).setObjects(("P-BRIDGE-MIB", "dot1dTpPortInOverflowDiscards"), ("P-BRIDGE-MIB", "dot1dTpPortInOverflowFrames"), ("P-BRIDGE-MIB", "dot1dTpPortOutOverflowFrames"), )
pBridgePortGarpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 8)).setObjects(("P-BRIDGE-MIB", "dot1dPortGarpLeaveAllTime"), ("P-BRIDGE-MIB", "dot1dPortGarpLeaveTime"), ("P-BRIDGE-MIB", "dot1dPortGarpJoinTime"), )
pBridgePortGmrpGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 12)).setObjects(("P-BRIDGE-MIB", "dot1dPortGmrpFailedRegistrations"), ("P-BRIDGE-MIB", "dot1dPortGmrpLastPduOrigin"), ("P-BRIDGE-MIB", "dot1dPortGmrpStatus"), ("P-BRIDGE-MIB", "dot1dPortRestrictedGroupRegistration"), )
pBridgePortGmrpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 9)).setObjects(("P-BRIDGE-MIB", "dot1dPortGmrpFailedRegistrations"), ("P-BRIDGE-MIB", "dot1dPortGmrpLastPduOrigin"), ("P-BRIDGE-MIB", "dot1dPortGmrpStatus"), )
pBridgeExtCapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 1)).setObjects(("P-BRIDGE-MIB", "dot1dPortCapabilities"), ("P-BRIDGE-MIB", "dot1dDeviceCapabilities"), )

# Exports

# Module identity
mibBuilder.exportSymbols("P-BRIDGE-MIB", PYSNMP_MODULE_ID=pBridgeMIB)

# Types
mibBuilder.exportSymbols("P-BRIDGE-MIB", EnabledStatus=EnabledStatus)

# Objects
mibBuilder.exportSymbols("P-BRIDGE-MIB", dot1dTpHCPortTable=dot1dTpHCPortTable, dot1dTpHCPortEntry=dot1dTpHCPortEntry, dot1dTpHCPortInFrames=dot1dTpHCPortInFrames, dot1dTpHCPortOutFrames=dot1dTpHCPortOutFrames, dot1dTpHCPortInDiscards=dot1dTpHCPortInDiscards, dot1dTpPortOverflowTable=dot1dTpPortOverflowTable, dot1dTpPortOverflowEntry=dot1dTpPortOverflowEntry, dot1dTpPortInOverflowFrames=dot1dTpPortInOverflowFrames, dot1dTpPortOutOverflowFrames=dot1dTpPortOutOverflowFrames, dot1dTpPortInOverflowDiscards=dot1dTpPortInOverflowDiscards, pBridgeMIB=pBridgeMIB, pBridgeMIBObjects=pBridgeMIBObjects, dot1dExtBase=dot1dExtBase, dot1dDeviceCapabilities=dot1dDeviceCapabilities, dot1dTrafficClassesEnabled=dot1dTrafficClassesEnabled, dot1dGmrpStatus=dot1dGmrpStatus, dot1dPortCapabilitiesTable=dot1dPortCapabilitiesTable, dot1dPortCapabilitiesEntry=dot1dPortCapabilitiesEntry, dot1dPortCapabilities=dot1dPortCapabilities, dot1dPriority=dot1dPriority, dot1dPortPriorityTable=dot1dPortPriorityTable, dot1dPortPriorityEntry=dot1dPortPriorityEntry, dot1dPortDefaultUserPriority=dot1dPortDefaultUserPriority, dot1dPortNumTrafficClasses=dot1dPortNumTrafficClasses, dot1dUserPriorityRegenTable=dot1dUserPriorityRegenTable, dot1dUserPriorityRegenEntry=dot1dUserPriorityRegenEntry, dot1dUserPriority=dot1dUserPriority, dot1dRegenUserPriority=dot1dRegenUserPriority, dot1dTrafficClassTable=dot1dTrafficClassTable, dot1dTrafficClassEntry=dot1dTrafficClassEntry, dot1dTrafficClassPriority=dot1dTrafficClassPriority, dot1dTrafficClass=dot1dTrafficClass, dot1dPortOutboundAccessPriorityTable=dot1dPortOutboundAccessPriorityTable, dot1dPortOutboundAccessPriorityEntry=dot1dPortOutboundAccessPriorityEntry, dot1dPortOutboundAccessPriority=dot1dPortOutboundAccessPriority, dot1dGarp=dot1dGarp, dot1dPortGarpTable=dot1dPortGarpTable, dot1dPortGarpEntry=dot1dPortGarpEntry, dot1dPortGarpJoinTime=dot1dPortGarpJoinTime, dot1dPortGarpLeaveTime=dot1dPortGarpLeaveTime, dot1dPortGarpLeaveAllTime=dot1dPortGarpLeaveAllTime, dot1dGmrp=dot1dGmrp, dot1dPortGmrpTable=dot1dPortGmrpTable, dot1dPortGmrpEntry=dot1dPortGmrpEntry, dot1dPortGmrpStatus=dot1dPortGmrpStatus, dot1dPortGmrpFailedRegistrations=dot1dPortGmrpFailedRegistrations, dot1dPortGmrpLastPduOrigin=dot1dPortGmrpLastPduOrigin, dot1dPortRestrictedGroupRegistration=dot1dPortRestrictedGroupRegistration, pBridgeConformance=pBridgeConformance, pBridgeGroups=pBridgeGroups, pBridgeCompliances=pBridgeCompliances)

# Groups
mibBuilder.exportSymbols("P-BRIDGE-MIB", pBridgeRegenPriorityGroup=pBridgeRegenPriorityGroup, pBridgeAccessPriorityGroup=pBridgeAccessPriorityGroup, pBridgeDeviceGmrpGroup=pBridgeDeviceGmrpGroup, pBridgeHCPortGroup=pBridgeHCPortGroup, pBridgeDevicePriorityGroup=pBridgeDevicePriorityGroup, pBridgeDefaultPriorityGroup=pBridgeDefaultPriorityGroup, pBridgePriorityGroup=pBridgePriorityGroup, pBridgePortOverflowGroup=pBridgePortOverflowGroup, pBridgePortGarpGroup=pBridgePortGarpGroup, pBridgePortGmrpGroup2=pBridgePortGmrpGroup2, pBridgePortGmrpGroup=pBridgePortGmrpGroup, pBridgeExtCapGroup=pBridgeExtCapGroup)
