%global source0_hash 4579094d5fc8a1a59555a9b18e51b320779d9bbc63e2302c519af0c4919d9543
Name:           python-graphql-core
Version:        3.2.12
Release:        1%{?dist}
Summary:        GraphQL implementation for Python, a port of GraphQL.js, the JavaScript reference implementation for GraphQL.
License:        MIT
URL:            https://github.com/graphql-python/graphql-core
Source0:        https://files.pythonhosted.org/packages/source/g/graphql_core/graphql_core-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) < 3
BuildRequires:  python3dist(poetry-core) >= 1
BuildRequires:  python3dist(setuptools) < 85
BuildRequires:  python3dist(setuptools) >= 59
Requires:       python3-graphql-core = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-graphql-core
Summary:        GraphQL implementation for Python, a port of GraphQL.js, the JavaScript reference implementation for GraphQL.
%description -n python3-graphql-core

%prep
%global oreon_srcdir graphql_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-graphql-core usr/lib/python3*/site-packages/graphql_core* usr/lib64/python3*/site-packages/graphql_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/graphql_core* usr/lib64/python3*/site-packages/graphql_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-graphql-core -f %{oreon_filedir}/python3-graphql-core.list

%changelog

%autochangelog
