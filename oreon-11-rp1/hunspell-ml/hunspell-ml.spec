%global source0_hash 3fc7430ef257868caff2e5969a36f7ec295d980f49432864880871d086b2640e

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ml
Summary: Malayalam hunspell dictionaries
Version: 0.1
Release: 37%{?dist}
Source:        http://download.savannah.gnu.org/releases/smc/Spellchecker/ooo-hunspell-ml-0.1.tar.bz2
URL: http://download.savannah.gnu.org/releases/smc/Spellchecker/
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ml)

%description
Malayalam hunspell dictionaries

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n ooo-hunspell-ml-%{version}

%build
echo "Nothing to build..."

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc README
%license COPYING
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1-37
- Prepare for Oreon 11 (RP1)
