# PySNMP SMI module. Autogenerated from smidump -f python IPV6-MLD-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:23 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
( InetAddressIPv6, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32", "mib-2")
( RowStatus, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue")

# Objects

mldMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 91))
mldMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 1))
mldInterfaceTable = MibTable((1, 3, 6, 1, 2, 1, 91, 1, 1))
mldInterfaceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 91, 1, 1, 1)).setIndexNames((0, "IPV6-MLD-MIB", "mldInterfaceIfIndex"))
mldInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 1)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("noaccess"))
mldInterfaceQueryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readwrite"))
mldInterfaceStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 3)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
mldInterfaceVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 4)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readwrite"))
mldInterfaceQuerier = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 5)).setColumnInitializer(MibVariable((), InetAddressIPv6().addConstraints(subtypes.ValueRangeConstraint(16, 16))).setMaxAccess("readonly"))
mldInterfaceQueryMaxResponseDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 6)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readwrite"))
mldInterfaceJoins = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 7)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mldInterfaceGroups = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 8)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
mldInterfaceRobustness = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 9)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readwrite"))
mldInterfaceLastListenQueryIntvl = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 10)).setColumnInitializer(MibVariable((), Unsigned32()).setMaxAccess("readwrite"))
mldInterfaceProxyIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 11)).setColumnInitializer(MibVariable((), InterfaceIndexOrZero()).setMaxAccess("readwrite"))
mldInterfaceQuerierUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 12)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
mldInterfaceQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 13)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
mldCacheTable = MibTable((1, 3, 6, 1, 2, 1, 91, 1, 2))
mldCacheEntry = MibTableRow((1, 3, 6, 1, 2, 1, 91, 1, 2, 1)).setIndexNames((0, "IPV6-MLD-MIB", "mldCacheAddress"), (0, "IPV6-MLD-MIB", "mldCacheIfIndex"))
mldCacheAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), InetAddressIPv6().addConstraints(subtypes.ValueRangeConstraint(16, 16))).setMaxAccess("noaccess"))
mldCacheIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), InterfaceIndex()).setMaxAccess("noaccess"))
mldCacheSelf = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 3)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
mldCacheLastReporter = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 4)).setColumnInitializer(MibVariable((), InetAddressIPv6().addConstraints(subtypes.ValueRangeConstraint(16, 16))).setMaxAccess("readonly"))
mldCacheUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 5)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
mldCacheExpiryTime = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 6)).setColumnInitializer(MibVariable((), TimeTicks()).setMaxAccess("readonly"))
mldCacheStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 7)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
mldMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 2))
mldMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 2, 1))
mldMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 91, 2, 2))

# Augmentions

# Groups

mldBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 1)).setObjects(("IPV6-MLD-MIB", "mldCacheStatus"), ("IPV6-MLD-MIB", "mldInterfaceStatus"), ("IPV6-MLD-MIB", "mldCacheSelf"), )
mldProxyMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 4)).setObjects(("IPV6-MLD-MIB", "mldInterfaceProxyIfIndex"), )
mldHostMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 3)).setObjects(("IPV6-MLD-MIB", "mldInterfaceQuerier"), )
mldRouterMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 91, 2, 2, 2)).setObjects(("IPV6-MLD-MIB", "mldInterfaceGroups"), ("IPV6-MLD-MIB", "mldInterfaceQuerierExpiryTime"), ("IPV6-MLD-MIB", "mldInterfaceQueryInterval"), ("IPV6-MLD-MIB", "mldInterfaceVersion"), ("IPV6-MLD-MIB", "mldInterfaceLastListenQueryIntvl"), ("IPV6-MLD-MIB", "mldInterfaceJoins"), ("IPV6-MLD-MIB", "mldCacheExpiryTime"), ("IPV6-MLD-MIB", "mldInterfaceQuerierUpTime"), ("IPV6-MLD-MIB", "mldCacheUpTime"), ("IPV6-MLD-MIB", "mldInterfaceQueryMaxResponseDelay"), ("IPV6-MLD-MIB", "mldInterfaceQuerier"), ("IPV6-MLD-MIB", "mldInterfaceRobustness"), ("IPV6-MLD-MIB", "mldCacheLastReporter"), )

# Exports

# Objects
mibBuilder.exportSymbols("IPV6-MLD-MIB", mldMIB=mldMIB, mldMIBObjects=mldMIBObjects, mldInterfaceTable=mldInterfaceTable, mldInterfaceEntry=mldInterfaceEntry, mldInterfaceIfIndex=mldInterfaceIfIndex, mldInterfaceQueryInterval=mldInterfaceQueryInterval, mldInterfaceStatus=mldInterfaceStatus, mldInterfaceVersion=mldInterfaceVersion, mldInterfaceQuerier=mldInterfaceQuerier, mldInterfaceQueryMaxResponseDelay=mldInterfaceQueryMaxResponseDelay, mldInterfaceJoins=mldInterfaceJoins, mldInterfaceGroups=mldInterfaceGroups, mldInterfaceRobustness=mldInterfaceRobustness, mldInterfaceLastListenQueryIntvl=mldInterfaceLastListenQueryIntvl, mldInterfaceProxyIfIndex=mldInterfaceProxyIfIndex, mldInterfaceQuerierUpTime=mldInterfaceQuerierUpTime, mldInterfaceQuerierExpiryTime=mldInterfaceQuerierExpiryTime, mldCacheTable=mldCacheTable, mldCacheEntry=mldCacheEntry, mldCacheAddress=mldCacheAddress, mldCacheIfIndex=mldCacheIfIndex, mldCacheSelf=mldCacheSelf, mldCacheLastReporter=mldCacheLastReporter, mldCacheUpTime=mldCacheUpTime, mldCacheExpiryTime=mldCacheExpiryTime, mldCacheStatus=mldCacheStatus, mldMIBConformance=mldMIBConformance, mldMIBCompliances=mldMIBCompliances, mldMIBGroups=mldMIBGroups)

# Groups
mibBuilder.exportSymbols("IPV6-MLD-MIB", mldBaseMIBGroup=mldBaseMIBGroup, mldProxyMIBGroup=mldProxyMIBGroup, mldHostMIBGroup=mldHostMIBGroup, mldRouterMIBGroup=mldRouterMIBGroup)
