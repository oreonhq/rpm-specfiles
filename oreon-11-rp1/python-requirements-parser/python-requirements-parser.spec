%global source0_hash 78811383b2089b6c5197a1431bc2c12ff950245edca39a23eea3460782038dd3
Name:           python-requirements-parser
Version:        0.13.1
Release:        1%{?dist}
Summary:        This is a small Python module for parsing Pip requirement files.
License:        Apache-2.0
URL:            https://github.com/madpah/requirements-parser/#readme
Source0:        https://files.pythonhosted.org/packages/source/r/requirements_parser/requirements_parser-%{version}.tar.gz
BuildArch:      noarch
Patch:          pyproject.toml-limit-documentation-to-the-sdist.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-requirements-parser = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-requirements-parser
Summary:        This is a small Python module for parsing Pip requirement files.
%description -n python3-requirements-parser

%prep
%global oreon_srcdir requirements_parser-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-requirements-parser usr/lib/python3*/site-packages/requirements_parser* usr/lib64/python3*/site-packages/requirements_parser* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/requirements_parser* usr/lib64/python3*/site-packages/requirements_parser* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-requirements-parser -f %{oreon_filedir}/python3-requirements-parser.list

%changelog

%autochangelog
