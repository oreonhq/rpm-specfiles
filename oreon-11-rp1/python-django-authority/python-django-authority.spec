%global source0_hash 93312a6318fc7ec14d2455c399e25d9d533b7dc4abae33b77afb394a0446b4ab

%global pypi_name django-authority

Name:           python-%{pypi_name}
Version:        0.11
Release:        35%{?dist}
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
