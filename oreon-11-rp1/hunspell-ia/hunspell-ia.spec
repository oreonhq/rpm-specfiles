%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ia
Summary: Interlingua hunspell dictionaries
%global upstreamid 20240316
Version: 0.%{upstreamid}
Release: 2%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/2215/12/dict-ia-2024-03-16.oxt
# Another URL is https://addons.mozilla.org/en-US/firefox/addon/dict-ia/
URL: https://extensions.openoffice.org/en/project/interlingua-dictionario-orthographic-e-regulas-de-division-de-parolas.html
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ia)

%description
Interlingua hunspell dictionaries.

%prep
%autosetup -c

%build
# nothing here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ia.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%license GPLv3.txt
%doc README_dict-ia.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-2
- Prepare for Oreon 11 (RP1)
