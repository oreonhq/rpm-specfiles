%global source0_hash 7e540cf54fe86d3e277e88048523c9a2113a5d20dbfbe733782833eaf7e33c32
Summary:        Blitzed open proxy monitor library
Name:           libopm
Version:        0.1
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            http://wiki.blitzed.org/BOPM
Source0:        %{name}-%{version}.tar.gz
Patch1:         libopm-0.1-multilib.patch
Patch2:         libopm-configure-c99.patch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
%oreon_prep
%build

%configure --disable-static
%make_build
%{!?_without_doc:cd doc && doxygen && mv -f api html}
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libopm-devel -f %{oreon_filedir}/libopm-devel.list
%files -n libopm-doc -f %{oreon_filedir}/libopm-doc.list

%changelog

%autochangelog
