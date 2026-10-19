%global source0_hash ad556772f3e06345f1ce503fc118ef5bd54cdd0469a990ea1f2d7cd9946d1fb2
Name:           python-pysubnettree
Version:        0.38.1
Release:        1%{?dist}
Summary:        Python Module for CIDR Lookups
License:        BSD-3-Clause-LBNL and BSD-4-Clause
URL:            https://github.com/zeek/pysubnettree
Source0:        https://github.com/zeek/pysubnettree/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        btest.cfg
Provides:       pysubnettree = %{version}-%{release}
Obsoletes:      pysubnettree < 0.35-16
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pysubnettree = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pysubnettree
Summary:        Python Module for CIDR Lookups
%description -n python3-pysubnettree

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pysubnettree-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pysubnettree usr/lib/python3*/site-packages/pysubnettree* usr/lib64/python3*/site-packages/pysubnettree* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pysubnettree* usr/lib64/python3*/site-packages/pysubnettree* usr/bin/*

%check

%pyproject_check_import
cd testing
cp %{SOURCE1} btest.cfg
PYTHONPATH="%{buildroot}%{python3_sitearch}:$PWD/Scripts" btest -c btest.cfg -d
%files
%files -n python3-pysubnettree -f %{oreon_filedir}/python3-pysubnettree.list

%changelog

%autochangelog
