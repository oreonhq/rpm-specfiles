%global source0_hash b1d6778924ed1fd50080a53402940c3b3b0b3ee3395473f2ec6c96972b11e617

Summary: Shamir's secret sharing scheme
Name: ssss
Version: 0.5
Release: 36%{?dist}.2
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Url:  http://point-at-infinity.org/%{name}
Source: http://point-at-infinity.org/%{name}/%{name}-%{version}.tar.gz
Source1: ssss.1.gz
BuildRequires:  gcc
BuildRequires: gmp-devel, xmlto

%description
ssss is an implementation of Shamir's secret sharing scheme.  ssss does
both: the generation of shares for a known secret and the reconstruction
of a secret using user provided shares.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
# fix transposed arguments in memset call
sed -i 's/memset(buf, degree \/ 8 + 1, 0);/memset(buf, 0, degree \/ 8 + 1);/' ssss.c
%build
# Makefile target strips binary
gcc $RPM_OPT_FLAGS -lgmp -o ssss-split ssss.c

%install
rm -rf ${RPM_BUILD_ROOT}
install -d 0755 ${RPM_BUILD_ROOT}%{_bindir} 
install -d 0755 ${RPM_BUILD_ROOT}%{_mandir}/man1
install -m 0755 ssss-split ${RPM_BUILD_ROOT}%{_bindir}
ln  ${RPM_BUILD_ROOT}%{_bindir}/ssss-split ${RPM_BUILD_ROOT}%{_bindir}/ssss-combine 
install -m 0644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_mandir}/man1/
ln  ${RPM_BUILD_ROOT}%{_mandir}/man1/ssss.1.gz ${RPM_BUILD_ROOT}%{_mandir}/man1/ssss-split.1.gz
ln  ${RPM_BUILD_ROOT}%{_mandir}/man1/ssss.1.gz ${RPM_BUILD_ROOT}%{_mandir}/man1/ssss-combine.1.gz

%files 
%doc doc.html HISTORY LICENSE THANKS ssss.manpage.xml
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
%autochangelog
