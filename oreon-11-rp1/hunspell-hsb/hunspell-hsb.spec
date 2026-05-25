%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon}
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-hsb
Summary: Upper Sorbian hunspell dictionaries
Version: 0.20060327.3
Release: 31%{?dist}
Source: https://addons.mozilla.org/firefox/downloads/file/113003/upper_sorbian_spelling_dictionary-0.0.20060327.3-tb+fx+sm.xpi
URL: http://sorbzilla.de/
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-hsb)

%description
Upper Sorbian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-hsb

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/hsb.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/hsb_DE.aff
cp -p dictionaries/hsb.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/hsb_DE.dic


%files
%doc COPYING README
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20060327.3-31
- Import
