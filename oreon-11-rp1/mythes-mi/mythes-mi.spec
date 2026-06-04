%global source0_hash none

Name: mythes-mi
Summary: Maori thesaurus
%global upstreamid 20080630
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source: mythes-mi-0.1.20080630-beta.tar.gz
URL: http://papakupu.maori.nz/
License: LicenseRef-Public-Domain
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-mi)

%description
Maori thesaurus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p mi.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_mi_NZ_v2.dat
cp -p mi.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_mi_NZ_v2.idx


%files
%doc mi.AUTHORS mi.README mi.LICENSE
%{_datadir}/mythes/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20080630-35
- Import
