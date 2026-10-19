%global source0_hash b957f3e6ea4d55d820e40ff76f450952807013d361a65d7f28acc0acbf29229d
Name:           python-argon2-cffi-bindings
Version:        25.1.0
Release:        1%{?dist}
Summary:        Low-level CFFI bindings for Argon2
License:        MIT
URL:            https://github.com/hynek/argon2-cffi-bindings
Source0:        https://files.pythonhosted.org/packages/source/a/argon2_cffi_bindings/argon2_cffi_bindings-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1.0.1
BuildRequires:  python3dist(cffi) >= 2.0.0b1
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-argon2-cffi-bindings = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-argon2-cffi-bindings
Summary:        Low-level CFFI bindings for Argon2
# oreon:reqs
Requires:       python3dist(cffi) >= 1.0.1
Requires:       python3dist(cffi) >= 2.0.0b1
# /oreon:reqs
%description -n python3-argon2-cffi-bindings

%prep
%global oreon_srcdir argon2_cffi_bindings-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-argon2-cffi-bindings usr/lib/python3*/site-packages/argon2_cffi_bindings* usr/lib64/python3*/site-packages/argon2_cffi_bindings* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/argon2_cffi_bindings* usr/lib64/python3*/site-packages/argon2_cffi_bindings* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-argon2-cffi-bindings -f %{oreon_filedir}/python3-argon2-cffi-bindings.list

%changelog

%autochangelog
