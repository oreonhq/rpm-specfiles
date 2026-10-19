%global source0_hash 8a02e4e36040e9dc8d356ff7457fca753e07fa06fc70c0614c7cb858feac0096
%global module python-binary-memcached
%global srcname %{module}
Name:           %{module}
Version:        0.31.2
Release:        1%{?dist}
Summary:        Python module python-binary-memcached
License:        MIT
URL:            https://github.com/jaysonsantos/%{module}
Source0:        https://github.com/jaysonsantos/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-binary-memcached = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-binary-memcached
Summary:        Python module python-binary-memcached
Requires:  memcached
%description -n python3-binary-memcached
A pure python module (thread safe) to access memcached via it’s binary with SASL auth support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{module}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-binary-memcached usr/lib/python3*/site-packages/binary_memcached* usr/lib64/python3*/site-packages/binary_memcached* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/binary_memcached* usr/lib64/python3*/site-packages/binary_memcached* usr/bin/*

%check

%pytest
%files
%files -n python3-binary-memcached -f %{oreon_filedir}/python3-binary-memcached.list

%changelog

%autochangelog
