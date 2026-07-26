%global source0_hash 35887b8851a931374dd697207a8f56c57a9c5cb9dbf0b9fa54314da5666cea5b

%global pypi_name django-crispy-forms

Name:           python-%{pypi_name}
Version:        1.14.0
Release:        15%{?dist}
Summary:        Best way to have Django DRY forms
License:        MIT
URL:            https://github.com/django-crispy-forms/django-crispy-forms
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-django
Requires:	python3-coverage
Requires:	python3-pytest-cov
Requires:	python3-wheel
Requires:	python3-twine
Requires:	python3-pytest

%description
The best way to have Django DRY forms. Build programmatic reusable layouts out
of components, having full control of the rendered HTML without writing HTML in
templates. All this without breaking the standard way of doing things in Django,
so it plays nice with any other form application.

%package -n python3-%{pypi_name}
Summary: %{summary} - Python 3 version
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The best way to have Django DRY forms. Build programmatic reusable layouts out
of components, having full control of the rendered HTML without writing HTML in
templates. All this without breaking the standard way of doing things in Django,
so it plays nice with any other form application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
 
%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/crispy_forms/
%{python3_sitelib}/django_crispy_forms-*.egg-info

%changelog
%autochangelog
