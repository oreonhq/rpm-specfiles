%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif

Name: hunspell-si
Summary: Sinhala hunspell dictionaries
Version: 0.2.1
Release: 36%{?dist}
Source: http://www.sandaru1.com/si-LK.tar.gz
#Following URL is down since few months informed to upstream
URL: http://www.sandaru1.com/2009/08/29/sinhala-spell-checker-for-firefox/
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell
Supplements: (hunspell and langpacks-si)

%description
Sinhala hunspell dictionaries.

%prep
%setup -q -c -n hunspell-si

%build
#nothing to build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p dictionaries/si-LK.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/si_LK.aff
cp -p dictionaries/si-LK.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/si_LK.dic

%files
%doc LICENSE README
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.1-36
- Prepare for Oreon 11 (RP1)
