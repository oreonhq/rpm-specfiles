%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-da
Summary: Danish hunspell dictionaries
Version: 2.9.053
Release: 2%{?dist}
Source:        https://stavekontrolden.dk/dictionaries/da_DK/da_DK-%{version}.oxt
URL: https://stavekontrolden.dk/
# license information from README_da_DK.txt
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-da)

%description
Danish hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p da_DK.dic da_DK.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_da_DK.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.053-2
- Prepare for Oreon 11 (RP1)
