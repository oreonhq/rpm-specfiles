%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ml
Summary: Malayalam hunspell dictionaries
Version: 0.1
Release: 37%{?dist}
Source: http://download.savannah.gnu.org/releases/smc/Spellchecker/ooo-hunspell-ml-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 3fc7430ef257868caff2e5969a36f7ec295d980f49432864880871d086b2640e
%global source0_file ooo-hunspell-ml-0.1.tar.bz2
# oreon url source checksums end
URL: http://download.savannah.gnu.org/releases/smc/Spellchecker/
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ml)

%description
Malayalam hunspell dictionaries

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ooo-hunspell-ml-0.1.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3fc7430ef257868caff2e5969a36f7ec295d980f49432864880871d086b2640e" || { echo "oreon: Source0 SHA256 mismatch for ooo-hunspell-ml-0.1.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
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
