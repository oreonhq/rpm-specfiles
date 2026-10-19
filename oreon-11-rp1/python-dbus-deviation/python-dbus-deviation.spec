%global source0_hash e06b88efe223885d2725df51cf7c9b7b463d1c6f04ea49d4690874318d0eb7a3
Name:           python-dbus-deviation
Version:        0.6.1
Release:        1%{?dist}
Summary:        D-Bus introspection XML linter
License:        LGPL-2.1-or-later
URL:            https://pypi.org/project/dbus-deviation/
Source0:        https://files.pythonhosted.org/packages/01/dc/047feaa6a81545e10c37d4eeff86443c90dd114c5ce13d6937c5ed38854d/dbus-deviation-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dbus-deviation = %{version}-%{release}
# /oreon:deps
%description
Tools for checking D-Bus interface XML.

%package -n python3-dbus-deviation
Summary:        D-Bus introspection XML linter
%description -n python3-dbus-deviation
Tools for checking D-Bus interface XML.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir dbus-deviation-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dbus-deviation usr/lib/python3*/site-packages/dbus_deviation* usr/lib64/python3*/site-packages/dbus_deviation* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dbus_deviation* usr/lib64/python3*/site-packages/dbus_deviation* usr/bin/*

%files
%files -n python3-dbus-deviation -f %{oreon_filedir}/python3-dbus-deviation.list
