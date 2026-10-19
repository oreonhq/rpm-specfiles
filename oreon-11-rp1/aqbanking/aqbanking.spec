%global source0_hash 244b5f7a139f829928f5cdc3f5f7488517b3e8aa63625a92741c3efc1892bb3f
Name: aqbanking
Summary:        A library for online banking functions and financial data import/export
Version: 6.9.2
Release:        1%{?dist}
Source0:        https://www.aquamaniac.de/rdm/attachments/download/654/aqbanking-%{version}.tar.gz
License: GPL-2.0-only AND GPL-3.0-only
URL: https://www.aquamaniac.de/rdm/projects/aqbanking
%global majmin %(echo %{version} | cut -d. -f1-2)
Requires: libchipcard
Obsoletes: aqhbci <= 1.0.3
Obsoletes: g2banking < 3.7.2-1 
Obsoletes: qbanking < 5.0
Obsoletes: q4banking < 5.0
Obsoletes: python-aqbanking < 6.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gmp-devel
BuildRequires:  gwenhywfar-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  xmlsec1-devel
BuildRequires:  xmlsec1-gcrypt
BuildRequires:  xmlsec1-gnutls
BuildRequires:  xmlsec1-gnutls-devel
# /oreon:deps
%description 
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%package devel
Summary: Development headers for Aqbanking
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gwenhywfar-devel
Obsoletes: aqhbci-devel <= 1.0.3
Obsoletes: g2banking-devel < 3.7.2-1 
Obsoletes: qbanking-devel < 5.0
Obsoletes: q4banking-devel < 5.0
%description devel
This package contains aqbanking-config and header files for writing and
compiling programs using Aqbanking.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

# hack to nuke rpaths, slighly less ugly than using overriding LIBTOOL below
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif

%build

export PKG_CONFIG=/usr/bin/pkg-config
%configure \
  --disable-static \
  --enable-gui-tests=no \
  --with-build-datetime="$(date +%Y%m%d)"
%make_build
%install
%make_install
rm -fv %{buildroot}%{_libdir}/lib*.la
pushd tutorials
make clean
rm -rf .deps
rm -f Makefile*
popd
%find_lang %{name}
%oreon_autofiles aqbanking-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check ||:
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n aqbanking-devel -f %{oreon_filedir}/aqbanking-devel.list

%changelog

%autochangelog
