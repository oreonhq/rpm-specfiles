%global source0_hash 8fc3e6cd0486c6af48e3317c299def719b57538332a194e0b3bc6a772f4faa0e
%global pypi_name zope.hookable
Name:           python-zope-hookable
Version:        5.1.0
Release:        1%{?dist}
Summary:        Efficient creation of hookable objects
License:        ZPL-2.1
URL:            http://github.com/zopefoundation/zope.hookable
Source0:        https://files.pythonhosted.org/packages/source/z/zope_hookable/zope_hookable-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# /oreon:deps
%description

%package -n python3-zope-hookable
Summary:        Efficient creation of hookable objects
%description -n python3-zope-hookable

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-zope-hookable usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest --pyargs %{pypi_name}
%files -f %{oreon_filedir}/main.list
%files -n python3-zope-hookable -f %{oreon_filedir}/python3-zope-hookable.list

%changelog

%autochangelog
