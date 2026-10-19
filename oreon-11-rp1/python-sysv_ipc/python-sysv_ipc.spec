%global source0_hash ef96ab33bb62e4d14142f0be0524dcc0c3c70c96442df2fc773c67b7c7514199
Name:           python-sysv-ipc
Version:        1.2.0
Release:        1%{?dist}
Summary:        SysV IPC primitives _semaphores, shared memory and message queues_ for Python
License:        BSD-3-Clause
URL:            https://github.com/osvenskan/sysv_ipc/
Source0:        https://files.pythonhosted.org/packages/source/s/sysv_ipc/sysv_ipc-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sysv-ipc = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sysv-ipc
Summary:        SysV IPC primitives _semaphores, shared memory and message queues_ for Python
%description -n python3-sysv-ipc

%prep
%global oreon_srcdir sysv_ipc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sysv-ipc usr/lib/python3*/site-packages/sysv_ipc* usr/lib64/python3*/site-packages/sysv_ipc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sysv_ipc* usr/lib64/python3*/site-packages/sysv_ipc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sysv-ipc -f %{oreon_filedir}/python3-sysv-ipc.list

%changelog

%autochangelog
