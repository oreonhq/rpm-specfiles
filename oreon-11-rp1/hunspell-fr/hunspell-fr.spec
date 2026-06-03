%global source0_hash 2dd9ce5fa04641ac0a8a70048fd0502b619765dbdaeae55f3dfd8f1e0e1aece6

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fr
Summary: French hunspell dictionaries
Version: 7.0
Release: 2%{?dist}
Source:        https://deb.debian.org/debian/pool/main/h/hunspell-fr/hunspell-fr_7.0.orig.tar.xz
URL: https://grammalecte.net/
License: MPL-2.0
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-fr)

%description
French (France, Belgium, etc.) hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n hunspell-fr

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p fr-toutesvariantes.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fr_FR.dic
cp -p fr-toutesvariantes.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/fr_FR.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
fr_FR_aliases="fr_BE fr_CA fr_CH fr_LU fr_MC"
for lang in $fr_FR_aliases; do
	ln -s fr_FR.aff $lang.aff
	ln -s fr_FR.dic $lang.dic
done
popd


%files
%doc README_dict_fr.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0-2
- Import
