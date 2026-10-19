%global source0_hash 928ae7e20211f3b6f3915a72f06a0cfd29ab9d24279dd6346b6b1a7146397d36
%bcond_with     bootstrap
%{?mingw_package_header}
%global pypi_name pyparsing
Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python pyparsing
Version:        3.3.3
Release:        1%{?dist}
BuildArch:      noarch
License:        MIT
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-pyparsing/mingw-python-pyparsing-%{version}.tar.gz
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
Version: 3.3.3
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-pyparsing -f %{oreon_filedir}/mingw32-python3-pyparsing.list
%files -n mingw64-python3-pyparsing -f %{oreon_filedir}/mingw64-python3-pyparsing.list

%changelog

%autochangelog
