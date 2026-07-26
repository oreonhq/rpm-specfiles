%global source0_hash 0c39471e9efcf7651c56561f7de670b1fb5adf8ca517c3afe121985b5b4035b1

%global pypi_name django-tastypie
%global sum A flexible and capable API layer for Django
Name:           python-%{pypi_name}
Version:        0.14.7
Release:        %autorelease
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/toastdriven/django-tastypie/

# Release version doesn't include tests
Source0:        https://github.com/%{pypi_name}/%{pypi_name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
# Let's keep Requires and BuildRequires sorted alphabetically
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

%description
Tastypie is an webservice API framework for Django. It provides a convenient, 
yet powerful and highly customizable, abstraction for creating REST-style 
interfaces.

%package doc
Summary: Documentation for %{name}

Requires: python3-%{pypi_name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%package -n python3-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-dateutil
Requires:       python3-django
Requires:       python3-mimeparse

Obsoletes:      %{pypi_name} < 0.9.11-3
Obsoletes:      python-%{pypi_name} <= 0.13.3-8
Obsoletes:      python2-%{pypi_name} <= 0.13.3-8

%description -n python3-%{pypi_name}
Tastypie is an webservice API framework for Django. It provides a convenient, 
yet powerful and highly customizable, abstraction for creating REST-style 
interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}

%build
# (re)generate the documentation
#pushd docs
sphinx-build-3 docs docs/_build/html
#make html
#popd
rm -rf docs/_build/html/.??*

%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst AUTHORS LICENSE
%dir %{python3_sitelib}/tastypie
%{python3_sitelib}/django_tastypie*
%{python3_sitelib}/tastypie/*

%files doc
%doc docs/_build/html

%changelog
%autochangelog
