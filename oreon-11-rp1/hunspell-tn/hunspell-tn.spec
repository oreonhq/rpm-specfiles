%global source0_hash 030bae2910a93220fdea8f7eb90aa37f4a62900d4619e636c317b048dcbc4d02

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-tn
Summary: Tswana hunspell dictionaries
%global upstreamid 20150904
Version: 0.%{upstreamid}
Release: 20%{?dist}
Source:        tswana_spell_checker-20150904-sm+tb+fx+an+fn.xpi
URL: https://addons.mozilla.org/en-US/firefox/addon/tswana-spell-checker/
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-tn)

%description
Tswana hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -c -n hunspell-tn

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/tn-ZA.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/tn_ZA.aff
cp -p dictionaries/tn-ZA.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/tn_ZA.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
tn_ZA_aliases="tn_BW"
for lang in $tn_ZA_aliases; do
        ln -s tn_ZA.aff $lang.aff
        ln -s tn_ZA.dic $lang.dic
done
popd


%files
%doc dictionaries/README_tn_ZA.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20150904-20
- Import
