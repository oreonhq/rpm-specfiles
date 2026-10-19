%global source0_hash 2f8dd4beaf7326d2f664f18205c024848dcb627ff29ceffb22ab410fbef2d761
%global pypi_name name-that-hash
Name:           python-%{pypi_name}
Version:        1.11.0
Release:        1%{?dist}
Summary:        The Modern Hash Identification System
License:        GPL-3.0-or-later
URL:            https://github.com/HashPals/Name-That-Hash
Source0:        https://github.com/HashPals/Name-That-Hash/archive/%{version}/Name-That-Hash-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-name-that-hash = %{version}-%{release}
# /oreon:deps
%description
Name That Hash will name that hash type! Identify MD5, SHA256 and 300+ other
hashes.

%package -n     python3-%{pypi_name}
Summary:        The Modern Hash Identification System
BuildRequires:  pytest
%description -n python3-%{pypi_name}
Name That Hash will name that hash type! Identify MD5, SHA256 and 300+ other
hashes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Name-That-Hash-%{version}
sed --in-place '1{\@^#! /usr/bin/env python@d}' name_that_hash/__main__.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/name_that_hash* usr/lib64/python3*/site-packages/name_that_hash* usr/bin/*

%check

%pytest
%files
%files -n python3-name-that-hash -f %{oreon_filedir}/python3-name-that-hash.list

%changelog

%autochangelog
