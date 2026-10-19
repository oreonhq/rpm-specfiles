%global source0_hash 047e713eeddecf11a674d4cd27ac72407f85ef13196856ba8dfeb4d691d521d4
%global pypi_name django-uuslug
Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        A Django slugify application that guarantees uniqueness and handles Unicode
License:        MIT
URL:            https://github.com/un33k/django-uuslug
Source0:        https://files.pythonhosted.org/packages/source/p/python-django-uuslug/python-django-uuslug-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0001-Add-upstream-test-suite.patch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(python-slugify)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
# /oreon:deps
%description
A Django slugify application that guarantees Uniqueness and handles Unicode

%package -n     python3-%{pypi_name}
Summary:        A Django slugify application that guarantees uniqueness and handles Unicode
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(python-slugify) >= 1.2.0
Requires:       python3dist(six)
Requires:       python3dist(django)
%description -n python3-%{pypi_name}
A Django slugify application that guarantees Uniqueness and handles Unicode

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf django_uuslug.egg-info

%check

%{__python3} manage.py test
%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-django-uuslug -f %{oreon_filedir}/python3-django-uuslug.list

%changelog

%autochangelog
