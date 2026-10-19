%global source0_hash 1e859bd5c40fae9448642dd871adf459e5e2084186e8d2c2a79a824c970da1f8
%bcond_with     bootstrap
%{?mingw_package_header}
%global pkgname pyproject-hooks
%global pypi_name pyproject_hooks
Name:           mingw-python-%{pkgname}
Summary:        MinGW Python pyproject_hooks library
Version:        1.3.3
Release:        1%{?dist}
BuildArch:      noarch
License:        MIT
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-pyproject-hooks/mingw-python-pyproject-hooks-%{version}.tar.gz
%if %{without bootstrap}
%endif
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw32-python3-flit-core
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
BuildRequires:  mingw64-python3-flit-core
# /oreon:deps
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
Version: 1.3.3
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-pyproject-hooks -f %{oreon_filedir}/mingw32-python3-pyproject-hooks.list
%files -n mingw64-python3-pyproject-hooks -f %{oreon_filedir}/mingw64-python3-pyproject-hooks.list

%changelog

%autochangelog
