%global source0_hash 4e1c6e8fe5255b7babe93b9af51532ba09c6946eee413c5db00cab3878d7ed2f
Name:           python-unix-ar
Version:        0.2.1
Release:        1%{?dist}
Summary:        .ar file handling for Python (including .deb)
License:        BSD-3-Clause
URL:            https://github.com/getninjas/unix_ar
Source0:        https://github.com/getninjas/unix_ar/archive/%{version}/unix-ar-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-unix-ar = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-unix-ar
Summary:        .ar file handling for Python (including .deb)
%description -n python3-unix-ar

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir unix_ar-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-unix-ar usr/lib/python3*/site-packages/unix_ar* usr/lib64/python3*/site-packages/unix_ar* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/unix_ar* usr/lib64/python3*/site-packages/unix_ar* usr/bin/*

%check

%{py3_test_envvars} %{python3} tests.py
%files
%files -n python3-unix-ar -f %{oreon_filedir}/python3-unix-ar.list

%changelog

%autochangelog
