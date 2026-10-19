%global source0_hash a4bff322e8b8e407d7809e942e63177790509f5a2a740d27199ce8368f36f113
Name:           python-urwid
Version:        4.2.4
Release:        1%{?dist}
Summary:        A full-featured console _xterm et al._ user interface library
License:        LGPL-2.1-only
URL:            https://urwid.org/
Source0:        https://files.pythonhosted.org/packages/source/u/urwid/urwid-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80.8.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 8.1.0
Requires:       python3-urwid = %{version}-%{release}
# /oreon:deps
%package -n       python3-urwid+curses
Summary:        Metapackage for python3-urwid curses extras
Requires:       python3-urwid = %{version}-%{release}
Provides:       python3dist(urwid[curses]) = %{version}-%{release}

%description -n python3-urwid+curses
Metapackage for python3-urwid curses extras.

%package -n       python3-urwid+glib
Summary:        Metapackage for python3-urwid glib extras
Requires:       python3-urwid = %{version}-%{release}
Provides:       python3dist(urwid[glib]) = %{version}-%{release}

%description -n python3-urwid+glib
Metapackage for python3-urwid glib extras.

%package -n       python3-urwid+tornado
Summary:        Metapackage for python3-urwid tornado extras
Requires:       python3-urwid = %{version}-%{release}
Requires:       python3dist(tornado) >= 6.5.8
Provides:       python3dist(urwid[tornado]) = %{version}-%{release}

%description -n python3-urwid+tornado
Metapackage for python3-urwid tornado extras.

%package -n       python3-urwid+trio
Summary:        Metapackage for python3-urwid trio extras
Requires:       python3-urwid = %{version}-%{release}
Requires:       python3dist(trio) >= 0.31.0
Provides:       python3dist(urwid[trio]) = %{version}-%{release}

%description -n python3-urwid+trio
Metapackage for python3-urwid trio extras.

%package -n       python3-urwid+twisted
Summary:        Metapackage for python3-urwid twisted extras
Requires:       python3-urwid = %{version}-%{release}
Requires:       python3dist(twisted) >= 24.7.0
Requires:       python3dist(twisted) >= 26.4.0
Provides:       python3dist(urwid[twisted]) = %{version}-%{release}

%description -n python3-urwid+twisted
Metapackage for python3-urwid twisted extras.

%package -n       python3-urwid+zmq
Summary:        Metapackage for python3-urwid zmq extras
Requires:       python3-urwid = %{version}-%{release}
Requires:       python3dist(pyzmq) >= 26.0.0
Provides:       python3dist(urwid[zmq]) = %{version}-%{release}

%description -n python3-urwid+zmq
Metapackage for python3-urwid zmq extras.

%package -n       python3-urwid+serial
Summary:        Metapackage for python3-urwid serial extras
Requires:       python3-urwid = %{version}-%{release}
Provides:       python3dist(urwid[serial]) = %{version}-%{release}

%description -n python3-urwid+serial
Metapackage for python3-urwid serial extras.

%package -n       python3-urwid+lcd
Summary:        Metapackage for python3-urwid lcd extras
Requires:       python3-urwid = %{version}-%{release}
Provides:       python3dist(urwid[lcd]) = %{version}-%{release}

%description -n python3-urwid+lcd
Metapackage for python3-urwid lcd extras.

%description

%package -n     python3-urwid
Summary:        A full-featured console _xterm et al._ user interface library
%description -n python3-urwid

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir urwid-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-urwid usr/lib/python3*/site-packages/urwid* usr/lib64/python3*/site-packages/urwid* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/urwid* usr/lib64/python3*/site-packages/urwid* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-urwid -f %{oreon_filedir}/python3-urwid.list

%changelog

%autochangelog
