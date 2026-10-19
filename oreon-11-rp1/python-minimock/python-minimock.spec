%global source0_hash 0e02d3acd756ee85a53b8f05c9826ab280a72df41d03119181321ab5a8e3520e
Name:           python-minimock
Version:        1.3.0
Release:        7%{?dist}
Summary:        The simplest possible mock library
License:        MIT
URL:            https://github.com/lowks/minimock/
Source0:        https://github.com/lowks/minimock//archive/v%{version}/minimock-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.8.0
Requires:       python3-minimock = %{version}-%{release}
# /oreon:deps
%description
minimock is a simple library for doing Mock objects with doctest.

%package -n python3-minimock
Summary:        The simplest possible mock library
%description -n python3-minimock
minimock is a simple library for doing Mock objects with doctest.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn minimock-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-minimock usr/lib/python3*/site-packages/minimock* usr/lib64/python3*/site-packages/minimock* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/minimock* usr/lib64/python3*/site-packages/minimock* usr/bin/*

%check

%{__python3} minimock.py -v
%files
%files -n python3-minimock -f %{oreon_filedir}/python3-minimock.list

%changelog

%autochangelog
