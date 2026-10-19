%global source0_hash 83ad2901e3bfc3fdde4a5046bcd6dca400c7c252d575375ec58236a27fecb861
Name:           python-django-clacks
Version:        0.3.1
Release:        1%{?dist}
Summary:        Django Middleware for X-Clacks-Overhead
License:        MIT
URL:            https://github.com/ractf/django-clacks
Source0:        https://github.com/ractf/django-clacks/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-django-clacks = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-clacks
Summary:        Django Middleware for X-Clacks-Overhead
%py_provides    python3-django-clacks
%description -n python3-django-clacks

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir django-clacks-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-clacks usr/lib/python3*/site-packages/django_clacks* usr/lib64/python3*/site-packages/django_clacks* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_clacks* usr/lib64/python3*/site-packages/django_clacks* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-django-clacks -f %{oreon_filedir}/python3-django-clacks.list

%changelog

%autochangelog
