%global source0_hash 8d73c88cab7c98b7926710299c1162bec7ce253f9b9c5f0a2ca8037f9f240234
Name:           python-flufl-lock
Version:        9.1.0
Release:        1%{?dist}
Summary:        NFS-safe file locking with timeouts for POSIX and Windows
License:        Apache-2.0
URL:            https://flufllock.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/f/flufl_lock/flufl_lock-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-flufl-lock = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flufl-lock
Summary:        NFS-safe file locking with timeouts for POSIX and Windows
%description -n python3-flufl-lock

%prep
%global oreon_srcdir flufl_lock-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flufl-lock usr/lib/python3*/site-packages/flufl_lock* usr/lib64/python3*/site-packages/flufl_lock* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flufl_lock* usr/lib64/python3*/site-packages/flufl_lock* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flufl-lock -f %{oreon_filedir}/python3-flufl-lock.list

%changelog

%autochangelog
