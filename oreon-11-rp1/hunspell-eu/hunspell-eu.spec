%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-eu
Summary: Basque hunspell dictionaries
Version: 5.1
Release: 15%{?dist}
Source0: http://xuxen.eus/static/hunspell/xuxen_%{version}_hunspell.zip
URL: http://xuxen.eus
License: LGPL-3.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-eu)

%description
Basque hunspell dictionaries.

%prep
%setup -q -c -n hunspell-eu

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
cp -p eu_ES.dic %{buildroot}%{_datadir}/%{dict_dirname}/eu_ES.dic
cp -p eu_ES.aff %{buildroot}%{_datadir}/%{dict_dirname}/eu_ES.aff


%files
%license LICENSE.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1-15
- Prepare for Oreon 11 (RP1)
