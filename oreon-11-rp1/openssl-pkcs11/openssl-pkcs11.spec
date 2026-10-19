%global source0_hash efdb523aef8613d447e6a2d38227d4b389866f4bcf4b503130acd7f759490847
Version: 0.4.21
Release:        1%{?dist}
%global enginesdir %{_libdir}/engines-3
Name:           openssl-pkcs11
Summary:        A PKCS#11 engine for use with OpenSSL
License:        LGPL-2.1-or-later AND BSD-2-Clause AND OpenSSL
URL:            https://github.com/OpenSC/libp11
Source0:        https://github.com/OpenSC/libp11/releases/download/libp11-%{version}/libp11-%{version}.tar.gz
Requires:       p11-kit-trust
Requires:       openssl-libs >= 3.0.0
Provides:       libp11%{?_isa} = %{version}-%{release}
Obsoletes:      libp11 < 0.4.7-4
Provides:       engine_pkcs11%{?_isa} = %{version}-%{release}
Obsoletes:      engine_pkcs11 < 0.4.7-4
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  opensc
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  procps-ng
BuildRequires:  softhsm
# /oreon:deps
%description -n openssl-pkcs11
openssl-pkcs11 enables hardware security module (HSM), and smart card support in
OpenSSL applications. More precisely, it is an OpenSSL engine which makes
registered PKCS#11 modules available for OpenSSL applications. The engine is
optional and can be loaded by configuration file, command line or through the
OpenSSL ENGINE API.

# The libp11-devel subpackage was reintroduced in libp11-0.4.7-7 for Fedora

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libp11-%{version}
%oreon_prep
%build

autoreconf -fvi
export CFLAGS="%{optflags}"
%configure --disable-static --with-enginesdir=%{enginesdir}
make V=1 %{?_smp_mflags}
%install
mkdir -p %{buildroot}%{enginesdir}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{enginesdir}/*.la
rm -rf %{buildroot}%{_docdir}/libp11/
%oreon_autofiles main

%check

%if %{?_with_check:1}%{!?_with_check:0}
make check %{?_smp_mflags} || if [ $? -ne 0 ]; then cat tests/*.log; exit 1; fi;
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
