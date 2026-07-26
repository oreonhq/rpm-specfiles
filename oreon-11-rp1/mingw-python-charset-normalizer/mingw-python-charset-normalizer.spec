%global source0_hash 94537985111c35f28720e43603b8e7b43a6ecfb2ce1d3058bbe955b73404e21a

%{?mingw_package_header}

%global pkg_name charset-normalizer
%global pypi_name charset_normalizer

Name:          mingw-python-%{pkg_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       3.4.4
Release:       2%{?dist}
BuildArch:     noarch

License:       MIT
URL:           https://github.com/ousret/charset_normalizer
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-build

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-build

%description
MinGW Windows Python %{pypi_name} library.

%package -n mingw32-python3-%{pkg_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw32-python3-%{pkg_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{pkg_name}
Summary:       MinGW Windows Python3 %{pypi_name} library

%description -n mingw64-python3-%{pkg_name}
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

%files -n mingw32-python3-%{pkg_name}
%license LICENSE
%{mingw32_bindir}/normalizer
%{mingw32_python3_sitearch}/charset_normalizer/
%{mingw32_python3_sitearch}/charset_normalizer-%{version}.dist-info/

%files -n mingw64-python3-%{pkg_name}
%license LICENSE
%{mingw64_bindir}/normalizer
%{mingw64_python3_sitearch}/charset_normalizer/
%{mingw64_python3_sitearch}/charset_normalizer-%{version}.dist-info/

%changelog
%autochangelog
