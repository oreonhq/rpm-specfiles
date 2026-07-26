%global source0_hash 760e984a931f4468d096f5541787efb8998c61217b73006163bf2f9523fe8f23

%global pypi_name django-filter
%global mod_name django_filter

Name:           python-%{pypi_name}
Version:        25.2
Release:        %autorelease
Summary:        A Django application for allowing users to filter queryset dynamically

License:        BSD-3-Clause
URL:            https://github.com/carltongibson/django-filter
Source0:        %{pypi_source %{mod_name}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description\
Django-filter is a reusable Django application for allowing users to filter\
querysets dynamically.

%description %_description

%package -n python3-%{pypi_name}
Summary:        %summary
Requires:       python3-django-rest-framework
%{?python_provide:%python_provide python3-%{pypi_name}}

Obsoletes:      python-%{pypi_name} < 1.0.2-3
Obsoletes:      python2-%{pypi_name} < 1.0.2-3

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:        django-filter documentation
%description -n python-%{pypi_name}-doc
Documentation for django-filter

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{mod_name}-%{version} -p1

# Fix requirements
sed -i '/^\.$/d' requirements/docs.txt

# Remove unnecessary test BR
sed -i '/^unittest-xml-reporting$/d' requirements/test-ci.txt

%generate_buildrequires
%pyproject_buildrequires -t requirements/docs.txt

%build
%pyproject_wheel

# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files -l %{mod_name}s

%check
%{__python3} runtests.py --verbosity=2

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.rst README.rst docs/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
