Name: hyphen-fr
Summary: French hyphenation rules
Version: 3.0
Release: 20%{?dist}
Source: http://www.dicollecte.org/download/fr/hyph-fr-v3.0.zip
# oreon url source checksums begin
%global source0_sha256 61ec17d669a21e75969a2050a4615d7cea612ffd66d35fe9f4a8259c6d4bcd91
%global source0_file hyph-fr-v3.0.zip
# oreon url source checksums end
URL: http://www.dicollecte.org/download.php?prj=fr
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-fr)

%description
French hyphenation rules.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/hyph-fr-v3.0.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "61ec17d669a21e75969a2050a4615d7cea612ffd66d35fe9f4a8259c6d4bcd91" || { echo "oreon: Source0 SHA256 mismatch for hyph-fr-v3.0.zip" >&2; exit 1; })
# oreon verify url source checksums end
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
