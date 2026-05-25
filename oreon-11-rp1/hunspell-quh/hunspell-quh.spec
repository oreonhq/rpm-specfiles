%if 0%{?fedora} > 35 || 0%{?oreon}
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-quh
Summary: Quechua, South Bolivia hunspell dictionaries
%global upstreamid 20110816
Version: 0.%{upstreamid}
Release: 32%{?dist}
# Following links are dead now
# don't report any bugs
Source: http://www.runasimipi.org/quh_BO-pack.zip
URL: http://www.runasimipi.org/blanco-en.php?file=desarrollar-orto
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-quh)

%description
Quechua South Bolivia hunspell dictionaries.

%prep
%autosetup -n quh_BO-pack
unzip -qq quh_BO.zip

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p quh_BO/quh_BO.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc quh_BO/Copyright quh_BO/README_quh_BO.txt
%license quh_BO/COPYING
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20110816-32
- Import
