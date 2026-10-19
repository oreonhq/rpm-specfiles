%global source0_hash 0033f2dfa89ae5f700b77875c6989172e6f4bf1170a3227f066e63c5b6e6f83f
Name: python-beaker
Version: 1.14.1
Release:        1%{?dist}
Summary:        WSGI middleware layer to provide sessions
License: LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL: http://beaker.readthedocs.io
Source0:        https://github.com/bbangert/beaker/archive/%{version}/beaker-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  //bin/netstat
BuildRequires:  //bin/redis-server
BuildRequires:  glibc-langpack-it
BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(funcsigs)
BuildRequires:  python3dist(paste)
BuildRequires:  python3dist(pycrypto)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(redis)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(webtest)
# /oreon:deps
%description

%package -n python3-beaker
Summary: %summary
BuildRequires: python3-devel
BuildRequires: python3dist(cryptography)
BuildRequires: python3dist(funcsigs)
BuildRequires: python3dist(paste)
BuildRequires: python3dist(pycrypto)
BuildRequires: python3dist(redis)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(sqlalchemy)
BuildRequires: python3dist(webtest)
BuildRequires: python3dist(pytest)
BuildRequires: glibc-langpack-it
Requires: python3dist(paste)
Recommends: python3dist(cryptography)
Recommends: python3dist(pycrypto)
Recommends: python3dist(pycryptodome)
Recommends: python3dist(pycryptopp)
%{?python_provide:%python_provide python3-beaker}
%description -n python3-beaker

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir beaker-%{version}
%oreon_prep
%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-beaker usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm -f tests/test_managers/test_ext_mongodb.py
redis-server &
%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-beaker -f %{oreon_filedir}/python3-beaker.list

%changelog

%autochangelog
