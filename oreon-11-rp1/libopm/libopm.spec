%global source0_hash 7e540cf54fe86d3e277e88048523c9a2113a5d20dbfbe733782833eaf7e33c32

Summary:        Blitzed open proxy monitor library
Name:           libopm
Version:        0.1
Release:        41.20050731cvs%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://wiki.blitzed.org/BOPM
# cvs -z3 -d:pserver:anon@cvs.blitzed.org:/ co -D "20050731 23:59" libopm
# find libopm -type f -name .cvsignore -exec rm -f {} ';'
# find libopm -type d -name CVS -exec rm -rf {} 2>/dev/null ';'
# mv -f libopm libopm-$(grep AC_INIT libopm/configure.in | sed -e 's/.*\[\(.*\)\].*/\1/')
Source:         %{name}-%{version}.tar.gz
Patch1:         libopm-0.1-multilib.patch
Patch2:         libopm-configure-c99.patch
BuildRequires:  gcc
BuildRequires:  make

%description
An open proxy detection library, developed by the blitzed
IRC network team. Its original use was to detect open proxies
running on clients connecting to various IRC servers, but it
has evolved to become a generic open proxy detection library.

%package devel
Summary:        Headers and development libraries for libopm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The libopm-devel package contains the header files and libraries
necessary for developing applications which use libopm.

%if 0%{!?_without_doc:1}
%package doc
Summary:        Documentation files for libopm
BuildArch:      noarch
BuildRequires:  doxygen

%description doc
This package contains the API documentation for developing
applications that use libopm, which is an open proxy detection
library. 
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static
%make_build
%{!?_without_doc:cd doc && doxygen && mv -f api html}

%install
%make_install

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license LICENSE
%doc ChangeLog
%{_libdir}/%{name}.so.*

%files devel
%doc doc/libopm-api.txt
%{_includedir}/opm*
%{_libdir}/%{name}.so

%if 0%{!?_without_doc:1}
%files doc
%doc doc/html/
%endif

%changelog
%autochangelog
