# PySNMP SMI module. Autogenerated from smidump -f python NETWORK-SERVICES-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:29:50 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp")

# Types

class DistinguishedName(TextualConvention, OctetString):
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)
    
class URLString(TextualConvention, OctetString):
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)
    

# Objects

application = ModuleIdentity((1, 3, 6, 1, 2, 1, 27)).setRevisions(("2000-03-03 00:00","1999-05-12 00:00","1997-08-17 00:00","1993-11-28 00:00",))
if mibBuilder.loadTexts: application.setOrganization("IETF Mail and Directory Management Working Group")
if mibBuilder.loadTexts: application.setContactInfo("        Ned Freed\n\nPostal: Innosoft International, Inc.\n        1050 Lakes Drive\n        West Covina, CA 91790\n        US\n\n   Tel: +1 626 919 3600\n   Fax: +1 626 919 3614\n\nE-Mail: ned.freed@innosoft.com")
if mibBuilder.loadTexts: application.setDescription("The MIB module describing network service applications")
applTable = MibTable((1, 3, 6, 1, 2, 1, 27, 1))
if mibBuilder.loadTexts: applTable.setDescription("The table holding objects which apply to all different\nkinds of applications providing network services.\nEach network service application capable of being\nmonitored should have a single entry in this table.")
applEntry = MibTableRow((1, 3, 6, 1, 2, 1, 27, 1, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: applEntry.setDescription("An entry associated with a single network service\napplication.")
applIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: applIndex.setDescription("An index to uniquely identify the network service\napplication. This attribute is the index used for\nlexicographic ordering of the table.")
applName = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applName.setDescription("The name the network service application chooses to be\nknown by.")
applDirectoryName = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 3), DistinguishedName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applDirectoryName.setDescription("The Distinguished Name of the directory entry where\nstatic information about this application is stored.\nAn empty string indicates that no information about\nthe application is available in the directory.")
applVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applVersion.setDescription("The version of network service application software.\nThis field is usually defined by the vendor of the\nnetwork service application software.")
applUptime = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applUptime.setDescription("The value of sysUpTime at the time the network service\napplication was last initialized.  If the application was\nlast initialized prior to the last initialization of the\nnetwork management subsystem, then this object contains\na zero value.")
applOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,2,5,6,4,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ("halted", 3), ("congested", 4), ("restarting", 5), ("quiescing", 6), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: applOperStatus.setDescription("Indicates the operational status of the network service\napplication. 'down' indicates that the network service is\nnot available. 'up' indicates that the network service\nis operational and available.  'halted' indicates that the\nservice is operational but not available.  'congested'\nindicates that the service is operational but no additional\ninbound associations can be accommodated.  'restarting'\nindicates that the service is currently unavailable but is\nin the process of restarting and will be available soon.\n'quiescing' indicates that service is currently operational\nbut is in the process of shutting down. Additional inbound\nassociations may be rejected by applications in the\n'quiescing' state.")
applLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applLastChange.setDescription("The value of sysUpTime at the time the network service\napplication entered its current operational state.  If\nthe current state was entered prior to the last\ninitialization of the local network management subsystem,\nthen this object contains a zero value.")
applInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applInboundAssociations.setDescription("The number of current associations to the network service\napplication, where it is the responder.  An inbound\nassociation occurs when another application successfully\nconnects to this one.")
applOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applOutboundAssociations.setDescription("The number of current associations to the network service\napplication, where it is the initiator.  An outbound\nassociation occurs when this application successfully\nconnects to another one.")
applAccumulatedInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applAccumulatedInboundAssociations.setDescription("The total number of associations to the application entity\nsince application initialization, where it was the responder.")
applAccumulatedOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applAccumulatedOutboundAssociations.setDescription("The total number of associations to the application entity\nsince application initialization, where it was the initiator.")
applLastInboundActivity = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applLastInboundActivity.setDescription("The value of sysUpTime at the time this application last\nhad an inbound association.  If the last association\noccurred prior to the last initialization of the network\nsubsystem, then this object contains a zero value.")
applLastOutboundActivity = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applLastOutboundActivity.setDescription("The value of sysUpTime at the time this application last\nhad an outbound association.  If the last association\noccurred prior to the last initialization of the network\nsubsystem, then this object contains a zero value.")
applRejectedInboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applRejectedInboundAssociations.setDescription("The total number of inbound associations the application\nentity has rejected, since application initialization.\nRejected associations are not counted in the accumulated\nassociation totals.  Note that this only counts\nassociations the application entity has rejected itself;\nit does not count rejections that occur at lower layers\nof the network.  Thus, this counter may not reflect the\ntrue number of failed inbound associations.")
applFailedOutboundAssociations = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applFailedOutboundAssociations.setDescription("The total number associations where the application entity\nis initiator and association establishment has failed,\nsince application initialization.  Failed associations are\nnot counted in the accumulated association totals.")
applDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 16), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applDescription.setDescription("A text description of the application.  This information\nis intended to identify and briefly describe the\napplication in a status display.")
applURL = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 1, 1, 17), URLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applURL.setDescription("A URL pointing to a description of the application.\nThis information is intended to identify and describe\nthe application in a status display.")
assocTable = MibTable((1, 3, 6, 1, 2, 1, 27, 2))
if mibBuilder.loadTexts: assocTable.setDescription("The table holding a set of all active application\nassociations.")
assocEntry = MibTableRow((1, 3, 6, 1, 2, 1, 27, 2, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "NETWORK-SERVICES-MIB", "assocIndex"))
if mibBuilder.loadTexts: assocEntry.setDescription("An entry associated with an association for a network\nservice application.")
assocIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: assocIndex.setDescription("An index to uniquely identify each association for a network\nservice application.  This attribute is the index that is\nused for lexicographic ordering of the table.  Note that the\ntable is also indexed by the applIndex.")
assocRemoteApplication = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocRemoteApplication.setDescription("The name of the system running remote network service\napplication.  For an IP-based application this should be\neither a domain name or IP address.  For an OSI application\nit should be the string encoded distinguished name of the\nmanaged object.  For X.400(1984) MTAs which do not have a\nDistinguished Name, the RFC 2156 syntax 'mta in\nglobalid' used in X400-Received: fields can be used. Note,\nhowever, that not all connections an MTA makes are\nnecessarily to another MTA.")
assocApplicationProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocApplicationProtocol.setDescription("An identification of the protocol being used for the\napplication.  For an OSI Application, this will be the\nApplication Context.  For Internet applications, OID\nvalues of the form {applTCPProtoID port} or {applUDPProtoID\nport} are used for TCP-based and UDP-based protocols,\nrespectively. In either case 'port' corresponds to the\nprimary port number being used by the protocol. The\nusual IANA procedures may be used to register ports for\nnew protocols.")
assocApplicationType = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,4,3,)).subtype(namedValues=NamedValues(("uainitiator", 1), ("uaresponder", 2), ("peerinitiator", 3), ("peerresponder", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocApplicationType.setDescription("This indicates whether the remote application is some type of\nclient making use of this network service (e.g., a Mail User\nAgent) or a server acting as a peer. Also indicated is whether\nthe remote end initiated an incoming connection to the network\nservice or responded to an outgoing connection made by the\nlocal application.  MTAs and messaging gateways are\nconsidered to be peers for the purposes of this variable.")
assocDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 27, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: assocDuration.setDescription("The value of sysUpTime at the time this association was\nstarted.  If this association started prior to the last\ninitialization of the network subsystem, then this\nobject contains a zero value.")
applConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 3))
applGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 3, 1))
applCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 3, 2))
applTCPProtoID = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 4))
applUDPProtoID = MibIdentifier((1, 3, 6, 1, 2, 1, 27, 5))

# Augmentions

# Groups

assocRFC1565Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 2)).setObjects(("NETWORK-SERVICES-MIB", "assocApplicationType"), ("NETWORK-SERVICES-MIB", "assocDuration"), ("NETWORK-SERVICES-MIB", "assocRemoteApplication"), ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"), )
if mibBuilder.loadTexts: assocRFC1565Group.setDescription("A collection of objects providing basic monitoring of\nnetwork service applications' associations.  This is the\noriginal set of such objects defined in RFC 1565.")
applRFC2248Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 3)).setObjects(("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"), ("NETWORK-SERVICES-MIB", "applName"), ("NETWORK-SERVICES-MIB", "applURL"), ("NETWORK-SERVICES-MIB", "applOperStatus"), ("NETWORK-SERVICES-MIB", "applUptime"), ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastChange"), ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applInboundAssociations"), ("NETWORK-SERVICES-MIB", "applOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applVersion"), ("NETWORK-SERVICES-MIB", "applLastInboundActivity"), ("NETWORK-SERVICES-MIB", "applDescription"), )
if mibBuilder.loadTexts: applRFC2248Group.setDescription("A collection of objects providing basic monitoring of\nnetwork service applications.  This group was originally\ndefined in RFC 2248; note that applDirectoryName is\nmissing.")
assocRFC2248Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 4)).setObjects(("NETWORK-SERVICES-MIB", "assocApplicationType"), ("NETWORK-SERVICES-MIB", "assocDuration"), ("NETWORK-SERVICES-MIB", "assocRemoteApplication"), ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"), )
if mibBuilder.loadTexts: assocRFC2248Group.setDescription("A collection of objects providing basic monitoring of\nnetwork service applications' associations.  This group\nwas originally defined by RFC 2248.")
applRFC2788Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 5)).setObjects(("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"), ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applInboundAssociations"), ("NETWORK-SERVICES-MIB", "applDirectoryName"), ("NETWORK-SERVICES-MIB", "applName"), ("NETWORK-SERVICES-MIB", "applURL"), ("NETWORK-SERVICES-MIB", "applOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applOperStatus"), ("NETWORK-SERVICES-MIB", "applVersion"), ("NETWORK-SERVICES-MIB", "applUptime"), ("NETWORK-SERVICES-MIB", "applLastInboundActivity"), ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applDescription"), ("NETWORK-SERVICES-MIB", "applLastChange"), )
if mibBuilder.loadTexts: applRFC2788Group.setDescription("A collection of objects providing basic monitoring of\nnetwork service applications.  This is the appropriate\ngroup for RFC 2788 -- it adds the applDirectoryName object\nmissing in RFC 2248.")
assocRFC2788Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 6)).setObjects(("NETWORK-SERVICES-MIB", "assocApplicationType"), ("NETWORK-SERVICES-MIB", "assocDuration"), ("NETWORK-SERVICES-MIB", "assocRemoteApplication"), ("NETWORK-SERVICES-MIB", "assocApplicationProtocol"), )
if mibBuilder.loadTexts: assocRFC2788Group.setDescription("A collection of objects providing basic monitoring of\nnetwork service applications' associations.  This is\nthe appropriate group for RFC 2788.")
applRFC1565Group = ObjectGroup((1, 3, 6, 1, 2, 1, 27, 3, 1, 7)).setObjects(("NETWORK-SERVICES-MIB", "applAccumulatedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastOutboundActivity"), ("NETWORK-SERVICES-MIB", "applName"), ("NETWORK-SERVICES-MIB", "applOperStatus"), ("NETWORK-SERVICES-MIB", "applUptime"), ("NETWORK-SERVICES-MIB", "applRejectedInboundAssociations"), ("NETWORK-SERVICES-MIB", "applLastChange"), ("NETWORK-SERVICES-MIB", "applAccumulatedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applInboundAssociations"), ("NETWORK-SERVICES-MIB", "applOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applFailedOutboundAssociations"), ("NETWORK-SERVICES-MIB", "applVersion"), ("NETWORK-SERVICES-MIB", "applLastInboundActivity"), )
if mibBuilder.loadTexts: applRFC1565Group.setDescription("A collection of objects providing basic monitoring of\nnetwork service applications.  This is the original set\nof such objects defined in RFC 1565.")

# Compliances

applCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 1)).setObjects(("NETWORK-SERVICES-MIB", "applRFC1565Group"), )
if mibBuilder.loadTexts: applCompliance.setDescription("The compliance statement for RFC 1565 implementations\nwhich support the Network Services Monitoring MIB\nfor basic monitoring of network service applications.\nThis is the basic compliance statement for RFC 1565.")
assocCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 2)).setObjects(("NETWORK-SERVICES-MIB", "assocRFC1565Group"), ("NETWORK-SERVICES-MIB", "applRFC1565Group"), )
if mibBuilder.loadTexts: assocCompliance.setDescription("The compliance statement for RFC 1565 implementations\nwhich support the Network Services Monitoring MIB\nfor basic monitoring of network service applications\nand their associations.")
applRFC2248Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 3)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2248Group"), )
if mibBuilder.loadTexts: applRFC2248Compliance.setDescription("The compliance statement for RFC 2248 implementations\nwhich support the Network Services Monitoring MIB\nfor basic monitoring of network service applications.")
assocRFC2248Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 4)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2248Group"), ("NETWORK-SERVICES-MIB", "assocRFC2248Group"), )
if mibBuilder.loadTexts: assocRFC2248Compliance.setDescription("The compliance statement for RFC 2248 implementations\nwhich support the Network Services Monitoring MIB for\nbasic monitoring of network service applications and\ntheir associations.")
applRFC2788Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 5)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2788Group"), )
if mibBuilder.loadTexts: applRFC2788Compliance.setDescription("The compliance statement for RFC 2788 implementations\nwhich support the Network Services Monitoring MIB\nfor basic monitoring of network service applications.")
assocRFC2788Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 27, 3, 2, 6)).setObjects(("NETWORK-SERVICES-MIB", "applRFC2788Group"), ("NETWORK-SERVICES-MIB", "assocRFC2788Group"), )
if mibBuilder.loadTexts: assocRFC2788Compliance.setDescription("The compliance statement for RFC 2788 implementations\nwhich support the Network Services Monitoring MIB for\nbasic monitoring of network service applications and\ntheir associations.")

# Exports

# Module identity
mibBuilder.exportSymbols("NETWORK-SERVICES-MIB", PYSNMP_MODULE_ID=application)

# Types
mibBuilder.exportSymbols("NETWORK-SERVICES-MIB", DistinguishedName=DistinguishedName, URLString=URLString)

# Objects
mibBuilder.exportSymbols("NETWORK-SERVICES-MIB", application=application, applTable=applTable, applEntry=applEntry, applIndex=applIndex, applName=applName, applDirectoryName=applDirectoryName, applVersion=applVersion, applUptime=applUptime, applOperStatus=applOperStatus, applLastChange=applLastChange, applInboundAssociations=applInboundAssociations, applOutboundAssociations=applOutboundAssociations, applAccumulatedInboundAssociations=applAccumulatedInboundAssociations, applAccumulatedOutboundAssociations=applAccumulatedOutboundAssociations, applLastInboundActivity=applLastInboundActivity, applLastOutboundActivity=applLastOutboundActivity, applRejectedInboundAssociations=applRejectedInboundAssociations, applFailedOutboundAssociations=applFailedOutboundAssociations, applDescription=applDescription, applURL=applURL, assocTable=assocTable, assocEntry=assocEntry, assocIndex=assocIndex, assocRemoteApplication=assocRemoteApplication, assocApplicationProtocol=assocApplicationProtocol, assocApplicationType=assocApplicationType, assocDuration=assocDuration, applConformance=applConformance, applGroups=applGroups, applCompliances=applCompliances, applTCPProtoID=applTCPProtoID, applUDPProtoID=applUDPProtoID)

# Groups
mibBuilder.exportSymbols("NETWORK-SERVICES-MIB", assocRFC1565Group=assocRFC1565Group, applRFC2248Group=applRFC2248Group, assocRFC2248Group=assocRFC2248Group, applRFC2788Group=applRFC2788Group, assocRFC2788Group=assocRFC2788Group, applRFC1565Group=applRFC1565Group)

# Compliances
mibBuilder.exportSymbols("NETWORK-SERVICES-MIB", applCompliance=applCompliance, assocCompliance=assocCompliance, applRFC2248Compliance=applRFC2248Compliance, assocRFC2248Compliance=assocRFC2248Compliance, applRFC2788Compliance=applRFC2788Compliance, assocRFC2788Compliance=assocRFC2788Compliance)
