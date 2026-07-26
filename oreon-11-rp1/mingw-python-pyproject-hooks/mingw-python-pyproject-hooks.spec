%global source0_hash 1e859bd5c40fae9448642dd871adf459e5e2084186e8d2c2a79a824c970da1f8

# This package is required by python-build to build wheels.
# To bootstrap, we copy the files to appropriate locations manually and create a minimal dist-info metadata.
# Note that as a pure Python package, the wheel contains no pre-built binary stuff.
%bcond_with     bootstrap

%{?mingw_package_header}

%global pkgname pyproject-hooks
%global pypi_name pyproject_hooks

Name:           mingw-python-%{pkgname}
Summary:        MinGW Python %{pypi_name} library
Version:        1.2.0
Release:        4%{?dist}
BuildArch:      noarch

License:        MIT
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-python3
%if %{without bootstrap}
BuildRequires:  mingw32-python3-flit-core
BuildRequires:  mingw32-python3-build
%endif

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-python3
%if %{without bootstrap}
BuildRequires:  mingw64-python3-flit-core
BuildRequires:  mingw64-python3-build
%endif

%description
MinGW Python %{pypi_name} library.

%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Python 3 %{pypi_name} library

%description -n mingw32-python3-%{pkgname}
MinGW Python 3 %{pypi_name} library.

%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Python 3 %{pypi_name} library

%description -n mingw64-python3-%{pkgname}
MinGW Python 3 %{pypi_name} library.

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
Version: 1.2.0
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
cp -a src/pyproject_hooks %{distinfo} %{buildroot}%{mingw32_python3_sitearch}/
cp -a src/pyproject_hooks %{distinfo} %{buildroot}%{mingw64_python3_sitearch}/
mkdir -p %{buildroot}%{mingw32_python3_hostsitearch}
mkdir -p %{buildroot}%{mingw64_python3_hostsitearch}
cp -a src/pyproject_hooks %{distinfo} %{buildroot}%{mingw32_python3_hostsitearch}/
cp -a src/pyproject_hooks %{distinfo} %{buildroot}%{mingw64_python3_hostsitearch}/
%else
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%mingw32_py3_install_host_wheel
%mingw64_py3_install_host_wheel
%endif

%files -n mingw32-python3-%{pkgname}
%license LICENSE
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{distinfo}
%{mingw32_python3_hostsitearch}/%{pypi_name}/
%{mingw32_python3_hostsitearch}/%{distinfo}

%files -n mingw64-python3-%{pkgname}
%license LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{distinfo}
%{mingw64_python3_hostsitearch}/%{pypi_name}/
%{mingw64_python3_hostsitearch}/%{distinfo}

%changelog
%autochangelog
