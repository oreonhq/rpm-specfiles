%global source0_hash none

%if 0%{?fedora} > 35 || (0%{?oreon} >= 11)
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-ru
Summary: Russian hunspell dictionaries
Version: 0.99g5
Release: 32%{?dist}
Epoch: 1
# Upstream source is gone now and recent alternative don't have license
# Source: http://releases.mozilla.org/pub/mozilla.org/addons/3703/russian_spellchecking_dictionary-0.4.4-fx+tb+sm.xpi
Source: russian_spellchecking_dictionary-0.4.4-fx+tb+sm.xpi
URL: http://scon155.phys.msu.su/eng/lebedev.html
License: BSD-3-Clause-Modification
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-ru)

%description
Russian hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hunspell-ru

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/ru.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ru_RU.dic
cp -p dictionaries/ru.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ru_RU.aff
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
ru_RU_aliases="ru_UA"
for lang in $ru_RU_aliases; do
        ln -s ru_RU.aff $lang.aff
        ln -s ru_RU.dic $lang.dic
done


%files
%doc dictionaries/Changelog dictionaries/LICENSE dictionaries/README
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.99g5-32
- Import
