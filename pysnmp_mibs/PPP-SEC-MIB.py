# PySNMP SMI module. Autogenerated from smidump -f python PPP-SEC-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 19:13:34 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ppp, ) = mibBuilder.importSymbols("PPP-LCP-MIB", "ppp")
( Bits, Integer32, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")

# Objects

pppSecurity = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2))
pppSecurityProtocols = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2, 1))
pppSecurityPapProtocol = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2, 1, 1))
pppSecurityChapMD5Protocol = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 2, 1, 2))
pppSecurityConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 2, 2))
pppSecurityConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1)).setIndexNames((0, "PPP-SEC-MIB", "pppSecurityConfigLink"), (0, "PPP-SEC-MIB", "pppSecurityConfigPreference"))
pppSecurityConfigLink = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readwrite")
pppSecurityConfigPreference = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readwrite")
pppSecurityConfigProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
pppSecurityConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 2, 1, 4), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("invalid", 1), ("valid", 2), )).clone(2)).setMaxAccess("readwrite")
pppSecuritySecretsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 2, 3))
pppSecuritySecretsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1)).setIndexNames((0, "PPP-SEC-MIB", "pppSecuritySecretsLink"), (0, "PPP-SEC-MIB", "pppSecuritySecretsIdIndex"))
pppSecuritySecretsLink = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
pppSecuritySecretsIdIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("readonly")
pppSecuritySecretsDirection = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("local-to-remote", 1), ("remote-to-local", 2), ))).setMaxAccess("readwrite")
pppSecuritySecretsProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readwrite")
pppSecuritySecretsIdentity = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 5), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
pppSecuritySecretsSecret = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 6), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
pppSecuritySecretsStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 2, 3, 1, 7), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("invalid", 1), ("valid", 2), )).clone(2)).setMaxAccess("readwrite")

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("PPP-SEC-MIB", pppSecurity=pppSecurity, pppSecurityProtocols=pppSecurityProtocols, pppSecurityPapProtocol=pppSecurityPapProtocol, pppSecurityChapMD5Protocol=pppSecurityChapMD5Protocol, pppSecurityConfigTable=pppSecurityConfigTable, pppSecurityConfigEntry=pppSecurityConfigEntry, pppSecurityConfigLink=pppSecurityConfigLink, pppSecurityConfigPreference=pppSecurityConfigPreference, pppSecurityConfigProtocol=pppSecurityConfigProtocol, pppSecurityConfigStatus=pppSecurityConfigStatus, pppSecuritySecretsTable=pppSecuritySecretsTable, pppSecuritySecretsEntry=pppSecuritySecretsEntry, pppSecuritySecretsLink=pppSecuritySecretsLink, pppSecuritySecretsIdIndex=pppSecuritySecretsIdIndex, pppSecuritySecretsDirection=pppSecuritySecretsDirection, pppSecuritySecretsProtocol=pppSecuritySecretsProtocol, pppSecuritySecretsIdentity=pppSecuritySecretsIdentity, pppSecuritySecretsSecret=pppSecuritySecretsSecret, pppSecuritySecretsStatus=pppSecuritySecretsStatus)

