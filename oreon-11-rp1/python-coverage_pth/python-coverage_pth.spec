%global source0_hash f8cfdc5f7f524267c5c8d5e92c39d72a3822875e6b0b53e7611af056e3ed9dbf

%global pypi_name coverage_pth

Name:           python-%{pypi_name}
Version:        0.0.2
Release:        26%{?dist}
Summary:        Coverage PTH file to enable coverage at the virtualenv level

# See github repo for license information
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/dougn/coverage_pth
Source0:        %pypi_source
Source1:        https://raw.githubusercontent.com/dougn/%{pypi_name}/master/LICENSE.txt
Patch0:         python310.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

%description
A .pth file to site-packages to enable coverage.py.

%package -n     python3-%{pypi_name}
Summary:        Coverage PTH file to enable coverage at the virtualenv level
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-coverage

# since there are no .py files, this is not picked automatically
Requires:       python(abi) = %python3_version

%description -n python3-%{pypi_name}
A .pth file to site-packages to enable coverage.py.
Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}*.pth
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
