%global source0_hash none

Name: hyphen-fr
Summary: French hyphenation rules
Version: 26.8.0.3.orig
Release: 1%{?dist}
Source: https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_26.8.0.3.orig.tar.xz#/libreoffice-dictionaries-26.8.0.3.orig.tar.xz
URL: https://github.com/LibreOffice/dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-fr)

%description
French hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-%{version}

%build
chmod -x dictionaries/fr_FR/hyph_fr.dic

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p dictionaries/fr_FR/hyph_fr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_fr_FR.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
fr_FR_aliases="fr_BE fr_CA fr_CH fr_LU fr_MC"
for lang in $fr_FR_aliases; do
        ln -s hyph_fr_FR.dic hyph_$lang.dic
done
popd

%files
%doc dictionaries/fr_FR/README_hyph_fr.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0-20
- Import
