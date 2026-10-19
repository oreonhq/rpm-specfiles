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
%bcond old_setuptools 0
Name:		python-django-compressor
Version:	4.6.0
Release:        1%{?dist}
Summary:        Compresses linked and inline JavaScript or CSS into single cached files
License:	MIT
URL:		https://github.com/django-compressor/django-compressor
Source0:        https://files.pythonhosted.org/packages/source/d/django_compressor/django_compressor-%{version}.tar.gz
Source1:        setup.py
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-django-compressor = %{version}-%{release}
# /oreon:deps
%description %_desc

%package -n python3-%{srcname}
Summary:        Compresses linked and inline JavaScript or CSS into single cached files
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

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/django_compressor* usr/lib64/python3*/site-packages/django_compressor* usr/bin/*

%files
%files -n python3-django-compressor -f %{oreon_filedir}/python3-django-compressor.list

%changelog

%autochangelog
