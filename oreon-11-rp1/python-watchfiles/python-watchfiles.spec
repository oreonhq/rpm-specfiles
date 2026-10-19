%global source0_hash c995fba777f1ea992f090f9236e9284cf7a5d1a0130dd5a3d82c598cacd76838
Name:           python-watchfiles
Version:        1.2.0
Release:        1%{?dist}
Summary:        Simple, modern and high performance file watching and code reload in python.
License:        MIT
URL:            https://github.com/samuelcolvin/watchfiles
Source0:        https://files.pythonhosted.org/packages/source/w/watchfiles/watchfiles-%{version}.tar.gz
Patch:          0001-Downstream-only-allow-a-slightly-older-pytest-to-sup.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2
BuildRequires:  python3dist(maturin) >= 0.14.16
Requires:       python3-watchfiles = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-watchfiles
Summary:        Simple, modern and high performance file watching and code reload in python.
# oreon:reqs
Requires:       python3dist(anyio) >= 3.0.0
# /oreon:reqs
%description -n python3-watchfiles

%prep
%global oreon_srcdir watchfiles-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-watchfiles usr/lib/python3*/site-packages/watchfiles* usr/lib64/python3*/site-packages/watchfiles* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/watchfiles* usr/lib64/python3*/site-packages/watchfiles* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-watchfiles -f %{oreon_filedir}/python3-watchfiles.list

%changelog

%autochangelog
