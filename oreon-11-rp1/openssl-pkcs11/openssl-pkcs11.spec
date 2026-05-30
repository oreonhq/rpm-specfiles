%global source0_hash d25dd9cff1b623e12d51b6d2c100e26063582d25c9a6f57c99d41f2da9567086

Version: 0.4.13
Release: 4%{?dist}

# Define the directory where the OpenSSL engines are installed
%global enginesdir %{_libdir}/engines-3

Name:           openssl-pkcs11
Summary:        A PKCS#11 engine for use with OpenSSL
# The source code is LGPLv2+ except eng_back.c and eng_parse.c which are BSD
# There are parts licensed with OpenSSL license too
License:        LGPL-2.1-or-later AND BSD-2-Clause AND OpenSSL
URL:            https://github.com/OpenSC/libp11
Source0:        https://github.com/OpenSC/libp11/releases/download/libp11-%{version}/libp11-%{version}.tar.gz

BuildRequires: make
BuildRequires:  autoconf automake libtool
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  openssl >= 3.0.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(p11-kit-1)
# Needed for testsuite
BuildRequires:  softhsm opensc procps-ng

%if 0%{?fedora}
BuildRequires:  doxygen
%endif

Requires:       p11-kit-trust
Requires:       openssl-libs >= 3.0.0

# Package renamed from libp11 to openssl-pkcs11 in release 0.4.7-4
Provides:       libp11%{?_isa} = %{version}-%{release}
Obsoletes:      libp11 < 0.4.7-4
# The engine_pkcs11 subpackage is also provided 
Provides:       engine_pkcs11%{?_isa} = %{version}-%{release}
Obsoletes:      engine_pkcs11 < 0.4.7-4

%if 0%{?fedora}
# The libp11-devel subpackage was removed in libp11-0.4.7-1, but not obsoleted
# This Obsoletes prevents the conflict in updates by removing old libp11-devel
Obsoletes:      libp11-devel < 0.4.7-4
%endif

%description -n openssl-pkcs11
openssl-pkcs11 enables hardware security module (HSM), and smart card support in
OpenSSL applications. More precisely, it is an OpenSSL engine which makes
registered PKCS#11 modules available for OpenSSL applications. The engine is
optional and can be loaded by configuration file, command line or through the
OpenSSL ENGINE API.

# The libp11-devel subpackage was reintroduced in libp11-0.4.7-7 for Fedora
%if 0%{?fedora}
%package -n libp11-devel
Summary:        Files for developing with libp11
Requires:       %{name} = %{version}-%{release}

%description -n libp11-devel
The libp11-devel package contains libraries and header files for
developing applications that use libp11.

%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p 1 -n libp11-%{version}

%build
autoreconf -fvi
export CFLAGS="%{optflags}"
%if 0%{?fedora}
%configure --disable-static --enable-api-doc --with-enginesdir=%{enginesdir}
%else
%configure --disable-static --with-enginesdir=%{enginesdir}
%endif
make V=1 %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{enginesdir}
make install DESTDIR=%{buildroot}

# Remove libtool .la files
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{enginesdir}/*.la

%if ! 0%{?fedora}
## Remove development files
rm -f %{buildroot}%{_libdir}/libp11.so
rm -f %{buildroot}%{_libdir}/libpkcs11.so
rm -f %{buildroot}%{_libdir}/pkgconfig/libp11.pc
rm -f %{buildroot}%{_includedir}/*.h
%endif

# Remove documentation automatically installed by make install
rm -rf %{buildroot}%{_docdir}/libp11/

%check
# to run tests use "--with check". They crash now in softhsm
%if %{?_with_check:1}%{!?_with_check:0}
make check %{?_smp_mflags} || if [ $? -ne 0 ]; then cat tests/*.log; exit 1; fi;
%endif

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS
%{_libdir}/libp11.so.*
%{_libdir}/libpkcs11.so.*
%{enginesdir}/*.so

%if 0%{?fedora}
%files -n libp11-devel
%doc examples/ doc/api.out/html/
%{_libdir}/libp11.so
%{_libdir}/libpkcs11.so
%{_libdir}/pkgconfig/libp11.pc
%{_includedir}/*.h
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.13-4
- Prepare for Oreon 11 (RP1)
