%global source0_hash fe5d7cb59fdc2c8c646ce84b727ac2bca8912a247e6e68e1fb507372178e59e8
Name:           python-django-cors-headers
Version:        4.9.0
Release:        1%{?dist}
Summary:        django-cors-headers is a Django application for handling the server headers required for Cross-Origin Resource Sharing _CORS_.
License:        MIT
URL:            https://github.com/adamchainz/django-cors-headers
Source0:        https://files.pythonhosted.org/packages/source/d/django_cors_headers/django_cors_headers-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-django-cors-headers = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-django-cors-headers
Summary:        django-cors-headers is a Django application for handling the server headers required for Cross-Origin Resource Sharing _CORS_.
# oreon:reqs
Requires:       python3dist(asgiref) >= 3.6
Requires:       python3dist(django) >= 4.2
# /oreon:reqs
%description -n python3-django-cors-headers

%prep
%global oreon_srcdir django_cors_headers-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-django-cors-headers usr/lib/python3*/site-packages/django_cors_headers* usr/lib64/python3*/site-packages/django_cors_headers* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/django_cors_headers* usr/lib64/python3*/site-packages/django_cors_headers* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-django-cors-headers -f %{oreon_filedir}/python3-django-cors-headers.list

%changelog

%autochangelog
