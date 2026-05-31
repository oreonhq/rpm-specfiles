%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ts
Summary: Tsonga hunspell dictionaries
%global upstreamid 20110323.1
Version: 0.%{upstreamid}
Release: 20%{?dist}
Source:https://addons.mozilla.org/firefox/downloads/file/376225/tsonga_spell_checker-20110323.1-typefix-fn+sm+tb+fx.xpi 
URL: https://addons.mozilla.org/en-US/firefox/addon/tsonga-spell-checker/
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ts)

%description
Tsonga hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c -n hunspell-ts

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/ts-ZA.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ts_ZA.aff
cp -p dictionaries/ts-ZA.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ts_ZA.dic


%files
%doc README-ts-ZA.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20110323.1-20
- Import
