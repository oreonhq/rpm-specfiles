%global source0_hash 4e953dcd963c036daaa2ac42b5bb6ea89a1c6ea7be0387c2022a59aca2f83043
Name:           python-mozilla-django-oidc
Version:        5.0.2
Release:        1%{?dist}
Summary:        A lightweight authentication and access management library for integration with OpenID Connect enabled authentication services.
License:        MPL-2.0
URL:            https://github.com/mozilla/mozilla-django-oidc
Source0:        https://files.pythonhosted.org/packages/source/m/mozilla_django_oidc/mozilla_django_oidc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 75.0.0
Requires:       python3-mozilla-django-oidc = %{version}-%{release}
# /oreon:deps
%package -n       python3-mozilla-django-oidc+drf
Summary:        Metapackage for python3-mozilla-django-oidc drf extras
Requires:       python3-mozilla-django-oidc = %{version}-%{release}
Requires:       python3dist(djangorestframework) >= 3.14
Provides:       python3dist(mozilla-django-oidc[drf]) = %{version}-%{release}

%description -n python3-mozilla-django-oidc+drf
Metapackage for python3-mozilla-django-oidc drf extras.

%package -n       python3-mozilla-django-oidc+test
Summary:        Metapackage for python3-mozilla-django-oidc test extras
Requires:       python3-mozilla-django-oidc = %{version}-%{release}
Requires:       python3dist(djangorestframework) >= 3.14
Requires:       python3dist(splinter[selenium]) >= 0.21.0
Provides:       python3dist(mozilla-django-oidc[test]) = %{version}-%{release}

%description -n python3-mozilla-django-oidc+test
Metapackage for python3-mozilla-django-oidc test extras.

%package -n       python3-mozilla-django-oidc+lint
Summary:        Metapackage for python3-mozilla-django-oidc lint extras
Requires:       python3-mozilla-django-oidc = %{version}-%{release}
Provides:       python3dist(mozilla-django-oidc[lint]) = %{version}-%{release}

%description -n python3-mozilla-django-oidc+lint
Metapackage for python3-mozilla-django-oidc lint extras.

%package -n       python3-mozilla-django-oidc+build
Summary:        Metapackage for python3-mozilla-django-oidc build extras
Requires:       python3-mozilla-django-oidc = %{version}-%{release}
Provides:       python3dist(mozilla-django-oidc[build]) = %{version}-%{release}

%description -n python3-mozilla-django-oidc+build
Metapackage for python3-mozilla-django-oidc build extras.

%package -n       python3-mozilla-django-oidc+docs
Summary:        Metapackage for python3-mozilla-django-oidc docs extras
Requires:       python3-mozilla-django-oidc = %{version}-%{release}
Provides:       python3dist(mozilla-django-oidc[docs]) = %{version}-%{release}

%description -n python3-mozilla-django-oidc+docs
Metapackage for python3-mozilla-django-oidc docs extras.

%package -n       python3-mozilla-django-oidc+dev
Summary:        Metapackage for python3-mozilla-django-oidc dev extras
Requires:       python3-mozilla-django-oidc = %{version}-%{release}
Provides:       python3dist(mozilla-django-oidc[dev]) = %{version}-%{release}

%description -n python3-mozilla-django-oidc+dev
Metapackage for python3-mozilla-django-oidc dev extras.

%description

%package -n     python3-mozilla-django-oidc
Summary:        A lightweight authentication and access management library for integration with OpenID Connect enabled authentication services.
# oreon:reqs
Requires:       python3dist(django) >= 4.2
# /oreon:reqs
%description -n python3-mozilla-django-oidc

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mozilla_django_oidc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mozilla-django-oidc usr/lib/python3*/site-packages/mozilla_django_oidc* usr/lib64/python3*/site-packages/mozilla_django_oidc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mozilla_django_oidc* usr/lib64/python3*/site-packages/mozilla_django_oidc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mozilla-django-oidc -f %{oreon_filedir}/python3-mozilla-django-oidc.list

%changelog

%autochangelog
