%global source0_hash 5d165555105606b8b08383e697fc48cf849f51d775f1d9a74817f5709db0f995
Summary:        Shamir's secret sharing scheme
Name: ssss
Version: 0.5
Release:        1%{?dist}
License: GPL-2.0-only
Url:  http://point-at-infinity.org/%{name}
Source0:        http://point-at-infinity.org/%{name}/%{name}-%{version}.tar.gz
Source1: ssss.1.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  xmlto
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
