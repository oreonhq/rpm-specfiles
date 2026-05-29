%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-dsb
Summary: Lower Sorbian hunspell dictionaries
Version: 1.4.8
Release: 21%{?dist}
Source:        https://downloads.sourceforge.net/project/aoo-extensions/3045/14/lower_sorbian_spelling_dictionary-1.4.8.oxt
URL: http://dsb-spell.sourceforge.net
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-dsb)

%description
Lower Sorbian hunspell dictionaries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dsb_DE.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc description/desc_de.txt description/desc_en.txt description/desc_pl.txt
%license registration/license_en.txt  

%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.8-21
- Prepare for Oreon 11 (RP1)
