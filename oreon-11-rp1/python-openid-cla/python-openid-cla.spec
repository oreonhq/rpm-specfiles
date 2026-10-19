%global source0_hash ea029d6bcfc69c245fbebe6b4115fc513e6369e740ccce2fcb72829015b1b029
Name:           python-openid-cla
Version:        1.2
Release:        1%{?dist}
Summary:        CLA extension for python-openid
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/puiterwijk/python-openid-cla
Source0:        https://github.com/puiterwijk/python-openid-cla/releases/download/v%{version}/python-openid-cla-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-openid
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-openid-cla
Summary:        OpenID support for Flask
Requires:       python3-openid
%description -n python3-openid-cla
CLA extension implementation for python-openid

This package includes the python 3 version of the module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%{__python3} setup.py build
%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
%oreon_autofiles python3-openid-cla usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-openid-cla -f %{oreon_filedir}/python3-openid-cla.list

%changelog

%autochangelog
