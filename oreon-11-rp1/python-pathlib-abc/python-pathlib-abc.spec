%global source0_hash fcd56f147234645e2c59c7ae22808b34c364bb231f685ddd9f96885aed78a94c
Name:           python-pathlib-abc
Version:        0.5.2
Release:        1%{?dist}
Summary:        Backport of pathlib ABCs
License:        PSF-2.0
URL:            https://github.com/barneygale/pathlib-abc
Source0:        https://files.pythonhosted.org/packages/source/p/pathlib_abc/pathlib_abc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pathlib-abc = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pathlib-abc
Summary:        Backport of pathlib ABCs
%description -n python3-pathlib-abc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pathlib_abc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pathlib-abc usr/lib/python3*/site-packages/pathlib_abc* usr/lib64/python3*/site-packages/pathlib_abc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pathlib_abc* usr/lib64/python3*/site-packages/pathlib_abc* usr/bin/*

%check

%pytest -ra
%files
%files -n python3-pathlib-abc -f %{oreon_filedir}/python3-pathlib-abc.list

%changelog

%autochangelog
