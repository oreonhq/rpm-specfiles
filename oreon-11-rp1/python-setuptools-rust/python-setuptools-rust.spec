%global source0_hash f2afcf4baeee689910ce49cfa8aad4e08cce72f417449bcc32891b8664fdc726
Name:           python-setuptools-rust
Version:        1.13.0
Release:        1%{?dist}
Summary:        Setuptools Rust extension plugin
License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source0:        https://files.pythonhosted.org/packages/source/s/setuptools_rust/setuptools_rust-%{version}.tar.gz
BuildArch:      noarch
Patch:          setuptools_rust-1.12.0-pyo3-0.28.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-setuptools-rust = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-setuptools-rust
Summary:        Setuptools Rust extension plugin
%description -n python3-setuptools-rust

%prep
%global oreon_srcdir setuptools_rust-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-setuptools-rust usr/lib/python3*/site-packages/setuptools_rust* usr/lib64/python3*/site-packages/setuptools_rust* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/setuptools_rust* usr/lib64/python3*/site-packages/setuptools_rust* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-setuptools-rust -f %{oreon_filedir}/python3-setuptools-rust.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.12.0-1
- Prepare for Oreon 11 (RP1)
