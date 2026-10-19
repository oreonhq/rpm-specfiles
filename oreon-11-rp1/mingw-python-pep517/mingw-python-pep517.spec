%global source0_hash 1b2fa2ffd3938bb4beffe5d6146cbcb2bda996a5a4da9f31abffd8b24e07b317
%bcond_without     bootstrap
%{?mingw_package_header}
%global pypi_name pep517
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python pep517 library
Version:       0.13.1
Release:        1%{?dist}
BuildArch:     noarch
License:       MIT AND Apache-2.0
URL:           https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/%/%{pypi_name/%{pypi_name-%{version}.tar.gz
%if %{without bootstrap}
%endif
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-python3
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-python3
# /oreon:deps
%description
MinGW Windows Python %{pypi_name} library.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%if %{with bootstrap}
Requires:      mingw32-python3-flit-core
%endif
%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%if %{with bootstrap}
Requires:      mingw64-python3-flit-core
%endif
%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

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
Version: %{version}+rpmbootstrap
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
cp -a pep517 %{distinfo} %{buildroot}%{mingw32_python3_sitearch}/
cp -a pep517 %{distinfo} %{buildroot}%{mingw64_python3_sitearch}/
mkdir -p %{buildroot}%{mingw32_python3_hostsitearch}
mkdir -p %{buildroot}%{mingw64_python3_hostsitearch}
cp -a pep517 %{distinfo} %{buildroot}%{mingw32_python3_hostsitearch}/
cp -a pep517 %{distinfo} %{buildroot}%{mingw64_python3_hostsitearch}/
%else
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%mingw32_py3_install_host_wheel
%mingw64_py3_install_host_wheel
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-pep517 -f %{oreon_filedir}/mingw32-python3-pep517.list
%files -n mingw64-python3-pep517 -f %{oreon_filedir}/mingw64-python3-pep517.list

%changelog

%autochangelog
