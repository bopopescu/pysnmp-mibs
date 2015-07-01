#
# PySNMP MIB module INTEGRATED-SERVICES-GUARANTEED-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/INTEGRATED-SERVICES-GUARANTEED-MIB
# Produced by pysmi-0.0.3 at Wed Jul  1 22:29:08 2015
# On host cray platform Linux version 2.6.37.6-smp by user ilya
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( intSrv, ) = mibBuilder.importSymbols("INTEGRATED-SERVICES-MIB", "intSrv")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, RowStatus, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
intSrvGuaranteed = ModuleIdentity((1, 3, 6, 1, 2, 1, 52, 5))
if mibBuilder.loadTexts: intSrvGuaranteed.setOrganization('IETF Integrated Services Working Group')
if mibBuilder.loadTexts: intSrvGuaranteed.setContactInfo('       Fred Baker\n       Postal: Cisco Systems\n               519 Lado Drive\n               Santa Barbara, California 93111\n       Tel:    +1 805 681 0115\n       E-Mail: fred@cisco.com')
if mibBuilder.loadTexts: intSrvGuaranteed.setDescription('The MIB module to describe the Guaranteed Service of\n       the Integrated Services Protocol')
intSrvGuaranteedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 1))
intSrvGuaranteedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 2))
intSrvGuaranteedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3))
intSrvGuaranteedIfTable = MibTable((1, 3, 6, 1, 2, 1, 52, 5, 1, 1), )
if mibBuilder.loadTexts: intSrvGuaranteedIfTable.setDescription("The attributes of the system's interfaces  ex-\n           ported by the Guaranteed Service.")
intSrvGuaranteedIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1), ).setIndexNames((0, "INTEGRATED-SERVICES-GUARANTEED-MIB", "ifIndex"))
if mibBuilder.loadTexts: intSrvGuaranteedIfEntry.setDescription('The reservable attributes of  a  given  inter-\n           face.')
intSrvGuaranteedIfBacklog = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,268435455))).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfBacklog.setDescription('The Backlog  parameter  is  the  data  backlog\n           resulting  from  the vagaries of how a specific\n           implementation deviates from a  strict  bit-by-\n           bit  service.  So, for instance, for packetized\n           weighted fair queueing, Backlog is set  to  the\n           Maximum Packet Size.\n\n           The Backlog term is measured in units of bytes.\n           An  individual  element can advertise a Backlog\n           value between 1 and 2**28 (a  little  over  250\n           megabytes)  and  the  total added over all ele-\n           ments can range as high as  (2**32)-1.   Should\n           the  sum of the different elements delay exceed\n           (2**32)-1, the end-to-end error term should  be\n           (2**32)-1.')
intSrvGuaranteedIfDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,268435455))).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfDelay.setDescription('The Delay parameter at  each  service  element\n           should  be  set  to the maximum packet transfer\n           delay (independent of bucket size) through  the\n           service  element.   For  instance,  in a simple\n           router, one might compute the worst case amount\n           of  time  it  make  take  for a datagram to get\n           through the input interface to  the  processor,\n           and how long it would take to get from the pro-\n           cessor to the outbound interface (assuming  the\n           queueing  schemes work correctly).  For an Eth-\n           ernet, it might represent the worst case  delay\n           if  the maximum number of collisions is experi-\n           enced.\n\n           The Delay term is measured in units of one  mi-\n           crosecond.  An individual element can advertise\n           a delay value between  1  and  2**28  (somewhat\n           over two minutes) and the total delay added all\n           elements  can  range  as  high  as   (2**32)-1.\n           Should  the sum of the different elements delay\n           exceed (2**32)-1, the end-to-end  delay  should\n           be (2**32)-1.')
intSrvGuaranteedIfSlack = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0,268435455))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfSlack.setDescription('If a network element uses a certain amount  of\n           slack,  Si,  to  reduce the amount of resources\n           that it has reserved for a particular flow,  i,\n           the  value  Si  should be stored at the network\n           element.   Subsequently,  if  reservation   re-\n           freshes  are  received  for flow i, the network\n           element must use the same slack Si without  any\n           further computation. This guarantees consisten-\n           cy in the reservation process.\n\n           As an example for the use of  the  slack  term,\n           consider the case where the required end-to-end\n           delay, Dreq, is larger than the  maximum  delay\n           of the fluid flow system.  In this, Ctot is the\n\n           sum of the Backlog terms end to end,  and  Dtot\n           is the sum of the delay terms end to end.  Dreq\n           is obtained by setting R=r in the  fluid  delay\n           formula, and is given by\n\n                        b/r + Ctot/r + Dtot.\n\n           In this case the slack term is\n\n                  S = Dreq - (b/r + Ctot/r + Dtot).\n\n           The slack term may be used by the network  ele-\n           ments  to  adjust  their local reservations, so\n           that they can admit flows that would  otherwise\n           have been rejected. A service element at an in-\n           termediate network element that can  internally\n           differentiate between delay and rate guarantees\n           can now take advantage of this  information  to\n           lower the amount of resources allocated to this\n           flow. For example, by taking an amount of slack\n           s  <= S, an RCSD scheduler [5] can increase the\n           local delay bound, d, assigned to the flow,  to\n           d+s. Given an RSpec, (Rin, Sin), it would do so\n           by setting Rout = Rin and Sout = Sin - s.\n\n           Similarly,  a  network  element  using  a   WFQ\n           scheduler  can  decrease  its local reservation\n           from Rin to Rout by using some of the slack  in\n           the  RSpec.  This  can be accomplished by using\n           the transformation rules given in the  previous\n           section,  that ensure that the reduced reserva-\n           tion level will not increase the  overall  end-\n           to-end delay.')
intSrvGuaranteedIfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 5, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfStatus.setDescription("'valid' on interfaces that are configured  for\n           the Guaranteed Service.")
intSrvGuaranteedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3, 1))
intSrvGuaranteedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 5, 3, 2))
intSrvGuaranteedCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 52, 5, 3, 2, 1)).setObjects(*(("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfAttribGroup"),))
if mibBuilder.loadTexts: intSrvGuaranteedCompliance.setDescription('The compliance statement ')
intSrvGuaranteedIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 5, 3, 1, 2)).setObjects(*(("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfBacklog"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfDelay"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfSlack"), ("INTEGRATED-SERVICES-GUARANTEED-MIB", "intSrvGuaranteedIfStatus"),))
if mibBuilder.loadTexts: intSrvGuaranteedIfAttribGroup.setDescription('These objects are required  for  Systems  sup-\n           porting the Guaranteed Service of the Integrat-\n           ed Services Architecture.')
mibBuilder.exportSymbols("INTEGRATED-SERVICES-GUARANTEED-MIB", intSrvGuaranteedConformance=intSrvGuaranteedConformance, intSrvGuaranteedIfEntry=intSrvGuaranteedIfEntry, intSrvGuaranteedIfBacklog=intSrvGuaranteedIfBacklog, intSrvGuaranteedIfSlack=intSrvGuaranteedIfSlack, intSrvGuaranteedCompliance=intSrvGuaranteedCompliance, intSrvGuaranteed=intSrvGuaranteed, intSrvGuaranteedIfAttribGroup=intSrvGuaranteedIfAttribGroup, PYSNMP_MODULE_ID=intSrvGuaranteed, intSrvGuaranteedIfDelay=intSrvGuaranteedIfDelay, intSrvGuaranteedIfTable=intSrvGuaranteedIfTable, intSrvGuaranteedObjects=intSrvGuaranteedObjects, intSrvGuaranteedGroups=intSrvGuaranteedGroups, intSrvGuaranteedIfStatus=intSrvGuaranteedIfStatus, intSrvGuaranteedNotifications=intSrvGuaranteedNotifications, intSrvGuaranteedCompliances=intSrvGuaranteedCompliances)
