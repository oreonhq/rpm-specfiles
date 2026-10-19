%global source0_hash 3c19d412350109423b12bfde196b5bd51e9b23552406bc82735c5ca5e7bcdda8
Name:           pkcs11-dump
Version:        0.3.4
Release:        1%{?dist}
Summary:        Small utility for querying PKCS#11 modules
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            http://code.google.com/p/pkcs11-tools/
Source0:        http://pkcs11-tools.googlecode.com/files/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
pkcs11-dump is a small utility for querying PKCS#11 provider
modules for objects available on a specific crypto device
and dumping them to stdout in a human-readable format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/pkcs11-dump/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
