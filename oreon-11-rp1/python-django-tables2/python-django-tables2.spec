%global source0_hash 4eb526464ee56a0b7d827d1da9a4f257e44edb5e1cbb6a0cfb6ca0fed70d8e4f

%global srcname django-tables2

Name:           python-django-tables2
Version:        2.4.0
Release:        %autorelease
Summary:        Table framework for Django

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jieter/django-tables2
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
django-tables2 simplifies the task of turning sets of data into HTML tables.
It has native support for pagination and sorting. It does for HTML tables
what django.forms does for HTML forms.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Obsoletes:      python-%{srcname} < 1.2.3-5
Obsoletes:      python2-%{srcname} < 1.2.3-5

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info/

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/django_tables2/
%{python3_sitelib}/django_tables2-*.egg-info/

%changelog
%autochangelog
