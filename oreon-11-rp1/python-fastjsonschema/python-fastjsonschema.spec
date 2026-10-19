%global source0_hash 72064e12356a7d6ef02165be2946b9abadbdf238536e07eb587e3dbaa33099cf
Name:           python-fastjsonschema
Version:        2.22.2
Release:        1%{?dist}
Summary:        Fastest Python implementation of JSON schema
License:        BSD-3-Clause
URL:            https://github.com/horejsek/python-fastjsonschema
Source0:        https://files.pythonhosted.org/packages/source/f/fastjsonschema/fastjsonschema-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fastjsonschema = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-fastjsonschema
Summary:        Fastest Python implementation of JSON schema
%description -n python3-fastjsonschema

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fastjsonschema-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fastjsonschema usr/lib/python3*/site-packages/fastjsonschema* usr/lib64/python3*/site-packages/fastjsonschema* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fastjsonschema* usr/lib64/python3*/site-packages/fastjsonschema* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fastjsonschema -f %{oreon_filedir}/python3-fastjsonschema.list

%changelog

%autochangelog
