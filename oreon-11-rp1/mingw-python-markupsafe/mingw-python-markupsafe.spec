%global source0_hash 722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698

%{?mingw_package_header}

%global mod_name markupsafe

Name:          mingw-python-%{mod_name}
Summary:       MinGW Windows Python %{mod_name} library
Version:       3.0.3
Release:       2%{?dist}
BuildArch:     noarch

License:       BSD-3-Clause
URL:           https://pypi.org/project/MarkupSafe/
Source0:       %{pypi_source markupsafe}

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-gcc
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-dlfcn
BuildRequires: mingw64-gcc
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build

%description
MinGW Windows Python %{mod_name} library.

%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{mod_name} library

%description -n mingw32-python3-%{mod_name}
MinGW Windows Python3 %{mod_name} library.

%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Windows Python3 %{mod_name} library

%description -n mingw64-python3-%{mod_name}
MinGW Windows Python3 %{mod_name} library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{mod_name}-%{version}
# Allow older setuptools
sed -i '/setuptools/s/>=.*"/"/' pyproject.toml

%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{mod_name}
%license LICENSE.txt
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/%{mod_name}-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE.txt
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/%{mod_name}-%{version}.dist-info/

%changelog
%autochangelog
