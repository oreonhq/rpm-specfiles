%global source0_hash a5bcffb52081ba39df0d5e9a884fc6f819d92e3a42389343ba77cbf809fe1f45
Name:           python-a2wsgi
Version:        1.10.10
Release:        1%{?dist}
Summary:        Convert WSGI app to ASGI app or ASGI app to WSGI app.
License:        Apache-2.0
URL:            https://github.com/abersheeran/a2wsgi
Source0:        https://files.pythonhosted.org/packages/source/a/a2wsgi/a2wsgi-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-a2wsgi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-a2wsgi
Summary:        Convert WSGI app to ASGI app or ASGI app to WSGI app.
%description -n python3-a2wsgi

%prep
%global oreon_srcdir a2wsgi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-a2wsgi usr/lib/python3*/site-packages/a2wsgi* usr/lib64/python3*/site-packages/a2wsgi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/a2wsgi* usr/lib64/python3*/site-packages/a2wsgi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-a2wsgi -f %{oreon_filedir}/python3-a2wsgi.list

%changelog

%autochangelog
