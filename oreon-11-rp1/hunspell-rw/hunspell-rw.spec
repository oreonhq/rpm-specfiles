%if 0%{?fedora} > 35 || 0%{?oreon}
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-rw
Summary: Kinyarwanda hunspell dictionaries
%global upstreamid 20050109
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/rw_RW.zip
URL: http://borel.slu.edu/crubadan/apps.html
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-rw)

%description
Kinyarwanda hunspell dictionaries.

%prep
%autosetup -c -n hunspell-rw

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p rw_RW.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc README_rw_RW.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20050109-35
- Import
