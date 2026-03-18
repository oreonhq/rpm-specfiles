%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-tpi
Summary: Tok Pisin hunspell dictionaries
Version: 0.07
Release: 29%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/4824/3/hunspell-tpi-0.07.oxt
URL: http://extensions.services.openoffice.org/en/project/tok-pisin-spell-checker
License: GPL-3.0-or-later
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-tpi)

%description
Tok Pisin hunspell dictionaries.

%prep
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/tpi_PG.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc dictionaries/README_tpi_PG.txt
%license LICENSES-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.07-29
- Prepare for Oreon 11 (RP1)
