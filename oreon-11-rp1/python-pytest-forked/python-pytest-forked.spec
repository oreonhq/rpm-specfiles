%global source0_hash 00f2bee51612f29b8e6b81eed2c3b2975e824c2693394f5bdaf7a1369078ba5f
Name:           python-pytest-forked
Version:        1.7.5
Release:        1%{?dist}
Summary:        run tests in isolated forked subprocesses
License:        MIT
URL:            https://github.com/pytest-dev/pytest-forked
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_forked/pytest_forked-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/pytest-dev/pytest-forked/commit/b2742322d3.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 41.4
BuildRequires:  python3dist(setuptools-scm) >= 3.3
Requires:       python3-pytest-forked = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-forked
Summary:        run tests in isolated forked subprocesses
%description -n python3-pytest-forked

%prep
%global oreon_srcdir pytest_forked-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-forked usr/lib/python3*/site-packages/pytest_forked* usr/lib64/python3*/site-packages/pytest_forked* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_forked* usr/lib64/python3*/site-packages/pytest_forked* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-forked -f %{oreon_filedir}/python3-pytest-forked.list

%changelog

%autochangelog
