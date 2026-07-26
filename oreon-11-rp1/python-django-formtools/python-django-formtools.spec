%global source0_hash c5272c03c1cd51b2375abf7397a199a3148a9fbbf2f100e186467a84025d13b2

%global pypi_name django-formtools

# skip test until test suite supports later django
%global skip_tests 1

Name:           python-%{pypi_name}
Version:        2.2
Release:        22%{?dist}
Summary:        A set of high-level abstractions for Django forms

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://django-formtools.readthedocs.org/en/latest/
Source0:        https://pypi.io/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%package -n python3-%{pypi_name}
Summary:        A set of high-level abstractions for Django forms
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-django >= 1.7
# Required for testing
BuildRequires:  python3-flake8
BuildRequires:  python3-coverage

Requires:       python3-django >= 1.7

Obsoletes:      python-%{pypi_name} < 2.1-5
Obsoletes:      python2-%{pypi_name} < 2.1-5

%description -n python3-%{pypi_name}
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%package -n python3-%{pypi_name}-doc
Summary:        A set of high-level abstractions for Django forms - documentation
%{?python_provide:%python_provide python3-%{pypi_name}-doc}

Requires:       python3-%{pypi_name} = %{version}-%{release}

Obsoletes:      python-%{pypi_name}-doc < 2.1-5
Obsoletes:      python2-%{pypi_name}-doc < 2.1-5

%description -n python3-%{pypi_name}-doc
Django's "formtools" is a set of high-level abstractions for Django forms.

This is the associated documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}

%build
%{py3_build}

%if 0%{?skip_tests} == 0
%check
PYTHONPATH=. DJANGO_SETTINGS_MODULE=tests.settings python3-coverage run %{python3_sitelib}/django/bin/django-admin.py test tests
%endif

%install
%{py3_install}
%find_lang django py3lang
# generate html docs
# Fix doc build with latest Sphinx, see https://github.com/jazzband/django-formtools/issues/279
sed -i "s#'http://docs.python.org/': None#'python': ('https://docs.python.org/3', None)#" docs/conf.py
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%files -n python3-%{pypi_name} -f py3lang
%doc README.rst
%license LICENSE
%{python3_sitelib}/formtools
%{python3_sitelib}/django_formtools-%{version}-py%{python3_version}.egg-info

%files -n python3-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
