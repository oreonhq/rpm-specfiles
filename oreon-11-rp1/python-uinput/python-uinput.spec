%global source0_hash 99392b676c77b5795b86b7d75274db33fe754fd1e06fb3d58b167c797dc47f0c

# No python3 on el6
%if 0%{?el6}
%global with_python3 0
%endif

Name:           python-uinput
Version:        0.11.2
Release:        19%{?dist}
Summary:        Pythonic API to the Linux uinput kernel module

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://pypi.python.org/pypi/python-uinput/
Source0:        http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
#http://pypi.python.org/packages/source/p/python-uinput/python-uinput-0.11.2.tar.gz

# https://github.com/tuomasjjrasanen/python-uinput/pull/41
Patch0:         python-uinput-add_python311_support.patch

BuildRequires:  kernel-headers
BuildRequires:  libudev-devel

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:	python-setuptools

%global _description\
Python-uinput is Python interface to the Linux uinput kernel module\
which allows attaching userspace device drivers into kernel.

%description %_description

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

%files -n python3-uinput
%doc COPYING NEWS README examples
%{python3_sitearch}/python_uinput-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/_libsuinput.*.so
%{python3_sitearch}/uinput

%changelog
%autochangelog
