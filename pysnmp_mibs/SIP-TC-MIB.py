# PySNMP SMI module. Autogenerated from smidump -f python SIP-TC-MIB
# by libsmi2pysnmp-0.0.9-alpha at Fri Jul  9 17:12:45 2010,
# Python version sys.version_info(major=2, minor=7, micro=0, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class SipTCEntityRole(Bits):
    namedValues = namedval.NamedValues(("other", 0), ("userAgent", 1), ("proxyServer", 2), ("redirectServer", 3), ("registrarServer", 4), )
    pass

class SipTCMethodName(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,100)
    pass

class SipTCOptionTagHeaders(Bits):
    namedValues = namedval.NamedValues(("require", 0), ("proxyRequire", 1), ("supported", 2), ("unsupported", 3), )
    pass

class SipTCTransportProtocol(Bits):
    namedValues = namedval.NamedValues(("other", 0), ("udp", 1), ("tcp", 2), ("sctp", 3), ("tlsTcp", 4), ("tlsSctp", 5), )
    pass


# Objects

sipTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 148)).setRevisions(("2007-04-20 00:00",))
if mibBuilder.loadTexts: sipTC.setOrganization("IETF Session Initiation Protocol Working Group")
if mibBuilder.loadTexts: sipTC.setContactInfo("SIP WG email: sip@ietf.org\n\nCo-editor  Kevin Lingle\n           Cisco Systems, Inc.\npostal:    7025 Kit Creek Road\n           P.O. Box 14987\n           Research Triangle Park, NC 27709\n           USA\nemail:     klingle@cisco.com\nphone:     +1 919 476 2029\n\nCo-editor  Joon Maeng\nemail:     jmaeng@austin.rr.com\n\nCo-editor  Jean-Francois Mule\n           CableLabs\npostal:    858 Coal Creek Circle\n           Louisville, CO 80027\n           USA\nemail:     jf.mule@cablelabs.com\nphone:     +1 303 661 9100\n\nCo-editor  Dave Walker\nemail:     drwalker@rogers.com")
if mibBuilder.loadTexts: sipTC.setDescription("Session Initiation Protocol (SIP) MIB TEXTUAL-CONVENTION\nmodule used by other SIP-related MIB Modules.\n\nCopyright (C) The IETF Trust (2007).  This version of\nthis MIB module is part of RFC 4780; see the RFC itself for\n\n\n\nfull legal notices.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("SIP-TC-MIB", PYSNMP_MODULE_ID=sipTC)

# Types
mibBuilder.exportSymbols("SIP-TC-MIB", SipTCEntityRole=SipTCEntityRole, SipTCMethodName=SipTCMethodName, SipTCOptionTagHeaders=SipTCOptionTagHeaders, SipTCTransportProtocol=SipTCTransportProtocol)

# Objects
mibBuilder.exportSymbols("SIP-TC-MIB", sipTC=sipTC)
