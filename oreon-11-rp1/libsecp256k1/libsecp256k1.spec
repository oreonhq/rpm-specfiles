%global source0_hash 785bb98e7d6705c51c8dfa8ac3af6aa2ccfa3774714d51c0b9e28fac1146e9f1
%global forgeurl https://github.com/bitcoin-core/secp256k1
Name:    libsecp256k1
Epoch:   1
Version: 0.6.0
Release:        1%{?dist}
Summary:        Optimized C library for EC operations on curve secp256k1
%forgemeta
License: MIT
URL:     %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/secp256k1-%{version}.tar.gz
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

Uses the implementation maintained by Bitcoin Core.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

./autogen.sh
%configure \
    --disable-static \
    --disable-benchmark \
    --disable-coverage \
    --enable-module-ecdh \
    --enable-module-recovery \
    --enable-module-extrakeys \
    --enable-module-schnorrsig \
    --enable-tests \
    --enable-exhaustive-tests \
    --with-gnu-ld
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libsecp256k1-devel -f %{oreon_filedir}/libsecp256k1-devel.list

%changelog

%autochangelog
