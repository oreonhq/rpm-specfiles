Name: hyphen-id
Summary: Indonesian hyphenation rules
%global upstreamid 20040812
Version: 0.%{upstreamid}
Release: 34%{?dist}
Source: http://download.services.openoffice.org/contrib/dictionaries/hyph_id_ID.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL-1.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-id)

%description
Indonesian hyphenation rules.

%prep
%autosetup -c

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen


%files
%doc README_id_ID.txt
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.%{upstreamid}-34
- Prepare for Oreon 11 (RP1)
