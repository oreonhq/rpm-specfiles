%global source0_hash 5c2c3179646480209616902a1cea7499755cf634adf228b039a50d6e5b5ca8b3
Name:           python-ptrace
Version:        1.0.1
Release:        1%{?dist}
Summary:        C extension providing access to ptrace_2_
License:        ...
URL:            UNKNOWN
Source0:        https://files.pythonhosted.org/packages/source/p/ptrace/ptrace-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ptrace = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ptrace
Summary:        C extension providing access to ptrace_2_
%description -n python3-ptrace

%prep
%global oreon_srcdir ptrace-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ptrace usr/lib/python3*/site-packages/ptrace* usr/lib64/python3*/site-packages/ptrace* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ptrace* usr/lib64/python3*/site-packages/ptrace* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ptrace -f %{oreon_filedir}/python3-ptrace.list

%changelog

%autochangelog
