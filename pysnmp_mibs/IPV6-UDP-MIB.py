# PySNMP SMI module. Autogenerated from smidump -f python IPV6-UDP-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:23 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Ipv6Address, Ipv6IfIndexOrZero, ) = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address", "Ipv6IfIndexOrZero")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, experimental, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "experimental", "mib-2")

# Objects

udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
ipv6UdpTable = MibTable((1, 3, 6, 1, 2, 1, 7, 6))
ipv6UdpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 6, 1)).setIndexNames((0, "IPV6-UDP-MIB", "ipv6UdpLocalAddress"), (0, "IPV6-UDP-MIB", "ipv6UdpLocalPort"), (0, "IPV6-UDP-MIB", "ipv6UdpIfIndex"))
ipv6UdpLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 1)).setColumnInitializer(MibVariable((), Ipv6Address()).setMaxAccess("noaccess"))
ipv6UdpLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 2)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess"))
ipv6UdpIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 3)).setColumnInitializer(MibVariable((), Ipv6IfIndexOrZero()).setMaxAccess("readonly"))
ipv6UdpMIB = ModuleIdentity((1, 3, 6, 1, 3, 87))
ipv6UdpConformance = MibIdentifier((1, 3, 6, 1, 3, 87, 2))
ipv6UdpCompliances = MibIdentifier((1, 3, 6, 1, 3, 87, 2, 1))
ipv6UdpGroups = MibIdentifier((1, 3, 6, 1, 3, 87, 2, 2))

# Augmentions

# Groups

ipv6UdpGroup = ObjectGroup((1, 3, 6, 1, 3, 87, 2, 2, 1)).setObjects(("IPV6-UDP-MIB", "ipv6UdpIfIndex"), )

# Exports

# Objects
mibBuilder.exportSymbols("IPV6-UDP-MIB", udp=udp, ipv6UdpTable=ipv6UdpTable, ipv6UdpEntry=ipv6UdpEntry, ipv6UdpLocalAddress=ipv6UdpLocalAddress, ipv6UdpLocalPort=ipv6UdpLocalPort, ipv6UdpIfIndex=ipv6UdpIfIndex, ipv6UdpMIB=ipv6UdpMIB, ipv6UdpConformance=ipv6UdpConformance, ipv6UdpCompliances=ipv6UdpCompliances, ipv6UdpGroups=ipv6UdpGroups)

# Groups
mibBuilder.exportSymbols("IPV6-UDP-MIB", ipv6UdpGroup=ipv6UdpGroup)
