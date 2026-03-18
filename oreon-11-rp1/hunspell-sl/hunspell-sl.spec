%if 0%{?fedora} > 35
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif
Name: hunspell-sl
Summary: Slovenian hunspell dictionaries
%global upstreamid 20070127
Version: 0.%{upstreamid}
Release: 37%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/sl_SI.zip
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/
License: GPL-1.0-or-later OR LGPL-2.1-or-later
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-sl)

%description
Slovenian hunspell dictionaries.

%prep
%autosetup -c -n hunspell-sl

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README_sl_SI.txt
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-37
- Prepare for Oreon 11 (RP1)
