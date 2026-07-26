%global source0_hash 3fa6de6efa2493a7c827472e984ce9b020797d0da16f1db67197bcc23c8fae54

Name:           python-raven

Version:        6.10.0
Release:        29%{?dist}
Summary:        Python client for Sentry

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/raven/
Source0:        https://files.pythonhosted.org/packages/source/r/raven/raven-%{version}.tar.gz
Patch0:         raven-use-system-cacert.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#needed for check:
#BuildRequires:  python3-contextlib2
#BuildRequires:  python3-flask-login
#BuildRequires:  python3-blinker
#BuildRequires:  python3-anyjson
#BuildRequires:  python3-webtest
#BuildRequires:  python3-tornado
#BuildRequires:  python3-requests
#BuildRequires:  python3-pytest

%global _description\
Raven is a Python client for Sentry <http://getsentry.com>. It provides full\
out-of-the-box support for many of the popular frameworks, including Django,\
and Flask. Raven also includes drop-in support for any WSGI-compatible web\
application.

%description %_description

%package -n python3-raven
Summary:        Python client for Sentry
%{?python_provide:%python_provide python3-raven}

%description -n python3-raven
Raven is a Python client for Sentry <http://getsentry.com>. It provides full
out-of-the-box support for many of the popular frameworks, including Django,
and Flask. Raven also includes drop-in support for any WSGI-compatible web
application.

%{?python_extras_subpkg:%python_extras_subpkg -n python3-raven -i %{python3_sitelib}/*.egg-info flask}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n raven-%{version}
%patch -P0 -p1

rm raven/data/cacert.pem
rmdir raven/data

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root=%{buildroot}

%check
#Disable check for now because of missing dependency pytest-timeout
#%%{__python3} setup.py test

%files -n python3-raven
%doc README.rst
%license LICENSE
%{_bindir}/raven
%{python3_sitelib}/*

%changelog
%autochangelog
