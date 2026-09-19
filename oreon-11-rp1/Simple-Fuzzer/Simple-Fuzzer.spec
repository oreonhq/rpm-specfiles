%global source0_hash e72731644eb889c4cdbefcd0cf61546394914c22ef4966d383fd1abb6ae0fd83

Summary: A simple fuzz test-case builder
Name: Simple-Fuzzer
Version: 0.7.1
Release: 25%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://aconole.bytheb.org/programs/sfuzz.html
Source: http://aaron.bytheb.org/files/sfuzz-0.7-dist/sfuzz-%{version}.tar.bz2

BuildRequires: make
BuildRequires: gcc
BuildRequires: openssl openssl-devel
Requires: openssl

Patch1: 0001-sfuzz-cleanup-snprintfs.patch
Patch2: 0001-configure-disable-snoop-on-OS-X.patch
Patch3: 0001-configure-Use-r-for-sed.patch
Patch4: 0001-array_fuzz-Fix-a-sizeof-issue.patch
Patch5: 0001-url-change-to-bytheb.org.patch

%description
Simple-Fuzzer (sfuzz) is a simplistic fuzz test case generator.
It is a generation-based fuzzer, intended to aid in fault finding.

%package devel
Summary: Simple Fuzzer development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the headers and other files needed for developing
plugins for Simple Fuzzer

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n sfuzz-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%configure --force-symbols --aux-search-path=%{_libdir}/simple-fuzzer
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_libdir}/simple-fuzzer/
mv %{buildroot}%{_datadir}/sfuzz-db/*.so %{buildroot}%{_libdir}/simple-fuzzer/

%files
%{_bindir}/*
%{_datadir}/man/man1/*
%{_datadir}/sfuzz-db/basic.*
%{_datadir}/sfuzz-db/*.list
%{_datadir}/sfuzz-db/*.inc
%{_datadir}/sfuzz-db/server.*
%{_datadir}/sfuzz-db/*.test
%{_datadir}/sfuzz-db/*.0day
%{_datadir}/sfuzz-db/*.cfg
%{_libdir}/simple-fuzzer/*

%files devel
%{_datadir}/sfuzz-db/*.c

%license LICENSING

%changelog
%autochangelog
