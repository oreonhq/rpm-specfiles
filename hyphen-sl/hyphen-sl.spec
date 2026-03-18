Name: hyphen-sl
Summary: Slovenian hyphenation rules
%global upstreamid 20070127
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/hyph_sl_SI.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-sl)

%description
Slovenian hyphenation rules.

%prep
%autosetup -c -n hyphen-sl

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sl_SI.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_sl_SI.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-34
- Prepare for Oreon 11 (RP1)
