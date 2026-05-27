%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-grc
Summary: Ancient Greek hunspell dictionaries
Version: 2.1.5
Release: 35%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/2313/1/grc.oxt
URL: http://www.himeros.eu/
License: GPL-1.0-or-later OR LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-grc)

%description
Ancient Greek hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/grc_GR.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/grc.aff
cp -p dictionaries/grc_GR.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/grc.dic


%files
%doc LICENSES-en.txt         

%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.5-35
- Prepare for Oreon 11 (RP1)
