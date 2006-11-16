# PySNMP SMI module. Autogenerated from smidump -f python DS0BUNDLE-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 19:13:17 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( DisplayString, RowStatus, TestAndIncr, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TestAndIncr")

# Objects

ds0Bundle = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 82)).setRevisions(("1998-07-16 16:30","1998-05-24 20:10",))
dsx0BondingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 82, 1))
dsx0BondingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 82, 1, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
dsx0BondMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 82, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,5,6,3,4,2,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("other", 2), ("mode0", 3), ("mode1", 4), ("mode2", 5), ("mode3", 6), ))).setMaxAccess("readcreate")
dsx0BondStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 82, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,3,2,)).subtype(namedValues=namedval.NamedValues(("idle", 1), ("callSetup", 2), ("dataTransfer", 3), ))).setMaxAccess("readonly")
dsx0BondRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 82, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
dsx0BundleNextIndex = MibScalar((1, 3, 6, 1, 2, 1, 10, 82, 2), TestAndIncr()).setMaxAccess("readwrite")
dsx0BundleTable = MibTable((1, 3, 6, 1, 2, 1, 10, 82, 3))
dsx0BundleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 82, 3, 1)).setIndexNames((0, "DS0BUNDLE-MIB", "dsx0BundleIndex"))
dsx0BundleIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 82, 3, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L))).setMaxAccess("noaccess")
dsx0BundleIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 82, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
dsx0BundleCircuitIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 82, 3, 1, 3), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
dsx0BundleRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 82, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
ds0BundleConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 82, 4))
ds0BundleGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 82, 4, 1))
ds0BundleCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 82, 4, 2))

# Augmentions

# Groups

ds0BundleConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 82, 4, 1, 2)).setObjects(("DS0BUNDLE-MIB", "dsx0BundleIfIndex"), ("DS0BUNDLE-MIB", "dsx0BundleRowStatus"), ("DS0BUNDLE-MIB", "dsx0BundleCircuitIdentifier"), ("DS0BUNDLE-MIB", "dsx0BundleNextIndex"), )
ds0BondingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 82, 4, 1, 1)).setObjects(("DS0BUNDLE-MIB", "dsx0BondMode"), ("DS0BUNDLE-MIB", "dsx0BondStatus"), ("DS0BUNDLE-MIB", "dsx0BondRowStatus"), )

# Exports

# Module identity
mibBuilder.exportSymbols("DS0BUNDLE-MIB", PYSNMP_MODULE_ID=ds0Bundle)

# Objects
mibBuilder.exportSymbols("DS0BUNDLE-MIB", ds0Bundle=ds0Bundle, dsx0BondingTable=dsx0BondingTable, dsx0BondingEntry=dsx0BondingEntry, dsx0BondMode=dsx0BondMode, dsx0BondStatus=dsx0BondStatus, dsx0BondRowStatus=dsx0BondRowStatus, dsx0BundleNextIndex=dsx0BundleNextIndex, dsx0BundleTable=dsx0BundleTable, dsx0BundleEntry=dsx0BundleEntry, dsx0BundleIndex=dsx0BundleIndex, dsx0BundleIfIndex=dsx0BundleIfIndex, dsx0BundleCircuitIdentifier=dsx0BundleCircuitIdentifier, dsx0BundleRowStatus=dsx0BundleRowStatus, ds0BundleConformance=ds0BundleConformance, ds0BundleGroups=ds0BundleGroups, ds0BundleCompliances=ds0BundleCompliances)

# Groups
mibBuilder.exportSymbols("DS0BUNDLE-MIB", ds0BundleConfigGroup=ds0BundleConfigGroup, ds0BondingGroup=ds0BondingGroup)
