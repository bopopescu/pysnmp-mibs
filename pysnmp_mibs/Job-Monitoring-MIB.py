# PySNMP SMI module. Autogenerated from smidump -f python Job-Monitoring-MIB
# by libsmi2pysnmp-0.0.6-alpha at Thu Apr  6 13:19:24 2006,
# Python version (2, 4, 0, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class JmAttributeTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(90,51,74,175,115,52,93,174,22,6,94,36,23,38,195,70,54,170,171,151,114,8,55,132,1,173,56,150,7,172,113,75,76,112,9,192,190,111,25,95,91,29,34,73,50,152,193,194,31,96,32,26,30,92,4,3,72,5,110,130,21,35,53,20,77,28,71,131,97,33,27,24,191,37,)
    namedValues = namedval.NamedValues(("other", 1), ("impressionsSpooled", 110), ("impressionsSentToDevice", 111), ("impressionsInterpreted", 112), ("impressionsCompletedCurrentCopy", 113), ("fullColorImpressionsCompleted", 114), ("highlightColorImpressionsCompleted", 115), ("pagesRequested", 130), ("pagesCompleted", 131), ("pagesCompletedCurrentCopy", 132), ("sheetsRequested", 150), ("sheetsCompleted", 151), ("sheetsCompletedCurrentCopy", 152), ("mediumRequested", 170), ("mediumConsumed", 171), ("colorantRequested", 172), ("colorantConsumed", 173), ("mediumTypeConsumed", 174), ("mediumSizeConsumed", 175), ("jobSubmissionToServerTime", 190), ("jobSubmissionTime", 191), ("jobStartedBeingHeldTime", 192), ("jobStartedProcessingTime", 193), ("jobCompletionTime", 194), ("jobProcessingCPUTime", 195), ("jobURI", 20), ("jobAccountName", 21), ("serverAssignedJobName", 22), ("jobName", 23), ("jobServiceTypes", 24), ("jobSourceChannelIndex", 25), ("jobSourcePlatformType", 26), ("submittingServerName", 27), ("submittingApplicationName", 28), ("jobOriginatingHost", 29), ("jobStateReasons2", 3), ("deviceNameRequested", 30), ("queueNameRequested", 31), ("physicalDevice", 32), ("numberOfDocuments", 33), ("fileName", 34), ("documentName", 35), ("jobComment", 36), ("documentFormatIndex", 37), ("documentFormat", 38), ("jobStateReasons3", 4), ("jobStateReasons4", 5), ("jobPriority", 50), ("jobProcessAfterDateAndTime", 51), ("jobHold", 52), ("jobHoldUntil", 53), ("outputBin", 54), ("sides", 55), ("finishing", 56), ("processingMessage", 6), ("processingMessageNaturalLangTag", 7), ("printQualityRequested", 70), ("printQualityUsed", 71), ("printerResolutionRequested", 72), ("printerResolutionUsed", 73), ("tonerEcomonyRequested", 74), ("tonerEcomonyUsed", 75), ("tonerDensityRequested", 76), ("tonerDensityUsed", 77), ("jobCodedCharSet", 8), ("jobNaturalLanguageTag", 9), ("jobCopiesRequested", 90), ("jobCopiesCompleted", 91), ("documentCopiesRequested", 92), ("documentCopiesCompleted", 93), ("jobKOctetsTransferred", 94), ("sheetCompletedCopyNumber", 95), ("sheetCompletedDocumentNumber", 96), ("jobCollationType", 97), )
    pass

class JmBooleanTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,2,4,)
    namedValues = namedval.NamedValues(("unknown", 2), ("false", 3), ("true", 4), )
    pass

class JmFinishingTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,2,6,5,1,7,4,)
    namedValues = namedval.NamedValues(("other", 1), ("unknown", 2), ("none", 3), ("staple", 4), ("punch", 5), ("cover", 6), ("bind", 7), )
    pass

class JmJobCollationTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(5,2,1,3,4,)
    namedValues = namedval.NamedValues(("other", 1), ("unknown", 2), ("uncollatedSheets", 3), ("collatedDocuments", 4), ("uncollatedDocuments", 5), )
    pass

class JmJobServiceTypesTC(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class JmJobSourcePlatformTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(10,9,12,2,4,11,3,1,5,7,6,8,)
    namedValues = namedval.NamedValues(("other", 1), ("sptVMS", 10), ("sptWindows", 11), ("sptNetWare", 12), ("unknown", 2), ("sptUNIX", 3), ("sptOS2", 4), ("sptPCDOS", 5), ("sptNT", 6), ("sptMVS", 7), ("sptVM", 8), ("sptOS400", 9), )
    pass

class JmJobStateReasons1TC(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class JmJobStateReasons2TC(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class JmJobStateReasons3TC(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class JmJobStateReasons4TC(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class JmJobStateTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,9,5,6,7,8,4,3,)
    namedValues = namedval.NamedValues(("unknown", 2), ("pending", 3), ("pendingHeld", 4), ("processing", 5), ("processingStopped", 6), ("canceled", 7), ("aborted", 8), ("completed", 9), )
    pass

class JmJobStringTC(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,63)
    pass

class JmJobSubmissionIDTypeTC(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,1)
    pass

class JmMediumTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(12,13,2,11,5,9,8,1,6,4,3,10,7,)
    namedValues = namedval.NamedValues(("other", 1), ("tabStock", 10), ("multiPartForm", 11), ("labels", 12), ("multiLayer", 13), ("unknown", 2), ("stationery", 3), ("transparency", 4), ("envelope", 5), ("envelopePlain", 6), ("envelopeWindow", 7), ("continuousLong", 8), ("continuousShort", 9), )
    pass

class JmNaturalLanguageTagTC(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,63)
    pass

class JmPrintQualityTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,2,5,1,3,)
    namedValues = namedval.NamedValues(("other", 1), ("unknown", 2), ("draft", 3), ("normal", 4), ("high", 5), )
    pass

class JmPrinterResolutionTC(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(9,9)
    pass

class JmTimeStampTC(Integer32):
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(0,2147483647L)
    pass

class JmTonerEconomyTC(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(4,3,2,)
    namedValues = namedval.NamedValues(("unknown", 2), ("off", 3), ("on", 4), )
    pass

class JmUTF8StringTC(TextualConvention, OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,63)
    pass


# Objects

pwg = MibIdentifier((1, 3, 6, 1, 4, 1, 2699))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1))
jobmonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2699, 1, 1)).setRevisions(("1999-02-19 00:00",))
jobmonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1))
jmGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1))
jmGeneralTable = MibTable((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1))
jmGeneralEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1)).setIndexNames((0, "Job-Monitoring-MIB", "jmGeneralJobSetIndex"))
jmGeneralJobSetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 32767))).setMaxAccess("noaccess")
jmGeneralNumberOfActiveJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readonly")
jmGeneralOldestActiveJobIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readonly")
jmGeneralNewestActiveJobIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readonly")
jmGeneralJobPersistence = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(15, 2147483647L)).clone(60)).setMaxAccess("readonly")
jmGeneralAttributePersistence = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(15, 2147483647L)).clone(60)).setMaxAccess("readonly")
jmGeneralJobSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 7), JmUTF8StringTC().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63)).clone('')).setMaxAccess("readonly")
jmJobID = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2))
jmJobIDTable = MibTable((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1))
jmJobIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1)).setIndexNames((0, "Job-Monitoring-MIB", "jmJobSubmissionID"))
jmJobSubmissionID = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(48, 48))).setMaxAccess("noaccess")
jmJobIDJobSetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 32767)).clone(0)).setMaxAccess("readonly")
jmJobIDJobIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 2147483647L)).clone(0)).setMaxAccess("readonly")
jmJob = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3))
jmJobTable = MibTable((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1))
jmJobEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1)).setIndexNames((0, "Job-Monitoring-MIB", "jmGeneralJobSetIndex"), (0, "Job-Monitoring-MIB", "jmJobIndex"))
jmJobIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
jmJobState = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 2), JmJobStateTC()).setMaxAccess("readonly")
jmJobStateReasons1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 3), JmJobStateReasons1TC()).setMaxAccess("readonly")
jmNumberOfInterveningJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L)).clone(0)).setMaxAccess("readonly")
jmJobKOctetsPerCopyRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L)).clone(-2)).setMaxAccess("readonly")
jmJobKOctetsProcessed = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L)).clone(0)).setMaxAccess("readonly")
jmJobImpressionsPerCopyRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L)).clone(-2)).setMaxAccess("readonly")
jmJobImpressionsCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L)).clone(0)).setMaxAccess("readonly")
jmJobOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 9), JmJobStringTC().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63)).clone('')).setMaxAccess("readonly")
jmAttribute = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4))
jmAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1))
jmAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1)).setIndexNames((0, "Job-Monitoring-MIB", "jmGeneralJobSetIndex"), (0, "Job-Monitoring-MIB", "jmJobIndex"), (0, "Job-Monitoring-MIB", "jmAttributeTypeIndex"), (0, "Job-Monitoring-MIB", "jmAttributeInstanceIndex"))
jmAttributeTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 1), JmAttributeTypeTC()).setMaxAccess("noaccess")
jmAttributeInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 32767))).setMaxAccess("noaccess")
jmAttributeValueAsInteger = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(-2, 2147483647L)).clone(-2)).setMaxAccess("readonly")
jmAttributeValueAsOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 63)).clone('')).setMaxAccess("readonly")
jobmonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 2))
jmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3))
jmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2))

# Augmentions

# Groups

jmJobIDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 2)).setObjects(("Job-Monitoring-MIB", "jmJobIDJobSetIndex"), ("Job-Monitoring-MIB", "jmJobIDJobIndex"), )
jmJobGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 3)).setObjects(("Job-Monitoring-MIB", "jmJobImpressionsCompleted"), ("Job-Monitoring-MIB", "jmJobImpressionsPerCopyRequested"), ("Job-Monitoring-MIB", "jmNumberOfInterveningJobs"), ("Job-Monitoring-MIB", "jmJobKOctetsProcessed"), ("Job-Monitoring-MIB", "jmJobStateReasons1"), ("Job-Monitoring-MIB", "jmJobOwner"), ("Job-Monitoring-MIB", "jmJobKOctetsPerCopyRequested"), ("Job-Monitoring-MIB", "jmJobState"), )
jmGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 1)).setObjects(("Job-Monitoring-MIB", "jmGeneralJobPersistence"), ("Job-Monitoring-MIB", "jmGeneralJobSetName"), ("Job-Monitoring-MIB", "jmGeneralOldestActiveJobIndex"), ("Job-Monitoring-MIB", "jmGeneralNumberOfActiveJobs"), ("Job-Monitoring-MIB", "jmGeneralAttributePersistence"), ("Job-Monitoring-MIB", "jmGeneralNewestActiveJobIndex"), )
jmAttributeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 4)).setObjects(("Job-Monitoring-MIB", "jmAttributeValueAsOctets"), ("Job-Monitoring-MIB", "jmAttributeValueAsInteger"), )

# Exports

# Module identity
mibBuilder.exportSymbols("Job-Monitoring-MIB", PYSNMP_MODULE_ID=jobmonMIB)

# Types
mibBuilder.exportSymbols("Job-Monitoring-MIB", JmAttributeTypeTC=JmAttributeTypeTC, JmBooleanTC=JmBooleanTC, JmFinishingTC=JmFinishingTC, JmJobCollationTypeTC=JmJobCollationTypeTC, JmJobServiceTypesTC=JmJobServiceTypesTC, JmJobSourcePlatformTypeTC=JmJobSourcePlatformTypeTC, JmJobStateReasons1TC=JmJobStateReasons1TC, JmJobStateReasons2TC=JmJobStateReasons2TC, JmJobStateReasons3TC=JmJobStateReasons3TC, JmJobStateReasons4TC=JmJobStateReasons4TC, JmJobStateTC=JmJobStateTC, JmJobStringTC=JmJobStringTC, JmJobSubmissionIDTypeTC=JmJobSubmissionIDTypeTC, JmMediumTypeTC=JmMediumTypeTC, JmNaturalLanguageTagTC=JmNaturalLanguageTagTC, JmPrintQualityTC=JmPrintQualityTC, JmPrinterResolutionTC=JmPrinterResolutionTC, JmTimeStampTC=JmTimeStampTC, JmTonerEconomyTC=JmTonerEconomyTC, JmUTF8StringTC=JmUTF8StringTC)

# Objects
mibBuilder.exportSymbols("Job-Monitoring-MIB", pwg=pwg, mibs=mibs, jobmonMIB=jobmonMIB, jobmonMIBObjects=jobmonMIBObjects, jmGeneral=jmGeneral, jmGeneralTable=jmGeneralTable, jmGeneralEntry=jmGeneralEntry, jmGeneralJobSetIndex=jmGeneralJobSetIndex, jmGeneralNumberOfActiveJobs=jmGeneralNumberOfActiveJobs, jmGeneralOldestActiveJobIndex=jmGeneralOldestActiveJobIndex, jmGeneralNewestActiveJobIndex=jmGeneralNewestActiveJobIndex, jmGeneralJobPersistence=jmGeneralJobPersistence, jmGeneralAttributePersistence=jmGeneralAttributePersistence, jmGeneralJobSetName=jmGeneralJobSetName, jmJobID=jmJobID, jmJobIDTable=jmJobIDTable, jmJobIDEntry=jmJobIDEntry, jmJobSubmissionID=jmJobSubmissionID, jmJobIDJobSetIndex=jmJobIDJobSetIndex, jmJobIDJobIndex=jmJobIDJobIndex, jmJob=jmJob, jmJobTable=jmJobTable, jmJobEntry=jmJobEntry, jmJobIndex=jmJobIndex, jmJobState=jmJobState, jmJobStateReasons1=jmJobStateReasons1, jmNumberOfInterveningJobs=jmNumberOfInterveningJobs, jmJobKOctetsPerCopyRequested=jmJobKOctetsPerCopyRequested, jmJobKOctetsProcessed=jmJobKOctetsProcessed, jmJobImpressionsPerCopyRequested=jmJobImpressionsPerCopyRequested, jmJobImpressionsCompleted=jmJobImpressionsCompleted, jmJobOwner=jmJobOwner, jmAttribute=jmAttribute, jmAttributeTable=jmAttributeTable, jmAttributeEntry=jmAttributeEntry, jmAttributeTypeIndex=jmAttributeTypeIndex, jmAttributeInstanceIndex=jmAttributeInstanceIndex, jmAttributeValueAsInteger=jmAttributeValueAsInteger, jmAttributeValueAsOctets=jmAttributeValueAsOctets, jobmonMIBNotifications=jobmonMIBNotifications, jmMIBConformance=jmMIBConformance, jmMIBGroups=jmMIBGroups)

# Groups
mibBuilder.exportSymbols("Job-Monitoring-MIB", jmJobIDGroup=jmJobIDGroup, jmJobGroup=jmJobGroup, jmGeneralGroup=jmGeneralGroup, jmAttributeGroup=jmAttributeGroup)
