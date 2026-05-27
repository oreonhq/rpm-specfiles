%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif

Name: hunspell-oc
Summary: Occitan hunspell dictionaries
Version: 1.5
Release: 8%{?dist}
Source: https://addons.mozilla.org/firefox/downloads/file/4085695/diccionari_occitan_lengadocian-%{version}.xpi
URL: https://addons.mozilla.org/en-US/firefox/addon/diccionari-occitan-lengadocian/
# https://www.mozilla.org/en-US/MPL/2.0/combining-mpl-and-gpl/
# oc_FR.aff is MPL-2.0
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-oc)

%description
Occitan hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hunspell-oc

%build
# nothing here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/oc_FR.aff dictionaries/oc_FR.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5-8
- Prepare for Oreon 11 (RP1)
