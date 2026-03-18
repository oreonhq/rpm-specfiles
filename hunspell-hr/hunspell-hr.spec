%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-hr
Summary: Croatian hunspell dictionaries
%global upstreamid 20040608
Version: 0.%{upstreamid}
Release: 36%{?dist}
Epoch: 1
Source: http://cvs.linux.hr/spell/myspell/hr_HR.zip
URL: http://cvs.linux.hr/spell/
License: LGPL-2.1-or-later OR SISSL
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-hr)

%description
Croatian hunspell dictionaries.

%package -n hyphen-hr
Requires: hyphen
Summary: Croatian hyphenation rules
Supplements: (hyphen and langpacks-hr)

%description -n hyphen-hr
Croatian hyphenation rules.

%prep
%setup -q -c -n hunspell-hr

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p hr_HR.dic hr_HR.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_hr_HR.dic


%files
%doc README_hr_HR.txt
%{_datadir}/%{dict_dirname}/*

%files -n hyphen-hr
%doc README_hr_HR.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-36
- Prepare for Oreon 11 (RP1)
