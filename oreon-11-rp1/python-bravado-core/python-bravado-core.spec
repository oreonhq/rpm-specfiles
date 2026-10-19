%global source0_hash fb1fd29ddcfae1819cca88bc0ae000ef79bc797515a8f2fe56364793188da0a0
Name:           python-bravado-core
Version:        6.4.1
Release:        1%{?dist}
Summary:        Library for adding Swagger support to clients and servers
License:        ...
URL:            https://github.com/Yelp/bravado-core
Source0:        https://files.pythonhosted.org/packages/source/b/bravado_core/bravado_core-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Use-standard-library-mock-when-possible.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-bravado-core = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-bravado-core
Summary:        Library for adding Swagger support to clients and servers
# oreon:reqs
Requires:       python3dist(jsonschema[format-nongpl]) >= 2.5.1
Requires:       python3dist(msgpack) >= 0.5.2
Requires:       python3dist(swagger-spec-validator) >= 2.0.1
# /oreon:reqs
%description -n python3-bravado-core

%prep
%global oreon_srcdir bravado_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bravado-core usr/lib/python3*/site-packages/bravado_core* usr/lib64/python3*/site-packages/bravado_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bravado_core* usr/lib64/python3*/site-packages/bravado_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bravado-core -f %{oreon_filedir}/python3-bravado-core.list

%changelog

%autochangelog
