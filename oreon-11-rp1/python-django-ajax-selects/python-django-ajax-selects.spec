%global source0_hash 539298874b2d26ce9e778a5173d312f55340c887a126c7e2d3460b9a5b4593a2
%global pkgname django-ajax-selects
Name:           python-django-ajax-selects
Version:        3.0.3
Release:        1%{?dist}
Summary:        Enables editing of ForeignKey, ManyToMany and simple text fields
License:        LicenseRef-Callaway-MIT OR GPL-1.0-or-later
URL:            https://github.com/crucialfelix/django-ajax-selects
Source0:        http://pypi.python.org/packages/source/d/%{pkgname}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-django-ajax-selects
Summary:        Intelligent schema migrations for Django apps
%{?python_provide:%python_provide python3-django-ajax-selects}
Requires:       python3-django
Obsoletes:      python2-django-ajax-selects < 1.3.4-14
Obsoletes:      python-django-ajax-selects < 1.3.4-14
%description -n python3-django-ajax-selects

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-django-ajax-selects usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-django-ajax-selects -f %{oreon_filedir}/python3-django-ajax-selects.list

%changelog

%autochangelog
