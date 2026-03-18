%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ca
Summary: Catalan hunspell dictionaries
Version: 3.0.8
Release: 7%{?dist}
Source: https://github.com/Softcatala/catalan-dict-tools/releases/download/v%{version}/ca.%{version}-hunspell.zip
URL: https://www.softcatala.org/projectes/corrector-ortografic/
License: GPL-2.0-or-later OR LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ca)

%description
Catalan hunspell dictionaries.

%prep
%setup -q -c

%build
tr -d '\r' < catalan.aff > ca_ES.aff
touch -r catalan.aff ca_ES.aff
tr -d '\r' < catalan.dic > ca_ES.dic
touch -r catalan.dic ca_ES.dic

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ca_ES.dic ca_ES.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
ca_ES_aliases="ca_AD ca_FR ca_IT"
for lang in $ca_ES_aliases; do
        ln -s ca_ES.aff $lang.aff
        ln -s ca_ES.dic $lang.dic
done
popd


%files
%doc README.txt release-notes_en.txt
%license LICENSE gpl-2.0.txt lgpl-2.1.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.8-7
- Prepare for Oreon 11 (RP1)
