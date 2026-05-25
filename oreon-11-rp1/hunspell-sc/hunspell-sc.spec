%if 0%{?fedora} > 35 || 0%{?oreon}
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-sc
Summary: Sardinian hunspell dictionaries
%global upstreamid 20081101
Version: 0.%{upstreamid}
Release: 38%{?dist}
Source: https://ayera.dl.sourceforge.net/project/aoo-extensions/1446/2/dict_sc_it03.oxt
URL: http://extensions.services.openoffice.org/project/Dict_sc
#The license included is AGPLv3 and pkg-desc/pkg-description.txt
#says AGPLv3 or later, but the sc_IT.aff header states "GPLv2"
License: AGPL-3.0-or-later AND GPL-2.0-only
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell
Supplements: (hunspell and langpacks-sc)

%description
Sardinian hunspell dictionaries.

%prep
%autosetup -c -n hunspell-sc

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p sc_IT.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sc_IT.aff
cp -p sc_it.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/sc_IT.dic


%files
%license registration/agpl3-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20081101-38
- Import
