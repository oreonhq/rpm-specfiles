Name: mythes-ro
Summary: Romanian thesaurus
Version: 3.3
Release: 32%{?dist}
Source: http://downloads.sourceforge.net/rospell/th_ro_RO.%{version}.zip
URL: http://rospell.sourceforge.net/
License: GPL-2.0-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-ro)

%description
Romanian thesaurus.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_ro_RO.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ro_RO_v2.dat
cp -p th_ro_RO.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ro_RO_v2.idx


%files
%doc README COPYING.GPL 
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3-32
- Prepare for Oreon 11 (RP1)
