# PySNMP SMI module. Autogenerated from smidump -f python COPS-CLIENT-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:11 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( RowStatus, TextualConvention, TimeInterval, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeInterval", "TimeStamp")

# Types

class CopsAuthType(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(2,4,0,3,5,1,), )
    namedValues = Integer.namedValues.clone(("authNone", 0), ("authOther", 1), ("authIpSecAh", 2), ("authIpSecEsp", 3), ("authTls", 4), ("authCopsIntegrity", 5), )
    pass

class CopsClientState(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(2,4,1,6,3,5,), )
    namedValues = Integer.namedValues.clone(("copsClientInvalid", 1), ("copsClientTcpconnected", 2), ("copsClientAuthenticating", 3), ("copsClientSecAccepted", 4), ("copsClientAccepted", 5), ("copsClientTimingout", 6), )
    pass

class CopsErrorCode(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(15,14,12,6,7,5,2,3,11,0,4,1,8,10,9,13,), )
    namedValues = Integer.namedValues.clone(("errorOther", 0), ("errorBadHandle", 1), ("errorUnspecified", 10), ("errorShuttingDown", 11), ("errorRedirectToPreferredServer", 12), ("errorUnknownCopsObject", 13), ("errorAuthenticationFailure", 14), ("errorAuthenticationMissing", 15), ("errorInvalidHandleReference", 2), ("errorBadMessageFormat", 3), ("errorUnableToProcess", 4), ("errorMandatoryClientSiMissing", 5), ("errorUnsupportedClientType", 6), ("errorMandatoryCopsObjectMissing", 7), ("errorClientFailure", 8), ("errorCommunicationFailure", 9), )
    pass

class CopsServerEntryType(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(2,1,), )
    namedValues = Integer.namedValues.clone(("copsServerStatic", 1), ("copsServerRedirect", 2), )
    pass

class CopsTcpPort(Integer32):
    subtypeConstraints = Integer32.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 65535), )
    pass


# Objects

copsClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 89))
copsClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1))
copsClientCapabilitiesGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1, 1))
copsClientCapabilities = MibVariable((1, 3, 6, 1, 2, 1, 89, 1, 1, 1), Bits().addNamedValues(("copsClientVersion1", 0), ("copsClientAuthIpSecAh", 1), ("copsClientAuthIpSecEsp", 2), ("copsClientAuthTls", 3), ("copsClientAuthInteg", 4), )).setMaxAccess("readonly")
copsClientStatusGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1, 2))
copsClientServerCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 89, 1, 2, 1))
copsClientServerCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1)).setIndexNames((0, "COPS-CLIENT-MIB", "copsClientServerAddressType"), (0, "COPS-CLIENT-MIB", "copsClientServerAddress"), (0, "COPS-CLIENT-MIB", "copsClientServerClientType"))
copsClientServerAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 1)).setColumnInitializer(MibVariable((), InetAddressType()).setMaxAccess("noaccess"))
copsClientServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 2)).setColumnInitializer(MibVariable((), InetAddress()).setMaxAccess("noaccess"))
copsClientServerClientType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess"))
copsClientServerTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 4)).setColumnInitializer(MibVariable((), CopsTcpPort()).setMaxAccess("readonly"))
copsClientServerType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 5)).setColumnInitializer(MibVariable((), CopsServerEntryType()).setMaxAccess("readonly"))
copsClientServerAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 6)).setColumnInitializer(MibVariable((), CopsAuthType()).setMaxAccess("readonly"))
copsClientServerLastConnAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 7)).setColumnInitializer(MibVariable((), TimeStamp()).setMaxAccess("readonly"))
copsClientState = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 8)).setColumnInitializer(MibVariable((), CopsClientState()).setMaxAccess("readonly"))
copsClientServerKeepaliveTime = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 9)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readonly"))
copsClientServerAccountingTime = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 10)).setColumnInitializer(MibVariable((), TimeInterval()).setMaxAccess("readonly"))
copsClientInPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 11)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientOutPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 12)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientInErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 13)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientLastError = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 14)).setColumnInitializer(MibVariable((), CopsErrorCode()).setMaxAccess("readonly"))
copsClientTcpConnectAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 15)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientTcpConnectFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 16)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientOpenAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 17)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientOpenFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 18)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrUnsupportClienttype = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 19)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrUnsupportedVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 20)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrLengthMismatch = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 21)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrUnknownOpcode = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 22)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrUnknownCnum = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 23)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrBadCtype = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 24)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrBadSends = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 25)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrWrongObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 26)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrWrongOpcode = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 27)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientKaTimedoutClients = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 28)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrAuthFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 29)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientErrAuthMissing = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 30)).setColumnInitializer(MibVariable((), Counter32()).setMaxAccess("readonly"))
copsClientConfigGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1, 3))
copsClientServerConfigTable = MibTable((1, 3, 6, 1, 2, 1, 89, 1, 3, 1))
copsClientServerConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1)).setIndexNames((0, "COPS-CLIENT-MIB", "copsClientServerConfigAddrType"), (0, "COPS-CLIENT-MIB", "copsClientServerConfigAddress"), (0, "COPS-CLIENT-MIB", "copsClientServerConfigClientType"), (0, "COPS-CLIENT-MIB", "copsClientServerConfigAuthType"))
copsClientServerConfigAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 1)).setColumnInitializer(MibVariable((), InetAddressType()).setMaxAccess("noaccess"))
copsClientServerConfigAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 2)).setColumnInitializer(MibVariable((), InetAddress()).setMaxAccess("noaccess"))
copsClientServerConfigClientType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("noaccess"))
copsClientServerConfigAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 4)).setColumnInitializer(MibVariable((), CopsAuthType()).setMaxAccess("noaccess"))
copsClientServerConfigTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 5)).setColumnInitializer(MibVariable((), CopsTcpPort()).setMaxAccess("readwrite"))
copsClientServerConfigPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 6)).setColumnInitializer(MibVariable((), Integer32()).setMaxAccess("readwrite"))
copsClientServerConfigRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 7)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readwrite"))
copsClientServerConfigRetryAlgrm = MibVariable((1, 3, 6, 1, 2, 1, 89, 1, 3, 2), Integer().addConstraints(subtypes.SingleValueConstraint(3,1,2,)).addNamedValues(("other", 1), ("sequential", 2), ("roundRobin", 3), ).set(2)).setMaxAccess("readwrite")
copsClientServerConfigRetryCount = MibVariable((1, 3, 6, 1, 2, 1, 89, 1, 3, 3), Unsigned32()).setMaxAccess("readwrite")
copsClientServerConfigRetryIntvl = MibVariable((1, 3, 6, 1, 2, 1, 89, 1, 3, 4), TimeInterval()).setMaxAccess("readwrite").setUnits("centi-seconds")
copsClientConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 2))
copsClientGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 2, 1))
copsClientCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 2, 2))

# Augmentions

# Groups

copsDeviceConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 89, 2, 1, 2)).setObjects(("COPS-CLIENT-MIB", "copsClientServerConfigPriority"), ("COPS-CLIENT-MIB", "copsClientServerConfigRowStatus"), ("COPS-CLIENT-MIB", "copsClientServerConfigTcpPort"), ("COPS-CLIENT-MIB", "copsClientServerConfigRetryIntvl"), ("COPS-CLIENT-MIB", "copsClientServerConfigRetryAlgrm"), ("COPS-CLIENT-MIB", "copsClientServerConfigRetryCount"), )
copsDeviceStatusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 89, 2, 1, 1)).setObjects(("COPS-CLIENT-MIB", "copsClientOutPkts"), ("COPS-CLIENT-MIB", "copsClientLastError"), ("COPS-CLIENT-MIB", "copsClientErrWrongObjects"), ("COPS-CLIENT-MIB", "copsClientInPkts"), ("COPS-CLIENT-MIB", "copsClientCapabilities"), ("COPS-CLIENT-MIB", "copsClientServerType"), ("COPS-CLIENT-MIB", "copsClientErrAuthFailures"), ("COPS-CLIENT-MIB", "copsClientState"), ("COPS-CLIENT-MIB", "copsClientKaTimedoutClients"), ("COPS-CLIENT-MIB", "copsClientErrUnknownCnum"), ("COPS-CLIENT-MIB", "copsClientErrUnsupportedVersion"), ("COPS-CLIENT-MIB", "copsClientErrLengthMismatch"), ("COPS-CLIENT-MIB", "copsClientServerKeepaliveTime"), ("COPS-CLIENT-MIB", "copsClientServerTcpPort"), ("COPS-CLIENT-MIB", "copsClientErrBadSends"), ("COPS-CLIENT-MIB", "copsClientErrWrongOpcode"), ("COPS-CLIENT-MIB", "copsClientServerAuthType"), ("COPS-CLIENT-MIB", "copsClientServerLastConnAttempt"), ("COPS-CLIENT-MIB", "copsClientErrAuthMissing"), ("COPS-CLIENT-MIB", "copsClientErrUnsupportClienttype"), ("COPS-CLIENT-MIB", "copsClientInErrs"), ("COPS-CLIENT-MIB", "copsClientTcpConnectFailures"), ("COPS-CLIENT-MIB", "copsClientErrUnknownOpcode"), ("COPS-CLIENT-MIB", "copsClientTcpConnectAttempts"), ("COPS-CLIENT-MIB", "copsClientOpenAttempts"), ("COPS-CLIENT-MIB", "copsClientServerAccountingTime"), ("COPS-CLIENT-MIB", "copsClientErrBadCtype"), ("COPS-CLIENT-MIB", "copsClientOpenFailures"), )

# Exports

# Types
mibBuilder.exportSymbols("COPS-CLIENT-MIB", CopsAuthType=CopsAuthType, CopsClientState=CopsClientState, CopsErrorCode=CopsErrorCode, CopsServerEntryType=CopsServerEntryType, CopsTcpPort=CopsTcpPort)

# Objects
mibBuilder.exportSymbols("COPS-CLIENT-MIB", copsClientMIB=copsClientMIB, copsClientMIBObjects=copsClientMIBObjects, copsClientCapabilitiesGroup=copsClientCapabilitiesGroup, copsClientCapabilities=copsClientCapabilities, copsClientStatusGroup=copsClientStatusGroup, copsClientServerCurrentTable=copsClientServerCurrentTable, copsClientServerCurrentEntry=copsClientServerCurrentEntry, copsClientServerAddressType=copsClientServerAddressType, copsClientServerAddress=copsClientServerAddress, copsClientServerClientType=copsClientServerClientType, copsClientServerTcpPort=copsClientServerTcpPort, copsClientServerType=copsClientServerType, copsClientServerAuthType=copsClientServerAuthType, copsClientServerLastConnAttempt=copsClientServerLastConnAttempt, copsClientState=copsClientState, copsClientServerKeepaliveTime=copsClientServerKeepaliveTime, copsClientServerAccountingTime=copsClientServerAccountingTime, copsClientInPkts=copsClientInPkts, copsClientOutPkts=copsClientOutPkts, copsClientInErrs=copsClientInErrs, copsClientLastError=copsClientLastError, copsClientTcpConnectAttempts=copsClientTcpConnectAttempts, copsClientTcpConnectFailures=copsClientTcpConnectFailures, copsClientOpenAttempts=copsClientOpenAttempts, copsClientOpenFailures=copsClientOpenFailures, copsClientErrUnsupportClienttype=copsClientErrUnsupportClienttype, copsClientErrUnsupportedVersion=copsClientErrUnsupportedVersion, copsClientErrLengthMismatch=copsClientErrLengthMismatch, copsClientErrUnknownOpcode=copsClientErrUnknownOpcode, copsClientErrUnknownCnum=copsClientErrUnknownCnum, copsClientErrBadCtype=copsClientErrBadCtype, copsClientErrBadSends=copsClientErrBadSends, copsClientErrWrongObjects=copsClientErrWrongObjects, copsClientErrWrongOpcode=copsClientErrWrongOpcode, copsClientKaTimedoutClients=copsClientKaTimedoutClients, copsClientErrAuthFailures=copsClientErrAuthFailures, copsClientErrAuthMissing=copsClientErrAuthMissing, copsClientConfigGroup=copsClientConfigGroup, copsClientServerConfigTable=copsClientServerConfigTable, copsClientServerConfigEntry=copsClientServerConfigEntry, copsClientServerConfigAddrType=copsClientServerConfigAddrType, copsClientServerConfigAddress=copsClientServerConfigAddress, copsClientServerConfigClientType=copsClientServerConfigClientType, copsClientServerConfigAuthType=copsClientServerConfigAuthType, copsClientServerConfigTcpPort=copsClientServerConfigTcpPort, copsClientServerConfigPriority=copsClientServerConfigPriority, copsClientServerConfigRowStatus=copsClientServerConfigRowStatus, copsClientServerConfigRetryAlgrm=copsClientServerConfigRetryAlgrm, copsClientServerConfigRetryCount=copsClientServerConfigRetryCount, copsClientServerConfigRetryIntvl=copsClientServerConfigRetryIntvl, copsClientConformance=copsClientConformance, copsClientGroups=copsClientGroups, copsClientCompliances=copsClientCompliances)

# Groups
mibBuilder.exportSymbols("COPS-CLIENT-MIB", copsDeviceConfigGroup=copsDeviceConfigGroup, copsDeviceStatusGroup=copsDeviceStatusGroup)
