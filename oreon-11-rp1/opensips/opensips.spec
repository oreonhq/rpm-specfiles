%global source0_hash 5e268186500a6a1f5db7379e90d7e32a26f46752ebeba583c148662631bffed4
%global git_commit 2367deb8e2c408a2d38e90d80b5a9580dbdff959
%global EXCLUDE_MODULES cachedb_cassandra cachedb_dynamodb %{!?_with_oracle:db_oracle} event_sqs example launch_darkly osp rtp.io sngtc tls_wolfssl
Summary:        Open Source SIP Server
Name:     opensips
Version:  4.0.2
Release:        1%{?dist}
License:  GPL-2.0-or-later
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source3:  opensips.sysusers
Patch: opensips-0001-Consistently-use-rtpproxy-switches.patch
Patch: opensips-0002-Cleanup-Oracle-s-makefiles.patch
Patch: opensips-0003-db_ora-null-terminating-string-is-more-safely-most-m.patch
Patch: opensips-0004-Return-actual-payload-ID-in-case-of-a-dynamic-payloa.patch
Patch: opensips-0005-Fix-rabbitmq-c-deprecated-header-warnings.patch
Patch: opensips-0006-Fix-uninitialized-variable-warnings-in-SQL-API-funct.patch
Patch: opensips-0007-Fix-const-correctness-warnings-in-HTTP-and-FreeSWITC.patch
Patch: opensips-0008-Fix-uninitialized-va_list-warning-on-ppc64le-and-i68.patch
Patch: opensips-0009-Fix-format-specifier-warnings-on-32-bit-architecture.patch
Patch: opensips-0010-Fix-pointer-truncation-warning-on-32-bit-architectur.patch
Patch: opensips-0011-Fix-C90-style-declaration-warnings-in-snmpstats-modu.patch
URL:      https://opensips.org
Requires(post): systemd
Requires(preun): systemd
Obsoletes: %{name}-auth_diameter < 2.2.2
Obsoletes: %{name}-event_datagram < 1.9.1
Obsoletes: %{name}-event_jsonrpc < 3.1.0
Obsoletes: %{name}-seas < 3.1.0
Obsoletes: %{name}-sms < 3.1.0
# oreon:deps
BuildRequires:  GeoIP-devel
BuildRequires:  bison
BuildRequires:  compat-lua-devel
BuildRequires:  curl-devel
BuildRequires:  docbook-xsl
BuildRequires:  expat-devel
BuildRequires:  flex
BuildRequires:  freeDiameter-devel
BuildRequires:  gcc
BuildRequires:  hiredis-devel
BuildRequires:  json-c-devel
BuildRequires:  libconfuse-devel
BuildRequires:  libcouchbase-devel
BuildRequires:  libdb-devel
BuildRequires:  libevent-devel
BuildRequires:  libjwt-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  libmemcached-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libmnl-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libpq-devel
BuildRequires:  librabbitmq-devel
BuildRequires:  librdkafka-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  lksctp-tools-devel
BuildRequires:  lynx
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  mongo-c-driver-devel
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openldap-devel
BuildRequires:  pcre-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(openssl)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  radcli-devel
BuildRequires:  snappy-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd-units
BuildRequires:  unixODBC-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
OpenSIPS or Open SIP Server is a very fast and flexible SIP (RFC3261)
proxy server. Written entirely in C, opensips can handle thousands calls
per second even on low-budget hardware. A C Shell like scripting language
provides full control over the server's behaviour. It's modular
architecture allows only required functionality to be loaded.
Currently the following modules are available: digest authentication,
CPL scripts, instant messaging, MySQL and UNIXODBC support, a presence agent,
radius authentication, record routing, an SMS gateway, a jabber gateway, a
transaction and dialog module, OSP module, statistics support,
registrar and user location.

%package  aaa_diameter
Summary:  Diameter backend for AAA API
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: freeDiameter-devel
%description aaa_diameter
This module provides the Diameter backend for the AAA API - group, auth, uri
module use the AAA API for performing Diameter ops.

%package  aaa_radius
Summary:  RADIUS backend for AAA API
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: radcli-devel
%description aaa_radius
This module provides the RADIUS backend for the AAA API - group, auth, uri
module use the AAA API for performing RADIUS ops.

%package  acc
Summary:  Accounts transactions information to different backends
Requires: %{name}%{?_isa} = %{version}-%{release}
%description acc
ACC module is used to account transactions information to different backends
like syslog, SQL, AAA.

%package  aka_av_diameter
Summary:  Diameter AKA AV Manager
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-aaa_diameter%{?_isa} = %{version}-%{release}
%description aka_av_diameter
This module is an extension to the AKA_AUTH module providing a Diameter AKA AV
Manager that implements the Multimedia-Auth-Request and Multimedia-Auth-Answer
Diameter commands defined in the Cx interface of the ETSI TS 129 229
specifications in order to fetch a set of authentication vectors and feed them
in the AKA authentication process.

%package  auth_aaa
Summary:  Performs authentication using an AAA server
Requires: %{name}%{?_isa} = %{version}-%{release}
%description auth_aaa
This module contains functions that are used to perform authentication using
an AAA server.  Basically the proxy will pass along the credentials to the
AAA server which will in turn send a reply containing result of the
authentication. So basically the whole authentication is done in the AAA
server.

%package  auth_jwt
Summary:  Performs authentication over JSON Web Tokens
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libjwt-devel
BuildRequires: pkgconfig(openssl)
%description auth_jwt
The module implements authentication over JSON Web Tokens. Any database module
(currently mysql, postgres, dbtext), must be loaded before this module in case
the db_url parameter is set.

%package  b2bua
Summary:  Back-2-Back User Agent
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
%description b2bua
B2BUA is an implementation of the behavior of a B2BUA as defined in RFC 3261
that offers the possibility to build certain services on top of it.

%package  cachedb_couchbase
Summary:  Couchbase connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libcouchbase-devel
%description cachedb_couchbase
Couchbase module is an implementation of a cache system designed to
work with a Couchbase server.

%package  cachedb_memcached
Summary:  Memcached connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-memcached%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-memcached < 1.11.6
BuildRequires: libmemcached-devel
%description cachedb_memcached
Memcached module is an implementation of a cache system designed to
work with a memcached server.

%package  cachedb_mongodb
Summary:  MongoDB connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: json-c-devel
BuildRequires: mongo-c-driver-devel
BuildRequires: snappy-devel
%description cachedb_mongodb
MongoDB module is an implementation of a cache system designed to
work with a MongoDB server.

%package  cachedb_redis
Summary:  Redis connector for cache subsystem
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-redis%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-redis < 1.11.6
BuildRequires: hiredis-devel
%description cachedb_redis
This module is an implementation of a cache system designed to work
with a Redis server.

%package  call_center
Summary:  An inbound call center system
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}
%description call_center
The Call Center module implements an inbound call center system with call flows
(for queueing the received calls) and agents (for answering the calls).

%package  carrierroute
Summary:  Routing extension suitable for carriers
BuildRequires: libconfuse-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description carrierroute
A module which provides routing, balancing and blacklisting capabilities.

%package  cgrates
Summary:  Billing module for CGRates engine
Requires: %{name}%{?_isa} = %{version}-%{release}
%description cgrates
This module can be used to communicate with the CGRates engine in order to do
call authorization and accounting for billing purposes. The OpenSIPS module
does not do any billing by itself, but provides an interface to communicate
with the CGRateS engine using efficient JSON-RPC APIs in both synchronous and
asynchronous ways.

%package  compression
Summary:  Message compression/decompression and base64 encoding
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: zlib-devel
%description compression
This module provides message compression/decompression and base64 encoding for
sip messages using deflate and gzip algorithm/headers. Another feature of this
module is reducing headers to compact for as specified in SIP RFC's, sdp body
codec unnecessary description removal (for codecs 0-97), whitelist for headers
not be removed (excepting necessary headers).

%package  cpl_c
Summary:  Call Processing Language interpreter
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-cpl-c%{?_isa} = %{version}-%{release}
Provides: %{name}-cpl-c = %{version}-%{release}
Obsoletes:%{name}-cpl-c < 2.2.2-1
%description cpl_c
This module implements a CPL (Call Processing Language) interpreter.
Support for uploading/downloading/removing scripts via SIP REGISTER method
is present.

%package  db_berkeley
Summary:  Berkeley DB backend support
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libdb-devel
%description db_berkeley
This is a module which integrates the Berkeley DB into OpenSIPS. It implements
the DB API defined in OpenSIPS.

%package  db_http
Summary:  HTTP DB backend support
Requires: %{name}%{?_isa} = %{version}-%{release}
%description db_http
This module provides access to a database that is implemented as a
HTTP server.

%package  db_mysql
Summary:  MySQL storage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-mysql%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-mysql < 1.11.6
BuildRequires: mariadb-connector-c-devel
%description db_mysql
This module contains the MySQL plugin for %{name}, which allows
a MySQL database to be used for persistent storage.

%if 0%{?_with_oracle}
%package  db_oracle
Summary:  Oracle storage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-oracle%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-oracle < 1.11.6
BuildRequires: oracle-instantclient-devel
%description db_oracle
This module package contains the Oracle plugin for %{name}, which allows
a Oracle database to be used for persistent storage.
%endif

%package  db_perlvdb
Summary:  Perl virtual database engine
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-perl%{?_isa} = %{version}-%{release}
Provides: %{name}-perlvdb%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-perlvdb < 1.11.6
%description db_perlvdb
The Perl Virtual Database (VDB) provides a virtualization framework for
OpenSIPS's database access. It does not handle a particular database engine
itself but lets the user relay database requests to arbitrary Perl functions.

%package  db_postgresql
Summary:  PostgreSQL storage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-postgresql%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-postgresql < 1.11.6
BuildRequires: libpq-devel
%description db_postgresql
This module contains the PostgreSQL plugin for %{name},
which allows a PostgreSQL database to be used for persistent storage.

%package  db_sqlite
Summary:  SQLite sorage support for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: sqlite-devel
%description db_sqlite
This module contains the SQLite plugin for %{name}, which
allows SQLite to be used for persistent storage.

%package  db_unixodbc
Summary:  OpenSIPS unixODBC Storage support
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-unixodbc%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-unixodbc < 1.11.6
BuildRequires: unixODBC-devel
%description db_unixodbc
This module contains the unixODBC plugin for %{name}, which
allows unixODBC to be used for persistent storage.

%package  event_kafka
Summary:  Event Kafka module
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librdkafka-devel
%description event_kafka
This module provides the implementation of a Kafka client for the Event
Interface. It is used to send AMQP messages to a Kafka server each time the
Event Interface triggers an event subscribed for.

%package  event_rabbitmq
Summary:  Event RabbitMQ module
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel
Obsoletes: %{name}-rabbitmq < 3.6.0
%description event_rabbitmq
This module provides the implementation of a RabbitMQ client for the Event Interface.
It is used to send AMQP messages to a RabbitMQ server each time the Event Interface
triggers an event subscribed for.

%package  emergency
Summary:  Emergency call treatment
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
%description emergency
This module provides emergency call treatment for OpenSIPS, following the
architecture i2 specification of the American entity NENA. (National Emergency
Number Association).

%package  h350
Summary:  H350 implementation
BuildRequires: openldap-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description h350
The OpenSIPS H350 module enables an OpenSIPS SIP proxy server to access SIP
account data stored in an LDAP [RFC4510] directory  containing H.350 [H.350]
commObjects.

%package  httpd
Summary:  HTTP transport layer implementation
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libmicrohttpd-devel
%description httpd
This module provides an HTTP transport layer for OpenSIPS.

%package  http2d
Summary:  HTTP/2 server implementation
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: libnghttp2-devel
BuildRequires: libevent-devel
%description http2d
This module provides an RFC 7540/9113 HTTP/2 server implementation with "h2"
ALPN support.

%package  identity
Summary:  Support for SIP Identity (see RFC 4474)
BuildRequires: pkgconfig(openssl)
Requires: %{name}%{?_isa} = %{version}-%{release}
%description identity
This module provides support for SIP Identity (see RFC 4474).

%package  jabber
Summary:  Gateway between OpenSIPS and a jabber server
BuildRequires: expat-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description jabber
Jabber module that integrates XODE XML parser for parsing Jabber messages.

%package  json
Summary:  A JSON variables within the script
BuildRequires: json-c-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description json
This module introduces a new type of variable that provides both serialization and
de-serialization from JSON format.

%package  ldap
Summary:  LDAP connector
BuildRequires: openldap-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description ldap
The LDAP module implements an LDAP search interface for OpenSIPS.

%package  lua
Summary:  Helps implement your own OpenSIPS extensions in Lua
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: compat-lua-devel
BuildRequires: libmemcached-devel
%description lua
The time needed when writing a new OpenSIPS module unfortunately is quite
high, while the options provided by the configuration file are limited to
the features implemented in the modules. With this Lua module, you can
easily implement your own OpenSIPS extensions in Lua.

%package  media_exchange
Summary:  Lets exchange SDP between calls
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}
%description media_exchange
This module provides the means to exchange media SDP between different SIP
proxied calls, and calls started or received from a Media Server. The module
itself does not have any media capabilities, it simply exposes primitives to
exchange the SDP body between two or more different calls.

The module can both originate calls, pushing an existing SDP to a media server,
to playback, or simply record an existing RTP, as well as take the SDP of a new
call and inject the SDP into an existing, proxied sip call. In order to
manipulate the new calls, either generated, or terminated, the module behaves
as a back-to-back user agent with the aim of the OpenSIPS B2B entities module.

%package  mi_html
Summary:  A minimal web user interface for the Management Interface
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}
%description mi_html
This module implements a minimal web user interface for the OpenSIPS's
Management Interface.

%package  mi_http
Summary:  A JSON REST interface for the Management Interface
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}
%description mi_http
This module implements a JSON server for the Management Interface that handles
GET requests and generates JSON responses.

%package  mi_xmlrpc_ng
Summary:  A xmlrpc server for the Management Interface (new version)
BuildRequires: libxml2-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}
Provides: %{name}-xmlrpc_ng%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-mi_xmlrpc_ng < 2.2.2
Obsoletes: %{name}-xmlrpc_ng < 1.11.6
Obsoletes: %{name}-xmlrpc < 1.11.6
%description mi_xmlrpc_ng
This module implements a xmlrpc server that handles xmlrpc requests and generates
xmlrpc responses. When a xmlrpc message is received a default method is executed.

%package  mmgeoip
Summary:  Wrapper for the MaxMind GeoIP API
BuildRequires: GeoIP-devel
BuildRequires: libmaxminddb-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description mmgeoip
Mmgeoip is a lightweight wrapper for the MaxMind GeoIP API. It adds
IP address-to-location lookup capability to OpenSIPS scripts.

%package  msrp
Summary:  MSRP support
BuildRequires: pkgconfig(openssl)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_mgm%{?_isa} = %{version}-%{release}
%description msrp
This module provides the MSRP support for OpenSIPS. This includes MSRP UA, MSRP
gateway between SIP MESSAGE and MSRP, MSRP relay as describned in RFC 4976.

%package  peering
Summary:  Radius peering
Requires: %{name}%{?_isa} = %{version}-%{release}
%description peering
Peering module allows SIP providers (operators or organizations)
to verify from a broker if source or destination  of a SIP request
is a trusted peer.

%package  perl
Summary:  Helps implement your own OpenSIPS extensions in Perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Embed), perl-devel
BuildRequires: perl-generators
Requires: %{name}%{?_isa} = %{version}-%{release}
%description perl
The time needed when writing a new OpenSIPS module unfortunately is quite
high, while the options provided by the configuration file are limited to
the features implemented in the modules. With this Perl module, you can
easily implement your own OpenSIPS extensions in Perl.  This allows for
simple access to the full world of CPAN modules. SIP URI rewriting could be
implemented based on regular expressions; accessing arbitrary data backends,
e.g. LDAP or Berkeley DB files, is now extremely simple.

%package  pi_http
Summary:  A HTTP provisioning interface for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}
%description pi_http
This module provides an HTTP provisioning interface for OpenSIPS. It is using
the OpenSIPS's internal database API to provide a simple way of manipulating
records inside OpenSIPS's tables.

%package  presence
Summary:  Presence server
Requires: %{name}%{?_isa} = %{version}-%{release}
%description presence
This module implements a presence server. It handles PUBLISH and SUBSCRIBE
messages and generates NOTIFY messages. It offers support for aggregation
of published presence information for the same presentity using more devices.
It can also filter the information provided to watchers according to privacy
rules.

%package  presence_callinfo
Summary:  SIMPLE Presence extension
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
%description presence_callinfo
The module enables the handling of "call-info" and "line-seize" events inside
the presence module. It is used with the general event handling module:
presence and it constructs and adds "Call-Info" headers to notification events.
To send "call-info" notification to watchers, a third-party application must
publish "call-info" events to the presence server.

%package  presence_dfks
Summary:  Extension to Presence server for Broadsoft's DFKS
BuildRequires: libxml2-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
%description presence_dfks
The module enables handling of the "as-feature-event" event package (as defined
by Broadsoft's Device Feature Key Synchronization protocol) by the presence
module.

%package  presence_dialoginfo
Summary:  Extension to Presence server for Dialog-Info
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
%description presence_dialoginfo
The module enables the handling of "Event: dialog" (as defined
in RFC 4235) inside of the presence module. This can be used
distribute the dialog-info status to the subscribed watchers.

%package  presence_mwi
Summary:  Extension to Presence server for Message Waiting Indication
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
%description presence_mwi
The module does specific handling for notify-subscribe message-summary
(message waiting indication) events as specified in RFC 3842. It is used
with the general event handling module, presence. It constructs and adds
message-summary event to it.

%package  presence_reginfo
Summary:  Handles of "Event: reg" inside of the presence module
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
%description presence_reginfo
The module enables the handling of "Event: reg" (as defined in RFC 3680) inside
of the presence module. This can be used distribute the registration-info
status to the subscribed watchers.

%package  presence_xcapdiff
Summary:  Extension to Presence server for XCAP-DIFF event
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-pua_mi%{?_isa} = %{version}-%{release}
%description presence_xcapdiff
The presence_xcapdiff is an OpenSIPS module that adds support
for the "xcap-diff" event to presence and pua.

%package  presence_xml
Summary:  SIMPLE Presence extension
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-xcap_client%{?_isa} = %{version}-%{release}
%description presence_xml
The module does specific handling for notify-subscribe events using xml bodies.
It is used with the general event handling module, presence.

%package  prometheus
Summary:  A HTTP interface for the Prometheus monitoring system
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-httpd%{?_isa} = %{version}-%{release}
%description prometheus
This module provides a HTTP interface for the Prometheus monitoring system,
allowing it to fetch different statistics from OpenSIPS.

%package  proto_bins
Summary:  A secure Binary clustering protocol
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_mgm%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-tlsops < 2.2.2
%description proto_bins
This module provides a secure Binary communication protocol
over TLS, to be used by the OpenSIPS clustering engine provided
by the clusterer module.

%package  proto_ipsec
Summary:  IPSec sockets for establishing secure communication channels
BuildRequires: libmnl-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description proto_ipsec
This module provides IPSec sockets for establishing secure communication
channels. It relies on RFC 3329 (Security Mechanism Agreement for the Session
Initiation Protocol (SIP)) to establish the IPSec parameters necessary for
creating dynamic Security Associations (SAs) for each connection.

%package  proto_sctp
Summary:  An optional SCTP transport module
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: lksctp-tools-devel
%description proto_sctp
This module is an optional transport module (shared library) which exports the
required logic in order to handle SCTP-based communication. (socket
initialization and send/recv primitives to be used by higher-level network
layers). Once loaded, you will be able to define "sctp:" listeners in your
script.

%package  proto_tls
Summary:  An optional TLS transport module
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_mgm%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-tlsops < 2.2.2
%description proto_tls
This module is an optional transport module (shared library) which exports the
required logic in order to handle TLS-based communication. (socket
initialization and send/recv primitives to be used by higher-level network
layers). Once loaded, you will be able to define "tls:" listeners in your
script.

%package  proto_wss
Summary:  An optional Secure WebSocket transport module
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_mgm%{?_isa} = %{version}-%{release}
%description proto_wss
This module is an optional transport module (shared library) which exports the
required logic in order to handle Secure WebSocket-based communication. (socket
initialization and send/recv primitives to be used by higher-level network
layers). Once loaded, you will be able to define "wss:" listeners in your
script.

%package  pua
Summary:  Offer the functionality of a presence user agent client
Requires: %{name}%{?_isa} = %{version}-%{release}
%description pua
This module offer the functionality of a presence user agent client, sending
Subscribe and Publish messages.

%package  pua_bla
Summary:  BLA extension for PUA
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
%description pua_bla
The pua_bla module enables Bridged Line Appearances support according to the
specifications in draft-anil-sipping-bla-03.txt.

%package  pua_dialoginfo
Summary:  Dialog-Info extension for PUA
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
%description pua_dialoginfo
The pua_dialoginfo retrieves dialog state information from the dialog module
and PUBLISHes the dialog-information using the pua module. Thus, in combination
with the presence_xml module this can be used to derive dialog-info from the
dialog module and NOTIFY the subscribed watchers about dialog-info changes.

%package  pua_mi
Summary:  Connector between usrloc and MI interface
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
%description pua_mi
The pua_mi sends offer the possibility to publish presence information
via MI transports.  Using this module you can create independent
applications/scripts to publish not sip-related information (e.g., system
resources like CPU-usage, memory, number of active subscribers ...)

%package  pua_reginfo
Summary:  Publishes information about "reg"-events according to to RFC 3680
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
%description pua_reginfo
This module publishes information about "reg"-events according to to RFC 3680.
This can be used distribute the registration-info status to the subscribed
watchers.

This module "PUBLISH"es information when a new user registers at this server
(e.g. when "save()" is called) to users, which have subscribed for the reg-info
for this user.

This module can "SUBSCRIBE" for information at another server, so it will
receive "NOTIFY"-requests, when the information about a user changes.

And finally, it can process received "NOTIFY" requests and it will update the
local registry accordingly.

%package  pua_usrloc
Summary:  Connector between usrloc and pua modules
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
%description pua_usrloc
This module is the connector between usrloc and pua modules. It creates the
environment to send PUBLISH requests for user location records, on specific
events (e.g., when new record is added in usrloc, a PUBLISH with status open
(online) is issued; when expires, it sends closed (offline)). Using this
module, phones which have no support for presence can be seen as
online/offline.

%package  pua_xmpp
Summary:  SIMPLE-XMPP Presence gateway
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-xmpp%{?_isa} = %{version}-%{release}
%description pua_xmpp
This module is a gateway for presence between SIP and XMPP. It translates one
format into another and uses xmpp, pua and presence modules to manage the
transmition of presence state information.

%package  -n python3-opensips
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < 2.4.6-4
Obsoletes: python2-%{name} < 2.4.6-4
Summary:  Python scripting support
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n python3-opensips
Helps implement your own OpenSIPS extensions in Python

%package  rabbitmq_consumer
Summary:  RabbitMQ message receiver
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: librabbitmq-devel
%description rabbitmq_consumer
This module allows managing received messages in queues, taking advantage of
the flexible AMQP protocol.

%package  regex
Summary:  RegExp via PCRE library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description regex
This module offers matching operations against regular
expressions using the powerful PCRE library.

%package  rest_client
Summary:  HTTP client module for OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
%description rest_client
This module provides a means of interacting with an HTTP server by doing
RESTful queries, such as GET and POST.

%package  rls
Summary:  Resource List Server
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-pua%{?_isa} = %{version}-%{release}
Requires: %{name}-presence%{?_isa} = %{version}-%{release}
Requires: %{name}-xcap%{?_isa} = %{version}-%{release}
%description rls
The modules is a Resource List Server implementation following the
specification in RFC 4662 and RFC 4826.

%package  siprec
Summary:  Call recording using SIPREC protocol
BuildRequires: libuuid-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}
%description siprec
This module provides the means to do calls recording using an external recorder
- the entity that records the call is not in the media path between the caller
and callee, but it is completely separate, thus it can not affect by any means
the quality of the conversation. This is done in a standardized manner, using
the SIPREC Protocol, thus it can be used by any recorder that implements this
protocol.

%package  snmpstats
Summary:  SNMP management interface for the OpenSIPS
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: net-snmp-devel
%description snmpstats
The %{name}-snmpstats package provides an SNMP management interface to
OpenSIPS.  Specifically, it provides general SNMP queryable scalar statistics,
table representations of more complicated data such as user and contact
information, and alarm monitoring capabilities.

%package  stir_shaken
Summary:  Support for implementing STIR/SHAKEN
BuildRequires: pkgconfig(openssl)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-b2bua%{?_isa} = %{version}-%{release}
%description stir_shaken
This module provides support for implementing STIR/SHAKEN (RFC 8224, RFC 8588)
Authentication and Verification services in OpenSIPS.

%package  tls_mgm
Summary:  Management for TLS certificates and parameters
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tls_openssl%{?_isa} = %{version}-%{release}
%description tls_mgm
This module provides an interfaces for all the modules that use the TLS
protocol. It also implements TLS related functions to use in the routing
script, and exports pseudo variables with certificate and TLS parameters.

%package  tls_openssl
Summary:  OpenSSL low level API for tls_mgm module
BuildRequires: pkgconfig(openssl)
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tls_openssl
This module provides an OpenSSL backend for tls_mgm module.

%package  uuid
Summary:  Generates UUIDs as specified in RFC 4122
BuildRequires: libuuid-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description uuid
The module generates universally unique identifiers (UUID) as specified in RFC
4122.

%package  xcap
Summary:  XCAP common functions
Requires: %{name}%{?_isa} = %{version}-%{release}
%description xcap
The module contains several parameters and functions common to all modules
using XCAP capabilities.

%package  xcap_client
Summary:  XCAP client
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildRequires: curl-devel
%description xcap_client
The modules is an XCAP client for OpenSIPS that can be used by other modules.
It fetches XCAP elements, either documents or part of them, by sending HTTP
GET requests. It also offers support for conditional queries. It uses libcurl
library as a client-side HTTP transfer library.

%package  xml
Summary:  Basic XML parsing and manipulation
Requires: %{name}%{?_isa} = %{version}-%{release}
%description xml
This module exposes a script variable that provides basic parsing and
manipulation of XML documents or blocks of XML data. The processing does not
take into account any DTDs or schemas in terms of validation.

%package  xmpp
Summary:  Gateway between OpenSIPS and a jabber server
BuildRequires: expat-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description xmpp
This modules is a gateway between Openser and a jabber server. It enables
the exchange of instant messages between SIP clients and XMPP(jabber)
clients.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

LOCALBASE=/usr NICER=0 CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" %{?_with_oracle:ORAHOME="$ORACLE_HOME"} %{__make} all modules-readme %{?_smp_mflags} TLS=1 VERSIONTYPE=git THISREVISION=%{sub %git_commit 0 9} HTTP2D_USE_SYSTEM=yes HTTP2D_USE_SHARED=yes \
  exclude_modules="%EXCLUDE_MODULES" \
  PYTHON=/usr/bin/python3 \
  cfg_target=%{_sysconfdir}/opensips/
%install
NICER=0 make install TLS=1 VERSIONTYPE=git THISREVISION=%{sub %git_commit 0 9} HTTP2D_USE_SYSTEM=yes HTTP2D_USE_SHARED=yes LIBDIR=%{_lib} \
  exclude_modules="%EXCLUDE_MODULES" \
  PYTHON=/usr/bin/python3 \
  basedir=%{buildroot} prefix=%{_prefix} \
  bin_dir=bin \
  cfg_prefix=%{buildroot} \
  DBTEXTON=yes # fixed dbtext documentation installation
mkdir -p %{buildroot}/%{perl_vendorlib}
if [ -d "%{buildroot}/%{_prefix}/perl" ]; then
  mv %{buildroot}/%{_prefix}/perl/* \
    %{buildroot}/%{perl_vendorlib}/
else
  mv %{buildroot}/%{_libdir}/opensips/perl/* \
    %{buildroot}/%{perl_vendorlib}/
fi
mv %{buildroot}/%{_sysconfdir}/opensips/tls/README \
  %{buildroot}/%{_docdir}/opensips/README.tls
rm -f %{buildroot}%{_docdir}/opensips/INSTALL
mv %{buildroot}/%{_docdir}/opensips docdir
install -D -m 0644 -p %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 0644 -p packaging/redhat_fedora/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p packaging/redhat_fedora/%{name}.tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
install -D -p -m 644 packaging/redhat_fedora/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%oreon_autofiles python3-opensips usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n opensips-aaa_diameter -f %{oreon_filedir}/opensips-aaa_diameter.list
%files -n opensips-aaa_radius -f %{oreon_filedir}/opensips-aaa_radius.list
%files -n opensips-acc -f %{oreon_filedir}/opensips-acc.list
%files -n opensips-aka_av_diameter -f %{oreon_filedir}/opensips-aka_av_diameter.list
%files -n opensips-auth_aaa -f %{oreon_filedir}/opensips-auth_aaa.list
%files -n opensips-auth_jwt -f %{oreon_filedir}/opensips-auth_jwt.list
%files -n opensips-b2bua -f %{oreon_filedir}/opensips-b2bua.list
%files -n opensips-cachedb_couchbase -f %{oreon_filedir}/opensips-cachedb_couchbase.list
%files -n opensips-cachedb_memcached -f %{oreon_filedir}/opensips-cachedb_memcached.list
%files -n opensips-cachedb_mongodb -f %{oreon_filedir}/opensips-cachedb_mongodb.list
%files -n opensips-cachedb_redis -f %{oreon_filedir}/opensips-cachedb_redis.list
%files -n opensips-call_center -f %{oreon_filedir}/opensips-call_center.list
%files -n opensips-carrierroute -f %{oreon_filedir}/opensips-carrierroute.list
%files -n opensips-cgrates -f %{oreon_filedir}/opensips-cgrates.list
%files -n opensips-compression -f %{oreon_filedir}/opensips-compression.list
%files -n opensips-cpl_c -f %{oreon_filedir}/opensips-cpl_c.list
%files -n opensips-db_berkeley -f %{oreon_filedir}/opensips-db_berkeley.list
%files -n opensips-db_http -f %{oreon_filedir}/opensips-db_http.list
%files -n opensips-db_mysql -f %{oreon_filedir}/opensips-db_mysql.list
%files -n opensips-db_perlvdb -f %{oreon_filedir}/opensips-db_perlvdb.list
%files -n opensips-db_postgresql -f %{oreon_filedir}/opensips-db_postgresql.list
%files -n opensips-db_sqlite -f %{oreon_filedir}/opensips-db_sqlite.list
%files -n opensips-db_unixodbc -f %{oreon_filedir}/opensips-db_unixodbc.list
%files -n opensips-event_kafka -f %{oreon_filedir}/opensips-event_kafka.list
%files -n opensips-event_rabbitmq -f %{oreon_filedir}/opensips-event_rabbitmq.list
%files -n opensips-emergency -f %{oreon_filedir}/opensips-emergency.list
%files -n opensips-h350 -f %{oreon_filedir}/opensips-h350.list
%files -n opensips-httpd -f %{oreon_filedir}/opensips-httpd.list
%files -n opensips-http2d -f %{oreon_filedir}/opensips-http2d.list
%files -n opensips-identity -f %{oreon_filedir}/opensips-identity.list
%files -n opensips-jabber -f %{oreon_filedir}/opensips-jabber.list
%files -n opensips-json -f %{oreon_filedir}/opensips-json.list
%files -n opensips-ldap -f %{oreon_filedir}/opensips-ldap.list
%files -n opensips-lua -f %{oreon_filedir}/opensips-lua.list
%files -n opensips-media_exchange -f %{oreon_filedir}/opensips-media_exchange.list
%files -n opensips-mi_html -f %{oreon_filedir}/opensips-mi_html.list
%files -n opensips-mi_http -f %{oreon_filedir}/opensips-mi_http.list
%files -n opensips-mi_xmlrpc_ng -f %{oreon_filedir}/opensips-mi_xmlrpc_ng.list
%files -n opensips-mmgeoip -f %{oreon_filedir}/opensips-mmgeoip.list
%files -n opensips-msrp -f %{oreon_filedir}/opensips-msrp.list
%files -n opensips-peering -f %{oreon_filedir}/opensips-peering.list
%files -n opensips-perl -f %{oreon_filedir}/opensips-perl.list
%files -n opensips-pi_http -f %{oreon_filedir}/opensips-pi_http.list
%files -n opensips-presence -f %{oreon_filedir}/opensips-presence.list
%files -n opensips-presence_callinfo -f %{oreon_filedir}/opensips-presence_callinfo.list
%files -n opensips-presence_dfks -f %{oreon_filedir}/opensips-presence_dfks.list
%files -n opensips-presence_dialoginfo -f %{oreon_filedir}/opensips-presence_dialoginfo.list
%files -n opensips-presence_mwi -f %{oreon_filedir}/opensips-presence_mwi.list
%files -n opensips-presence_reginfo -f %{oreon_filedir}/opensips-presence_reginfo.list
%files -n opensips-presence_xcapdiff -f %{oreon_filedir}/opensips-presence_xcapdiff.list
%files -n opensips-presence_xml -f %{oreon_filedir}/opensips-presence_xml.list
%files -n opensips-prometheus -f %{oreon_filedir}/opensips-prometheus.list
%files -n opensips-proto_bins -f %{oreon_filedir}/opensips-proto_bins.list
%files -n opensips-proto_ipsec -f %{oreon_filedir}/opensips-proto_ipsec.list
%files -n opensips-proto_sctp -f %{oreon_filedir}/opensips-proto_sctp.list
%files -n opensips-proto_tls -f %{oreon_filedir}/opensips-proto_tls.list
%files -n opensips-proto_wss -f %{oreon_filedir}/opensips-proto_wss.list
%files -n opensips-pua -f %{oreon_filedir}/opensips-pua.list
%files -n opensips-pua_bla -f %{oreon_filedir}/opensips-pua_bla.list
%files -n opensips-pua_dialoginfo -f %{oreon_filedir}/opensips-pua_dialoginfo.list
%files -n opensips-pua_mi -f %{oreon_filedir}/opensips-pua_mi.list
%files -n opensips-pua_reginfo -f %{oreon_filedir}/opensips-pua_reginfo.list
%files -n opensips-pua_usrloc -f %{oreon_filedir}/opensips-pua_usrloc.list
%files -n opensips-pua_xmpp -f %{oreon_filedir}/opensips-pua_xmpp.list
%files -n python3-opensips -f %{oreon_filedir}/python3-opensips.list
%files -n opensips-rabbitmq_consumer -f %{oreon_filedir}/opensips-rabbitmq_consumer.list
%files -n opensips-regex -f %{oreon_filedir}/opensips-regex.list
%files -n opensips-rest_client -f %{oreon_filedir}/opensips-rest_client.list
%files -n opensips-rls -f %{oreon_filedir}/opensips-rls.list
%files -n opensips-siprec -f %{oreon_filedir}/opensips-siprec.list
%files -n opensips-snmpstats -f %{oreon_filedir}/opensips-snmpstats.list
%files -n opensips-stir_shaken -f %{oreon_filedir}/opensips-stir_shaken.list
%files -n opensips-tls_mgm -f %{oreon_filedir}/opensips-tls_mgm.list
%files -n opensips-tls_openssl -f %{oreon_filedir}/opensips-tls_openssl.list
%files -n opensips-uuid -f %{oreon_filedir}/opensips-uuid.list
%files -n opensips-xcap -f %{oreon_filedir}/opensips-xcap.list
%files -n opensips-xcap_client -f %{oreon_filedir}/opensips-xcap_client.list
%files -n opensips-xml -f %{oreon_filedir}/opensips-xml.list
%files -n opensips-xmpp -f %{oreon_filedir}/opensips-xmpp.list

%changelog

%autochangelog
