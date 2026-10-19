%global source0_hash 58f7f86d63b9f4052c90f4964a37b608b4defabf0723902fa9b6f007a35fbdd4
Name: mythes-ru
Summary:        Russian thesaurus
%global upstreamid 20070613
Version: 0.%{upstreamid}
Release:        1%{?dist}
Source0:        http://download.i-rs.ru/pub/openoffice/dict/thes_ru_RU_v2.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-ru)
# oreon:deps
BuildRequires:  unzip
# /oreon:deps
%description
Russian thesaurus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_ru_RU_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
ru_RU_aliases="ru_UA"
for lang in $ru_RU_aliases; do
        ln -s th_ru_RU_v2.idx "th_"$lang"_v2.idx"
        ln -s th_ru_RU_v2.dat "th_"$lang"_v2.dat"
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070613-35
- Import
