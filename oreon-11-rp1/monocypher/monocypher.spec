%global source0_hash 8cc9bc341a66249016db9bd70e9142d8d0aef9945973744b1ac05dbc55d8ee66
Name:           monocypher
Version:        4.0.3
Release:        1%{?dist}
Summary:        Boring crypto that simply works
License:        LicenseRef-Callaway-BSD OR CC0-1.0
URL:            https://monocypher.org/
Source0:        https://monocypher.org/download/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Monocypher is an easy to use cryptographic library. It provides functions for
authenticated encryption, hashing, password hashing and key derivation, key
exchange, and public key signatures. It is:

- Small. Monocypher contains under 2000 lines of code, small enough to allow
audits. The binaries can be under 50KB, small enough for many embedded targets.
- Easy to deploy. Just add monocypher.c and monocypher.h to your project. They
compile as C99 or C++ and are dedicated to the public domain (CC0-1.0,
alternatively 2-clause BSD).
- Portable. There are no dependencies, not even on libc.
- Honest. The API is small, consistent, and cannot fail on correct input.
- Direct. The abstractions are minimal. A developer with experience in applied
cryptography can be productive in minutes.
- Fast. The primitives are fast to begin with, and performance wasn't
needlessly sacrificed. Monocypher holds up pretty well against Libsodium,
despite being closer in size to TweetNaCl.

%package devel
Summary:        Development files for monocypher
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description devel
This package contains the development files for monocypher.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="${RPM_OPT_FLAGS}"
%make_build CFLAGS="${RPM_OPT_FLAGS}"
%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -v %{buildroot}%{_libdir}/*.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check CFLAGS="${RPM_OPT_FLAGS}"
%files -f %{oreon_filedir}/main.list
%files -n monocypher-devel -f %{oreon_filedir}/monocypher-devel.list

%changelog

%autochangelog
