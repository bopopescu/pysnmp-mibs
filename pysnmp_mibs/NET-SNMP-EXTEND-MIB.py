# PySNMP SMI module. Autogenerated from smidump -f python NET-SNMP-EXTEND-MIB
# by libsmi2pysnmp-0.1.2 at Sat Nov 19 23:29:49 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( nsExtensions, ) = mibBuilder.importSymbols("NET-SNMP-AGENT-MIB", "nsExtensions")
( NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, RowStatus, StorageType, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType")

# Objects

netSnmpExtendMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 1, 3, 1)).setRevisions(("2004-05-08 00:00",))
if mibBuilder.loadTexts: netSnmpExtendMIB.setOrganization("www.net-snmp.org")
if mibBuilder.loadTexts: netSnmpExtendMIB.setContactInfo("postal:   Wes Hardaker\nP.O. Box 382\nDavis CA  95617\n\nemail:    net-snmp-coders@lists.sourceforge.net")
if mibBuilder.loadTexts: netSnmpExtendMIB.setDescription("Defines a framework for scripted extensions for the Net-SNMP agent.")
nsExtendObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2))
nsExtendNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendNumEntries.setDescription("The number of rows in the nsExtendConfigTable")
nsExtendConfigTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2))
if mibBuilder.loadTexts: nsExtendConfigTable.setDescription("A table of scripted extensions - configuration and (basic) output.")
nsExtendConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1)).setIndexNames((0, "NET-SNMP-EXTEND-MIB", "nsExtendToken"))
if mibBuilder.loadTexts: nsExtendConfigEntry.setDescription("A conceptual row within the extension table.")
nsExtendToken = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsExtendToken.setDescription("An arbitrary token to identify this extension entry")
nsExtendCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendCommand.setDescription("The full path of the command binary (or script) to run")
nsExtendArgs = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 3), DisplayString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendArgs.setDescription("Any command-line arguments for the command")
nsExtendInput = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 4), DisplayString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendInput.setDescription("The standard input for the command")
nsExtendCacheTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 5), Integer32().clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendCacheTime.setDescription("The length of time for which the output of\nthis command will be cached.  During this time,\nretrieving the output-related values will not\nreinvoke the command.\nA value of -1 indicates that the output results\nshould not be cached at all, and retrieving each\nindividual output-related value will invoke the\ncommand afresh.")
nsExtendExecType = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("exec", 1), ("shell", 2), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendExecType.setDescription("The mechanism used to invoke the command.")
nsExtendRunType = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,2,)).subtype(namedValues=NamedValues(("run-on-read", 1), ("run-on-set", 2), ("run-command", 3), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendRunType.setDescription("Used to implement 'push-button' command invocation.\nThe command for a 'run-on-read' entry will be invoked\nwhenever one of the corresponding output-related\ninstances is requested (and assuming the cached value\nis not still current).\nThe command for a 'run-on-set' entry will only be invoked\non receipt of a SET assignment for this object with the\nvalue 'run-command'.\nReading an instance of this object will always return either\n'run-on-read' or 'run-on-set'.")
nsExtendStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 20), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendStorage.setDescription("The storage type for this conceptual row.")
nsExtendStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 21), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendStatus.setDescription("Used to create new rows in the table, in the standard manner.\nNote that is valid for an instance to be left with the value\nnotInService(2) indefinitely - i.e. the meaning of 'abnormally\nlong' (see RFC 2579, RowStatus) for this table is infinite.")
nsExtendOutput1Table = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3))
if mibBuilder.loadTexts: nsExtendOutput1Table.setDescription("A table of scripted extensions - configuration and (basic) output.")
nsExtendOutput1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1))
if mibBuilder.loadTexts: nsExtendOutput1Entry.setDescription("A conceptual row within the extension table.")
nsExtendOutput1Line = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendOutput1Line.setDescription("The first line of output from the command")
nsExtendOutputFull = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendOutputFull.setDescription("The full output from the command, as a single string")
nsExtendOutNumLines = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendOutNumLines.setDescription("The number of lines of output (and hence\nthe number of rows in nsExtendOutputTable\nrelating to this particular entry).")
nsExtendResult = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendResult.setDescription("The return value of the command.")
nsExtendOutput2Table = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4))
if mibBuilder.loadTexts: nsExtendOutput2Table.setDescription("A table of (line-based) output from scripted extensions.")
nsExtendOutput2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4, 1)).setIndexNames((0, "NET-SNMP-EXTEND-MIB", "nsExtendToken"), (0, "NET-SNMP-EXTEND-MIB", "nsExtendLineIndex"))
if mibBuilder.loadTexts: nsExtendOutput2Entry.setDescription("A conceptual row within the line-based output table.")
nsExtendLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: nsExtendLineIndex.setDescription("The index of this line of output.\nFor a given nsExtendToken, this will run from\n1 to the corresponding value of nsExtendNumLines.")
nsExtendOutLine = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendOutLine.setDescription("A single line of output from the extension command.")
nsExtendGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 3, 3))

# Augmentions
nsExtendConfigEntry.registerAugmentions(("NET-SNMP-EXTEND-MIB", "nsExtendOutput1Entry"))
nsExtendOutput1Entry.setIndexNames(*nsExtendConfigEntry.getIndexNames())

# Groups

nsExtendConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8072, 1, 3, 3, 1)).setObjects(("NET-SNMP-EXTEND-MIB", "nsExtendNumEntries"), ("NET-SNMP-EXTEND-MIB", "nsExtendExecType"), ("NET-SNMP-EXTEND-MIB", "nsExtendCacheTime"), ("NET-SNMP-EXTEND-MIB", "nsExtendInput"), ("NET-SNMP-EXTEND-MIB", "nsExtendStatus"), ("NET-SNMP-EXTEND-MIB", "nsExtendRunType"), ("NET-SNMP-EXTEND-MIB", "nsExtendStorage"), ("NET-SNMP-EXTEND-MIB", "nsExtendArgs"), ("NET-SNMP-EXTEND-MIB", "nsExtendCommand"), )
if mibBuilder.loadTexts: nsExtendConfigGroup.setDescription("Objects relating to the configuration of extension commands.")
nsExtendOutputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8072, 1, 3, 3, 2)).setObjects(("NET-SNMP-EXTEND-MIB", "nsExtendResult"), ("NET-SNMP-EXTEND-MIB", "nsExtendOutNumLines"), ("NET-SNMP-EXTEND-MIB", "nsExtendOutLine"), ("NET-SNMP-EXTEND-MIB", "nsExtendOutput1Line"), ("NET-SNMP-EXTEND-MIB", "nsExtendOutputFull"), )
if mibBuilder.loadTexts: nsExtendOutputGroup.setDescription("Objects relating to the output of extension commands.")

# Exports

# Module identity
mibBuilder.exportSymbols("NET-SNMP-EXTEND-MIB", PYSNMP_MODULE_ID=netSnmpExtendMIB)

# Objects
mibBuilder.exportSymbols("NET-SNMP-EXTEND-MIB", netSnmpExtendMIB=netSnmpExtendMIB, nsExtendObjects=nsExtendObjects, nsExtendNumEntries=nsExtendNumEntries, nsExtendConfigTable=nsExtendConfigTable, nsExtendConfigEntry=nsExtendConfigEntry, nsExtendToken=nsExtendToken, nsExtendCommand=nsExtendCommand, nsExtendArgs=nsExtendArgs, nsExtendInput=nsExtendInput, nsExtendCacheTime=nsExtendCacheTime, nsExtendExecType=nsExtendExecType, nsExtendRunType=nsExtendRunType, nsExtendStorage=nsExtendStorage, nsExtendStatus=nsExtendStatus, nsExtendOutput1Table=nsExtendOutput1Table, nsExtendOutput1Entry=nsExtendOutput1Entry, nsExtendOutput1Line=nsExtendOutput1Line, nsExtendOutputFull=nsExtendOutputFull, nsExtendOutNumLines=nsExtendOutNumLines, nsExtendResult=nsExtendResult, nsExtendOutput2Table=nsExtendOutput2Table, nsExtendOutput2Entry=nsExtendOutput2Entry, nsExtendLineIndex=nsExtendLineIndex, nsExtendOutLine=nsExtendOutLine, nsExtendGroups=nsExtendGroups)

# Groups
mibBuilder.exportSymbols("NET-SNMP-EXTEND-MIB", nsExtendConfigGroup=nsExtendConfigGroup, nsExtendOutputGroup=nsExtendOutputGroup)

