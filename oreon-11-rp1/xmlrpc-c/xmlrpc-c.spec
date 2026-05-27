%global source0_hash none

# build order matters and multiple threads break it
%global _smp_mflags -j1

Name:           xmlrpc-c
Version:        1.60.04
Release:        5%{?dist}
Summary:        Lightweight RPC library based on XML and HTTP
# See doc/COPYING for details.
# The Python 1.5.2 license used by a few files is just BSD.
# Automatically converted from old format: BSD and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            http://xmlrpc-c.sourceforge.net/
Source:         http://dl.sourceforge.net/sourceforge/xmlrpc-c/xmlrpc-c-%version.tgz

# Upstreamable patches
Patch102:       0002-Use-proper-datatypes-for-long-long.patch
Patch103:       0003-allow-30x-redirections.patch

BuildRequires:  git-core
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel

%package c++
Summary:        C++ libraries for xmlrpc-c
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%package client
Summary:        C client libraries for xmlrpc-c
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%package client++
Summary:        C++ client libraries for xmlrpc-c
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-c++%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-client%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%package devel
Summary:        Development files for xmlrpc-c based programs
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-c++%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-client%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-client++%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%package apps
Summary:        Sample XML-RPC applications
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-c++%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-client%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-client++%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}


%description
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C.


%description c++
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C++.


%description client
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C
clients.

%description client++
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C++
clients.


%description devel
Static libraries and header files for writing XML-RPC applications in
C and C++.


%description apps
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This package contains some handy XML-RPC demo applications.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -Sgit


%build
%configure
%make_build CFLAGS="%{optflags} -std=gnu17"
%make_build CFLAGS="%{optflags} -std=gnu17" -C tools


%install
%make_install
%make_install -C tools


%check
#%%make_test


%files
%license doc/COPYING lib/abyss/license.txt
%doc doc/CREDITS doc/HISTORY
%{_libdir}/libxmlrpc_xml*.so.*
%{_libdir}/libxmlrpc.so.*
%{_libdir}/libxmlrpc_openssl.so.*
%{_libdir}/libxmlrpc_util.so.*
%{_libdir}/libxmlrpc_abyss.so.*
%{_libdir}/libxmlrpc_server.so.*
%{_libdir}/libxmlrpc_server_abyss.so.*
%{_libdir}/libxmlrpc_server_cgi.so.*
%exclude %{_libdir}/libxmlrpc*.a


%files client
%{_libdir}/libxmlrpc_client.so.*

%files c++
%{_libdir}/libxmlrpc_cpp.so.*
%{_libdir}/libxmlrpc++.so.*
%{_libdir}/libxmlrpc_util++.so.*
%{_libdir}/libxmlrpc_abyss++.so.*
%{_libdir}/libxmlrpc_server++.so.*
%{_libdir}/libxmlrpc_server_abyss++.so.*
%{_libdir}/libxmlrpc_server_cgi++.so.*
%{_libdir}/libxmlrpc_packetsocket.so.*
%{_libdir}/libxmlrpc_server_pstream++.so.*

%files client++
%{_libdir}/libxmlrpc_client++.so.*

%files devel
%{_bindir}/xmlrpc-c-config
%{_includedir}/xmlrpc-c/
%{_includedir}/*.h
%{_libdir}/pkgconfig/xmlrpc*.pc
%{_libdir}/libxmlrpc*.so

%files apps
%{_bindir}/xmlrpc_parsecall
%{_bindir}/xmlrpc
%{_bindir}/xmlrpc_transport
%doc tools/xmlrpc_transport/xmlrpc_transport.html
%{_bindir}/xml-rpc-api2cpp
%{_mandir}/man1/xml-rpc-api2cpp.1*
%{_bindir}/xml-rpc-api2txt
%{_mandir}/man1/xml-rpc-api2txt.1*
%{_bindir}/xmlrpc_cpp_proxy
%{_bindir}/xmlrpc_pstream
%{_bindir}/xmlrpc_dumpserver

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.60.04-5
- Import
