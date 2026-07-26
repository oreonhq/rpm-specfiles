%global source0_hash 47fad0f17ac1e2cad3de3b458570fbc9b03560aa029ed5e16ee5554da9a2251c

# This package is required by python-build to build wheels.
# To bootstrap, we copy the files to appropriate locations manually and create a minimal dist-info metadata.
# Note that as a pure Python package, the wheel contains no pre-built binary stuff.
%bcond_with     bootstrap

%{?mingw_package_header}

%global pypi_name pyparsing

Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python %{pypi_name}
Version:        3.3.1
Release:        2%{?dist}
BuildArch:      noarch

License:        MIT
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
MinGW Python %{pypi_name}.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name}

%description -n mingw32-python3-%{pypi_name}
MinGW Python 3 %{pypi_name}.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name}

%description -n mingw64-python3-%{pypi_name}
MinGW Python 3 %{pypi_name}.

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
Version: 3.3.1
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
cp -a pyparsing %{distinfo} %{buildroot}%{mingw32_python3_sitearch}/
cp -a pyparsing %{distinfo} %{buildroot}%{mingw64_python3_sitearch}/
mkdir -p %{buildroot}%{mingw32_python3_hostsitearch}
mkdir -p %{buildroot}%{mingw64_python3_hostsitearch}
cp -a pyparsing %{distinfo} %{buildroot}%{mingw32_python3_hostsitearch}/
cp -a pyparsing %{distinfo} %{buildroot}%{mingw64_python3_hostsitearch}/
%else
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%mingw32_py3_install_host_wheel
%mingw64_py3_install_host_wheel
%endif

%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{distinfo}
%{mingw32_python3_hostsitearch}/%{pypi_name}/
%{mingw32_python3_hostsitearch}/%{distinfo}

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{distinfo}
%{mingw64_python3_hostsitearch}/%{pypi_name}/
%{mingw64_python3_hostsitearch}/%{distinfo}

%changelog
%autochangelog
