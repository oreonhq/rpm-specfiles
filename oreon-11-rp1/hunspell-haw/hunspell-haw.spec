%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon}
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-haw
Summary: Hawaiian hunspell dictionaries
Version: 0.03
Release: 20%{?dist}
Source: https://addons.mozilla.org/firefox/downloads/file/248540/hawaiian_spell_checker-%{version}-tb+fx+fn+sm.xpi
URL: http://borel.slu.edu/crubadan/
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-haw)

%description
Hawaiian hunspell dictionaries.

%prep
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/haw-US.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/haw.aff
cp -p dictionaries/haw-US.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/haw.dic


%files
%doc dictionaries/README_haw_US.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.03-20
- Import
