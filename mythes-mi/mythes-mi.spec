Name: mythes-mi
Summary: Maori thesaurus
%global upstreamid 20080630
Version: 0.%{upstreamid}
Release: 35%{?dist}
# Source is dead now
# Source: http://packages.papakupu.maori.nz/mythes/mythes-mi-0.1.%%{upstreamid}-beta.tar.gz
Source: mythes-mi-0.1.%{upstreamid}-beta.tar.gz
URL: http://papakupu.maori.nz/
License: LicenseRef-Fedora-Public-Domain
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-mi)

%description
Maori thesaurus.

%prep
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-35
- Prepare for Oreon 11 (RP1)
