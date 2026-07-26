%global source0_hash 1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed

%{?mingw_package_header}

%global pypi_name urllib3

Name:          mingw-python-%{pypi_name}
Summary:       MinGW Windows Python %{pypi_name}
Version:       2.6.3
Release:       2%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://urllib3.readthedocs.io/en/latest/
Source0:       %{pypi_source}
# Switch back to flit as build-system, hatchling is not packaged for mingw
Patch0:        urllib3-no-hatch.patch

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-flit-core

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-flit-core

%description
MinGW Windows Python %{pypi_name}.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}

%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name}

%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name}.

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
%license LICENSE.txt
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.txt
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
