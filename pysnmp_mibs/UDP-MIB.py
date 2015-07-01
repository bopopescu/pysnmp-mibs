#
# PySNMP MIB module UDP-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/UDP-MIB.txt
# Produced by pysmi-0.0.3 at Wed Jul  1 22:32:58 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( InetAddress, InetPortNumber, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, Bits, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, IpAddress, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "Bits", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
udpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 50)).setRevisions(("2005-05-20 00:00", "1994-11-01 00:00", "1991-03-31 00:00",))
if mibBuilder.loadTexts: udpMIB.setOrganization('IETF IPv6 Working Group\n            http://www.ietf.org/html.charters/ipv6-charter.html')
if mibBuilder.loadTexts: udpMIB.setContactInfo('Bill Fenner (editor)\n\n            AT&T Labs -- Research\n            75 Willow Rd.\n            Menlo Park, CA 94025\n\n            Phone: +1 650 330-7893\n            Email: <fenner@research.att.com>\n\n            John Flick (editor)\n\n            Hewlett-Packard Company\n            8000 Foothills Blvd. M/S 5557\n            Roseville, CA 95747\n\n            Phone: +1 916 785 4018\n            Email: <john.flick@hp.com>\n\n            Send comments to <ipv6@ietf.org>')
if mibBuilder.loadTexts: udpMIB.setDescription('The MIB module for managing UDP implementations.\n            Copyright (C) The Internet Society (2005).  This\n            version of this MIB module is part of RFC 4113;\n            see the RFC itself for full legal notices.')
udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
udpInDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInDatagrams.setDescription('The total number of UDP datagrams delivered to UDP\n            users.\n\n            Discontinuities in the value of this counter can occur\n            at re-initialization of the management system, and at\n            other times as indicated by discontinuities in the\n            value of sysUpTime.')
udpNoPorts = MibScalar((1, 3, 6, 1, 2, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpNoPorts.setDescription('The total number of received UDP datagrams for which\n            there was no application at the destination port.\n\n            Discontinuities in the value of this counter can occur\n            at re-initialization of the management system, and at\n            other times as indicated by discontinuities in the\n            value of sysUpTime.')
udpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInErrors.setDescription('The number of received UDP datagrams that could not be\n            delivered for reasons other than the lack of an\n            application at the destination port.\n\n            Discontinuities in the value of this counter can occur\n            at re-initialization of the management system, and at\n            other times as indicated by discontinuities in the\n            value of sysUpTime.')
udpOutDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpOutDatagrams.setDescription('The total number of UDP datagrams sent from this\n            entity.\n\n            Discontinuities in the value of this counter can occur\n            at re-initialization of the management system, and at\n            other times as indicated by discontinuities in the\n            value of sysUpTime.')
udpHCInDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpHCInDatagrams.setDescription('The total number of UDP datagrams delivered to UDP\n            users, for devices that can receive more than 1\n            million UDP datagrams per second.\n\n            Discontinuities in the value of this counter can occur\n            at re-initialization of the management system, and at\n            other times as indicated by discontinuities in the\n            value of sysUpTime.')
udpHCOutDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpHCOutDatagrams.setDescription('The total number of UDP datagrams sent from this\n            entity, for devices that can transmit more than 1\n            million UDP datagrams per second.\n\n            Discontinuities in the value of this counter can occur\n            at re-initialization of the management system, and at\n            other times as indicated by discontinuities in the\n            value of sysUpTime.')
udpEndpointTable = MibTable((1, 3, 6, 1, 2, 1, 7, 7), )
if mibBuilder.loadTexts: udpEndpointTable.setDescription("A table containing information about this entity's UDP\n            endpoints on which a local application is currently\n            accepting or sending datagrams.\n\n            The address type in this table represents the address\n            type used for the communication, irrespective of the\n            higher-layer abstraction.  For example, an application\n            using IPv6 'sockets' to communicate via IPv4 between\n            ::ffff:10.0.0.1 and ::ffff:10.0.0.2 would use\n            InetAddressType ipv4(1).\n\n            Unlike the udpTable in RFC 2013, this table also allows\n            the representation of an application that completely\n            specifies both local and remote addresses and ports.  A\n            listening application is represented in three possible\n            ways:\n\n            1) An application that is willing to accept both IPv4\n               and IPv6 datagrams is represented by a\n               udpEndpointLocalAddressType of unknown(0) and a\n               udpEndpointLocalAddress of ''h (a zero-length\n               octet-string).\n\n            2) An application that is willing to accept only IPv4\n               or only IPv6 datagrams is represented by a\n               udpEndpointLocalAddressType of the appropriate\n               address type and a udpEndpointLocalAddress of\n               '0.0.0.0' or '::' respectively.\n\n            3) An application that is listening for datagrams only\n               for a specific IP address but from any remote\n               system is represented by a\n               udpEndpointLocalAddressType of the appropriate\n               address type, with udpEndpointLocalAddress\n               specifying the local address.\n\n            In all cases where the remote is a wildcard, the\n            udpEndpointRemoteAddressType is unknown(0), the\n            udpEndpointRemoteAddress is ''h (a zero-length\n            octet-string), and the udpEndpointRemotePort is 0.\n\n            If the operating system is demultiplexing UDP packets\n            by remote address and port, or if the application has\n            'connected' the socket specifying a default remote\n            address and port, the udpEndpointRemote* values should\n            be used to reflect this.")
udpEndpointEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 7, 1), ).setIndexNames((0, "UDP-MIB", "udpEndpointLocalAddressType"), (0, "UDP-MIB", "udpEndpointLocalAddress"), (0, "UDP-MIB", "udpEndpointLocalPort"), (0, "UDP-MIB", "udpEndpointRemoteAddressType"), (0, "UDP-MIB", "udpEndpointRemoteAddress"), (0, "UDP-MIB", "udpEndpointRemotePort"), (0, "UDP-MIB", "udpEndpointInstance"))
if mibBuilder.loadTexts: udpEndpointEntry.setDescription('Information about a particular current UDP endpoint.\n\n            Implementers need to be aware that if the total number\n            of elements (octets or sub-identifiers) in\n            udpEndpointLocalAddress and udpEndpointRemoteAddress\n            exceeds 111, then OIDs of column instances in this table\n            will have more than 128 sub-identifiers and cannot be\n            accessed using SNMPv1, SNMPv2c, or SNMPv3.')
udpEndpointLocalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 1), InetAddressType())
if mibBuilder.loadTexts: udpEndpointLocalAddressType.setDescription('The address type of udpEndpointLocalAddress.  Only\n            IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or\n            unknown(0) if datagrams for all local IP addresses are\n            accepted.')
udpEndpointLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 2), InetAddress())
if mibBuilder.loadTexts: udpEndpointLocalAddress.setDescription("The local IP address for this UDP endpoint.\n\n            The value of this object can be represented in three\n\n            possible ways, depending on the characteristics of the\n            listening application:\n\n            1. For an application that is willing to accept both\n               IPv4 and IPv6 datagrams, the value of this object\n               must be ''h (a zero-length octet-string), with\n               the value of the corresponding instance of the\n               udpEndpointLocalAddressType object being unknown(0).\n\n            2. For an application that is willing to accept only IPv4\n               or only IPv6 datagrams, the value of this object\n               must be '0.0.0.0' or '::', respectively, while the\n               corresponding instance of the\n               udpEndpointLocalAddressType object represents the\n               appropriate address type.\n\n            3. For an application that is listening for data\n               destined only to a specific IP address, the value\n               of this object is the specific IP address for which\n               this node is receiving packets, with the\n               corresponding instance of the\n               udpEndpointLocalAddressType object representing the\n               appropriate address type.\n\n            As this object is used in the index for the\n            udpEndpointTable, implementors of this table should be\n            careful not to create entries that would result in OIDs\n            with more than 128 subidentifiers; else the information\n            cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
udpEndpointLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: udpEndpointLocalPort.setDescription('The local port number for this UDP endpoint.')
udpEndpointRemoteAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 4), InetAddressType())
if mibBuilder.loadTexts: udpEndpointRemoteAddressType.setDescription('The address type of udpEndpointRemoteAddress.  Only\n            IPv4, IPv4z, IPv6, and IPv6z addresses are expected, or\n            unknown(0) if datagrams for all remote IP addresses are\n            accepted.  Also, note that some combinations of\n\n            udpEndpointLocalAdressType and\n            udpEndpointRemoteAddressType are not supported.  In\n            particular, if the value of this object is not\n            unknown(0), it is expected to always refer to the\n            same IP version as udpEndpointLocalAddressType.')
udpEndpointRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 5), InetAddress())
if mibBuilder.loadTexts: udpEndpointRemoteAddress.setDescription("The remote IP address for this UDP endpoint.  If\n            datagrams from any remote system are to be accepted,\n            this value is ''h (a zero-length octet-string).\n            Otherwise, it has the type described by\n            udpEndpointRemoteAddressType and is the address of the\n            remote system from which datagrams are to be accepted\n            (or to which all datagrams will be sent).\n\n            As this object is used in the index for the\n            udpEndpointTable, implementors of this table should be\n            careful not to create entries that would result in OIDs\n            with more than 128 subidentifiers; else the information\n            cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.")
udpEndpointRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 6), InetPortNumber())
if mibBuilder.loadTexts: udpEndpointRemotePort.setDescription('The remote port number for this UDP endpoint.  If\n            datagrams from any remote system are to be accepted,\n            this value is zero.')
udpEndpointInstance = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,4294967295)))
if mibBuilder.loadTexts: udpEndpointInstance.setDescription("The instance of this tuple.  This object is used to\n            distinguish among multiple processes 'connected' to\n            the same UDP endpoint.  For example, on a system\n            implementing the BSD sockets interface, this would be\n            used to support the SO_REUSEADDR and SO_REUSEPORT\n            socket options.")
udpEndpointProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 7, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpEndpointProcess.setDescription("The system's process ID for the process associated with\n            this endpoint, or zero if there is no such process.\n            This value is expected to be the same as\n            HOST-RESOURCES-MIB::hrSWRunIndex or SYSAPPL-MIB::\n            sysApplElmtRunIndex for some row in the appropriate\n            tables.")
udpTable = MibTable((1, 3, 6, 1, 2, 1, 7, 5), )
if mibBuilder.loadTexts: udpTable.setDescription('A table containing IPv4-specific UDP listener\n            information.  It contains information about all local\n            IPv4 UDP end-points on which an application is\n            currently accepting datagrams.  This table has been\n            deprecated in favor of the version neutral\n            udpEndpointTable.')
udpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 5, 1), ).setIndexNames((0, "UDP-MIB", "udpLocalAddress"), (0, "UDP-MIB", "udpLocalPort"))
if mibBuilder.loadTexts: udpEntry.setDescription('Information about a particular current UDP listener.')
udpLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpLocalAddress.setDescription('The local IP address for this UDP listener.  In the\n            case of a UDP listener that is willing to accept\n            datagrams for any IP interface associated with the\n            node, the value 0.0.0.0 is used.')
udpLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpLocalPort.setDescription('The local port number for this UDP listener.')
udpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2))
udpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2, 1))
udpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 50, 2, 2))
udpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 50, 2, 1, 2)).setObjects(*(("UDP-MIB", "udpBaseGroup"), ("UDP-MIB", "udpEndpointGroup"), ("UDP-MIB", "udpHCGroup"),))
if mibBuilder.loadTexts: udpMIBCompliance2.setDescription('The compliance statement for systems that implement\n            UDP.\n\n            There are a number of INDEX objects that cannot be\n            represented in the form of OBJECT clauses in SMIv2, but\n            for which we have the following compliance\n            requirements, expressed in OBJECT clause form in this\n            description clause:\n\n            -- OBJECT      udpEndpointLocalAddressType\n            -- SYNTAX      InetAddressType { unknown(0), ipv4(1),\n            --                               ipv6(2), ipv4z(3),\n            --                               ipv6z(4) }\n            -- DESCRIPTION\n            --     Support for dns(5) is not required.\n            -- OBJECT      udpEndpointLocalAddress\n\n            -- SYNTAX      InetAddress (SIZE(0|4|8|16|20))\n            -- DESCRIPTION\n            --     Support is only required for zero-length\n            --     octet-strings, and for scoped and unscoped\n            --     IPv4 and IPv6 addresses.\n            -- OBJECT      udpEndpointRemoteAddressType\n            -- SYNTAX      InetAddressType { unknown(0), ipv4(1),\n            --                               ipv6(2), ipv4z(3),\n            --                               ipv6z(4) }\n            -- DESCRIPTION\n            --     Support for dns(5) is not required.\n            -- OBJECT      udpEndpointRemoteAddress\n            -- SYNTAX      InetAddress (SIZE(0|4|8|16|20))\n            -- DESCRIPTION\n            --     Support is only required for zero-length\n            --     octet-strings, and for scoped and unscoped\n            --     IPv4 and IPv6 addresses.\n           ')
udpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 50, 2, 1, 1)).setObjects(*(("UDP-MIB", "udpGroup"),))
if mibBuilder.loadTexts: udpMIBCompliance.setDescription('The compliance statement for IPv4-only systems that\n            implement UDP.  For IP version independence, this\n            compliance statement is deprecated in favor of\n            udpMIBCompliance2.  However, agents are still\n            encouraged to implement these objects in order to\n            interoperate with the deployed base of managers.')
udpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 1)).setObjects(*(("UDP-MIB", "udpInDatagrams"), ("UDP-MIB", "udpNoPorts"), ("UDP-MIB", "udpInErrors"), ("UDP-MIB", "udpOutDatagrams"), ("UDP-MIB", "udpLocalAddress"), ("UDP-MIB", "udpLocalPort"),))
if mibBuilder.loadTexts: udpGroup.setDescription('The deprecated group of objects providing for\n            management of UDP over IPv4.')
udpBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 2)).setObjects(*(("UDP-MIB", "udpInDatagrams"), ("UDP-MIB", "udpNoPorts"), ("UDP-MIB", "udpInErrors"), ("UDP-MIB", "udpOutDatagrams"),))
if mibBuilder.loadTexts: udpBaseGroup.setDescription('The group of objects providing for counters of UDP\n            statistics.')
udpHCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 3)).setObjects(*(("UDP-MIB", "udpHCInDatagrams"), ("UDP-MIB", "udpHCOutDatagrams"),))
if mibBuilder.loadTexts: udpHCGroup.setDescription('The group of objects providing for counters of high\n            speed UDP implementations.')
udpEndpointGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 50, 2, 2, 4)).setObjects(*(("UDP-MIB", "udpEndpointProcess"),))
if mibBuilder.loadTexts: udpEndpointGroup.setDescription("The group of objects providing for the IP version\n            independent management of UDP 'endpoints'.")
mibBuilder.exportSymbols("UDP-MIB", udpMIBConformance=udpMIBConformance, udpInErrors=udpInErrors, udpEndpointEntry=udpEndpointEntry, udp=udp, udpGroup=udpGroup, udpTable=udpTable, udpBaseGroup=udpBaseGroup, udpMIBCompliance2=udpMIBCompliance2, udpEndpointRemotePort=udpEndpointRemotePort, udpEndpointGroup=udpEndpointGroup, udpEndpointTable=udpEndpointTable, udpLocalPort=udpLocalPort, udpEndpointInstance=udpEndpointInstance, udpEndpointRemoteAddress=udpEndpointRemoteAddress, udpEntry=udpEntry, udpInDatagrams=udpInDatagrams, udpNoPorts=udpNoPorts, udpEndpointProcess=udpEndpointProcess, udpLocalAddress=udpLocalAddress, udpHCInDatagrams=udpHCInDatagrams, udpEndpointLocalAddressType=udpEndpointLocalAddressType, PYSNMP_MODULE_ID=udpMIB, udpHCGroup=udpHCGroup, udpHCOutDatagrams=udpHCOutDatagrams, udpMIB=udpMIB, udpMIBCompliance=udpMIBCompliance, udpOutDatagrams=udpOutDatagrams, udpEndpointLocalAddress=udpEndpointLocalAddress, udpMIBCompliances=udpMIBCompliances, udpEndpointRemoteAddressType=udpEndpointRemoteAddressType, udpEndpointLocalPort=udpEndpointLocalPort, udpMIBGroups=udpMIBGroups)
