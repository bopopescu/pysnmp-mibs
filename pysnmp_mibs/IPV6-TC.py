# PySNMP SMI module. Autogenerated from smidump -f python IPV6-TC
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:23 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, Integer32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "MibIdentifier", "TimeTicks")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class Ipv6Address(TextualConvention, OctetString):
    subtypeConstraints = OctetString.subtypeConstraints + ( subtypes.ValueRangeConstraint(16, 16), )
    pass

class Ipv6AddressIfIdentifier(TextualConvention, OctetString):
    subtypeConstraints = OctetString.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 8), )
    pass

class Ipv6AddressPrefix(TextualConvention, OctetString):
    subtypeConstraints = OctetString.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 16), )
    pass

class Ipv6IfIndex(TextualConvention, Integer32):
    subtypeConstraints = Integer32.subtypeConstraints + ( subtypes.ValueRangeConstraint(1, 2147483647L), )
    pass

class Ipv6IfIndexOrZero(TextualConvention, Integer32):
    subtypeConstraints = Integer32.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 2147483647L), )
    pass


# Exports

# Types
mibBuilder.exportSymbols("IPV6-TC", Ipv6Address=Ipv6Address, Ipv6AddressIfIdentifier=Ipv6AddressIfIdentifier, Ipv6AddressPrefix=Ipv6AddressPrefix, Ipv6IfIndex=Ipv6IfIndex, Ipv6IfIndexOrZero=Ipv6IfIndexOrZero)

