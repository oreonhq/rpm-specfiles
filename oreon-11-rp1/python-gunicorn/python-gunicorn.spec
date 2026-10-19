%global source0_hash 62b864895d9ebff0b2f9867ba04fe811c93121596540830c9c916d0769668447
Name:           python-gunicorn
Version:        26.2.0
Release:        1%{?dist}
Summary:        WSGI HTTP Server for UNIX
License:        MIT
URL:            https://gunicorn.org
Source0:        https://files.pythonhosted.org/packages/source/g/gunicorn/gunicorn-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-use-dev-log-for-syslog.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-gunicorn = %{version}-%{release}
# /oreon:deps
%package -n       python3-gunicorn+gevent
Summary:        Metapackage for python3-gunicorn gevent extras
Requires:       python3-gunicorn = %{version}-%{release}
Requires:       python3dist(gevent) >= 24.10.1
Provides:       python3dist(gunicorn[gevent]) = %{version}-%{release}

%description -n python3-gunicorn+gevent
Metapackage for python3-gunicorn gevent extras.

%package -n       python3-gunicorn+tornado
Summary:        Metapackage for python3-gunicorn tornado extras
Requires:       python3-gunicorn = %{version}-%{release}
Requires:       python3dist(tornado) >= 6.5.7
Provides:       python3dist(gunicorn[tornado]) = %{version}-%{release}

%description -n python3-gunicorn+tornado
Metapackage for python3-gunicorn tornado extras.

%package -n       python3-gunicorn+gthread
Summary:        Metapackage for python3-gunicorn gthread extras
Requires:       python3-gunicorn = %{version}-%{release}
Provides:       python3dist(gunicorn[gthread]) = %{version}-%{release}

%description -n python3-gunicorn+gthread
Metapackage for python3-gunicorn gthread extras.

%package -n       python3-gunicorn+setproctitle
Summary:        Metapackage for python3-gunicorn setproctitle extras
Requires:       python3-gunicorn = %{version}-%{release}
Provides:       python3dist(gunicorn[setproctitle]) = %{version}-%{release}

%description -n python3-gunicorn+setproctitle
Metapackage for python3-gunicorn setproctitle extras.

%package -n       python3-gunicorn+http2
Summary:        Metapackage for python3-gunicorn http2 extras
Requires:       python3-gunicorn = %{version}-%{release}
Requires:       python3dist(h2) >= 4.4.1
Provides:       python3dist(gunicorn[http2]) = %{version}-%{release}

%description -n python3-gunicorn+http2
Metapackage for python3-gunicorn http2 extras.

%package -n       python3-gunicorn+fast
Summary:        Metapackage for python3-gunicorn fast extras
Requires:       python3-gunicorn = %{version}-%{release}
Requires:       python3dist(gunicorn-h1c) >= 0.6.9
Provides:       python3dist(gunicorn[fast]) = %{version}-%{release}

%description -n python3-gunicorn+fast
Metapackage for python3-gunicorn fast extras.

%package -n       python3-gunicorn+testing
Summary:        Metapackage for python3-gunicorn testing extras
Requires:       python3-gunicorn = %{version}-%{release}
Requires:       python3dist(gevent) >= 24.10.1
Requires:       python3dist(h2) >= 4.4.1
Requires:       python3dist(pytest) >= 9.0.3
Requires:       python3dist(uvloop) >= 0.19.0
Requires:       python3dist(httpx[http2]) >= 0.23.0
Requires:       python3dist(inotify) >= 0.2.10
Provides:       python3dist(gunicorn[testing]) = %{version}-%{release}

%description -n python3-gunicorn+testing
Metapackage for python3-gunicorn testing extras.

%description

%package -n     python3-gunicorn
Summary:        WSGI HTTP Server for UNIX
%description -n python3-gunicorn

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir gunicorn-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gunicorn usr/lib/python3*/site-packages/gunicorn* usr/lib64/python3*/site-packages/gunicorn* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gunicorn* usr/lib64/python3*/site-packages/gunicorn* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gunicorn -f %{oreon_filedir}/python3-gunicorn.list

%changelog

%autochangelog
