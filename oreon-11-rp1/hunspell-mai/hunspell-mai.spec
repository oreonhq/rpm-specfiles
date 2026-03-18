%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-mai
Summary: Maithili hunspell dictionaries
Version: 1.0.1
Release: 34%{?dist}
Source: https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/bhashaghar/mai_IN.oxt
URL: https://code.google.com/archive/p/bhashaghar/wikis/Maithili.wiki
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-mai)

%description
Maithili hunspell dictionaries.

%prep
%autosetup -c -n hunspell-mai

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p mai_IN.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/

%files
%doc README_mai_IN.txt
%license COPYING COPYING.MPL COPYING.GPL COPYING.LGPL
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.1-34
- Prepare for Oreon 11 (RP1)
