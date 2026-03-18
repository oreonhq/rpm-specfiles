%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ht
Summary: Haitian Creole hunspell dictionaries
Version: 0.06
Release: 32%{?dist}
Source: http://extensions.services.openoffice.org/files/3247/3/%{name}-%{version}.oxt
URL: http://kok.logipam.org/
License: GPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ht)

%description
Haitian Creole hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/ht_HT.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc dictionaries/README_ht_HT.txt LICENSES-en.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.06-32
- Prepare for Oreon 11 (RP1)
