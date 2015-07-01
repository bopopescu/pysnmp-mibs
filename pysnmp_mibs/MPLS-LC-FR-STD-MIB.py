#
# PySNMP MIB module MPLS-LC-FR-STD-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/MPLS-LC-FR-STD-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:30:10 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( DLCI, ) = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "DLCI")
( mplsInterfaceIndex, ) = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsInterfaceIndex")
( mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( StorageType, DisplayString, RowStatus, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "RowStatus", "TextualConvention")
mplsLcFrStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 10)).setRevisions(("2006-01-12 00:00",))
if mibBuilder.loadTexts: mplsLcFrStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsLcFrStdMIB.setContactInfo('        Thomas D. Nadeau\n                Cisco Systems, Inc.\n        Email:  tnadeau@cisco.com\n\n                Subrahmanya Hegde\n        Email:  subrah@cisco.com\n\n        General comments should be sent to mpls@uu.net\n       ')
if mibBuilder.loadTexts: mplsLcFrStdMIB.setDescription('This MIB module contains managed object definitions for\n        MPLS Label-Controlled Frame-Relay interfaces as defined\n        in (RFC3034).\n\n        Copyright (C) The Internet Society (2006).  This\n        version of this MIB module is part of RFC 4368; see\n        the RFC itself for full legal notices.')
mplsLcFrStdNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 0))
mplsLcFrStdObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 1))
mplsLcFrStdConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 2))
mplsLcFrStdInterfaceConfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1), )
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfTable.setDescription("This table specifies per-interface MPLS LC-FR\n        capability and associated information.  In particular,\n        this table sparsely extends the MPLS-LSR-STD-MIB's\n        mplsInterfaceConfTable.")
mplsLcFrStdInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1), ).setIndexNames((0, "MPLS-LC-FR-STD-MIB", "mplsInterfaceIndex"))
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfEntry.setDescription('An entry in this table is created by an LSR for\n        every interface capable of supporting MPLS LC-FR.\n        Each entry in this table will exist only if a\n        corresponding entry in ifTable and mplsInterfaceConfTable\n        exists.  If the associated entries in ifTable and\n        mplsInterfaceConfTable are deleted, the corresponding\n        entry in this table must also be deleted shortly\n        thereafter.')
mplsLcFrStdTrafficMinDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 1), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdTrafficMinDlci.setDescription('This is the minimum DLCI value over which this\n        LSR is willing to accept traffic on this\n        interface.')
mplsLcFrStdTrafficMaxDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 2), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdTrafficMaxDlci.setDescription('This is the max DLCI value over which this\n        LSR is willing to accept traffic on this\n        interface.')
mplsLcFrStdCtrlMinDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 3), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdCtrlMinDlci.setDescription('This is the min DLCI value over which this\n        LSR is willing to accept control traffic\n        on this interface.')
mplsLcFrStdCtrlMaxDlci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 4), DLCI()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdCtrlMaxDlci.setDescription('This is the max DLCI value over which this\n        LSR is willing to accept control traffic\n        on this interface.')
mplsLcFrStdInterfaceConfRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfRowStatus.setDescription('This object is used to create and\n        delete entries in this table.  When configuring\n        entries in this table, the corresponding ifEntry and\n        mplsInterfaceConfEntry MUST exist beforehand.  If a manager\n        attempts to create an entry for a corresponding\n        mplsInterfaceConfEntry that does not support LC-FR,\n        the agent MUST return an inconsistentValue error.\n        If this table is implemented read-only, then the\n        agent must set this object to active(1) when this\n        row is made active.  If this table is implemented\n        writable, then an agent MUST not allow modification\n        to its objects once this value is set to active(1),\n        except to mplsLcFrStdInterfaceConfRowStatus and\n        mplsLcFrStdInterfaceConfStorageType.')
mplsLcFrStdInterfaceConfStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 10, 1, 1, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcFrStdInterfaceConfStorageType.setDescription("The storage type for this conceptual row.\n        Conceptual rows having the value 'permanent(4)'\n        need not allow write-access to any columnar\n        objects in the row.")
mplsLcFrStdCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1))
mplsLcFrStdGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 2))
mplsLcFrStdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1, 1)).setObjects(*(("MPLS-LC-FR-STD-MIB", "mplsLcFrStdIfGroup"),))
if mibBuilder.loadTexts: mplsLcFrStdModuleFullCompliance.setDescription('Compliance statement for agents that provide\n        full support for MPLS-LC-FR-STD-MIB.  Such\n        devices can be monitored and also be configured\n        using this MIB module.')
mplsLcFrStdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 1, 2)).setObjects(*(("MPLS-LC-FR-STD-MIB", "mplsLcFrStdIfGroup"),))
if mibBuilder.loadTexts: mplsLcFrStdModuleReadOnlyCompliance.setDescription('Compliance requirement for implementations that only\n        provide read-only support for MPLS-LC-FR-STD-MIB.\n        Such devices can be monitored but cannot be configured\n        using this MIB module.\n       ')
mplsLcFrStdIfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 10, 2, 2, 1)).setObjects(*(("MPLS-LC-FR-STD-MIB", "mplsLcFrStdTrafficMinDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdTrafficMaxDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdCtrlMinDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdCtrlMaxDlci"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdInterfaceConfRowStatus"), ("MPLS-LC-FR-STD-MIB", "mplsLcFrStdInterfaceConfStorageType"),))
if mibBuilder.loadTexts: mplsLcFrStdIfGroup.setDescription('Collection of objects needed for MPLS LC-FR\n           interface configuration.')
mibBuilder.exportSymbols("MPLS-LC-FR-STD-MIB", mplsLcFrStdIfGroup=mplsLcFrStdIfGroup, mplsLcFrStdMIB=mplsLcFrStdMIB, mplsLcFrStdModuleReadOnlyCompliance=mplsLcFrStdModuleReadOnlyCompliance, mplsLcFrStdInterfaceConfEntry=mplsLcFrStdInterfaceConfEntry, PYSNMP_MODULE_ID=mplsLcFrStdMIB, mplsLcFrStdCtrlMaxDlci=mplsLcFrStdCtrlMaxDlci, mplsLcFrStdInterfaceConfTable=mplsLcFrStdInterfaceConfTable, mplsLcFrStdObjects=mplsLcFrStdObjects, mplsLcFrStdTrafficMaxDlci=mplsLcFrStdTrafficMaxDlci, mplsLcFrStdCtrlMinDlci=mplsLcFrStdCtrlMinDlci, mplsLcFrStdInterfaceConfStorageType=mplsLcFrStdInterfaceConfStorageType, mplsLcFrStdInterfaceConfRowStatus=mplsLcFrStdInterfaceConfRowStatus, mplsLcFrStdGroups=mplsLcFrStdGroups, mplsLcFrStdNotifications=mplsLcFrStdNotifications, mplsLcFrStdTrafficMinDlci=mplsLcFrStdTrafficMinDlci, mplsLcFrStdModuleFullCompliance=mplsLcFrStdModuleFullCompliance, mplsLcFrStdCompliances=mplsLcFrStdCompliances, mplsLcFrStdConformance=mplsLcFrStdConformance)
