%global source0_hash aa1d79df6f215b78396cdd50ed162f8741dc4993e9fba2c78483d9b6f1e722b4
Name:           python-django-pipeline
Version:        4.1.0
Release:        1%{?dist}
Summary:        Pipeline is an asset packaging library for Django.
License:        MIT
URL:            https://github.com/jazzband/django-pipeline/
Source0:        https://files.pythonhosted.org/packages/source/d/django_pipeline/django_pipeline-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm[toml]) >= 8
Requires:       python3-django-pipeline = %{version}-%{release}
# /oreon:deps
%package -n       python3-django-pipeline+testing
Summary:        Metapackage for python3-django-pipeline testing extras
Requires:       python3-django-pipeline = %{version}-%{release}
Provides:       python3dist(django-pipeline[testing]) = %{version}-%{release}

%description -n python3-django-pipeline+testing
Metapackage for python3-django-pipeline testing extras.

%description

%package -n     python3-django-pipeline
Summary:        Pipeline is an asset packaging library for Django.
%description -n python3-django-pipeline

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir django_pipeline-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-pipeline usr/lib/python3*/site-packages/django_pipeline* usr/lib64/python3*/site-packages/django_pipeline* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_pipeline* usr/lib64/python3*/site-packages/django_pipeline* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-pipeline -f %{oreon_filedir}/python3-django-pipeline.list

%changelog

%autochangelog
