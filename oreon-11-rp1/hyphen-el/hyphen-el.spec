%global source0_hash 8609bd1f835839b2b44ebd3587a2c4fc25327fb22f7de02a7528cae39d9d17d5

Name: hyphen-el
Summary: Greek hyphenation rules
%global upstreamid 20051018
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source:        http://download.services.openoffice.org/contrib/dictionaries/hyph_el_GR.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-el)

%description
Greek hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
el_GR_aliases="el_CY"
for lang in $el_GR_aliases; do
        ln -s hyph_el_GR.dic hyph_$lang.dic
done


%files
%doc README_hyph_el_GR.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20051018-35
- Import
