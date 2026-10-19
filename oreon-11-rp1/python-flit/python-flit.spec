%global source0_hash 18b463c435db03b8cbecf139b6b0bb285b2dfd8a7e623558136abd66f4a04af4
Name:           python-flit
Version:        4.1.0
Release:        1%{?dist}
Summary:        A simple packaging tool for simple packages.
License:        BSD-3-Clause
URL:            https://github.com/pypa/flit
Source0:        https://files.pythonhosted.org/packages/source/f/flit/flit-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-flit = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flit
Summary:        A simple packaging tool for simple packages.
%description -n python3-flit

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir flit-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flit usr/lib/python3*/site-packages/flit* usr/lib64/python3*/site-packages/flit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flit* usr/lib64/python3*/site-packages/flit* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flit -f %{oreon_filedir}/python3-flit.list

%changelog

%autochangelog
