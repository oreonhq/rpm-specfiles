%global source0_hash 680003f3b15a2959e4e6a351f3b858e3c07dd3e073a0d54954e34d8ea5e1308e
Name:           python-jstyleson
Version:        0.0.2
Release:        1%{?dist}
Summary:        Library to parse JSON with js-style comments.
License:        MIT
URL:            https://github.com/linjackson78/jstyleson
Source0:        https://files.pythonhosted.org/packages/source/j/jstyleson/jstyleson-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jstyleson = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jstyleson
Summary:        Library to parse JSON with js-style comments.
%description -n python3-jstyleson

%prep
%global oreon_srcdir jstyleson-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jstyleson usr/lib/python3*/site-packages/jstyleson* usr/lib64/python3*/site-packages/jstyleson* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jstyleson* usr/lib64/python3*/site-packages/jstyleson* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jstyleson -f %{oreon_filedir}/python3-jstyleson.list

%changelog

%autochangelog
