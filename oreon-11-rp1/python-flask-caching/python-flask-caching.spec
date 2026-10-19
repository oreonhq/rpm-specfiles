%global source0_hash f75b451fde3faac0e278da72263818134deca8c4ba6bb07b9b3b238991368dae
Name:           python-flask-caching
Version:        2.5.1
Release:        1%{?dist}
Summary:        Adds caching support to Flask applications.
License:        BSD-3-Clause
URL:            https://github.com/pallets-eco/flask-caching
Source0:        https://files.pythonhosted.org/packages/source/f/flask_caching/flask_caching-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/pallets-eco/flask-caching/pull/599/commits/3c8df1714292549d2fe27fa4a03110657fd647a3.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-flask-caching = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flask-caching
Summary:        Adds caching support to Flask applications.
# oreon:reqs
Requires:       python3dist(cachelib) >= 0.17.0
Requires:       python3dist(flask) >= 3.0
# /oreon:reqs
%description -n python3-flask-caching

%prep
%global oreon_srcdir flask_caching-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-caching usr/lib/python3*/site-packages/flask_caching* usr/lib64/python3*/site-packages/flask_caching* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_caching* usr/lib64/python3*/site-packages/flask_caching* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flask-caching -f %{oreon_filedir}/python3-flask-caching.list

%changelog

%autochangelog
