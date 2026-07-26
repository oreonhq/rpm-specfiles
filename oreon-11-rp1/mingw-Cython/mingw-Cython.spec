%global source0_hash 84226ecd313b233da27dc2eb3601b4f222b8209c3a7216d8733b031da1dc64e6

%{?mingw_package_header}

# Disable debugsource packages
%undefine _debugsource_packages

%global pypi_name cython
%global mod_name Cython

Name:          mingw-%{mod_name}
Summary:       MinGW Windows Python %{mod_name} library
Version:       3.2.4
Release:       1%{?dist}

License:       Apache-2.0
URL:           http://www.cython.org
Source:        %{pypi_source}

BuildRequires: gcc

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

%autosetup -p1 -n %{pypi_name}-%{version}

%build
%mingw32_py3_build_host_wheel
%mingw64_py3_build_host_wheel
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_host_wheel
%mingw64_py3_install_host_wheel
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{mod_name}
%license LICENSE.txt
%{mingw32_bindir}/cygdb
%{mingw32_bindir}/cython
%{mingw32_bindir}/cythonize
%{mingw32_python3_sitearch}/cython.py
%{mingw32_python3_sitearch}/__pycache__/cython*.pyc
%{mingw32_python3_sitearch}/pyximport/
%{mingw32_python3_sitearch}/%{mod_name}/
%{mingw32_python3_sitearch}/cython-%{version}.dist-info/
%{_prefix}/%{mingw32_target}/bin/cygdb
%{_prefix}/%{mingw32_target}/bin/cython
%{_prefix}/%{mingw32_target}/bin/cythonize
%{mingw32_python3_hostsitearch}/cython.py
%{mingw32_python3_hostsitearch}/__pycache__/cython*.pyc
%{mingw32_python3_hostsitearch}/pyximport/
%{mingw32_python3_hostsitearch}/%{mod_name}/
%{mingw32_python3_hostsitearch}/cython-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%license LICENSE.txt
%{mingw64_bindir}/cygdb
%{mingw64_bindir}/cython
%{mingw64_bindir}/cythonize
%{mingw64_python3_sitearch}/cython.py
%{mingw64_python3_sitearch}/__pycache__/cython*.pyc
%{mingw64_python3_sitearch}/pyximport/
%{mingw64_python3_sitearch}/%{mod_name}/
%{mingw64_python3_sitearch}/cython-%{version}.dist-info/
%{_prefix}/%{mingw64_target}/bin/cygdb
%{_prefix}/%{mingw64_target}/bin/cython
%{_prefix}/%{mingw64_target}/bin/cythonize
%{mingw64_python3_hostsitearch}/cython.py
%{mingw64_python3_hostsitearch}/__pycache__/cython*.pyc
%{mingw64_python3_hostsitearch}/pyximport/
%{mingw64_python3_hostsitearch}/%{mod_name}/
%{mingw64_python3_hostsitearch}/cython-%{version}.dist-info/

%changelog
%autochangelog
