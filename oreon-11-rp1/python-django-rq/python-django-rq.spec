%global source0_hash f09059ab37403a47c7933bca396fabb7f3058732d132462eade5333bc4bcac5f

%global srcname django-rq

Name:           python-%{srcname}
Version:        2.4.1
Release:        19%{?dist}
Summary:        App that provides django integration for RQ (Redis Queue)

License:        MIT
URL:            https://github.com/rq/django-rq
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Django integration with RQ, a Redis based Python queuing library.
Django-RQ is a simple app that allows you to configure your queues
in django's settings.py and easily use them in your project.}

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

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/django_rq-*.egg-info/
%{python3_sitelib}/django_rq/

%changelog
%autochangelog
