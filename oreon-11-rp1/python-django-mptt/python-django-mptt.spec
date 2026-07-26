%global source0_hash 8ae6c3821127b529bb2f938de27bf0771b1bcbe9dbccdfba33986af78611f13a

%global srcname django-mptt

Summary:    Utilities for implementing Modified Preorder Tree Traversal
Name:       python-%{srcname}
Version:    0.12.0
Release:    19%{?dist}
License:    MIT
URL:        https://github.com/django-mptt/django-mptt
Source:     %{pypi_source}
BuildArch:  noarch

%global _description\
Utilities for implementing Modified Preorder Tree Traversal (MPTT)\
with your Django Model classes and working with trees of Model instances.\

%description %_description

%package -n python3-%{srcname}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Obsoletes: python2-django-mptt < 0.9.0-2
Obsoletes: python-django-mptt < 0.9.0-2

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info/

# remove unnecessary language ressources:
rm mptt/locale/*/LC_MESSAGES/django.po

%build
%py3_build

%install
%py3_install

%find_lang django

%check

# tests require django-js-asset
#cd tests
#sh runtests.sh

%files -n python3-django-mptt -f django.lang
%license LICENSE
%doc README.rst NOTES
%{python3_sitelib}/django_mptt-*.egg-info/
%{python3_sitelib}/mptt/

%changelog
%autochangelog
