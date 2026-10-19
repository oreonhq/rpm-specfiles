%global source0_hash e67e9ddc70ea00ba2cc1f3c048bd8146015e4ede019ae1d76adf325e78813df0
Name:           python-xdot
Version:        1.6
Release:        1%{?dist}
Summary:        Interactive viewer for Graphviz dot files
License:        LGPL-3.0-or-later AND Apache-1.1
URL:            https://pypi.python.org/pypi/xdot
Source0:        https://github.com/jrfonseca/xdot.py/archive/%{version}.tar.gz#/xdot-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-gobject
Requires:       graphviz
# oreon:deps
BuildRequires:  graphviz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
xdot.py is an interactive viewer for graphs written in Graphviz's dot
language.

Internally it uses the graphviz's xdot output format as an intermediate
format, and PyGTK and Cairo for rendering.

xdot.py can be used either as a standalone application from command line
(as "xdot"), or as a library embedded in a python application.

%{?python_provide:%python_provide python3-xdot}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n xdot.py-%{version}

# Strip the shebang from xdot/__main__.py to avoid an rpmlint warning:
sed '1{\@^#!/usr/bin/env python@d}' xdot/__main__.py > xdot/__main__.py.new &&
 touch -r xdot/__main__.py xdot/__main__.py.new &&
 mv xdot/__main__.py.new xdot/__main__.py

# Remove pre-built egg present in upstream tarball:
rm -rf xdot.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
