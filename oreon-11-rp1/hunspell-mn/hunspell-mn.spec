%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-mn
Summary: Mongolian hunspell dictionaries
%global upstreamid 20080709
Version: 0.%{upstreamid}
Release: 35%{?dist}
# Another Upstream https://extensions.openoffice.org/en/project/mongolian-spell-checking-dictionary
# gives below Source URL
Source: https://downloads.sourceforge.net/project/aoo-extensions/1408/0/dict-mn_0.06-5.oxt 
URL: http://mnspell.openmn.org
License: GPL-2.0-only
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-mn)

%description
Mongolian hunspell dictionaries.

%prep
%autosetup -c -n hunspell-mn

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p mn_MN.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc README_mn_MN.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-35
- Prepare for Oreon 11 (RP1)
