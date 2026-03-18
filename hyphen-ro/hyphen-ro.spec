Name: hyphen-ro
Summary: Romanian hyphenation rules
Version: 3.3.6
Release: 31%{?dist}
Source: http://downloads.sourceforge.net/rospell/hyph_ro_RO.3.3.6.zip
URL: http://rospell.sourceforge.net/
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hyphen
Supplements: (hyphen and langpacks-ro)

%description
Romanian hyphenation rules.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/


%files
%doc COPYING.GPL README          
%{_datadir}/hyphen/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.6-31
- Prepare for Oreon 11 (RP1)
