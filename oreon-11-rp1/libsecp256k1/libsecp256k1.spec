%global source0_hash 785bb98e7d6705c51c8dfa8ac3af6aa2ccfa3774714d51c0b9e28fac1146e9f1

%global forgeurl https://github.com/bitcoin-core/secp256k1

Name:    libsecp256k1
Epoch:   1
Version: 0.6.0
Release: 4%{?dist}
Summary: Optimized C library for EC operations on curve secp256k1

%forgemeta
License: MIT
URL:     %{forgeurl}
Source0: %{forgesource}

BuildRequires: automake autoconf libtool
BuildRequires: gcc
BuildRequires: gmp-devel
BuildRequires: make
BuildRequires: openssl-devel

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

%check
make check

%files
%license COPYING
%doc README.md
%doc CHANGELOG.md
%doc SECURITY.md
%{_libdir}/%{name}.so.5
%{_libdir}/%{name}.so.5.0.0

%files devel
%license COPYING
%doc README.md
%doc examples
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
