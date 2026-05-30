%global source0_hash none

Name: mythes-es
Summary: Spanish thesaurus
Version: 2.3
Release: 20%{?dist}
Source:        https://github.com/sbosio/rla-es/releases/download/v%{version}/es_ANY.oxt
URL: https://github.com/sbosio/rla-es/tree/master/sinonimos
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-es)

%description
Spanish thesaurus.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c -n %{name}


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_es_ES_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
es_aliases="es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE"

for lang in $es_aliases; do
        ln -s th_es_ES_v2.dat "th_"$lang"_v2.dat"
        ln -s th_es_ES_v2.idx "th_"$lang"_v2.idx"
done
popd

mv COPYING_th_es_ES COPYING

%files
%doc README_th_es_ES.txt
%license COPYING
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3-20
- Prepare for Oreon 11 (RP1)
