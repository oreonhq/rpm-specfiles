Name: hyphen-fr
Summary: French hyphenation rules
Version: 3.0
Release: 20%{?dist}
Source: http://www.dicollecte.org/download/fr/hyph-fr-v3.0.zip
URL: http://www.dicollecte.org/download.php?prj=fr
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-fr)

%description
French hyphenation rules.

%prep
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_fr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_fr_FR.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
fr_FR_aliases="fr_BE fr_CA fr_CH fr_LU fr_MC"
for lang in $fr_FR_aliases; do
        ln -s hyph_fr_FR.dic hyph_$lang.dic
done
popd


%files
%doc README_hyph_fr-3.0.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0-20
- Import
