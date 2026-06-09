%global source0_hash fdeb5ab1c9ed703ff5cc4d304fb59a3ffd966f8a16f5b263999dcd747b0f30f7

Name: zaf
Summary: South Africa hyphenation rules
%define upstreamid 20080714
Version: 0
Release: 0.33.%{upstreamid}svn%{?dist}
Source0:        https://github.com/LibreOffice/dictionaries/archive/refs/heads/master.tar.gz#/zaf-0.tar.gz
URL: https://github.com/LibreOffice/dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
BuildRequires: tar

%description
South Africa hyphenation rules.

%package -n hyphen-af
Summary: Afrikaans hyphenation rules
Requires: hyphen

%description -n hyphen-af
Afrikaans hyphenation rules.

%package -n hyphen-zu
Summary: Zulu hyphenation rules
Requires: hyphen

%description -n hyphen-zu
Zulu hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
rm -rf zaf dictionaries-*
tar xzf %{SOURCE0}
_dict=$(ls -d dictionaries-*)
mkdir -p zaf/af/hyph zaf/zu/hyph
  cp -p $_dict/af_ZA/hyph_af_ZA.dic zaf/af/hyph/hyph_af_ZA.dic
  cp -p $_dict/zu_ZA/hyph_zu_ZA.dic zaf/zu/hyph/hyph_zu_ZA.dic
cp -p $_dict/af_ZA/README_af_ZA.txt zaf/af/README
printf "LibreOffice dictionaries\n" > zaf/af/CREDITS
cp -p zaf/af/README zaf/af/COPYING
cp -p zaf/af/README zaf/zu/README
cp -p zaf/af/CREDITS zaf/zu/CREDITS
cp -p zaf/af/COPYING zaf/zu/COPYING
rm -rf $_dict

%build

%install
mkdir -p %{buildroot}%{_datadir}/hyphen
cp -p zaf/af/hyph/hyph_af_ZA.dic %{buildroot}%{_datadir}/hyphen/
cp -p zaf/zu/hyph/hyph_zu_ZA.dic %{buildroot}%{_datadir}/hyphen/

pushd %{buildroot}%{_datadir}/hyphen/
af_ZA_aliases="af_NA"
for lang in $af_ZA_aliases; do
        ln -sf hyph_af_ZA.dic hyph_$lang.dic
done
popd

%files -n hyphen-af
%doc zaf/af/CREDITS zaf/af/README
%license zaf/af/COPYING
%{_datadir}/hyphen/hyph_af*

%files -n hyphen-zu
%doc zaf/zu/CREDITS zaf/zu/README
%license zaf/zu/COPYING
%{_datadir}/hyphen/hyph_zu*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0-0.33.20080714svn
- Import
