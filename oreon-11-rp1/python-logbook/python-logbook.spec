%global source0_hash 7fdf8d09d60c9eaa4d8d27b37363b4ce277d019f4cae5c259ea03040f7b634b7
Name:           python-logbook
Version:        1.10.1
Release:        1%{?dist}
Summary:        A logging replacement for Python
License:        BSD-3-Clause
URL:            https://github.com/getlogbook/logbook
Source0:        https://files.pythonhosted.org/packages/source/l/logbook/logbook-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-rust) >= 1.11.1
Requires:       python3-logbook = %{version}-%{release}
# /oreon:deps
%package -n       python3-logbook+all
Summary:        Metapackage for python3-logbook all extras
Requires:       python3-logbook = %{version}-%{release}
Provides:       python3dist(logbook[all]) = %{version}-%{release}

%description -n python3-logbook+all
Metapackage for python3-logbook all extras.

%package -n       python3-logbook+brotli
Summary:        Metapackage for python3-logbook brotli extras
Requires:       python3-logbook = %{version}-%{release}
Requires:       python3dist(brotli) >= 1.1.0
Requires:       python3dist(brotlicffi) >= 1.1.0.0
Provides:       python3dist(logbook[brotli]) = %{version}-%{release}

%description -n python3-logbook+brotli
Metapackage for python3-logbook brotli extras.

%package -n       python3-logbook+compression
Summary:        Metapackage for python3-logbook compression extras
Requires:       python3-logbook = %{version}-%{release}
Provides:       python3dist(logbook[compression]) = %{version}-%{release}

%description -n python3-logbook+compression
Metapackage for python3-logbook compression extras.

%package -n       python3-logbook+execnet
Summary:        Metapackage for python3-logbook execnet extras
Requires:       python3-logbook = %{version}-%{release}
Requires:       python3dist(execnet) >= 1.5
Provides:       python3dist(logbook[execnet]) = %{version}-%{release}

%description -n python3-logbook+execnet
Metapackage for python3-logbook execnet extras.

%package -n       python3-logbook+jinja
Summary:        Metapackage for python3-logbook jinja extras
Requires:       python3-logbook = %{version}-%{release}
Requires:       python3dist(jinja2) >= 2.11.3
Provides:       python3dist(logbook[jinja]) = %{version}-%{release}

%description -n python3-logbook+jinja
Metapackage for python3-logbook jinja extras.

%package -n       python3-logbook+nteventlog
Summary:        Metapackage for python3-logbook nteventlog extras
Requires:       python3-logbook = %{version}-%{release}
Requires:       python3dist(pywin32) >= 227
Requires:       python3dist(pywin32) >= 302
Requires:       python3dist(pywin32) >= 303
Requires:       python3dist(pywin32) >= 306
Requires:       python3dist(pywin32) >= 307
Requires:       python3dist(pywin32) >= 311
Requires:       python3dist(pywin32) >= 312
Provides:       python3dist(logbook[nteventlog]) = %{version}-%{release}

%description -n python3-logbook+nteventlog
Metapackage for python3-logbook nteventlog extras.

%package -n       python3-logbook+redis
Summary:        Metapackage for python3-logbook redis extras
Requires:       python3-logbook = %{version}-%{release}
Requires:       python3dist(redis) >= 4.6.0
Provides:       python3dist(logbook[redis]) = %{version}-%{release}

%description -n python3-logbook+redis
Metapackage for python3-logbook redis extras.

%package -n       python3-logbook+sqlalchemy
Summary:        Metapackage for python3-logbook sqlalchemy extras
Requires:       python3-logbook = %{version}-%{release}
Requires:       python3dist(sqlalchemy) >= 1.4
Provides:       python3dist(logbook[sqlalchemy]) = %{version}-%{release}

%description -n python3-logbook+sqlalchemy
Metapackage for python3-logbook sqlalchemy extras.

%package -n       python3-logbook+zmq
Summary:        Metapackage for python3-logbook zmq extras
Requires:       python3-logbook = %{version}-%{release}
Requires:       python3dist(pyzmq) >= 27.0.2
Provides:       python3dist(logbook[zmq]) = %{version}-%{release}

%description -n python3-logbook+zmq
Metapackage for python3-logbook zmq extras.

%description

%package -n     python3-logbook
Summary:        A logging replacement for Python
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.14.0
# /oreon:reqs
%description -n python3-logbook

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir logbook-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-logbook usr/lib/python3*/site-packages/logbook* usr/lib64/python3*/site-packages/logbook* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/logbook* usr/lib64/python3*/site-packages/logbook* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-logbook -f %{oreon_filedir}/python3-logbook.list

%changelog

%autochangelog
