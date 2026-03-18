Name:           python-kmod
License:        LGPL-2.0-or-later
Summary:        Python module to work with kernel modules
Version:        0.9.2
Release:        12%{?dist}
URL:            https://github.com/maurizio-lombardi/python-kmod/
Source0:        https://github.com/downloads/maurizio-lombardi/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3
BuildRequires:  kmod-devel

%global _description\
Python module to allow listing, loading, and unloading\
Linux kernel modules, using libkmod.

%description %_description

%package -n python3-kmod
Summary:        Python module to work with kernel modules

%description -n python3-kmod
Python module to allow listing, loading, and unloading
Linux kernel modules, using libkmod.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%files -n python3-kmod
%{python3_sitearch}/kmod/
%{python3_sitearch}/kmod*.egg-info
%doc COPYING.LESSER README

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.2-12
- Prepare for Oreon 11 (RP1)
