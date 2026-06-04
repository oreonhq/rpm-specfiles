%global source0_hash none

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-fa
Summary: Farsi hunspell dictionaries
%global upstreamid 20070116
Version: 0.%{upstreamid}
Release: 38%{?dist}
Source0:        https://github.com/LibreOffice/dictionaries/archive/refs/heads/master.tar.gz
URL:            https://github.com/LibreOffice/dictionaries
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-fa)

%description
Farsi hunspell dictionaries.

%prep
%autosetup -c -T -n dictionaries-master

%build
# nothing to build here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p fa_IR/fa_IR.dic fa_IR/fa_IR.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/

%files
%{_datadir}/%{dict_dirname}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070116-38
- Import
