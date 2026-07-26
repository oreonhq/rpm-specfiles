%global source0_hash fc94a2bebfbb4fc26b98dc93c8fa36a8026298cd7995f79821c480db35587f6b

Name: aqbanking
Summary: A library for online banking functions and financial data import/export
Version: 6.9.1
Release: 3%{?dist}
# Download is PHP form at http://www.aquamaniac.de/sites/download/packages.php
Source0: https://www.aquamaniac.de/rdm/attachments/download/652/aqbanking-%{version}.tar.gz
License: GPL-2.0-only AND GPL-3.0-only
URL: https://www.aquamaniac.de/rdm/projects/aqbanking

%global majmin %(echo %{version} | cut -d. -f1-2)

BuildRequires: gcc-c++
BuildRequires: gwenhywfar-devel >= 5.0.0
BuildRequires: gmp-devel, gettext, libtool
BuildRequires: xmlsec1-gnutls-devel, xmlsec1-devel, libtool-ltdl-devel, libxslt-devel, libxml2-devel
# For AutoReq cmake-filesystem
BuildRequires: cmake
# bug in xmlscec1
BuildRequires: xmlsec1-gnutls, xmlsec1-gcrypt
BuildRequires: make
Requires: libchipcard
Obsoletes: aqhbci <= 1.0.3
Obsoletes: g2banking < 3.7.2-1 
Obsoletes: qbanking < 5.0
Obsoletes: q4banking < 5.0
Obsoletes: python-aqbanking < 6.0

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
# avoid detection/use of stuff like x86_64-redhat-linux-gnu-pkg-config -- rdieter
export PKG_CONFIG=/usr/bin/pkg-config

%configure \
  --disable-static \
  --enable-gui-tests=no \
  --with-build-datetime="$(date +%Y%m%d)"

%make_build

%install

%make_install

## unpackaged files
rm -fv %{buildroot}%{_libdir}/lib*.la

pushd tutorials
make clean
rm -rf .deps
rm -f Makefile*
popd

%find_lang %{name}

%check
## meh, requires X server
make check ||:

%ldconfig_scriptlets

%files -f %{name}.lang
%doc %{_datadir}/doc/%{name}
%{_libdir}/libaqbanking.so.44*
# plugins, plugins, plugins
%{_libdir}/aqbanking/
%{_datadir}/aqbanking
%{_bindir}/aqbanking-cli
%{_bindir}/aqebics-tool
%{_bindir}/aqhbci-tool4
%{_bindir}/aqpaypal-tool
%{_bindir}/aqofxconnect-tool

%files devel
%doc doc/0[12]* tutorials
%{_bindir}/aqbanking-config
%{_libdir}/libaqbanking.so
%{_includedir}/aqbanking6/
%{_libdir}/cmake/aqbanking-%{majmin}/
%{_libdir}/pkgconfig/aqbanking.pc
%{_datadir}/aclocal/aqbanking.m4
%{_datadir}/aqbanking/aqbanking/typemaker2
%{_datadir}/aqbanking/typemaker2

%changelog
%autochangelog
