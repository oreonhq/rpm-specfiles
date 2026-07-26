%global source0_hash 6136f3ee4128b704abb654d0c767b27d6412896d0dee16973e86fd703cec5ec9

%{?mingw_package_header}

%global mod_name waitress
%global pypi_name waitress

Name:          mingw-python-%{mod_name}
Summary:       MinGW Windows Python %{pypi_name} library
Version:       3.0.2
Release:       3%{?dist}
BuildArch:     noarch

License:       ZPL-2.1
URL:           https://github.com/Pylons/waitress
# Remove docs folder it is released under the non-free
# Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License
# See CONTRIBUTORS.txt
# Generate with ./waitress-tarball-nodocs.sh $version
Source0:       waitress-%{version}-nodocs.tar.xz
Source1:       waitress-tarball-nodocs.sh

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

%autosetup -p1 -n %{pypi_name}-%{version}-nodocs

%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{mod_name}
%license LICENSE.txt
%{mingw32_bindir}/waitress-serve
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE.txt
%{mingw64_bindir}/waitress-serve
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
