%global source0_hash a3d552682dc50c92a7bd0fe5f026e3e889758085d0894a301fe4437c57c9d64f
Name:           python-django-pglocks
Version:        2.1.0
Release:        1%{?dist}
Summary:        DEPRECATED â€” consolidated into django-pgware. Context managers for PostgreSQL advisory locks in Django.
License:        MIT
URL:            https://github.com/Xof/django-pglocks
Source0:        https://files.pythonhosted.org/packages/source/d/django_pglocks/django_pglocks-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-django-pglocks = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-pglocks
Summary:        DEPRECATED â€” consolidated into django-pgware. Context managers for PostgreSQL advisory locks in Django.
# oreon:reqs
Requires:       python3dist(django) >= 4.2
Requires:       python3dist(django-pgware) >= 1.0.0
# /oreon:reqs
%description -n python3-django-pglocks

%prep
%global oreon_srcdir django_pglocks-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-pglocks usr/lib/python3*/site-packages/django_pglocks* usr/lib64/python3*/site-packages/django_pglocks* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_pglocks* usr/lib64/python3*/site-packages/django_pglocks* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-pglocks -f %{oreon_filedir}/python3-django-pglocks.list

%changelog

%autochangelog
