%global source0_hash 3c19d412350109423b12bfde196b5bd51e9b23552406bc82735c5ca5e7bcdda8

Name:           pkcs11-dump
Version:        0.3.4
Release:        34%{?dist}
Summary:        Small utility for querying PKCS#11 modules

# Automatically converted from old format: GPLv2 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            http://code.google.com/p/pkcs11-tools/
Source0:        http://pkcs11-tools.googlecode.com/files/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  openssl-devel

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

# Remove docs which get installed in a wrong dir
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/pkcs11-dump/

%files
%doc AUTHORS ChangeLog COPYING* README THANKS
%{_bindir}/pkcs11-dump
%{_mandir}/man1/pkcs11-dump.1*

%changelog
%autochangelog
