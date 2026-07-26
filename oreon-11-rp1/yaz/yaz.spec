%global source0_hash 9257feb06e2fdbbfceb7d040c139fa13957c4d1ebba6aa293a6dd13cab2225ce

Name:           yaz
Version:        5.37.0
Release:        2%{?dist}
Summary:        Z39.50/SRW/SRU toolkit
# SPDX confirmed
License:        BSD-3-Clause
URL:            http://www.indexdata.com/yaz/
Source0:        http://ftp.indexdata.com/pub/yaz/yaz-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  make

# When autoreconf is needed:
%if 0
BuildRequires:  autoconf
BuildRequires:  automake
%endif

BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libmemcached)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)

BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  /usr/bin/tclsh

Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
YAZ is a programmers toolkit supporting the development of Z39.50/SRW/SRU 
clients and servers. Z39.50-2003 (version 3) as well as SRW/SRU version 1.1 
are supported in both the client and server roles. The SOLR webservice is 
supported in the client role through the ZOOM API.

The current version of YAZ includes support for the industry standard ZOOM 
API for Z39.50. This API vastly simplifies the process of writing new clients 
using YAZ, and it reduces your dependency on any single toolkit. YAZ can be 
used by itself to build Z39.50 applications in C.For programmers preferring 
another language, YAZ has three language bindings to commonly used application
development languages.

This package contains both a test-server and clients (normal & ssl).

%package -n     lib%{name}
Summary:        Shared libraries for %{name}

%description -n lib%{name}
This packages contains shared libraries for %{name}.

%package -n     lib%{name}-devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
This package contains libraries and header files for
developing applications that use lib%{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}, a Z39.50 protocol
server and client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
sed -i.rpath configure \
	-e 's|hardcode_libdir_flag_spec=|hardcode_libdir_flag_spec_goodby=|' \
	-e '\@sys_lib_dlsearch_path_spec=@s|/lib /usr/lib|/lib /usr/lib %{_libdir} /%{_lib}|' \
	%{nil}

%configure \
        --enable-shared \
        --with-memcached \
        --with-redis \
        --disable-static \
        %{nil}

%make_build

%install
%make_install

# Remove cruft
find %{buildroot} -name '*.*a' -delete -print

%check
make check

%ldconfig_scriptlets -n lib%{name}

%ldconfig_scriptlets -n lib%{name}

%files
%doc NEWS
%doc README.md
%license LICENSE
%{_bindir}/yaz-client
%{_bindir}/yaz-iconv
%{_bindir}/yaz-icu
%{_bindir}/yaz-illclient
%{_bindir}/yaz-json-parse
%{_bindir}/yaz-marcdump
%{_bindir}/yaz-record-conv
%{_bindir}/yaz-url
%{_bindir}/yaz-ztest
%{_bindir}/zoomsh
%{_mandir}/man1/yaz-client.*
%{_mandir}/man1/yaz-iconv.*
%{_mandir}/man1/yaz-icu.*
%{_mandir}/man1/yaz-illclient.*
%{_mandir}/man1/yaz-json-parse.*
%{_mandir}/man7/yaz-log.*
%{_mandir}/man1/yaz-marcdump.*
%{_mandir}/man1/yaz-record-conv.*
%{_mandir}/man1/yaz-url.*
%{_mandir}/man8/yaz-ztest.*
%{_mandir}/man1/zoomsh.*

%files -n lib%{name}
%license LICENSE
%{_libdir}/libyaz.so.5*
%{_libdir}/libyaz_icu.so.5*
%{_libdir}/libyaz_server.so.5*
%{_mandir}/man7/yaz.*
%{_mandir}/man7/bib1-attr.*

%files -n lib%{name}-devel
%doc NEWS README.md
%{_bindir}/yaz-asncomp
%{_bindir}/yaz-config
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/%{name}/
%{_datadir}/yaz/
%{_datadir}/aclocal/*
%{_mandir}/man1/yaz-asncomp.*
%{_mandir}/man1/yaz-config.*

%files -n %{name}-doc
%{_pkgdocdir}

%changelog
%autochangelog
