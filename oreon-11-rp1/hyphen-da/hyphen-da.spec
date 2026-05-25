Name: hyphen-da
Summary: Danish hyphenation rules
%global upstreamid 20070903
Version: 0.%{upstreamid}
Release: 35%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/hyph_da_DK.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
Patch0: hyphen-da-lppl-license-fix.patch
License: LGPL-2.1-or-later
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-da)

%description
Danish hyphenation rules.

%prep
%autosetup -c -n hyphen-da
chmod -x *

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_da_DK.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_hyph_da_DK.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20070903-35
- Import
