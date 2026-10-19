%global source0_hash 694ae5cc8a42f4c4e2bf2ca0e64e51e23a040c6a517a85074683d3959e1346c1
Name:           python-argon2-cffi
Version:        25.1.0
Release:        1%{?dist}
Summary:        Argon2 for Python
License:        MIT
URL:            https://github.com/hynek/argon2-cffi
Source0:        https://files.pythonhosted.org/packages/source/a/argon2_cffi/argon2_cffi-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-argon2-cffi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-argon2-cffi
Summary:        Argon2 for Python
%description -n python3-argon2-cffi

%prep
%global oreon_srcdir argon2_cffi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-argon2-cffi usr/lib/python3*/site-packages/argon2_cffi* usr/lib64/python3*/site-packages/argon2_cffi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/argon2_cffi* usr/lib64/python3*/site-packages/argon2_cffi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-argon2-cffi -f %{oreon_filedir}/python3-argon2-cffi.list

%changelog

%autochangelog
