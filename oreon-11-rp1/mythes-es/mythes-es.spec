%global source0_hash 8313cd843bbf235849278ad2ce04eb66a76b22332f68190a1ca7726d7a5c890d

Name: mythes-es
Summary: Spanish thesaurus
Version: 2.8
Release: %autorelease
Source:        https://github.com/sbosio/rla-es/releases/download/v%{version}/es.oxt#/mythes-es-%{version}.oxt
URL: https://github.com/sbosio/rla-es/tree/master/sinonimos
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-es)

%description
Spanish thesaurus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n %{name}


%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_es_v2.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_es_ES_v2.dat
cp -p th_es_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_es_ES_v2.idx

pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
es_aliases="es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE"

for lang in $es_aliases; do
        ln -s th_es_ES_v2.dat "th_"$lang"_v2.dat"
        ln -s th_es_ES_v2.idx "th_"$lang"_v2.idx"
done
popd


%files
%doc README_th_es.txt
%{_datadir}/mythes/*

%changelog
%autochangelog
