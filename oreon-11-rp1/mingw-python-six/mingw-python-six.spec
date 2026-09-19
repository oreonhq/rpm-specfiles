%global source0_hash ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81

%{?mingw_package_header}

%global pypi_name six

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       1.17.0
Release:       4%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://pypi.python.org/pypi/six
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build

%description
MinGW Windows Python %{pypi_name} library.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{mingw32_python3_sitearch}/%{pypi_name}.py
%{mingw32_python3_sitearch}/__pycache__/%{pypi_name}.*
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}.py
%{mingw64_python3_sitearch}/__pycache__/%{pypi_name}.*
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
