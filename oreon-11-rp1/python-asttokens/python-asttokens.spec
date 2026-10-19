%global source0_hash 3ecdbd8f2cc195f53ccada3a613538bb5f9ef6f6869129f13e03c30a677b8fe2
Name:           python-asttokens
Version:        3.0.2
Release:        1%{?dist}
Summary:        Annotate AST trees with source code positions
License:        ...
URL:            https://asttokens.readthedocs.io/en/latest/index.html
Source0:        https://files.pythonhosted.org/packages/source/a/asttokens/asttokens-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 44
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-asttokens = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-asttokens
Summary:        Annotate AST trees with source code positions
%description -n python3-asttokens

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir asttokens-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-asttokens usr/lib/python3*/site-packages/asttokens* usr/lib64/python3*/site-packages/asttokens* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/asttokens* usr/lib64/python3*/site-packages/asttokens* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-asttokens -f %{oreon_filedir}/python3-asttokens.list

%changelog

%autochangelog
