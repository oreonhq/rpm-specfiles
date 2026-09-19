%global source0_hash c7478feab98f3368780591f9ee28a433350f5277dd28811f7f710f5bc6dff3c0

%global srcname django-compressor
%global pypi_name django_compressor
%global _desc\
Django Compressor combines and compresses linked and inline Javascript\
or CSS in a Django templates into cacheable static files by using the\
``compress`` template tag.  HTML in between\
``{% compress js/css %}`` and ``{% endcompress %}`` is\
parsed and searched for CSS or JS. These styles and scripts are subsequently\
processed with optional, configurable compilers and filters.

# setuptools < 77.0.3
%if (%{defined fedora} && 0%{?fedora} <= 42) || (%{defined rhel} && 0%{?rhel} <= 10)
%bcond old_setuptools 1
%else
%bcond old_setuptools 0
%endif

Name:		python-django-compressor
Version:	4.6.0
Release:	%autorelease
Summary:	Compresses linked and inline JavaScript or CSS into single cached files

License:	MIT
URL:		https://github.com/django-compressor/django-compressor
Source0:	%{pypi_source django_compressor}
# deleted in 4e543307 - migration to pyproject.toml
Source1:        setup.py

BuildArch:	noarch

BuildRequires:	python3-devel

%description %_desc

%package -n python3-%{srcname}
Summary:	%{summary}

# Added in f28 cycle.
Obsoletes: python2-%{srcname} < 2.1-6
Obsoletes: python-%{srcname} < 2.1-6

%description -n python3-%{srcname} %_desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
%if %{with old_setuptools}
rm pyproject.toml
cp -p %{SOURCE1} setup.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files compressor

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
