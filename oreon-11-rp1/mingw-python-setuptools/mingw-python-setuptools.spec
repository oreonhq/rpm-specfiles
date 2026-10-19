%global source0_hash 8b0e9d10c784bf7d262c4e5ec5d4ec94127ce206e8738f29a437945fbc219b70
%{?mingw_package_header}
%global pypi_name setuptools
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python setuptools library
Version:       80.10.2
Release:        1%{?dist}
BuildArch:     noarch
License:       MIT
URL:           https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/%/%{pypi_name/%{pypi_name-%{version}.tar.gz
Patch0:        mingw-python-setuptools_is_mingw.patch
Patch1:        mingw-python-setuptools_nostrip.patch
Patch2:        mingw-python-setuptools-shlib-suffix.patch
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
%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled exes
rm -f setuptools/*.exe

# Strip shebangs on python modules
find setuptools -name \*.py | xargs sed -i -e '1 {/^#!\//d}'

%build

%{mingw32_py3_build_host}
%{mingw64_py3_build_host}
%{mingw32_py3_build}
%{mingw64_py3_build}
%install
%{mingw32_py3_install_host}
%{mingw64_py3_install_host}
%{mingw32_py3_install}
%{mingw64_py3_install}
find %{buildroot}%{mingw32_python3_sitearch}/ -name '*.exe' | xargs rm -f
find %{buildroot}%{mingw64_python3_sitearch}/ -name '*.exe' | xargs rm -f
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-setuptools -f %{oreon_filedir}/mingw32-python3-setuptools.list
%files -n mingw64-python3-setuptools -f %{oreon_filedir}/mingw64-python3-setuptools.list

%changelog

%autochangelog
