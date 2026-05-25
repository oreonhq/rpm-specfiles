%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || 0%{?oreon}
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ak
Summary: Akan hunspell dictionaries
Version: 0.9.1
Release: 22%{?dist}
Source: https://addons.mozilla.org/firefox/downloads/file/376172/akan_spelling_dictionary-0.9.1-typefix-fx.xpi
URL: http://kasahorow.org/content/akan-nsɛmfuaasekyerɛ
#https://addons.mozilla.org/en-US/firefox/versions/license/73122
License: LGPL-3.0-only
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ak)

%description
Akan hunspell dictionaries.

%prep
%autosetup -c

%build
chmod -x dictionaries/ak-GH.*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/ak-GH.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ak_GH.aff
cp -p dictionaries/ak-GH.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ak_GH.dic


%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.1-22
- Import
