%global source0_hash 34dc67d7d21a12399828dd13e63b352750580beea54ea7c729e708f2d2905fef
Name:           python-dbus-fast
Version:        5.0.22
Release:        1%{?dist}
Summary:        A faster version of dbus-next
License:        MIT
URL:            https://github.com/bluetooth-devices/dbus-fast
Source0:        https://files.pythonhosted.org/packages/source/d/dbus_fast/dbus_fast-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) < 3.3.0
BuildRequires:  python3dist(cython) >= 3
BuildRequires:  python3dist(poetry-core) >= 1.0.0
BuildRequires:  python3dist(setuptools) >= 65.4.1
Requires:       python3-dbus-fast = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-dbus-fast
Summary:        A faster version of dbus-next
%description -n python3-dbus-fast

%prep
%global oreon_srcdir dbus_fast-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dbus-fast usr/lib/python3*/site-packages/dbus_fast* usr/lib64/python3*/site-packages/dbus_fast* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dbus_fast* usr/lib64/python3*/site-packages/dbus_fast* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dbus-fast -f %{oreon_filedir}/python3-dbus-fast.list

%changelog

%autochangelog
