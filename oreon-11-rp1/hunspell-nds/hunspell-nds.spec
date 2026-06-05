%global source0_hash ee6ce9007b5c0a632a39515cee216fa07e556567577a1fc9821e18fb2b170170

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-nds
Summary: Lowlands Saxon hunspell dictionaries
Version: 0.1
Release: 34%{?dist}
URL: http://aspell-nds.sourceforge.net/
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-nds)

Source0:        https://downloads.sourceforge.net/aspell-nds/hunspell-nds-0.1.zip

%description
Lowlands Saxon hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n hunspell-nds

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p nds.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/nds_DE.aff
cp -p nds.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/nds_DE.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/
nds_DE_aliases="nds_NL"
for lang in $nds_DE_aliases; do
        ln -s nds_DE.aff $lang.aff
        ln -s nds_DE.dic $lang.dic
done
popd

%files
%doc README_nds.txt Copyright COPYING
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1-34
- Prepare for Oreon 11 (RP1)
