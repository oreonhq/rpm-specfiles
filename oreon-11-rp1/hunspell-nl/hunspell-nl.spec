%global source0_hash 0a86ec393450d7070bd69ee83f69c37ff27dbbc5fe684803375f113d7128bd87

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif 

Name: hunspell-nl
Summary: Dutch hunspell dictionaries
Version: 2.20.19
Release: 17%{?dist}
Source:        https://github.com/OpenTaal/opentaal-hunspell/archive/refs/tags/2.20.19.tar.gz

URL: https://opentaal.org/
License: BSD-3-Clause OR CC-BY-3.0
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-nl)

%description
Dutch hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n opentaal-hunspell-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p nl.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/nl_NL.dic
cp -p nl.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/nl_NL.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
nl_NL_aliases="nl_AW nl_BE"
for lang in $nl_NL_aliases; do
        ln -s nl_NL.aff $lang.aff
        ln -s nl_NL.dic $lang.dic
done


%files
%doc LICENSE.txt README.md
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.20.19-17
- Prepare for Oreon 11 (RP1)
