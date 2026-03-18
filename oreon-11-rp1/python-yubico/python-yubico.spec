%{?python_enable_dependency_generator}
%global srcname yubico

Name:           python-%{srcname}
Version:        1.3.3
Release:        23%{?dist}
Summary:        Pure-python library for interacting with Yubikeys

License:        BSD-2-Clause
URL:            https://github.com/Yubico/%{name}
Source0:        https://github.com/Yubico/%{name}/archive/%{name}-%{version}.tar.gz
Patch0001:      0001-literal-comparison.patch

BuildArch:      noarch

%description
Pure-python library for interacting with Yubikeys


%package -n python3-%{srcname}
Summary:        Pure-python library for interacting with Yubikeys
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pyusb

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Pure-python library for interacting with Yubikeys. For Python 3.


%prep
%autosetup -n %{name}-%{name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
%pytest test/soft/


%files -n python3-%{srcname}
%license COPYING
%doc NEWS README
%{python3_sitelib}/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.3-23
- Prepare for Oreon 11 (RP1)
