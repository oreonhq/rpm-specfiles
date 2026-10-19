%global source0_hash 1fd888ea08f3b13489016850c80d07742c19d6f177daf3c3b73a87f8f6a45bb1
Name: python-pytest-sourceorder
Version: 0.6.0
Release:        19%{?dist}
Summary:        Test-ordering plugin for pytest
License: GPL-3.0-or-later
URL: https://github.com/encukou/pytest-sourceorder
Source0:        https://github.com/encukou/pytest-sourceorder/archive/v%{version}.tar.gz#/pytest-sourceorder-%{version}.tar.gz
Patch:   https://pagure.io/python-pytest-sourceorder/pull-request/4.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-sourceorder = %{version}-%{release}
# /oreon:deps
%description
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.

%package -n python3-pytest-sourceorder
Summary: %summary
%{?python_provide:%python_provide python3-pytest-sourceorder}
%description -n python3-pytest-sourceorder
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest-sourceorder-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-sourceorder usr/lib/python3*/site-packages/pytest_sourceorder* usr/lib64/python3*/site-packages/pytest_sourceorder* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_sourceorder* usr/lib64/python3*/site-packages/pytest_sourceorder* usr/bin/*

%check

%tox
%files
%files -n python3-pytest-sourceorder -f %{oreon_filedir}/python3-pytest-sourceorder.list

%changelog

%autochangelog
