%global source0_hash 99392b676c77b5795b86b7d75274db33fe754fd1e06fb3d58b167c797dc47f0c
%if 0%{?el6}
%global with_python3 0
%endif
Name:           python-uinput
Version:        0.11.2
Release:        1%{?dist}
Summary:        Pythonic API to the Linux uinput kernel module
License:        GPL-3.0-only
URL:            http://pypi.python.org/pypi/python-uinput/
Source0:        http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch0:         python-uinput-add_python311_support.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libudev-devel
BuildRequires:  python-setuptools
BuildRequires:  python3-devel
# /oreon:deps
%description

%package -n     python3-uinput
Summary:        Pythonic API to the Linux uinput kernel module
%description -n python3-uinput
Python-uinput is Python interface to the Linux uinput kernel module
which
allows attaching userspace device drivers into kernel.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Use unversioned .so
sed -i "s/libudev.so.0/libudev.so/" setup.py

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build

%py3_build
%install
%py3_install
chmod a-x examples/*
%oreon_autofiles python3-uinput usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-uinput -f %{oreon_filedir}/python3-uinput.list

%changelog

%autochangelog
