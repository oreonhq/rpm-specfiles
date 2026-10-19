%global source0_hash 5edc0433c00146139fd2c1fc20b42315cd39348d96d25d7f7437281c4e19d09c
%global srcname into-dbus-python
Name:           python-%{srcname}
Version:        0.8.4
Release:        1%{?dist}
Summary:        Transformer to dbus-python types
License:        Apache-2.0
URL:            https://github.com/stratis-storage/into-dbus-python
Source0:        https://github.com/stratis-storage/into-dbus-python/archive/refs/tags/v%{version}.tar.gz#/into-dbus-python-0.8.4.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-into-dbus-python = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Transformer to dbus-python types
BuildRequires:  python3-devel
%description -n python3-%{srcname}

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/into_dbus_python* usr/lib64/python3*/site-packages/into_dbus_python* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-into-dbus-python -f %{oreon_filedir}/python3-into-dbus-python.list

%changelog

%autochangelog
