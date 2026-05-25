Name: zaf
Summary: South Africa hyphenation rules
%define upstreamid 20080714
Version: 0
Release: 0.33.%{upstreamid}svn%{?dist}
Source: zaf-0-0.1.%{upstreamid}svn.tar.bz2
# Below URL is dead now, don't file any bugs for updating it.
URL: http://zaf.sourceforge.net/
#Hyphenation rules are already generated in upstream code
License: LGPL-2.1-or-later
BuildArch: noarch

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
