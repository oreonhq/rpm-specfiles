%global source0_hash e2e151fdd47a345b6ef72cae1d8ecf3099bb90420f276761f2793ec317809307
%global apiversion 0.6
Name: libcmis
Version: 0.6.3
Release:        1%{?dist}
Summary:        A C/C++ client library for CM interfaces
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
URL: https://github.com/tdf/libcmis
Source0:        https://github.com/tdf/libcmis/releases/download/v%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  xmlto
# /oreon:deps
%description
LibCMIS is a C/C++ client library for working with CM (content management)
interfaces. The primary supported interface (which gave the library its
name) is CMIS, which allows applications to connect to any ECM behaving
as a CMIS server (Alfresco or Nuxeo are examples of open source ones).
Another supported interface is Google Drive.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Command line tool to access CMIS
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
The %{name}-tools package contains a tool for accessing CMIS from the
command line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CC=gcc
export CXX=g++
CFLAGS="${CFLAGS//-nostdinc/}"
CXXFLAGS="${CXXFLAGS//-nostdinc/}"
export CFLAGS CXXFLAGS
%configure --disable-silent-rules --disable-static --disable-werror \
    DOCBOOK2MAN='xmlto man'
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
find %{buildroot}/%{_libdir} -type f -name '*.so.*' -print0 | xargs -0 chrpath --delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libcmis-devel -f %{oreon_filedir}/libcmis-devel.list
%files -n libcmis-tools -f %{oreon_filedir}/libcmis-tools.list

%changelog

%autochangelog
