%global source0_hash 3fa6de6efa2493a7c827472e984ce9b020797d0da16f1db67197bcc23c8fae54
Name:           python-raven
Version:        6.10.0
Release:        29%{?dist}
Summary:        Python client for Sentry
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/raven/
Source0:        https://files.pythonhosted.org/packages/source/r/raven/raven-%{version}.tar.gz
Patch0:         raven-use-system-cacert.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

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
%oreon_autofiles python3-raven usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n python3-raven -f %{oreon_filedir}/python3-raven.list

%changelog

%autochangelog
