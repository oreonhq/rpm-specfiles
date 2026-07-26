%global source0_hash f80a2e16d553e4b119634fd0e85ff86fc42afb4c9cc4569077854d1b6f5ef4f9

Name:           monocypher
Version:        3.1.2
Release:        13%{?dist}
Summary:        Boring crypto that simply works

# Automatically converted from old format: BSD or CC0 - review is highly recommended.
License:        LicenseRef-Callaway-BSD OR CC0-1.0
URL:            https://monocypher.org/
Source0:        https://monocypher.org/download/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

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

%autosetup

%build
export CFLAGS="${RPM_OPT_FLAGS}"
%make_build CFLAGS="${RPM_OPT_FLAGS}"

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -v %{buildroot}%{_libdir}/*.a

%check
make check CFLAGS="${RPM_OPT_FLAGS}"

%files
%doc AUTHORS.md README.md CHANGELOG.md
%license LICENCE.md
%{_libdir}/libmonocypher.so.3

%files devel
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
