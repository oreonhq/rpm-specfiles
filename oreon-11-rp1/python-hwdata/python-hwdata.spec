Name:		python-hwdata
Version:	2.4.3
Release:	6%{?dist}
Summary:	Python bindings to hwdata package
BuildArch:  noarch
License:	GPL-2.0-or-later
URL:		https://github.com/xsuchy/python-hwdata
# git clone https://github.com/xsuchy/python-hwdata.git
# cd python-hwdata
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz

%description
Provide python interface to database stored in hwdata package.
It allows you to get human readable description of USB and PCI devices.

%package -n python3-hwdata
Summary:	Python bindings to hwdata package

BuildRequires:	python3-devel

%{?python_provide:%python_provide python3-hwdata}

%description -n python3-hwdata
Provide python interface to database stored in hwdata package.
It allows you to get human readable description of USB and PCI devices.

This is the Python 3 build of the module.

%generate_buildrequires
%pyproject_buildrequires

%prep
%setup -q

%build
%pyproject_wheel

%install
%pyproject_install

%check
%py3_check_import hwdata

%files -n python3-hwdata
%license LICENSE
%doc README.md example.py
%doc html
%{python3_sitelib}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.3-6
- Import
