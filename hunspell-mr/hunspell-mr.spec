%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-mr
Summary: Marathi hunspell dictionaries
Version: 15.02webext
Release: 2%{?dist}
Epoch: 1
Source: https://addons.mozilla.org/firefox/downloads/file/4592209/marathi_dictionary-15.02webext.xpi
URL: https://addons.mozilla.org/en-US/firefox/addon/marathi-dictionary/
# license information is taken from above URL
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-mr)

%description
Marathi hunspell dictionaries.

%prep
%autosetup -c

%build
#nothing to do here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/mr-IN.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/mr_IN.dic
cp -p dictionaries/mr-IN.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/mr_IN.aff

%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.02webext-2
- Prepare for Oreon 11 (RP1)
