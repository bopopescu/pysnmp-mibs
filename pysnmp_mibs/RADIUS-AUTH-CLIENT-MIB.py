# PySNMP SMI module. Autogenerated from smidump -f python RADIUS-AUTH-CLIENT-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:30:02 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetAddress, InetAddressType, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2")

# Objects

radiusMIB = ObjectIdentity((1, 3, 6, 1, 2, 1, 67))
if mibBuilder.loadTexts: radiusMIB.setDescription("The OID assigned to RADIUS MIB work by the IANA.")
radiusAuthentication = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1))
radiusAuthClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67, 1, 2)).setRevisions(("2006-08-21 00:00","1999-06-11 00:00",))
if mibBuilder.loadTexts: radiusAuthClientMIB.setOrganization("IETF RADIUS Extensions Working Group.")
if mibBuilder.loadTexts: radiusAuthClientMIB.setContactInfo(" Bernard Aboba\nMicrosoft\nOne Microsoft Way\nRedmond, WA  98052\n\n\n\nUS\nPhone: +1 425 936 6605\nEMail: bernarda@microsoft.com")
if mibBuilder.loadTexts: radiusAuthClientMIB.setDescription("The MIB module for entities implementing the client\nside of the Remote Authentication Dial-In User Service\n(RADIUS) authentication protocol.  Copyright (C) The\nInternet Society (2006).  This version of this MIB\nmodule is part of RFC 4668; see the RFC itself for\nfull legal notices.")
radiusAuthClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 1))
radiusAuthClient = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1))
radiusAuthClientInvalidServerAddresses = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly").setUnits("packets")
if mibBuilder.loadTexts: radiusAuthClientInvalidServerAddresses.setDescription("The number of RADIUS Access-Response packets\nreceived from unknown addresses.")
radiusAuthClientIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientIdentifier.setDescription("The NAS-Identifier of the RADIUS authentication client.\nThis is not necessarily the same as sysName in MIB II.")
radiusAuthServerTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3))
if mibBuilder.loadTexts: radiusAuthServerTable.setDescription("The (conceptual) table listing the RADIUS authentication\nservers with which the client shares a secret.")
radiusAuthServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1)).setIndexNames((0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerIndex"))
if mibBuilder.loadTexts: radiusAuthServerEntry.setDescription("An entry (conceptual row) representing a RADIUS\nauthentication server with which the client shares\na secret.")
radiusAuthServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: radiusAuthServerIndex.setDescription("A number uniquely identifying each RADIUS\nAuthentication server with which this client\ncommunicates.")
radiusAuthServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServerAddress.setDescription("The IP address of the RADIUS authentication server\nreferred to in this table entry.")
radiusAuthClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientServerPortNumber.setDescription("The UDP port the client is using to send requests to\nthis server.")
radiusAuthClientRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientRoundTripTime.setDescription("The time interval (in hundredths of a second) between\nthe most recent Access-Reply/Access-Challenge and the\nAccess-Request that matched it from this RADIUS\nauthentication server.")
radiusAuthClientAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRequests.setDescription("The number of RADIUS Access-Request packets sent\nto this server.  This does not include retransmissions.")
radiusAuthClientAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRetransmissions.setDescription("The number of RADIUS Access-Request packets\nretransmitted to this RADIUS authentication server.")
radiusAuthClientAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessAccepts.setDescription("The number of RADIUS Access-Accept packets\n(valid or invalid) received from this server.")
radiusAuthClientAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessRejects.setDescription("The number of RADIUS Access-Reject packets\n(valid or invalid) received from this server.")
radiusAuthClientAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientAccessChallenges.setDescription("The number of RADIUS Access-Challenge packets\n(valid or invalid) received from this server.")
radiusAuthClientMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientMalformedAccessResponses.setDescription("The number of malformed RADIUS Access-Response\npackets received from this server.\nMalformed packets include packets with\nan invalid length.  Bad authenticators or\nMessage Authenticator attributes or unknown types\nare not included as malformed access responses.")
radiusAuthClientBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientBadAuthenticators.setDescription("The number of RADIUS Access-Response packets\ncontaining invalid authenticators or Message\nAuthenticator attributes received from this server.")
radiusAuthClientPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientPendingRequests.setDescription("The number of RADIUS Access-Request packets\ndestined for this server that have not yet timed out\nor received a response.  This variable is incremented\n\n\n\nwhen an Access-Request is sent and decremented due to\nreceipt of an Access-Accept, Access-Reject,\nAccess-Challenge, timeout, or retransmission.")
radiusAuthClientTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientTimeouts.setDescription("The number of authentication timeouts to this server.\nAfter a timeout, the client may retry to the same\nserver, send to a different server, or\ngive up.  A retry to the same server is counted as a\nretransmit as well as a timeout.  A send to a different\nserver is counted as a Request as well as a timeout.")
radiusAuthClientUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientUnknownTypes.setDescription("The number of RADIUS packets of unknown type that\nwere received from this server on the authentication\nport.")
radiusAuthClientPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientPacketsDropped.setDescription("The number of RADIUS packets that were\nreceived from this server on the authentication port\nand dropped for some other reason.")
radiusAuthServerExtTable = MibTable((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4))
if mibBuilder.loadTexts: radiusAuthServerExtTable.setDescription("The (conceptual) table listing the RADIUS authentication\nservers with which the client shares a secret.")
radiusAuthServerExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1)).setIndexNames((0, "RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerExtIndex"))
if mibBuilder.loadTexts: radiusAuthServerExtEntry.setDescription("An entry (conceptual row) representing a RADIUS\nauthentication server with which the client shares\na secret.")
radiusAuthServerExtIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: radiusAuthServerExtIndex.setDescription("A number uniquely identifying each RADIUS\nAuthentication server with which this client\ncommunicates.")
radiusAuthServerInetAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServerInetAddressType.setDescription("The type of address format used for the\nradiusAuthServerInetAddress object.")
radiusAuthServerInetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthServerInetAddress.setDescription("The IP address of the RADIUS authentication\nserver referred to in this table entry, using\nthe version-neutral IP address format.")
radiusAuthClientServerInetPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 4), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientServerInetPortNumber.setDescription("The UDP port the client is using to send requests\nto this server.  The value of zero (0) is invalid.")
radiusAuthClientExtRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtRoundTripTime.setDescription("The time interval (in hundredths of a second) between\nthe most recent Access-Reply/Access-Challenge and the\nAccess-Request that matched it from this RADIUS\nauthentication server.")
radiusAuthClientExtAccessRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessRequests.setDescription("The number of RADIUS Access-Request packets sent\nto this server.  This does not include retransmissions.\nThis counter may experience a discontinuity when the\nRADIUS Client module within the managed entity is\nreinitialized, as indicated by the current value of\nradiusAuthClientCounterDiscontinuity.")
radiusAuthClientExtAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessRetransmissions.setDescription("The number of RADIUS Access-Request packets\nretransmitted to this RADIUS authentication server.\nThis counter may experience a discontinuity when\nthe RADIUS Client module within the managed entity\nis reinitialized, as indicated by the current value\nof radiusAuthClientCounterDiscontinuity.")
radiusAuthClientExtAccessAccepts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessAccepts.setDescription("The number of RADIUS Access-Accept packets\n(valid or invalid) received from this server.\nThis counter may experience a discontinuity when\nthe RADIUS Client module within the managed entity\nis reinitialized, as indicated by the current value\n\n\n\nof radiusAuthClientCounterDiscontinuity.")
radiusAuthClientExtAccessRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessRejects.setDescription("The number of RADIUS Access-Reject packets\n(valid or invalid) received from this server.\nThis counter may experience a discontinuity when\nthe RADIUS Client module within the managed\nentity is reinitialized, as indicated by the\ncurrent value of\nradiusAuthClientCounterDiscontinuity.")
radiusAuthClientExtAccessChallenges = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtAccessChallenges.setDescription("The number of RADIUS Access-Challenge packets\n(valid or invalid) received from this server.\nThis counter may experience a discontinuity when\nthe RADIUS Client module within the managed\nentity is reinitialized, as indicated by the\ncurrent value of\nradiusAuthClientCounterDiscontinuity.")
radiusAuthClientExtMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtMalformedAccessResponses.setDescription("The number of malformed RADIUS Access-Response\npackets received from this server.\nMalformed packets include packets with\n\n\n\nan invalid length.  Bad authenticators or\nMessage Authenticator attributes or unknown types\nare not included as malformed access responses.\nThis counter may experience a discontinuity when\nthe RADIUS Client module within the managed entity\nis reinitialized, as indicated by the current value\nof radiusAuthClientCounterDiscontinuity.")
radiusAuthClientExtBadAuthenticators = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtBadAuthenticators.setDescription("The number of RADIUS Access-Response packets\ncontaining invalid authenticators or Message\nAuthenticator attributes received from this server.\nThis counter may experience a discontinuity when\nthe RADIUS Client module within the managed entity\nis reinitialized, as indicated by the current value\nof radiusAuthClientCounterDiscontinuity.")
radiusAuthClientExtPendingRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtPendingRequests.setDescription("The number of RADIUS Access-Request packets\ndestined for this server that have not yet timed out\nor received a response.  This variable is incremented\nwhen an Access-Request is sent and decremented due to\nreceipt of an Access-Accept, Access-Reject,\nAccess-Challenge, timeout, or retransmission.")
radiusAuthClientExtTimeouts = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtTimeouts.setDescription("The number of authentication timeouts to this server.\n\n\n\nAfter a timeout, the client may retry to the same\nserver, send to a different server, or\ngive up.  A retry to the same server is counted as a\nretransmit as well as a timeout.  A send to a different\nserver is counted as a Request as well as a timeout.\nThis counter may experience a discontinuity when the\nRADIUS Client module within the managed entity is\nreinitialized, as indicated by the current value of\nradiusAuthClientCounterDiscontinuity.")
radiusAuthClientExtUnknownTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtUnknownTypes.setDescription("The number of RADIUS packets of unknown type that\nwere received from this server on the authentication\nport.  This counter may experience a discontinuity\nwhen the RADIUS Client module within the managed\nentity is reinitialized, as indicated by the current\nvalue of radiusAuthClientCounterDiscontinuity.")
radiusAuthClientExtPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientExtPacketsDropped.setDescription("The number of RADIUS packets that were\nreceived from this server on the authentication port\nand dropped for some other reason.  This counter may\nexperience a discontinuity when the RADIUS Client\nmodule within the managed entity is reinitialized,\nas indicated by the current value of\nradiusAuthClientCounterDiscontinuity.")
radiusAuthClientCounterDiscontinuity = MibTableColumn((1, 3, 6, 1, 2, 1, 67, 1, 2, 1, 1, 4, 1, 17), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusAuthClientCounterDiscontinuity.setDescription("The number of centiseconds since the last discontinuity\nin the RADIUS Client counters.  A discontinuity may\nbe the result of a reinitialization of the RADIUS\nClient module within the managed entity.")
radiusAuthClientMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2))
radiusAuthClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1))
radiusAuthClientMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2))

# Augmentions

# Groups

radiusAuthClientMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 1)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientRoundTripTime"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessChallenges"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessAccepts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRejects"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientUnknownTypes"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientBadAuthenticators"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientAccessRetransmissions"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPacketsDropped"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMalformedAccessResponses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientPendingRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientTimeouts"), )
if mibBuilder.loadTexts: radiusAuthClientMIBGroup.setDescription("The basic collection of objects providing management of\nRADIUS Authentication Clients.")
radiusAuthClientExtMIBGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 2, 2)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerInetPortNumber"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRejects"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtBadAuthenticators"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerInetAddressType"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientCounterDiscontinuity"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtUnknownTypes"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtTimeouts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientIdentifier"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessAccepts"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtRoundTripTime"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientInvalidServerAddresses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtPacketsDropped"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRequests"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtMalformedAccessResponses"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessChallenges"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtAccessRetransmissions"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerInetAddress"), ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtPendingRequests"), )
if mibBuilder.loadTexts: radiusAuthClientExtMIBGroup.setDescription("The collection of extended objects providing\nmanagement of RADIUS Authentication Clients\nusing version-neutral IP address format.")

# Compliances

radiusAuthClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1, 1)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientMIBGroup"), )
if mibBuilder.loadTexts: radiusAuthClientMIBCompliance.setDescription("The compliance statement for authentication clients\nimplementing the RADIUS Authentication Client MIB.\nImplementation of this module is for IPv4-only\nentities, or for backwards compatibility use with\nentities that support both IPv4 and IPv6.")
radiusAuthClientExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 67, 1, 2, 2, 1, 2)).setObjects(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientExtMIBGroup"), )
if mibBuilder.loadTexts: radiusAuthClientExtMIBCompliance.setDescription("The compliance statement for authentication\nclients implementing the RADIUS Authentication\nClient IPv6 Extensions MIB.  Implementation of\nthis module is for entities that support IPv6,\nor support IPv4 and IPv6.")

# Exports

# Module identity
mibBuilder.exportSymbols("RADIUS-AUTH-CLIENT-MIB", PYSNMP_MODULE_ID=radiusAuthClientMIB)

# Objects
mibBuilder.exportSymbols("RADIUS-AUTH-CLIENT-MIB", radiusMIB=radiusMIB, radiusAuthentication=radiusAuthentication, radiusAuthClientMIB=radiusAuthClientMIB, radiusAuthClientMIBObjects=radiusAuthClientMIBObjects, radiusAuthClient=radiusAuthClient, radiusAuthClientInvalidServerAddresses=radiusAuthClientInvalidServerAddresses, radiusAuthClientIdentifier=radiusAuthClientIdentifier, radiusAuthServerTable=radiusAuthServerTable, radiusAuthServerEntry=radiusAuthServerEntry, radiusAuthServerIndex=radiusAuthServerIndex, radiusAuthServerAddress=radiusAuthServerAddress, radiusAuthClientServerPortNumber=radiusAuthClientServerPortNumber, radiusAuthClientRoundTripTime=radiusAuthClientRoundTripTime, radiusAuthClientAccessRequests=radiusAuthClientAccessRequests, radiusAuthClientAccessRetransmissions=radiusAuthClientAccessRetransmissions, radiusAuthClientAccessAccepts=radiusAuthClientAccessAccepts, radiusAuthClientAccessRejects=radiusAuthClientAccessRejects, radiusAuthClientAccessChallenges=radiusAuthClientAccessChallenges, radiusAuthClientMalformedAccessResponses=radiusAuthClientMalformedAccessResponses, radiusAuthClientBadAuthenticators=radiusAuthClientBadAuthenticators, radiusAuthClientPendingRequests=radiusAuthClientPendingRequests, radiusAuthClientTimeouts=radiusAuthClientTimeouts, radiusAuthClientUnknownTypes=radiusAuthClientUnknownTypes, radiusAuthClientPacketsDropped=radiusAuthClientPacketsDropped, radiusAuthServerExtTable=radiusAuthServerExtTable, radiusAuthServerExtEntry=radiusAuthServerExtEntry, radiusAuthServerExtIndex=radiusAuthServerExtIndex, radiusAuthServerInetAddressType=radiusAuthServerInetAddressType, radiusAuthServerInetAddress=radiusAuthServerInetAddress, radiusAuthClientServerInetPortNumber=radiusAuthClientServerInetPortNumber, radiusAuthClientExtRoundTripTime=radiusAuthClientExtRoundTripTime, radiusAuthClientExtAccessRequests=radiusAuthClientExtAccessRequests, radiusAuthClientExtAccessRetransmissions=radiusAuthClientExtAccessRetransmissions, radiusAuthClientExtAccessAccepts=radiusAuthClientExtAccessAccepts, radiusAuthClientExtAccessRejects=radiusAuthClientExtAccessRejects, radiusAuthClientExtAccessChallenges=radiusAuthClientExtAccessChallenges, radiusAuthClientExtMalformedAccessResponses=radiusAuthClientExtMalformedAccessResponses, radiusAuthClientExtBadAuthenticators=radiusAuthClientExtBadAuthenticators, radiusAuthClientExtPendingRequests=radiusAuthClientExtPendingRequests, radiusAuthClientExtTimeouts=radiusAuthClientExtTimeouts, radiusAuthClientExtUnknownTypes=radiusAuthClientExtUnknownTypes, radiusAuthClientExtPacketsDropped=radiusAuthClientExtPacketsDropped, radiusAuthClientCounterDiscontinuity=radiusAuthClientCounterDiscontinuity, radiusAuthClientMIBConformance=radiusAuthClientMIBConformance, radiusAuthClientMIBCompliances=radiusAuthClientMIBCompliances, radiusAuthClientMIBGroups=radiusAuthClientMIBGroups)

# Groups
mibBuilder.exportSymbols("RADIUS-AUTH-CLIENT-MIB", radiusAuthClientMIBGroup=radiusAuthClientMIBGroup, radiusAuthClientExtMIBGroup=radiusAuthClientExtMIBGroup)

# Compliances
mibBuilder.exportSymbols("RADIUS-AUTH-CLIENT-MIB", radiusAuthClientMIBCompliance=radiusAuthClientMIBCompliance, radiusAuthClientExtMIBCompliance=radiusAuthClientExtMIBCompliance)
