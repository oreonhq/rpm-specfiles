%global source0_hash 539289ed2d19af61ae38d8fe46aec9e4de2b56f9f8b46da0b98c0d387f1d975a
%global mod_name Flask-OpenID
Name:           python-flask-openid
Version:        1.3.0
Release:        1%{?dist}
Summary:        OpenID support for Flask
License:        LicenseRef-Callaway-BSD
URL:            http://github.com/mitsuhiko/flask-openid/
Source0:        https://files.pythonhosted.org/packages/source/%/%{mod_name/%{mod_name-%{version}.tar.gz
Patch01:        71.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-openid
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-flask-openid
Summary:        OpenID support for Flask
Requires:       python3-openid
%description -n python3-flask-openid
Flask-OpenID is an extension to flask that allows you to add openid
based authentication to your website in a matter of minutes.

This package includes the python 3 version of the module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{mod_name}-%{version} -p1
rm -f docs/_themes/.git
rm -f docs/_themes/.gitignore
rm -f docs/.DS_Store
rm -f docs/_static/.DS_Store
rm -f docs/_static/._.DS_Store
rm -f docs/._.DS_Store

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-flask-openid usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-flask-openid -f %{oreon_filedir}/python3-flask-openid.list

%changelog

%autochangelog
