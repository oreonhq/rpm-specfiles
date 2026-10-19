%global source0_hash 6a05291c4ca12169287d78f9e6d083c85b4eb180ceeb16403924e4310b681651
Name:           libcanlock
Version:        3.3.3
Release:        1%{?dist}
Summary:        Create and verify RFC 8315 Netnews Cancel-Locks
License:        BSD-3-Clause AND ICU
URL:            https://micha.freeshell.org/libcanlock
Source0:        https://micha.freeshell.org/%{name}/src/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  byacc
BuildRequires:  dos2unix
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
A library for creating and verifying RFC 8315 Netnews Cancel-Locks.
This implementation uses the recommended algorithm from Section 4 with HMAC
based on the same hash function as <scheme>.

%package devel
Summary:        Development files for libcanlock
Requires:       libcanlock%{?_isa} = %{version}-%{release}
%description devel
This package holds the development files for libcanlock.

%package -n canlock
Summary:        Command line utilities for Netnews Cancel-Lock authentication scheme
Requires:       libcanlock%{?_isa} = %{version}-%{release}
%description -n canlock
Command line utilities for Netnews Cancel-Lock authentication scheme.

canlock can be used to create <c-lock> and <c-key> elements according to
RFC 8315.  The secret data is read from standard input (using EOF for
termination).

canlock also provides a verify interface with the -c option.  An external
header parser is required to extract the <c-key> and <c-lock> elements
from the article headers. The command line utilities canlock-mhp(1) and
canlock-hfp(1) can be used for this purpose.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
dos2unix -k hp/examples/{supersede,target}.txt
cp -p hp/COPYING COPYING.hp

%build

%configure --enable-pc-files
%make_build
%install
%make_install
rm -v %{buildroot}%{_libdir}/libcanlock{,-hp}.a
%oreon_autofiles canlock usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libcanlock-devel -f %{oreon_filedir}/libcanlock-devel.list
%files -n canlock -f %{oreon_filedir}/canlock.list

%changelog

%autochangelog
