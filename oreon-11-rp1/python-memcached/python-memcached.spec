%global source0_hash 2877f0885ade0c4c6871c863914838d23c955621f1a9f56a9b941dd1facb250a
Name:           python-memcached
Version:        1.62
Release:        1%{?dist}
Summary:        A Python memcached client library
License:        LicenseRef-Callaway-Python
URL:            https://github.com/linsomniac/python-memcached
Source0:        https://github.com/linsomniac/python-memcached/archive/%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-memcached = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-memcached
Summary: %summary
%{?python_provide:%python_provide python3-memcached}
%description -n python3-memcached

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-memcached usr/lib/python3*/site-packages/memcached* usr/lib64/python3*/site-packages/memcached* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/memcached* usr/lib64/python3*/site-packages/memcached* usr/bin/*

%check

pidfile=$(mktemp)
memcached -d -P $pidfile
%pytest
kill $(cat $pidfile)
%files
%files -n python3-memcached -f %{oreon_filedir}/python3-memcached.list

%changelog

%autochangelog
