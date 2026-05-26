%global pypi_name netifaces

Name:           python-netifaces
Version:        0.11.0
Release:        16%{?dist}
Summary:        Python library to retrieve information about network interfaces
License:        MIT
URL:            https://pypi.python.org/pypi/netifaces
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 043a79146eb2907edf439899f262b3dfe41717d34124298ed281139a8b93ca32
%global source0_file netifaces-0.11.0.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/netifaces-0.11.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "043a79146eb2907edf439899f262b3dfe41717d34124298ed281139a8b93ca32" || { echo "oreon: Source0 SHA256 mismatch for netifaces-0.11.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
