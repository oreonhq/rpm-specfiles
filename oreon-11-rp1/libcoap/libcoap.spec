%global source0_hash bca78a2076ebb02179f93ab6cf2363b1256d878b540f810c238ea231ad5948ab
Name:     libcoap
Version:  4.3.5a
Release:        1%{?dist}
Summary:        C library implementation of CoAP
URL:      https://libcoap.net/
License:  LicenseRef-Callaway-BSD
Source0:        https://github.com/obgm/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ctags
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
# /oreon:deps
%description
The Constrained Application Protocol (CoAP) is a specialized web transfer 
protocol for use with constrained nodes and constrained networks in the Internet 
of Things. The protocol is designed for machine-to-machine (M2M) applications 
such as smart energy and building automation.

libcoap implements a lightweight application-protocol for devices with 
constrained resources such as computing power, RF range, memory, bandwidth,
or network packet sizes. This protocol, CoAP, was standardized in the IETF
working group "CoRE" as RFC 7252.

%package  utils
Summary:  Client and server CoAP utilities
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
Utilities for working with %{name}.

%package  devel
Summary:  Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%package  doc
Summary:  Documentation package for %{name}
BuildArch: noarch
%description doc
Documentation for development with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?candidate:-%{candidate}}

%build

autoreconf -vif
%configure --without-debug CFLAGS="$RPM_OPT_FLAGS -D COAP_DEBUG_FD=stderr" \
           --enable-examples --enable-documentation --enable-doxygen --enable-manpages \
           --enable-dtls --with-openssl --disable-static
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
rm -rf %{buildroot}/%{_datadir}/%{name}
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libcoap-utils -f %{oreon_filedir}/libcoap-utils.list
%files -n libcoap-devel -f %{oreon_filedir}/libcoap-devel.list
%files -n libcoap-doc -f %{oreon_filedir}/libcoap-doc.list

%changelog

%autochangelog
