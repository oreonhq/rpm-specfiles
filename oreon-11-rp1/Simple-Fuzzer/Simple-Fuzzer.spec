%global source0_hash e72731644eb889c4cdbefcd0cf61546394914c22ef4966d383fd1abb6ae0fd83
Summary:        A simple fuzz test-case builder
Name: Simple-Fuzzer
Version: 0.7.1
Release:        25%{?dist}
License: LicenseRef-Callaway-BSD
URL: http://aconole.bytheb.org/programs/sfuzz.html
Source0:        http://aaron.bytheb.org/files/sfuzz-0.7-dist/sfuzz-%{version}.tar.bz2
Requires: openssl
Patch1: 0001-sfuzz-cleanup-snprintfs.patch
Patch2: 0001-configure-disable-snoop-on-OS-X.patch
Patch3: 0001-configure-Use-r-for-sed.patch
Patch4: 0001-array_fuzz-Fix-a-sizeof-issue.patch
Patch5: 0001-url-change-to-bytheb.org.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
# /oreon:deps
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
%oreon_autofiles Simple-Fuzzer-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n Simple-Fuzzer-devel -f %{oreon_filedir}/Simple-Fuzzer-devel.list

%changelog

%autochangelog
