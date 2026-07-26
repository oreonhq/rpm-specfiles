%global source0_hash e5bb62891f458d55332e36a32e19c08d20142c43f74bc5656c803f8af25c084a

%global srcname django-taggit

Name:           python-%{srcname}
Version:        1.5.1
Release:        %autorelease
Summary:        Reusable Django application for simple tagging

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jazzband/django-taggit
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info
# remove unnecessary language ressources:
rm taggit/locale/*/LC_MESSAGES/django.po

%build
%py3_build

%install
%py3_install
%find_lang django

%files -n python3-%{srcname} -f django.lang
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python3_sitelib}/django_taggit-*.egg-info/
%{python3_sitelib}/taggit/

%changelog
%autochangelog
