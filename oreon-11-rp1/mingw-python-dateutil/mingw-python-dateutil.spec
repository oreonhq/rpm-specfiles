%global source0_hash 37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3

%{?mingw_package_header}

%global mod_name dateutil
%global pypi_name python-dateutil

Name:          mingw-python-%{mod_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       2.9.0.post0
Release:       3%{?dist}
BuildArch:     noarch

# According to the LICENSE file:
# - Apache-2.0 applies to all contributions after 2017-12-01, as well as
#   all contributions that have been re-licensed.
# - BSD-3-Clause applies to all code, even that also covered by Apache-2.0
License:       (Apache-2.0 AND BSD-3-Clause) OR BSD-3-Clause
URL:           https://github.com/dateutil/%{name}
Source0:       %{pypi_source}

# Don't depend on setuptools_scm (see also %%prep)
Patch0:        python-dateutil_noscm.patch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build

%description
MinGW Windows Python %{pypi_name} library.

%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 %{pypi_name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Manually write version, rather than using setuptools_scm
sed -i 's|{version}|%{version}|' setup.py

%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{mod_name}
%license LICENSE
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/python_dateutil-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/python_dateutil-%{version}.dist-info/

%changelog
%autochangelog
