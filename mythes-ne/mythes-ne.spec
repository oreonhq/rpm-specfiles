Name: mythes-ne
Summary: Nepali thesaurus
Version: 1.1
Release: 32%{?dist}
Source0: http://download.services.openoffice.org/contrib/dictionaries/thes_ne_NP_v2.zip
URL: https://wiki.openoffice.org/wiki/Dictionaries
License: LGPL-2.0-or-later
BuildArch: noarch
BuildRequires: mythes-devel
Requires: mythes
Supplements: (mythes and langpacks-ne)

%description
Nepali thesaurus.

%prep
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_ne_NP_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes/


%files
%doc README_th_ne_NP_v2.txt
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-32
- Prepare for Oreon 11 (RP1)
