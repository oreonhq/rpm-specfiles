%global source0_hash 00243ae351a257117b6a241061796684b084ed1c516a08c48a3f7e147a9d80b4

# This package is required by python-build to build wheels.
# To bootstrap, we copy the files to appropriate locations manually and create a minimal dist-info metadata.
# Note that as a pure Python package, the wheel contains no pre-built binary stuff.
%bcond_with     bootstrap

%{?mingw_package_header}

%global pypi_name packaging

Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python packaging core utils
Version:        26.0
Release:        1%{?dist}
BuildArch:      noarch

License:        BSD-2-Clause OR Apache-2.0
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-python3
%if %{without bootstrap}
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw32-python3-flit-core
%endif

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-python3
%if %{without bootstrap}
BuildRequires:  mingw64-python3-build
BuildRequires:  mingw64-python3-flit-core
%endif

%description
MinGW Python packaging core utils.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Python 3 packaging core utils
%if %{with bootstrap}
Requires:      mingw32-python3-pyparsing
%endif

%description -n mingw32-python3-%{pypi_name}
MinGW Python 3 packaging core utils.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Python 3 packaging core utils
%if %{with bootstrap}
Requires:      mingw64-python3-pyparsing
%endif

%description -n mingw64-python3-%{pypi_name}
MinGW Python 3 packaging core utils.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build
%if %{with bootstrap}
%global distinfo %{pypi_name}-%{version}+rpmbootstrap.dist-info
mkdir %{distinfo}
cat > %{distinfo}/METADATA << EOF
Metadata-Version: 2.2
Name: %{pypi_name}
Version: 26.0
EOF
%else
%global distinfo %{pypi_name}-%{version}.dist-info
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%mingw32_py3_build_host_wheel
%mingw64_py3_build_host_wheel
%endif

%install
%if %{with bootstrap}
mkdir -p %{buildroot}%{mingw32_python3_sitearch}
mkdir -p %{buildroot}%{mingw64_python3_sitearch}
cp -a packaging %{distinfo} %{buildroot}%{mingw32_python3_sitearch}/
cp -a packaging %{distinfo} %{buildroot}%{mingw64_python3_sitearch}/
mkdir -p %{buildroot}%{mingw32_python3_hostsitearch}
mkdir -p %{buildroot}%{mingw64_python3_hostsitearch}
cp -a packaging %{distinfo} %{buildroot}%{mingw32_python3_hostsitearch}/
cp -a packaging %{distinfo} %{buildroot}%{mingw64_python3_hostsitearch}/
%else
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%mingw32_py3_install_host_wheel
%mingw64_py3_install_host_wheel
%endif

%files -n mingw32-python3-%{pypi_name}
%license LICENSE.BSD LICENSE.APACHE LICENSE
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{distinfo}
%{mingw32_python3_hostsitearch}/%{pypi_name}/
%{mingw32_python3_hostsitearch}/%{distinfo}

%files -n mingw64-python3-%{pypi_name}
%license LICENSE.BSD LICENSE.APACHE LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{distinfo}
%{mingw64_python3_hostsitearch}/%{pypi_name}/
%{mingw64_python3_hostsitearch}/%{distinfo}

%changelog
%autochangelog
