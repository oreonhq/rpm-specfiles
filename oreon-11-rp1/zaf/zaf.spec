%global source0_hash d16958cd5eee0ad1d44c3631ed15f8e2a437716ccf9a415ada70a8429704e705
Name: zaf
Summary:        South Africa hyphenation rules
%define upstreamid 20080714
Version: 0
Release:        1%{?dist}
Source0:        https://github.com/LibreOffice/dictionaries/archive/refs/heads/master.tar.gz#/zaf-0.tar.gz
URL: https://github.com/LibreOffice/dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
# oreon:deps
BuildRequires:  tar
# /oreon:deps
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
%oreon_autofiles hyphen-af usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles hyphen-zu usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hyphen-af -f %{oreon_filedir}/hyphen-af.list
%files -n hyphen-zu -f %{oreon_filedir}/hyphen-zu.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0-0.33.20080714svn
- Import
