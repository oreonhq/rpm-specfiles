%global source0_hash 2806b2f49903b3f77ded3204f580eb0d7b8d9a74775ca2801f6394211d86e2d7

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
