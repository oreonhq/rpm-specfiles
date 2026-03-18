%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-ln
Summary: Lingala hunspell dictionaries
Version: 0.02
Release: 33%{?dist}
Source: http://downloads.sourceforge.net/lingala/hunspell-ln-0.02.zip
URL: http://lingala.sourceforge.net/
License: GPL-2.0-or-later
BuildArch: noarch
Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-ln)

%description
Lingala hunspell dictionaries.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p ln_CD.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_ln_CD.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.02-33
- Prepare for Oreon 11 (RP1)
