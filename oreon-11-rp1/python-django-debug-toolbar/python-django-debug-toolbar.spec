%global source0_hash a5ff2a54f24bf88286f9872836081078f4baa843dc3735ee88524e89f8821e33

%global srcname django-debug-toolbar

Name:           python-%{srcname}
Version:        3.2.1
Release:        20%{?dist}
Summary:        Configurable set of panels that display various debug information

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jazzband/django-debug-toolbar
Source:         %{pypi_source}

BuildArch:      noarch

%global _description\
The Django Debug Toolbar is a configurable set of panels that display various\
debug information about the current request/response and when clicked, display\
more details about the panel's content.\
\
Currently, the following panels have been written and are working:\
\
 -   Django version\
 -   Request timer\
 -   A list of settings in settings.py\
 -   Common HTTP headers\
 -   GET/POST/cookie/session variable display\
 -   Templates and context used, and their template paths\
 -   SQL queries including time to execute and links to EXPLAIN each query\
 -   List of signals, their args and receivers\
 -   Logging output via Python's built-in logging, or via the logbook module

%description %_description

%package -n python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Obsoletes:     python-django-debug-toolbar < 1.9.1-3
Obsoletes:     python2-django-debug-toolbar < 1.9.1-3

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info/

%build
%py3_build

%install
%py3_install

%check
# test needs config
# %{__python3} setup.py test

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/debug_toolbar/
%{python3_sitelib}/django_debug_toolbar-*.egg-info/

%changelog
%autochangelog
