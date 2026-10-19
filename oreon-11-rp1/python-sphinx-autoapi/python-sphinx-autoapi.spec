%global source0_hash 04643fc50485039294ace8b660d0d1b821a1686824a975725a5106e8cf1fb30b
Name:           python-sphinx-autoapi
Version:        3.8.1
Release:        1%{?dist}
Summary:        Sphinx API documentation generator
License:        MIT
URL:            http://github.com/readthedocs/sphinx-autoapi
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_autoapi/sphinx_autoapi-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-sphinx-autoapi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinx-autoapi
Summary:        Sphinx API documentation generator
# oreon:reqs
Requires:       python3dist(astroid) >= 3.0
Requires:       python3dist(sphinx) >= 7.4.0
# /oreon:reqs
%description -n python3-sphinx-autoapi

%prep
%global oreon_srcdir sphinx_autoapi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-autoapi usr/lib/python3*/site-packages/sphinx_autoapi* usr/lib64/python3*/site-packages/sphinx_autoapi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_autoapi* usr/lib64/python3*/site-packages/sphinx_autoapi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-autoapi -f %{oreon_filedir}/python3-sphinx-autoapi.list

%changelog

%autochangelog
