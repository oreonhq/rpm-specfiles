%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-th
Summary: Thai hunspell dictionaries
%global upstreamid 20061212
Version: 0.%{upstreamid}
Release: 36%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/th_TH.zip
URL: https://wiki.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-th)

%description
Thai hunspell dictionaries.

%prep
%setup -q -c -n hunspell-th

%build
#set encoding to IANA prefered name
sed -i -e 's/TIS620-2533/TIS620/g' th_TH.aff
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_th_TH.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-36
- Prepare for Oreon 11 (RP1)
