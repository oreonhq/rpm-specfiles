%global source0_hash 8291def038ac3ba753fdcc53fdedc89b4b4c8a80f670f19f0b11794b8c5aaca5
%global srcname Flask-Mako
%global eggname Flask_Mako
Name:               python-flask-mako
Version:            0.4
Release:        37%{?dist}
Summary:        Mako templating support for Flask applications
License:            LicenseRef-Callaway-BSD
URL:                http://pypi.python.org/pypi/%{srcname}
Source0:        http://pypi.python.org/packages/source/F/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:          noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-flask
BuildRequires:  python3-mako
BuildRequires:  python3-setuptools
# /oreon:deps
%description
This extension for the Flask micro web framework allows developers
to use Mako Templates instead of the default Jinja2 templating engine.

%package -n python3-flask-mako
Summary:            Mako templating support for Flask applications
%{?python_provide:%python_provide python3-flask-mako}
Requires:           python3-flask
Requires:           python3-mako
%description -n python3-flask-mako
This extension for the Flask micro web framework allows developers
to use Mako Templates instead of the default Jinja2 templating engine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-flask-mako usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-flask-mako -f %{oreon_filedir}/python3-flask-mako.list

%changelog

%autochangelog
