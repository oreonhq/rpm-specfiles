%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-hi
Summary: Hindi hunspell dictionaries
Version: 1.0.0
Release: 28%{?dist}
Epoch:   1
Source:  http://anishpatil.fedorapeople.org/hi_in.%{version}.tar.gz
URL: https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-hi)

%description
Hindi hunspell dictionaries.

%prep
%autosetup -c -n hi_IN
iconv -f ISO-8859-1 -t UTF-8 hi_IN/Copyright > hi_IN/Copyright.utf8
mv hi_IN/Copyright.utf8 hi_IN/Copyright

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p hi_IN/*.dic hi_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc hi_IN/README
%license hi_IN/COPYING hi_IN/Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-28
- Prepare for Oreon 11 (RP1)
