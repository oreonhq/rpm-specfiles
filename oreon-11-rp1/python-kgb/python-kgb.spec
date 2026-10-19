%global source0_hash b8af7e79cb8b0df5a2ec596010b8e5d014845cfaa9203577b85b99d4df192927
Name:           python-kgb
Version:        7.3
Release:        1%{?dist}
Summary:        Utilities for spying on function calls in unit tests.
License:        MIT
URL:            https://github.com/beanbaginc/kgb
Source0:        https://files.pythonhosted.org/packages/source/k/kgb/kgb-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-kgb = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-kgb
Summary:        Utilities for spying on function calls in unit tests.
%description -n python3-kgb

%prep
%global oreon_srcdir kgb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-kgb usr/lib/python3*/site-packages/kgb* usr/lib64/python3*/site-packages/kgb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/kgb* usr/lib64/python3*/site-packages/kgb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-kgb -f %{oreon_filedir}/python3-kgb.list

%changelog

%autochangelog
