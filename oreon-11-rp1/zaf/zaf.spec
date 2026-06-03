%global source0_hash none

Name: zaf
Summary: South Africa hyphenation rules
%define upstreamid 20080714
Version: 0
Release: 0.33.%{upstreamid}svn%{?dist}
Source0: zaf-0-0.1.%{upstreamid}svn.tar.bz2
URL: https://github.com/LibreOffice/dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
BuildRequires: curl
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
_tar="zaf-0-0.1.%{upstreamid}svn.tar.bz2"
if test ! -f "$_tar"; then
  curl -sfL -o _dict.tar.gz "https://github.com/LibreOffice/dictionaries/archive/refs/heads/master.tar.gz"
  rm -rf zaf dictionaries-*
  mkdir -p zaf/af/hyph zaf/zu/hyph
  tar xzf _dict.tar.gz
  _dict=$(ls -d dictionaries-*)
  cp -p $_dict/af_ZA/hyph_af_ZA.dic zaf/af/hyph/
  cp -p $_dict/zu_ZA/hyph_zu_ZA.dic zaf/zu/hyph/
  cp -p $_dict/af_ZA/README_af_ZA.txt zaf/af/README
  printf "LibreOffice dictionaries\n" > zaf/af/CREDITS
  cp -p zaf/af/README zaf/af/COPYING
  cp -p zaf/af/README zaf/zu/README
  cp -p zaf/af/CREDITS zaf/zu/CREDITS
  cp -p zaf/af/COPYING zaf/zu/COPYING
  tar cjf "$_tar" zaf
  rm -rf _dict.tar.gz $_dict zaf
fi
test "%{source0_hash}" = "none" || { f="$_tar"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n zaf

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p ./af/hyph/hyph_af_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p ./zu/hyph/hyph_zu_ZA.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
af_ZA_aliases="af_NA"
for lang in $af_ZA_aliases; do
        ln -s hyph_af_ZA.dic hyph_$lang.dic
done
popd

%files -n hyphen-af
%doc af/CREDITS af/README
%license af/COPYING
%{_datadir}/hyphen/hyph_af*

%files -n hyphen-zu
%doc zu/CREDITS zu/README
%license zu/COPYING
%{_datadir}/hyphen/hyph_zu*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0-0.33.20080714svn
- Import
