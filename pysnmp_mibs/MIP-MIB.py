# PySNMP SMI module. Autogenerated from smidump -f python MIP-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:25 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( RowStatus, TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeStamp", "TruthValue")

# Types

class RegistrationFlags(Bits):
    namedValues = Bits.namedValues.clone(("vjCompression", 0), ("gre", 1), ("minEnc", 2), ("decapsulationbyMN", 3), ("broadcastDatagram", 4), ("simultaneousBindings", 5), )
    pass


# Objects

mipMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 44))
mipMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1))
mipSystem = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 1))
mipEntities = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 1, 1), Bits().addNamedValues(("mobileNode", 0), ("foreignAgent", 1), ("homeAgent", 2), )).setMaxAccess("readonly")
mipEnable = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 1, 2), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("enabled", 1), ("disabled", 2), )).setMaxAccess("readwrite")
mipEncapsulationSupported = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 1, 3), Bits().addNamedValues(("ipInIp", 0), ("gre", 1), ("minEnc", 2), ("other", 3), )).setMaxAccess("readonly")
mipSecurity = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 2))
mipSecAssocTable = MibTable((1, 3, 6, 1, 2, 1, 44, 1, 2, 1))
mipSecAssocEntry = MibTableRow((1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1)).setIndexNames((0, "MIP-MIB", "mipSecPeerAddress"), (0, "MIP-MIB", "mipSecSPI"))
mipSecPeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("noaccess"))
mipSecSPI = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 2)).setColumnInitializer(MibVariable((), Unsigned32().addConstraints(subtypes.ValueRangeConstraint(0, 4294967295L))).setMaxAccess("noaccess"))
mipSecAlgorithmType = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(1,2,)).addNamedValues(("other", 1), ("md5", 2), )).setMaxAccess("readwrite"))
mipSecAlgorithmMode = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 4)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,1,)).addNamedValues(("other", 1), ("prefixSuffix", 2), )).setMaxAccess("readwrite"))
mipSecKey = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 5)).setColumnInitializer(MibVariable((), OctetString().addConstraints(subtypes.ValueRangeConstraint(16, 16))).setMaxAccess("readwrite"))
mipSecReplayMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(2,3,1,)).addNamedValues(("other", 1), ("timestamps", 2), ("nonces", 3), )).setMaxAccess("readwrite"))
mipSecTotalViolations = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 2, 2), Counter32()).setMaxAccess("readonly")
mipSecViolationTable = MibTable((1, 3, 6, 1, 2, 1, 44, 1, 2, 3))
mipSecViolationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1)).setIndexNames((0, "MIP-MIB", "mipSecViolatorAddress"))
mipSecViolatorAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("notifyonly"))
mipSecViolationCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
mipSecRecentViolationSPI = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 3)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
mipSecRecentViolationTime = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 4)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
mipSecRecentViolationIDLow = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 5)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
mipSecRecentViolationIDHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 6)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
mipSecRecentViolationReason = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 2, 3, 1, 7)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(6,3,2,1,5,4,)).addNamedValues(("noMobilitySecurityAssociation", 1), ("badAuthenticator", 2), ("badIdentifier", 3), ("badSPI", 4), ("missingSecurityExtension", 5), ("other", 6), )).setMaxAccess("readonly"))
mipMN = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 3))
mnSystem = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 3, 1))
mnState = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 1), Integer().addConstraints(subtypes.SingleValueConstraint(1,5,2,4,3,)).addNamedValues(("home", 1), ("registered", 2), ("pending", 3), ("isolated", 4), ("unknown", 5), )).setMaxAccess("readonly")
mnHomeAddress = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
mnHATable = MibTable((1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 3))
mnHAEntry = MibTableRow((1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 3, 1)).setIndexNames((0, "MIP-MIB", "mnHAAddress"))
mnHAAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 3, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("noaccess"))
mnCurrentHA = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 3, 1, 2)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
mnHAStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 1, 3, 1, 3)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
mnDiscovery = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 3, 2))
mnFATable = MibTable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 1))
mnFAEntry = MibTableRow((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 1, 1)).setIndexNames((0, "MIP-MIB", "mnFAAddress"), (0, "MIP-MIB", "mnCOA"))
mnFAAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 1, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
mnCOA = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 1, 1, 2)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
mnRecentAdvReceived = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2))
mnAdvSourceAddress = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 1), IpAddress()).setMaxAccess("readonly")
mnAdvSequence = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 2), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
mnAdvFlags = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 3), Bits().addNamedValues(("vjCompression", 0), ("gre", 1), ("minEnc", 2), ("foreignAgent", 3), ("homeAgent", 4), ("busy", 5), ("regRequired", 6), )).setMaxAccess("readonly")
mnAdvMaxRegLifetime = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 4), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly").setUnits("seconds")
mnAdvMaxAdvLifetime = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 5), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly").setUnits("seconds")
mnAdvTimeReceived = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 2, 6), TimeStamp()).setMaxAccess("readonly")
mnSolicitationsSent = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 3), Counter32()).setMaxAccess("readonly")
mnAdvertisementsReceived = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 4), Counter32()).setMaxAccess("readonly")
mnAdvsDroppedInvalidExtension = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 5), Counter32()).setMaxAccess("readonly")
mnAdvsIgnoredUnknownExtension = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 6), Counter32()).setMaxAccess("readonly")
mnMoveFromHAToFA = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 7), Counter32()).setMaxAccess("readonly")
mnMoveFromFAToFA = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 8), Counter32()).setMaxAccess("readonly")
mnMoveFromFAToHA = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 9), Counter32()).setMaxAccess("readonly")
mnGratuitousARPsSend = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 10), Counter32()).setMaxAccess("readonly")
mnAgentRebootsDectected = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 2, 11), Counter32()).setMaxAccess("readonly")
mnRegistration = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 3, 3))
mnRegistrationTable = MibTable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1))
mnRegistrationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1)).setIndexNames((0, "MIP-MIB", "mnRegAgentAddress"), (0, "MIP-MIB", "mnRegCOA"))
mnRegAgentAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
mnRegCOA = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 2)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
mnRegFlags = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 3)).setColumnInitializer(MibVariable((), RegistrationFlags()).setMaxAccess("readonly"))
mnRegIDLow = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 4)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
mnRegIDHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 5)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
mnRegTimeRequested = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
mnRegTimeRemaining = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 7)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
mnRegTimeSent = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 8)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
mnRegIsAccepted = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 9)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
mnCOAIsLocal = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 1, 1, 10)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
mnRegRequestsSent = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 2), Counter32()).setMaxAccess("readonly")
mnDeRegRequestsSent = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 3), Counter32()).setMaxAccess("readonly")
mnRegRepliesRecieved = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 4), Counter32()).setMaxAccess("readonly")
mnDeRegRepliesRecieved = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 5), Counter32()).setMaxAccess("readonly")
mnRepliesInvalidHomeAddress = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 6), Counter32()).setMaxAccess("readonly")
mnRepliesUnknownHA = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 7), Counter32()).setMaxAccess("readonly")
mnRepliesUnknownFA = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 8), Counter32()).setMaxAccess("readonly")
mnRepliesInvalidID = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 9), Counter32()).setMaxAccess("readonly")
mnRepliesDroppedInvalidExtension = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 10), Counter32()).setMaxAccess("readonly")
mnRepliesIgnoredUnknownExtension = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 11), Counter32()).setMaxAccess("readonly")
mnRepliesHAAuthenticationFailure = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 12), Counter32()).setMaxAccess("readonly")
mnRepliesFAAuthenticationFailure = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 13), Counter32()).setMaxAccess("readonly")
mnRegRequestsAccepted = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 14), Counter32()).setMaxAccess("readonly")
mnRegRequestsDeniedByHA = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 15), Counter32()).setMaxAccess("readonly")
mnRegRequestsDeniedByFA = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 16), Counter32()).setMaxAccess("readonly")
mnRegRequestsDeniedByHADueToID = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 17), Counter32()).setMaxAccess("readonly")
mnRegRequestsWithDirectedBroadcast = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 3, 3, 18), Counter32()).setMaxAccess("readonly")
mipMA = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 4))
maAdvertisement = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 4, 2))
maAdvConfigTable = MibTable((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1))
maAdvConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1)).setIndexNames((0, "MIP-MIB", "maInterfaceAddress"))
maInterfaceAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("noaccess"))
maAdvMaxRegLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 2)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite"))
maAdvPrefixLengthInclusion = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 3)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
maAdvAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 4)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readwrite"))
maAdvMaxInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 5)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(4, 1800))).setMaxAccess("readwrite"))
maAdvMinInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(3, 1800))).setMaxAccess("readwrite"))
maAdvMaxAdvLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 7)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(4, 9000))).setMaxAccess("readwrite"))
maAdvResponseSolicitationOnly = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 8)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readwrite"))
maAdvStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 1, 1, 9)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
maAdvertisementsSent = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 2), Counter32()).setMaxAccess("readonly")
maAdvsSentForSolicitation = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 3), Counter32()).setMaxAccess("readonly")
maSolicitationsReceived = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 4, 2, 4), Counter32()).setMaxAccess("readonly")
mipFA = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 5))
faSystem = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 5, 1))
faCOATable = MibTable((1, 3, 6, 1, 2, 1, 44, 1, 5, 1, 1))
faCOAEntry = MibTableRow((1, 3, 6, 1, 2, 1, 44, 1, 5, 1, 1, 1)).setIndexNames((0, "MIP-MIB", "faSupportedCOA"))
faSupportedCOA = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 1, 1, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("noaccess"))
faCOAStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
faAdvertisement = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 5, 2))
faIsBusy = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 2, 1), TruthValue()).setMaxAccess("readonly")
faRegistrationRequired = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 2, 2), TruthValue()).setMaxAccess("readwrite")
faRegistration = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 5, 3))
faVisitorTable = MibTable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1))
faVisitorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1)).setIndexNames((0, "MIP-MIB", "faVisitorIPAddress"))
faVisitorIPAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
faVisitorHomeAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 2)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
faVisitorHomeAgentAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 3)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
faVisitorTimeGranted = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 4)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
faVisitorTimeRemaining = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 5)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
faVisitorRegFlags = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 6)).setColumnInitializer(MibVariable((), RegistrationFlags()).setMaxAccess("readonly"))
faVisitorRegIDLow = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 7)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
faVisitorRegIDHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 8)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
faVisitorRegIsAccepted = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 1, 1, 9)).setColumnInitializer(MibVariable((), TruthValue()).setMaxAccess("readonly"))
faRegRequestsReceived = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 2), Counter32()).setMaxAccess("readonly")
faRegRequestsRelayed = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 3), Counter32()).setMaxAccess("readonly")
faReasonUnspecified = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 4), Counter32()).setMaxAccess("readonly")
faAdmProhibited = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 5), Counter32()).setMaxAccess("readonly")
faInsufficientResource = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 6), Counter32()).setMaxAccess("readonly")
faMNAuthenticationFailure = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 7), Counter32()).setMaxAccess("readonly")
faRegLifetimeTooLong = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 8), Counter32()).setMaxAccess("readonly")
faPoorlyFormedRequests = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 9), Counter32()).setMaxAccess("readonly")
faEncapsulationUnavailable = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 10), Counter32()).setMaxAccess("readonly")
faVJCompressionUnavailable = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 11), Counter32()).setMaxAccess("readonly")
faHAUnreachable = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 12), Counter32()).setMaxAccess("readonly")
faRegRepliesRecieved = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 13), Counter32()).setMaxAccess("readonly")
faRegRepliesRelayed = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 14), Counter32()).setMaxAccess("readonly")
faHAAuthenticationFailure = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 15), Counter32()).setMaxAccess("readonly")
faPoorlyFormedReplies = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 5, 3, 16), Counter32()).setMaxAccess("readonly")
mipHA = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 6))
haRegistration = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 1, 6, 3))
haMobilityBindingTable = MibTable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1))
haMobilityBindingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1)).setIndexNames((0, "MIP-MIB", "haMobilityBindingMN"), (0, "MIP-MIB", "haMobilityBindingCOA"))
haMobilityBindingMN = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 1)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
haMobilityBindingCOA = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 2)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
haMobilityBindingSourceAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 3)).setColumnInitializer(MibVariable((), IpAddress()).setMaxAccess("readonly"))
haMobilityBindingRegFlags = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 4)).setColumnInitializer(MibVariable((), RegistrationFlags()).setMaxAccess("readonly"))
haMobilityBindingRegIDLow = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 5)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
haMobilityBindingRegIDHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
haMobilityBindingTimeGranted = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 7)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readonly"))
haMobilityBindingTimeRemaining = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 1, 1, 8)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
haCounterTable = MibTable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2))
haCounterEntry = MibTableRow((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1)).setIndexNames((0, "MIP-MIB", "haMobilityBindingMN"))
haServiceRequestsAccepted = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 2)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
haServiceRequestsDenied = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 3)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
haOverallServiceTime = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 4)).setColumnInitializer(MibVariable((), Gauge32()).setMaxAccess("readonly"))
haRecentServiceAcceptedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 5)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
haRecentServiceDeniedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 6)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
haRecentServiceDeniedCode = MibTableColumn((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 2, 1, 7)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(128,136,134,133,131,129,132,130,135,)).addNamedValues(("reasonUnspecified", 128), ("admProhibited", 129), ("insufficientResource", 130), ("mnAuthenticationFailure", 131), ("faAuthenticationFailure", 132), ("idMismatch", 133), ("poorlyFormedRequest", 134), ("tooManyBindings", 135), ("unknownHA", 136), )).setMaxAccess("readonly"))
haRegistrationAccepted = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 3), Counter32()).setMaxAccess("readonly")
haMultiBindingUnsupported = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 4), Counter32()).setMaxAccess("readonly")
haReasonUnspecified = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 5), Counter32()).setMaxAccess("readonly")
haAdmProhibited = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 6), Counter32()).setMaxAccess("readonly")
haInsufficientResource = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 7), Counter32()).setMaxAccess("readonly")
haMNAuthenticationFailure = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 8), Counter32()).setMaxAccess("readonly")
haFAAuthenticationFailure = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 9), Counter32()).setMaxAccess("readonly")
haIDMismatch = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 10), Counter32()).setMaxAccess("readonly")
haPoorlyFormedRequest = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 11), Counter32()).setMaxAccess("readonly")
haTooManyBindings = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 12), Counter32()).setMaxAccess("readonly")
haUnknownHA = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 13), Counter32()).setMaxAccess("readonly")
haGratuitiousARPsSent = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 14), Counter32()).setMaxAccess("readonly")
haProxyARPsSent = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 15), Counter32()).setMaxAccess("readonly")
haRegRequestsReceived = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 16), Counter32()).setMaxAccess("readonly")
haDeRegRequestsReceived = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 17), Counter32()).setMaxAccess("readonly")
haRegRepliesSent = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 18), Counter32()).setMaxAccess("readonly")
haDeRegRepliesSent = MibVariable((1, 3, 6, 1, 2, 1, 44, 1, 6, 3, 19), Counter32()).setMaxAccess("readonly")
mipMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 2))
mipMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 2, 0))
mipMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 3))
mipGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 3, 1))
mipCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 3, 2))

# Augmentions

# Notifications

mipAuthFailure = NotificationType((1, 3, 6, 1, 2, 1, 44, 2, 0, 1)).setObjects(("MIP-MIB", "mipSecRecentViolationIDLow"), ("MIP-MIB", "mipSecRecentViolationReason"), ("MIP-MIB", "mipSecViolatorAddress"), ("MIP-MIB", "mipSecRecentViolationSPI"), ("MIP-MIB", "mipSecRecentViolationIDHigh"), )

# Groups

haRegistrationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 11)).setObjects(("MIP-MIB", "haMobilityBindingSourceAddress"), ("MIP-MIB", "haRegistrationAccepted"), ("MIP-MIB", "haRegRequestsReceived"), ("MIP-MIB", "haMultiBindingUnsupported"), ("MIP-MIB", "haDeRegRequestsReceived"), ("MIP-MIB", "haMobilityBindingTimeGranted"), ("MIP-MIB", "haFAAuthenticationFailure"), ("MIP-MIB", "haPoorlyFormedRequest"), ("MIP-MIB", "haMobilityBindingRegIDHigh"), ("MIP-MIB", "haTooManyBindings"), ("MIP-MIB", "haMobilityBindingRegIDLow"), ("MIP-MIB", "haInsufficientResource"), ("MIP-MIB", "haUnknownHA"), ("MIP-MIB", "haProxyARPsSent"), ("MIP-MIB", "haDeRegRepliesSent"), ("MIP-MIB", "haMobilityBindingCOA"), ("MIP-MIB", "haReasonUnspecified"), ("MIP-MIB", "haIDMismatch"), ("MIP-MIB", "haMobilityBindingMN"), ("MIP-MIB", "haAdmProhibited"), ("MIP-MIB", "haMNAuthenticationFailure"), ("MIP-MIB", "haGratuitiousARPsSent"), ("MIP-MIB", "haRegRepliesSent"), ("MIP-MIB", "haMobilityBindingTimeRemaining"), ("MIP-MIB", "haMobilityBindingRegFlags"), )
faSystemGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 8)).setObjects(("MIP-MIB", "faCOAStatus"), )
mipSecNotificationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 13)).setObjects(("MIP-MIB", "mipAuthFailure"), )
mipSecAssociationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 2)).setObjects(("MIP-MIB", "mipSecReplayMethod"), ("MIP-MIB", "mipSecKey"), ("MIP-MIB", "mipSecAlgorithmMode"), ("MIP-MIB", "mipSecAlgorithmType"), )
mnSystemGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 4)).setObjects(("MIP-MIB", "mnState"), ("MIP-MIB", "mnHAStatus"), ("MIP-MIB", "mnHomeAddress"), ("MIP-MIB", "mnCurrentHA"), )
mipSystemGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 1)).setObjects(("MIP-MIB", "mipEntities"), ("MIP-MIB", "mipEncapsulationSupported"), ("MIP-MIB", "mipEnable"), )
haRegNodeCountersGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 12)).setObjects(("MIP-MIB", "haRecentServiceDeniedTime"), ("MIP-MIB", "haRecentServiceAcceptedTime"), ("MIP-MIB", "haRecentServiceDeniedCode"), ("MIP-MIB", "haServiceRequestsAccepted"), ("MIP-MIB", "haServiceRequestsDenied"), ("MIP-MIB", "haOverallServiceTime"), )
maAdvertisementGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 7)).setObjects(("MIP-MIB", "maAdvsSentForSolicitation"), ("MIP-MIB", "maAdvPrefixLengthInclusion"), ("MIP-MIB", "maAdvAddress"), ("MIP-MIB", "maAdvMaxRegLifetime"), ("MIP-MIB", "maAdvertisementsSent"), ("MIP-MIB", "maAdvResponseSolicitationOnly"), ("MIP-MIB", "maAdvMaxInterval"), ("MIP-MIB", "maSolicitationsReceived"), ("MIP-MIB", "maAdvMinInterval"), ("MIP-MIB", "maAdvMaxAdvLifetime"), ("MIP-MIB", "maAdvStatus"), )
mnRegistrationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 6)).setObjects(("MIP-MIB", "mnRegRequestsSent"), ("MIP-MIB", "mnRegRepliesRecieved"), ("MIP-MIB", "mnRegIsAccepted"), ("MIP-MIB", "mnRepliesInvalidID"), ("MIP-MIB", "mnRegRequestsDeniedByHA"), ("MIP-MIB", "mnDeRegRequestsSent"), ("MIP-MIB", "mnCOAIsLocal"), ("MIP-MIB", "mnRepliesHAAuthenticationFailure"), ("MIP-MIB", "mnRegIDLow"), ("MIP-MIB", "mnRepliesUnknownHA"), ("MIP-MIB", "mnRegFlags"), ("MIP-MIB", "mnRegCOA"), ("MIP-MIB", "mnRegRequestsWithDirectedBroadcast"), ("MIP-MIB", "mnRepliesFAAuthenticationFailure"), ("MIP-MIB", "mnDeRegRepliesRecieved"), ("MIP-MIB", "mnRegIDHigh"), ("MIP-MIB", "mnRegTimeRemaining"), ("MIP-MIB", "mnRegRequestsAccepted"), ("MIP-MIB", "mnRepliesUnknownFA"), ("MIP-MIB", "mnRegAgentAddress"), ("MIP-MIB", "mnRepliesIgnoredUnknownExtension"), ("MIP-MIB", "mnRegRequestsDeniedByFA"), ("MIP-MIB", "mnRegRequestsDeniedByHADueToID"), ("MIP-MIB", "mnRegTimeSent"), ("MIP-MIB", "mnRepliesDroppedInvalidExtension"), ("MIP-MIB", "mnRegTimeRequested"), ("MIP-MIB", "mnRepliesInvalidHomeAddress"), )
faAdvertisementGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 9)).setObjects(("MIP-MIB", "faRegistrationRequired"), ("MIP-MIB", "faIsBusy"), )
mnDiscoveryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 5)).setObjects(("MIP-MIB", "mnMoveFromFAToHA"), ("MIP-MIB", "mnAdvTimeReceived"), ("MIP-MIB", "mnSolicitationsSent"), ("MIP-MIB", "mnAdvSequence"), ("MIP-MIB", "mnAdvSourceAddress"), ("MIP-MIB", "mnAgentRebootsDectected"), ("MIP-MIB", "mnGratuitousARPsSend"), ("MIP-MIB", "mnCOA"), ("MIP-MIB", "mnAdvertisementsReceived"), ("MIP-MIB", "mnAdvFlags"), ("MIP-MIB", "mnFAAddress"), ("MIP-MIB", "mnAdvsDroppedInvalidExtension"), ("MIP-MIB", "mnMoveFromFAToFA"), ("MIP-MIB", "mnMoveFromHAToFA"), ("MIP-MIB", "mnAdvsIgnoredUnknownExtension"), ("MIP-MIB", "mnAdvMaxRegLifetime"), ("MIP-MIB", "mnAdvMaxAdvLifetime"), )
faRegistrationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 10)).setObjects(("MIP-MIB", "faVisitorRegIsAccepted"), ("MIP-MIB", "faHAAuthenticationFailure"), ("MIP-MIB", "faRegRepliesRelayed"), ("MIP-MIB", "faVisitorHomeAgentAddress"), ("MIP-MIB", "faPoorlyFormedRequests"), ("MIP-MIB", "faVisitorTimeRemaining"), ("MIP-MIB", "faVisitorRegIDLow"), ("MIP-MIB", "faInsufficientResource"), ("MIP-MIB", "faHAUnreachable"), ("MIP-MIB", "faMNAuthenticationFailure"), ("MIP-MIB", "faAdmProhibited"), ("MIP-MIB", "faVisitorIPAddress"), ("MIP-MIB", "faVisitorHomeAddress"), ("MIP-MIB", "faRegRequestsRelayed"), ("MIP-MIB", "faPoorlyFormedReplies"), ("MIP-MIB", "faVisitorRegFlags"), ("MIP-MIB", "faVisitorRegIDHigh"), ("MIP-MIB", "faReasonUnspecified"), ("MIP-MIB", "faRegRepliesRecieved"), ("MIP-MIB", "faVJCompressionUnavailable"), ("MIP-MIB", "faEncapsulationUnavailable"), ("MIP-MIB", "faRegRequestsReceived"), ("MIP-MIB", "faVisitorTimeGranted"), ("MIP-MIB", "faRegLifetimeTooLong"), )
mipSecViolationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 3, 1, 3)).setObjects(("MIP-MIB", "mipSecTotalViolations"), ("MIP-MIB", "mipSecRecentViolationSPI"), ("MIP-MIB", "mipSecRecentViolationIDLow"), ("MIP-MIB", "mipSecRecentViolationTime"), ("MIP-MIB", "mipSecViolationCounter"), ("MIP-MIB", "mipSecRecentViolationIDHigh"), ("MIP-MIB", "mipSecRecentViolationReason"), )

# Exports

# Types
mibBuilder.exportSymbols("MIP-MIB", RegistrationFlags=RegistrationFlags)

# Objects
mibBuilder.exportSymbols("MIP-MIB", mipMIB=mipMIB, mipMIBObjects=mipMIBObjects, mipSystem=mipSystem, mipEntities=mipEntities, mipEnable=mipEnable, mipEncapsulationSupported=mipEncapsulationSupported, mipSecurity=mipSecurity, mipSecAssocTable=mipSecAssocTable, mipSecAssocEntry=mipSecAssocEntry, mipSecPeerAddress=mipSecPeerAddress, mipSecSPI=mipSecSPI, mipSecAlgorithmType=mipSecAlgorithmType, mipSecAlgorithmMode=mipSecAlgorithmMode, mipSecKey=mipSecKey, mipSecReplayMethod=mipSecReplayMethod, mipSecTotalViolations=mipSecTotalViolations, mipSecViolationTable=mipSecViolationTable, mipSecViolationEntry=mipSecViolationEntry, mipSecViolatorAddress=mipSecViolatorAddress, mipSecViolationCounter=mipSecViolationCounter, mipSecRecentViolationSPI=mipSecRecentViolationSPI, mipSecRecentViolationTime=mipSecRecentViolationTime, mipSecRecentViolationIDLow=mipSecRecentViolationIDLow, mipSecRecentViolationIDHigh=mipSecRecentViolationIDHigh, mipSecRecentViolationReason=mipSecRecentViolationReason, mipMN=mipMN, mnSystem=mnSystem, mnState=mnState, mnHomeAddress=mnHomeAddress, mnHATable=mnHATable, mnHAEntry=mnHAEntry, mnHAAddress=mnHAAddress, mnCurrentHA=mnCurrentHA, mnHAStatus=mnHAStatus, mnDiscovery=mnDiscovery, mnFATable=mnFATable, mnFAEntry=mnFAEntry, mnFAAddress=mnFAAddress, mnCOA=mnCOA, mnRecentAdvReceived=mnRecentAdvReceived, mnAdvSourceAddress=mnAdvSourceAddress, mnAdvSequence=mnAdvSequence, mnAdvFlags=mnAdvFlags, mnAdvMaxRegLifetime=mnAdvMaxRegLifetime, mnAdvMaxAdvLifetime=mnAdvMaxAdvLifetime, mnAdvTimeReceived=mnAdvTimeReceived, mnSolicitationsSent=mnSolicitationsSent, mnAdvertisementsReceived=mnAdvertisementsReceived, mnAdvsDroppedInvalidExtension=mnAdvsDroppedInvalidExtension, mnAdvsIgnoredUnknownExtension=mnAdvsIgnoredUnknownExtension, mnMoveFromHAToFA=mnMoveFromHAToFA, mnMoveFromFAToFA=mnMoveFromFAToFA, mnMoveFromFAToHA=mnMoveFromFAToHA, mnGratuitousARPsSend=mnGratuitousARPsSend, mnAgentRebootsDectected=mnAgentRebootsDectected, mnRegistration=mnRegistration, mnRegistrationTable=mnRegistrationTable, mnRegistrationEntry=mnRegistrationEntry, mnRegAgentAddress=mnRegAgentAddress, mnRegCOA=mnRegCOA, mnRegFlags=mnRegFlags, mnRegIDLow=mnRegIDLow, mnRegIDHigh=mnRegIDHigh, mnRegTimeRequested=mnRegTimeRequested, mnRegTimeRemaining=mnRegTimeRemaining, mnRegTimeSent=mnRegTimeSent, mnRegIsAccepted=mnRegIsAccepted, mnCOAIsLocal=mnCOAIsLocal, mnRegRequestsSent=mnRegRequestsSent, mnDeRegRequestsSent=mnDeRegRequestsSent, mnRegRepliesRecieved=mnRegRepliesRecieved, mnDeRegRepliesRecieved=mnDeRegRepliesRecieved, mnRepliesInvalidHomeAddress=mnRepliesInvalidHomeAddress, mnRepliesUnknownHA=mnRepliesUnknownHA, mnRepliesUnknownFA=mnRepliesUnknownFA, mnRepliesInvalidID=mnRepliesInvalidID, mnRepliesDroppedInvalidExtension=mnRepliesDroppedInvalidExtension, mnRepliesIgnoredUnknownExtension=mnRepliesIgnoredUnknownExtension, mnRepliesHAAuthenticationFailure=mnRepliesHAAuthenticationFailure, mnRepliesFAAuthenticationFailure=mnRepliesFAAuthenticationFailure, mnRegRequestsAccepted=mnRegRequestsAccepted, mnRegRequestsDeniedByHA=mnRegRequestsDeniedByHA, mnRegRequestsDeniedByFA=mnRegRequestsDeniedByFA, mnRegRequestsDeniedByHADueToID=mnRegRequestsDeniedByHADueToID, mnRegRequestsWithDirectedBroadcast=mnRegRequestsWithDirectedBroadcast, mipMA=mipMA, maAdvertisement=maAdvertisement, maAdvConfigTable=maAdvConfigTable, maAdvConfigEntry=maAdvConfigEntry, maInterfaceAddress=maInterfaceAddress, maAdvMaxRegLifetime=maAdvMaxRegLifetime, maAdvPrefixLengthInclusion=maAdvPrefixLengthInclusion, maAdvAddress=maAdvAddress, maAdvMaxInterval=maAdvMaxInterval, maAdvMinInterval=maAdvMinInterval, maAdvMaxAdvLifetime=maAdvMaxAdvLifetime, maAdvResponseSolicitationOnly=maAdvResponseSolicitationOnly, maAdvStatus=maAdvStatus, maAdvertisementsSent=maAdvertisementsSent, maAdvsSentForSolicitation=maAdvsSentForSolicitation, maSolicitationsReceived=maSolicitationsReceived, mipFA=mipFA, faSystem=faSystem, faCOATable=faCOATable, faCOAEntry=faCOAEntry, faSupportedCOA=faSupportedCOA, faCOAStatus=faCOAStatus, faAdvertisement=faAdvertisement, faIsBusy=faIsBusy, faRegistrationRequired=faRegistrationRequired, faRegistration=faRegistration, faVisitorTable=faVisitorTable, faVisitorEntry=faVisitorEntry, faVisitorIPAddress=faVisitorIPAddress, faVisitorHomeAddress=faVisitorHomeAddress, faVisitorHomeAgentAddress=faVisitorHomeAgentAddress, faVisitorTimeGranted=faVisitorTimeGranted, faVisitorTimeRemaining=faVisitorTimeRemaining, faVisitorRegFlags=faVisitorRegFlags, faVisitorRegIDLow=faVisitorRegIDLow, faVisitorRegIDHigh=faVisitorRegIDHigh, faVisitorRegIsAccepted=faVisitorRegIsAccepted, faRegRequestsReceived=faRegRequestsReceived, faRegRequestsRelayed=faRegRequestsRelayed, faReasonUnspecified=faReasonUnspecified, faAdmProhibited=faAdmProhibited, faInsufficientResource=faInsufficientResource, faMNAuthenticationFailure=faMNAuthenticationFailure)
mibBuilder.exportSymbols("MIP-MIB", faRegLifetimeTooLong=faRegLifetimeTooLong, faPoorlyFormedRequests=faPoorlyFormedRequests, faEncapsulationUnavailable=faEncapsulationUnavailable, faVJCompressionUnavailable=faVJCompressionUnavailable, faHAUnreachable=faHAUnreachable, faRegRepliesRecieved=faRegRepliesRecieved, faRegRepliesRelayed=faRegRepliesRelayed, faHAAuthenticationFailure=faHAAuthenticationFailure, faPoorlyFormedReplies=faPoorlyFormedReplies, mipHA=mipHA, haRegistration=haRegistration, haMobilityBindingTable=haMobilityBindingTable, haMobilityBindingEntry=haMobilityBindingEntry, haMobilityBindingMN=haMobilityBindingMN, haMobilityBindingCOA=haMobilityBindingCOA, haMobilityBindingSourceAddress=haMobilityBindingSourceAddress, haMobilityBindingRegFlags=haMobilityBindingRegFlags, haMobilityBindingRegIDLow=haMobilityBindingRegIDLow, haMobilityBindingRegIDHigh=haMobilityBindingRegIDHigh, haMobilityBindingTimeGranted=haMobilityBindingTimeGranted, haMobilityBindingTimeRemaining=haMobilityBindingTimeRemaining, haCounterTable=haCounterTable, haCounterEntry=haCounterEntry, haServiceRequestsAccepted=haServiceRequestsAccepted, haServiceRequestsDenied=haServiceRequestsDenied, haOverallServiceTime=haOverallServiceTime, haRecentServiceAcceptedTime=haRecentServiceAcceptedTime, haRecentServiceDeniedTime=haRecentServiceDeniedTime, haRecentServiceDeniedCode=haRecentServiceDeniedCode, haRegistrationAccepted=haRegistrationAccepted, haMultiBindingUnsupported=haMultiBindingUnsupported, haReasonUnspecified=haReasonUnspecified, haAdmProhibited=haAdmProhibited, haInsufficientResource=haInsufficientResource, haMNAuthenticationFailure=haMNAuthenticationFailure, haFAAuthenticationFailure=haFAAuthenticationFailure, haIDMismatch=haIDMismatch, haPoorlyFormedRequest=haPoorlyFormedRequest, haTooManyBindings=haTooManyBindings, haUnknownHA=haUnknownHA, haGratuitiousARPsSent=haGratuitiousARPsSent, haProxyARPsSent=haProxyARPsSent, haRegRequestsReceived=haRegRequestsReceived, haDeRegRequestsReceived=haDeRegRequestsReceived, haRegRepliesSent=haRegRepliesSent, haDeRegRepliesSent=haDeRegRepliesSent, mipMIBNotificationPrefix=mipMIBNotificationPrefix, mipMIBNotifications=mipMIBNotifications, mipMIBConformance=mipMIBConformance, mipGroups=mipGroups, mipCompliances=mipCompliances)

# Notifications
mibBuilder.exportSymbols("MIP-MIB", mipAuthFailure=mipAuthFailure)

# Groups
mibBuilder.exportSymbols("MIP-MIB", haRegistrationGroup=haRegistrationGroup, faSystemGroup=faSystemGroup, mipSecNotificationsGroup=mipSecNotificationsGroup, mipSecAssociationGroup=mipSecAssociationGroup, mnSystemGroup=mnSystemGroup, mipSystemGroup=mipSystemGroup, haRegNodeCountersGroup=haRegNodeCountersGroup, maAdvertisementGroup=maAdvertisementGroup, mnRegistrationGroup=mnRegistrationGroup, faAdvertisementGroup=faAdvertisementGroup, mnDiscoveryGroup=mnDiscoveryGroup, faRegistrationGroup=faRegistrationGroup, mipSecViolationGroup=mipSecViolationGroup)
