%global source0_hash none

Name: hyphen-es
Summary: Spanish hyphenation rules
Version: 2.3
Release: 21%{?dist}
Source:        https://github.com/sbosio/rla-es/releases/download/v2.3/es_ANY.oxt
URL: https://github.com/sbosio/rla-es/tree/master/separacion
License: LGPL-3.0-or-later OR GPL-3.0-or-later OR MPL-1.1
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-es)

%description
Spanish hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c -n %{name}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_es_ANY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_es.dic

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
es_aliases="es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_ES es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE"

for lang in $es_aliases; do
        ln -s hyph_es.dic hyph_$lang.dic
done
popd

%files
%doc README_hyph_es_ANY.txt
%license GPLv3.txt LGPLv3.txt MPL-1.1.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3-21
- Prepare for Oreon 11 (RP1)
