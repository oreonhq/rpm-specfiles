%global source0_hash 15a88d60dd942d6059f467412fe4581db632ef03018a3c183fb415d6fc9e5cec

%global pypi_name django-appconf

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        %autorelease
Summary:        An app to handle configuration defaults of packaged Django apps gracefully

License:        BSD-3-Clause
URL:            http://pypi.python.org/pypi/django-appconf/
Source:         %{pypi_source django_appconf}

BuildArch:      noarch

%global _description %{expand:
A helper class for handling configuration defaults of packaged Django apps
gracefully.

Note:
This app precedes Django's own AppConfig classes that act as "objects [to] store
metadata for an application" inside Django's app loading mechanism. In other
words, they solve a related but different use case than django-appconf and can't
easily be used as a replacement. The similarity in name is purely coincidental.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3dist(pytest)

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n django_appconf-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%pyproject_save_files -l appconf

%check
export PYTHONPATH=.:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=tests.test_settings
%pytest -v tests/*

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc html README.rst

%changelog
%autochangelog
