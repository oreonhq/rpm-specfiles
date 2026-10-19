%global source0_hash 640caf961f9098f26e00a22b743c4eb63da681a5390829b1ed951db677866e67
Name:           python-django-q2
Version:        1.11.1
Release:        1%{?dist}
Summary:        A multiprocessing distributed task queue for Django
License:        MIT
URL:            https://django-q2.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/d/django_q2/django_q2-%{version}.tar.gz
BuildArch:      noarch
Patch:          django-q2-rm-changelog.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) <= 0.12.1
BuildRequires:  python3dist(uv-build) >= 0.10.7
Requires:       python3-django-q2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-q2+testing
Summary:        Metapackage for python3-django-q2 testing extras
Requires:       python3-django-q2 = %{version}-%{release}
Provides:       python3dist(django-q2[testing]) = %{version}-%{release}

%description -n python3-django-q2+testing
Metapackage for python3-django-q2 testing extras.

%package -n       python3-django-q2+croniter
Summary:        Metapackage for python3-django-q2 croniter extras
Requires:       python3-django-q2 = %{version}-%{release}
Provides:       python3dist(django-q2[croniter]) = %{version}-%{release}

%description -n python3-django-q2+croniter
Metapackage for python3-django-q2 croniter extras.

%description

%package -n     python3-django-q2
Summary:        A multiprocessing distributed task queue for Django
# oreon:reqs
Requires:       python3dist(django) >= 5.2
Requires:       python3dist(django-picklefield) < 4
Requires:       python3dist(django-picklefield) >= 3.1
Requires:       python3dist(importlib-metadata) >= 3.6
# /oreon:reqs
%description -n python3-django-q2

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_q2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-q2 usr/lib/python3*/site-packages/django_q2* usr/lib64/python3*/site-packages/django_q2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_q2* usr/lib64/python3*/site-packages/django_q2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-q2 -f %{oreon_filedir}/python3-django-q2.list

%changelog

%autochangelog
