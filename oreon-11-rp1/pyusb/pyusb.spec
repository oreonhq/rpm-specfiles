%global source0_hash 3af070b607467c1c164f49d5b0caabe8ac78dbed9298d703a8dbf9df4052d17e
Name: pyusb
Version: 1.3.1
Release:        7%{?dist}
Summary:        Python bindings for libusb
License: BSD-3-Clause
URL: https://github.com/pyusb/pyusb/
Source0:        https://files.pythonhosted.org/packages/source/p/pyusb/pyusb-1.3.1.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 30.3.0
Requires:       python3-pyusb = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pyusb
Summary:       %summary
BuildRequires: python3-devel
BuildRequires:  python3-setuptools_scm
Requires:       libusb1
%description -n python3-pyusb
PyUSB provides easy USB access to python. The module contains classes and 
methods to support most USB operations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
sed -i -e 's/\r//g' README.rst

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyusb usr/lib/python3*/site-packages/pyusb* usr/lib64/python3*/site-packages/pyusb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyusb* usr/lib64/python3*/site-packages/pyusb* usr/bin/*

%check

%pyproject_check_import
cd tests
%{py3_test_envvars} %{python3} ./testall.py
%files
%files -n python3-pyusb -f %{oreon_filedir}/python3-pyusb.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-7
- Prepare for Oreon 11 (RP1)
