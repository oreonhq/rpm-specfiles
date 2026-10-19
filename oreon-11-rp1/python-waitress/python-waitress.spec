%global source0_hash 4c5583cee40bee842b48443ed899b5d445947c5d88fe170d31c3becab09710c3
Name:           python-waitress
Version:        3.0.2
Release:        1%{?dist}
Summary:        Waitress WSGI server
License:        ZPL-2.1
URL:            https://github.com/Pylons/waitress
Source0:        https://github.com/Pylons/waitress/archive/refs/tags/v%{version}.tar.gz#/waitress-%{version}.tar.gz
Source1: generate-tarball.sh
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 41
Requires:       python3-waitress = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-waitress
Summary:        Waitress WSGI server
BuildRequires:  python3-devel
%description -n python3-waitress

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n waitress-%{version}
sed -e '/pytest-cov/d' \
    -e '/coverage/d' \
    -e '/addopts/d' \
    -i setup.cfg

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-waitress usr/lib/python3*/site-packages/waitress* usr/lib64/python3*/site-packages/waitress* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/waitress* usr/lib64/python3*/site-packages/waitress* usr/bin/*

%check

%pytest
%files
%files -n python3-waitress -f %{oreon_filedir}/python3-waitress.list

%changelog

%autochangelog
