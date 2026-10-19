%global source0_hash b6032923e05e9d75ec17a5af9a98429c46d2839adfaf80604d52e0faacd7a32f
%global pypi_name pyserial-asyncio
Name:           %{pypi_name}
Version:        0.6
Release:        1%{?dist}
Summary:        Asynchronous Python Serial Port Extension
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/pyserial/pyserial-asyncio
Source0:        https://files.pythonhosted.org/packages/source/p/pyserial-asyncio/pyserial-asyncio-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
# /oreon:deps
%description
Async I/O extension package for the Python Serial Port Extension.

%package -n     python3-%{pypi_name}
Summary:        Asynchronous Python Serial Port Extension
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
Async I/O extension package for the Python Serial Port Extension.

%package -n python-%{pypi_name}-doc
Summary:        pyserial-asyncio documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%description -n python-%{pypi_name}-doc
Documentation for pyserial-asyncio.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' serial_asyncio/__init__.py

%build

%py3_build
PYTHONPATH=${PWD} sphinx-build-3 documentation html
rm -rf html/.{doctrees,buildinfo}
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v test
%files -f %{oreon_filedir}/main.list
%files -n python3-pyserial-asyncio -f %{oreon_filedir}/python3-pyserial-asyncio.list
%files -n python-pyserial-asyncio-doc -f %{oreon_filedir}/python-pyserial-asyncio-doc.list

%changelog

%autochangelog
