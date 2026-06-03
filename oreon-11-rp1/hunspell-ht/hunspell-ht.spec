%global source0_hash 3aed6c3fe4e009b4a228d83366d4132030320e20215b939ea3f6f227dfe9c563

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ht
Summary: Haitian Creole hunspell dictionaries
Version: 0.06
Release: 32%{?dist}
Source:        https://downloads.sourceforge.net/project/aoo-extensions/3247/3/hunspell-ht-0.06.oxt
URL: http://kok.logipam.org/
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ht)

%description
Haitian Creole hunspell dictionaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/ht_HT.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc dictionaries/README_ht_HT.txt LICENSES-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.06-32
- Import
