%global source0_hash 8d0538dbbd7babbd207f261ed969c65de439f6bc9e5dbd3b3b9a77f25d95f343
%{?mingw_package_header}
%global pypi_name pip
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python pip library
Version:       26.2.1
Release:        1%{?dist}
BuildArch:     noarch
License:       MIT AND Python-2.0.1 AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LGPL-2.1-only AND MPL-2.0 AND (Apache-2.0 OR BSD-2-Clause)
URL:           https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-pip/mingw-python-pip-%{version}.tar.gz
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
MinGW Windows Python %{pypi_name} library.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Copy vendor licenses for %%license
mkdir vendor_licenses
destdir=$PWD/vendor_licenses
(cd src/pip/_vendor && find  -name 'LICENSE*' -exec install -Dp {} $destdir/{} \;)

%build

%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
sed -i '1d' %{buildroot}%{mingw32_python3_sitearch}/pip/_vendor/distro/distro.py
sed -i '1d' %{buildroot}%{mingw64_python3_sitearch}/pip/_vendor/distro/distro.py
sed -i '1d' %{buildroot}%{mingw32_python3_sitearch}/pip/_vendor/requests/certs.py
sed -i '1d' %{buildroot}%{mingw64_python3_sitearch}/pip/_vendor/requests/certs.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-pip -f %{oreon_filedir}/mingw32-python3-pip.list
%files -n mingw64-python3-pip -f %{oreon_filedir}/mingw64-python3-pip.list

%changelog

%autochangelog
