%global pypi_name netifaces

Name:           python-netifaces
Version:        0.11.0
Release:        16%{?dist}
Summary:        Python library to retrieve information about network interfaces
License:        MIT
URL:            https://pypi.python.org/pypi/netifaces
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc

%generate_buildrequires
%pyproject_buildrequires

%description
This package provides a cross platform API for getting address information
from network interfaces.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Python %{python3_pkgversion} library to retrieve information about network interfaces
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
This package provides a cross platform API for getting address information
from network interfaces.


%prep
%setup -q -n %{pypi_name}-%{version}


%build
%pyproject_wheel


%install
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}*.dist-info/
%{python3_sitearch}/%{pypi_name}*.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11.0-16
- Prepare for Oreon 11 (RP1)
