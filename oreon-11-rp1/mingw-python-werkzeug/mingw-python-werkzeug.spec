%global source0_hash cd3cd98b1b92dc3b7b3995038826c68097dcb16f9baa63abe35f20eafeb9fe5e

%{?mingw_package_header}

%global mod_name werkzeug
%global pypi_name werkzeug

Name:          mingw-python-%{mod_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       3.1.4
Release:       2%{?dist}
BuildArch:     noarch

License:       BSD-3-Clause
URL:           https://palletsprojects.com/p/werkzeug/
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build
BuildRequires: mingw32-python3-flit-core

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build
BuildRequires: mingw64-python3-flit-core

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

%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{mod_name}
%license LICENSE.txt src/werkzeug/debug/shared/ICON_LICENSE.md
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE.txt src/werkzeug/debug/shared/ICON_LICENSE.md
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
