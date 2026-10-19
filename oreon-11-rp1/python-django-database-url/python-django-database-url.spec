%global source0_hash 63c20e4bbaa51690dfd4c8d189521f6bf6bc9da9fcdb23d95d2ee8ee87f9ec62
Name:           python-dj-database-url
Version:        3.1.2
Release:        1%{?dist}
Summary:        Use Database URLs in your Django Application.
License:        BSD-3-Clause
URL:            https://jazzband.co/projects/dj-database-url
Source0:        https://files.pythonhosted.org/packages/source/d/dj_database_url/dj_database_url-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.10.0
BuildRequires:  python3dist(uv-build) >= 0.9.17
Requires:       python3-dj-database-url = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-dj-database-url
Summary:        Use Database URLs in your Django Application.
# oreon:reqs
Requires:       python3dist(django) >= 4.2
# /oreon:reqs
%description -n python3-dj-database-url

%prep
%global oreon_srcdir dj_database_url-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dj-database-url usr/lib/python3*/site-packages/dj_database_url* usr/lib64/python3*/site-packages/dj_database_url* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dj_database_url* usr/lib64/python3*/site-packages/dj_database_url* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dj-database-url -f %{oreon_filedir}/python3-dj-database-url.list

%changelog

%autochangelog
