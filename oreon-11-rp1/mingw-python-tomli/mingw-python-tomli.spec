%global source0_hash aa89c3f6c277dd275d8e243ad24f3b5e701491a860d5121f2cdd399fbb31fc9c

%{?mingw_package_header}

%global pkgname tomli
%global pypi_name %{pkgname}

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       2.4.0
Release:       2%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://github.com/hukkin/%{name}
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
MinGW Windows Python %{pkgname} library.

%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.

%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pkgname}-%{version}.dist-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pkgname}-%{version}.dist-info/

%changelog
%autochangelog
