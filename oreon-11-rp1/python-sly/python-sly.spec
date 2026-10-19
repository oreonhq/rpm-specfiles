%global source0_hash 251d42015e8507158aec2164f06035df4a82b0314ce6450f457d7125e7649024
Name:           python-sly
Version:        0.5
Release:        1%{?dist}
Summary:        _SLY - Sly Lex Yacc_
License:        MIT
URL:            https://github.com/dabeaz/sly
Source0:        https://files.pythonhosted.org/packages/source/s/sly/sly-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sly = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sly
Summary:        _SLY - Sly Lex Yacc_
%description -n python3-sly

%prep
%global oreon_srcdir sly-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sly usr/lib/python3*/site-packages/sly* usr/lib64/python3*/site-packages/sly* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sly* usr/lib64/python3*/site-packages/sly* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sly -f %{oreon_filedir}/python3-sly.list

%changelog

%autochangelog
