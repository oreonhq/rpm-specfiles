%global source0_hash 04c305f30a2ca25d5c54b3cd6ce9bb64c36e5f07967b23b3fb6aaecc851b90b6
%global pypi_name adb-shell
Name:           python-%{pypi_name}
Version:        0.4.4
Release:        8%{?dist}
Summary:        Python implementation for ADB shell and file sync
License:        Apache-2.0
URL:            https://github.com/JeffLIrion/adb_shell
Source0:        https://files.pythonhosted.org/packages/source/a/adb_shell/adb_shell-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-adb-shell = %{version}-%{release}
# /oreon:deps
%description
Python package implements ADB shell and FileSync functionality.

%package -n     python3-%{pypi_name}
Summary:        Python implementation for ADB shell and file sync
BuildRequires:  python3-devel
%description -n python3-%{pypi_name}
Python package implements ADB shell and FileSync functionality.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n adb_shell-%{version}
rm -rf %{pypi_name}.egg-info
# Conflict with crypto
sed -i -e 's/pycryptodome/pycryptodomex/g' setup.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/adb_shell* usr/lib64/python3*/site-packages/adb_shell* usr/bin/*

%files
%files -n python3-adb-shell -f %{oreon_filedir}/python3-adb-shell.list

%changelog

%autochangelog
