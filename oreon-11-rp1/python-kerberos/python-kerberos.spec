%global source0_hash cdd046142a4e0060f96a00eb13d82a5d9ebc0f2d7934393ed559bac773460a2c
Name:           python-kerberos
Version:        1.3.1
Release:        1%{?dist}
Summary:        Kerberos high-level interface
License:        ...
URL:            https://github.com/apple/ccs-pykerberos
Source0:        https://files.pythonhosted.org/packages/source/k/kerberos/kerberos-%{version}.tar.gz
Patch1:         PY_SSIZE_T_CLEAN.patch
Patch2:         include_unistd.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-kerberos = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-kerberos
Summary:        Kerberos high-level interface
%description -n python3-kerberos

%prep
%global oreon_srcdir kerberos-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-kerberos usr/lib/python3*/site-packages/kerberos* usr/lib64/python3*/site-packages/kerberos* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/kerberos* usr/lib64/python3*/site-packages/kerberos* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-kerberos -f %{oreon_filedir}/python3-kerberos.list

%changelog

%autochangelog
