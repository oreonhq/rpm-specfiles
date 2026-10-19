%global source0_hash 2426148e2bb0ddb19110a062561158eede3e4a0e4449ec38e8bcdc4b27af5161
%global forgeurl https://github.com/Bitcoin-ABC/secp256k1
Name:    libsecp256k1-abc
Version: 0.27.1
Release:        1%{?dist}
Summary:        Optimized C library for EC operations on curve secp256k1
%forgemeta
License: MIT
URL:     %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/secp256k1-%{version}.tar.gz
Conflicts: libsecp256k1
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libsecp256k1-abc-devel -f %{oreon_filedir}/libsecp256k1-abc-devel.list

%changelog

%autochangelog
