%global source0_hash 05fc3eef2429fe26ae42283cccb1f3831b53b12d4bd8b4734bf42973d4af6e16
Name:           python-pytest-datafiles
Version:        3.0.1
Release:        1%{?dist}
Summary:        py.test plugin to create a _tmp_path_ containing predefined files/directories.
License:        MIT
URL:            https://github.com/omarkohl/pytest-datafiles
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_datafiles/pytest_datafiles-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-datafiles = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-datafiles
Summary:        py.test plugin to create a _tmp_path_ containing predefined files/directories.
# oreon:reqs
Requires:       python3dist(pytest) >= 6.2.0
# /oreon:reqs
%description -n python3-pytest-datafiles

%prep
%global oreon_srcdir pytest_datafiles-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-datafiles usr/lib/python3*/site-packages/pytest_datafiles* usr/lib64/python3*/site-packages/pytest_datafiles* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_datafiles* usr/lib64/python3*/site-packages/pytest_datafiles* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-datafiles -f %{oreon_filedir}/python3-pytest-datafiles.list

%changelog

%autochangelog
