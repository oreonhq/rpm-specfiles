%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-hy
Summary: Armenian hunspell dictionaries
Version: 0.20.0
Release: 32%{?dist}
Source: http://downloads.sourceforge.net/armspell/myspell-hy-%{version}.tar.gz
URL: http://sourceforge.net/projects/armspell
License: GPL-2.0-or-later
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-hy)

%description
Armenian hunspell dictionaries.

%prep
%setup -q -n myspell-hy-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p hy_AM.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/


%files
%doc Copyright ChangeLog COPYING
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20.0-32
- Prepare for Oreon 11 (RP1)
