%global forgeurl https://github.com/RedHatOfficial/ksc
%global commitdate 20210216
%global commit 5955c6b2288353c5b093677221cc91a83a2c800c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%{?python_enable_dependency_generator}
%forgemeta

Name:		ksc
Version:	1.7
Release:	14%{?dist}
Summary:	Kernel source code checker
Group:		Development/Tools
AutoReqProv:	no
License:	GPL-2.0-or-later
URL:		https://github.com/RedHatOfficial/ksc
BuildArch:	noarch
Requires:	kmod
Requires:	binutils
Requires:	kernel-devel
Requires:	python3-requests
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
Source0:	https://github.com/RedHatOfficial/ksc/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

%description
A kernel module source code checker to find usage of select symbols

%prep
%forgesetup
# Fix build with setuptools 62.1
# https://github.com/RedHatOfficial/ksc/issues/3
sed -i "15i packages=[]," setup.py

%build
%py3_build

%install
%py3_install
install -D ksc.1 %{buildroot}%{_mandir}/man1/ksc.1

%files
%license COPYING
%doc README PKG-INFO
%{_bindir}/ksc
%{_datadir}/ksc
%{_mandir}/man1/ksc.*
%config(noreplace) %{_sysconfdir}/ksc.conf
%{python3_sitelib}/ksc-%{version}*.egg-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7-14
- Prepare for Oreon 11 (RP1)
