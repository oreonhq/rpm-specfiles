%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-mk
Summary: Macedonian hunspell dictionaries
%global upstreamid 20051126
Version: 0.%{upstreamid}
Release: 36%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/mk_MK.zip
URL: https://wiki.openoffice.org/wiki/Dictionaries
License: GPL-1.0-or-later
BuildArch: noarch
#change encoding name to use the name that iconv knows this under
Patch0: hunspell-mk-iconv.patch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-mk)

%description
Macedonian hunspell dictionaries.

%prep
%autosetup -c -n hunspell-mk

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_mk_MK.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-36
- Prepare for Oreon 11 (RP1)
