# PySNMP SMI module. Autogenerated from smidump -f python IANA-RTPROTO-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:58 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class IANAipMRouteProtocol(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(10,4,3,6,12,9,5,8,1,7,2,11,), )
    namedValues = Integer.namedValues.clone(("other", 1), ("igmpOnly", 10), ("bgmp", 11), ("msdp", 12), ("local", 2), ("netmgmt", 3), ("dvmrp", 4), ("mospf", 5), ("pimSparseDense", 6), ("cbt", 7), ("pimSparseMode", 8), ("pimDenseMode", 9), )
    pass

class IANAipRouteProtocol(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(10,9,6,13,16,5,8,14,15,11,1,17,12,4,2,7,3,), )
    namedValues = Integer.namedValues.clone(("other", 1), ("esIs", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15), ("ciscoEigrp", 16), ("dvmrp", 17), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("isIs", 9), )
    pass


# Objects

ianaRtProtoMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 84))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("IANA-RTPROTO-MIB", IANAipMRouteProtocol=IANAipMRouteProtocol, IANAipRouteProtocol=IANAipRouteProtocol)

# Objects
mibBuilder.exportSymbols("IANA-RTPROTO-MIB", ianaRtProtoMIB=ianaRtProtoMIB)

