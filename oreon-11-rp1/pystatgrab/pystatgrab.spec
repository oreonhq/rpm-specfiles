%global source0_hash 0d6572fb7f778467740f3fe72dfa3d0e65909d53db922891d6478f18e27bb56c
%global srcname pystatgrab
Name:           pystatgrab
Version:        0.7.3
Release:        6%{?dist}
Summary:        Python bindings for libstatgrab
License:        LGPL-2.0-or-later
URL:            https://libstatgrab.org/pystatgrab/
Source0:        https://github.com/libstatgrab/pystatgrab/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libstatgrab-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Pystatgrab contains Python bindings for libstatgrab.

%package -n python3-%{name}
Summary:        Python bindings for libstatgrab
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}
Pystatgrab contains Python bindings for libstatgrab.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

rm -rf statgrab.c
%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PYTHONPATH=%{buildroot}/%{python3_sitearch} %{__python3} test.py
%files -f %{oreon_filedir}/main.list
%files -n python3-pystatgrab -f %{oreon_filedir}/python3-pystatgrab.list

%changelog

%autochangelog
