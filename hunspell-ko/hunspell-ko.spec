%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ko
Summary: Korean hunspell dictionaries
Version: 0.7.0
Release: 23%{?dist}
Source: https://github.com/spellcheck-ko/hunspell-dict-ko/archive/%{version}.tar.gz
URL: https://github.com/spellcheck-ko/hunspell-dict-ko
License: MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-only
BuildArch: noarch
BuildRequires: python3
BuildRequires: hunspell
BuildRequires: make
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ko)

%description
Korean hunspell dictionaries.

%prep
%setup -q -n hunspell-dict-ko-%{version}

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ko.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ko_KR.aff
cp -p ko.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/ko_KR.dic

%check
make test

%files
%doc README.md
%license LICENSE LICENSE.GPL LICENSE.LGPL LICENSE.MPL
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-23
- Prepare for Oreon 11 (RP1)
