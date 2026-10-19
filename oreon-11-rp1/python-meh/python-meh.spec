%global source0_hash 84dddea4c8ad1c9e54dccd91bb20f1b7886f825e3fde985be849bea78c7dd427
%global libreportver 2.0.18-1
Summary:        A python library for handling exceptions
Name: python-meh
Url: https://github.com/rhinstaller/python-meh
Version: 0.53
Release:        1%{?dist}
Source0:        https://github.com/rhinstaller/python-meh/archive/%{name}-%{version}.tar.gz#/python-meh-%{version}.tar.gz
License: GPL-2.0-or-later
BuildArch: noarch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-meh
Summary:  A python 3 library for handling exceptions
%{?python_provide:%python_provide python3-meh}
Obsoletes: python-meh < 0.46-1
Obsoletes: python2-meh < 0.46-1
Requires: python3
Requires: python3-dbus
Requires: python3-rpm
%description -n python3-meh
The python3-meh package is a python 3 library for handling, saving, and reporting
exceptions.

%package -n python3-meh-gui
Summary: Graphical user interface for the python3-meh library
%{?python_provide:%python_provide python3-meh-gui}
Obsoletes: python-meh-gui < 0.46-1
Obsoletes: python2-meh-gui < 0.46-1
Requires: python3-meh = %{version}-%{release}
Requires: python3-gobject, gtk3
%description -n python3-meh-gui
The python3-meh-gui package provides a GUI for the python3-meh library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{name}-%{version}

%build

make
%check

make test
%install
make DESTDIR=%{buildroot} install
%oreon_autofiles python3-meh usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-meh-gui usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-meh -f %{oreon_filedir}/python3-meh.list
%files -n python3-meh-gui -f %{oreon_filedir}/python3-meh-gui.list

%changelog

%autochangelog
