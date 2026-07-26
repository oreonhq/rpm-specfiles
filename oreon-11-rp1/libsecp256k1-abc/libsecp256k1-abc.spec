%global source0_hash 2426148e2bb0ddb19110a062561158eede3e4a0e4449ec38e8bcdc4b27af5161

%global forgeurl https://github.com/Bitcoin-ABC/secp256k1

Name:    libsecp256k1-abc
Version: 0.27.1
Release: 3%{?dist}
Summary: Optimized C library for EC operations on curve secp256k1

%forgemeta
License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}

BuildRequires: gcc
BuildRequires: automake autoconf libtool
BuildRequires: gmp-devel
BuildRequires: openssl-devel
BuildRequires: make

Conflicts: libsecp256k1

%description
%{summary}.

Includes support for Schnorr signature.

Uses the implementation maintained by Bitcoin-ABC.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
./autogen.sh
%configure --disable-static \
           --enable-module-recovery \
           --enable-experimental \
           --enable-module-ecdh

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%check
make check

%files
%license COPYING
%doc README.md
%{_libdir}/libsecp256k1.so.0
%{_libdir}/libsecp256k1.so.0.0.0

%files devel
%license COPYING
%doc README.md
%{_includedir}/*
%{_libdir}/libsecp256k1.so
%{_libdir}/pkgconfig/libsecp256k1.pc

%changelog
%autochangelog
