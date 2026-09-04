%global source0_hash f2e0b2adfa98cc5f0b4766f35d2666c7d040452d91e93fc47401e85f85bbecbd

%global pypi_name django-authority

Name:           python-%{pypi_name}
Version:        0.14
Release:        1%{?dist}
Summary:        A Django app for generic per-object permissions and custom permission checks

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jazzband/django-authority
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
This is a Django app for generic per-object permissions, custom permission
checks and permission requests. It also includes view decorators and template
tags for ease of use.

%package -n python3-%{pypi_name}
Summary:        Django app for permissions - Python 3 version

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-django

%{?python_provide:%python_provide python3-%{pypi_name}}

Obsoletes:      python-%{pypi_name} < 0.11-5
Obsoletes:      python2-%{pypi_name} < 0.11-5

%description -n python3-%{pypi_name}
This is a Django app for generic per-object permissions, custom permission
checks and permission requests. It also includes view decorators and template
tags for ease of use. This package provides Python 3 build of %{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# remove executable-flag from manage.py in example 
chmod ugo-x example/manage.py

# remove hidden files in example
find example -name '._*.py' -exec rm '{}' \;

%build
%py3_build

%install
%py3_install

# example gets accidently installed to python_sitelib, too
rm -rf %{buildroot}/%{python3_sitelib}/example

%files -n python3-%{pypi_name}
%license LICENSE
%doc AUTHORS README.rst docs/ example/
%{python3_sitelib}/authority/
%{python3_sitelib}/django_authority-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
