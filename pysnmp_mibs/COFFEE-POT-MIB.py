# PySNMP SMI module. Autogenerated from smidump -f python COFFEE-POT-MIB
# by libsmi2pysnmp-0.0.9-alpha at Thu Mar 26 19:36:14 2009,
# Python version (2, 4, 4, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( DisplayString, TimeInterval, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeInterval")

# Objects

coffee = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 132)).setRevisions(("1998-03-23 17:00",))
if mibBuilder.loadTexts: coffee.setOrganization("Networked Appliance Management Working Group")
if mibBuilder.loadTexts: coffee.setContactInfo("        Michael Slavitch\nLoran Technologies,\n955 Green Valley Crescent\nOttawa, Ontario Canada K2A 0B6\n\nTel: 613-723-7505\nFax: 613-723-7209\nE-mail: slavitch@loran.com")
if mibBuilder.loadTexts: coffee.setDescription("The MIB Module for coffee vending devices.")
potName = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 1), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: potName.setDescription("The vendor description of the pot under management")
potCapacity = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: potCapacity.setDescription("The number of units of beverage supported by this device\n(regardless of its current state) .")
potType = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,4,3,)).subtype(namedValues=namedval.NamedValues(("automatic-drip", 1), ("percolator", 2), ("french-press", 3), ("espresso", 4), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: potType.setDescription("The brew type of the coffee pot.")
potLocation = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 4), DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: potLocation.setDescription("The physical location of the pot in question")
potMonitor = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 132, 6))
potOperStatus = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,5,4,3,)).subtype(namedValues=namedval.NamedValues(("off", 1), ("brewing", 2), ("holding", 3), ("other", 4), ("waiting", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: potOperStatus.setDescription("The operating status of the pot in question. Note\nthat this is a read-only feature. Current hardware\nprevents us from changing the port state via SNMP.")
potLevel = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: potLevel.setDescription("The number of units of coffee under management. The\nunits of level are defined in potMetric below.")
potMetric = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(3,1,5,4,2,)).subtype(namedValues=namedval.NamedValues(("espresso", 1), ("demi-tasse", 2), ("cup", 3), ("mug", 4), ("bucket", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: potMetric.setDescription("The vendor description of the pot under management")
potStartTime = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: potStartTime.setDescription("The time in seconds since Jan 1 1970 to start the pot\nif and only if potOperStatus is waiting(5)")
lastStartTime = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 5), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastStartTime.setDescription("The amount of time, in TimeTicks, since the coffee\nmaking process was initiated.")
potTemperature = MibScalar((1, 3, 6, 1, 2, 1, 10, 132, 6, 6), Integer32()).setMaxAccess("readonly").setUnits("degrees Centigrade")
if mibBuilder.loadTexts: potTemperature.setDescription("The ambient temperature of the coffee within the pot")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("COFFEE-POT-MIB", PYSNMP_MODULE_ID=coffee)

# Objects
mibBuilder.exportSymbols("COFFEE-POT-MIB", coffee=coffee, potName=potName, potCapacity=potCapacity, potType=potType, potLocation=potLocation, potMonitor=potMonitor, potOperStatus=potOperStatus, potLevel=potLevel, potMetric=potMetric, potStartTime=potStartTime, lastStartTime=lastStartTime, potTemperature=potTemperature)

