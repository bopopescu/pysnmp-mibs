# PySNMP SMI module. Autogenerated from smidump -f python HC-PerfHist-TC-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:18 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class HCPerfCurrentCount(Counter64):
    pass

class HCPerfIntervalCount(Counter64):
    pass

class HCPerfIntervalThreshold(Unsigned32):
    subtypeConstraints = Unsigned32.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 900), )
    pass

class HCPerfInvalidIntervals(Integer32):
    subtypeConstraints = Integer32.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 96), )
    pass

class HCPerfTimeElapsed(Integer32):
    subtypeConstraints = Integer32.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 86399), )
    pass

class HCPerfTotalCount(Counter64):
    pass

class HCPerfValidIntervals(Integer32):
    subtypeConstraints = Integer32.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 96), )
    pass


# Objects

hcPerfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 107))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", HCPerfCurrentCount=HCPerfCurrentCount, HCPerfIntervalCount=HCPerfIntervalCount, HCPerfIntervalThreshold=HCPerfIntervalThreshold, HCPerfInvalidIntervals=HCPerfInvalidIntervals, HCPerfTimeElapsed=HCPerfTimeElapsed, HCPerfTotalCount=HCPerfTotalCount, HCPerfValidIntervals=HCPerfValidIntervals)

# Objects
mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", hcPerfHistTCMIB=hcPerfHistTCMIB)

