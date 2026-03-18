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
URL: http://download.savannah.gnu.org/releases/smc/Spellchecker/
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ml)

%description
Malayalam hunspell dictionaries

%prep
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
