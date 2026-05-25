Name: mythes-cs
Summary: Czech thesaurus
%global upstreamid 20070926
Version: 0.%{upstreamid}
Release: 37%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/thes_cs_CZ_v2.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: MIT
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-cs)

%description
Czech thesaurus.

%prep
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_cs_CZ_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes


%files
%doc th_cs_CZ_license.txt
%{_datadir}/mythes/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070926-37
- Import
