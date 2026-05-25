%if 0%{?fedora} > 35 || 0%{?oreon}
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-pl
Summary: Polish hunspell dictionaries
%global upstreamid 20240901
Version: 0.%{upstreamid}
Release: 4%{?dist}
Source: https://sjp.pl/sl/ort/sjp-myspell-pl-%{upstreamid}.zip
URL: https://sjp.pl/sl/ort/
License: LGPL-2.1-or-later OR GPL-1.0-or-later OR MPL-1.1 OR Apache-2.0 OR CC-BY-SA-4.0
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-pl)

%description
Polish hunspell dictionaries.

%prep
%autosetup -c hunspell-pl

%build
unzip pl_PL.zip

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_pl_PL.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20240901-4
- Import
