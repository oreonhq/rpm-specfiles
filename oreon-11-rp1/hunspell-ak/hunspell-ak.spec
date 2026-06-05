%global source0_hash f12af065aeea2a1acb37a359a215cb0404dbdd075f766faaf330dba41822869e

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ak
Summary: Akan hunspell dictionaries
Version: 0.9.1
Release: 22%{?dist}
URL: http://kasahorow.org/content/akan-nsɛmfuaasekyerɛ
#https://addons.mozilla.org/en-US/firefox/versions/license/73122
License: LGPL-3.0-only
BuildArch: noarch
BuildRequires: redland

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ak)

Source0:        https://github.com/openela-main/hunspell-ak/raw/el9/SOURCES/akan_spelling_dictionary-0.9.1-typefix-fx.xpi

%description
Akan hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
unzip -q %{SOURCE0}

%build
rdfproc hunspell-oc parse install.rdf
rdfproc hunspell-oc print | grep install-manifest | grep -v targetApplication | sed -e 's/.*#//' | sed -e 's/], "/: /'| sed -e 's/"}//' > CREDITS
chmod -x dictionaries/ak-GH.*

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/ak-GH.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ak_GH.aff
cp -p dictionaries/ak-GH.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ak_GH.dic

%files
%doc CREDITS
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.1-22
- Import
