%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ta
Summary: Tamil hunspell dictionaries
Version: 1.0.0
Release: 28%{?dist}
Epoch:   1
Source: http://anishpatil.fedorapeople.org/ta_in.%{version}.tar.gz
URL: https://gitorious.org/hunspell_dictionaries/hunspell_dictionaries.git
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ta)

%description
Tamil hunspell dictionaries.

%prep
%autosetup -c -n ta_IN

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ta_IN/*.dic ta_IN/*.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}

%files
%doc ta_IN/README
%license ta_IN/LICENSE ta_IN/Copyright
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-28
- Prepare for Oreon 11 (RP1)
