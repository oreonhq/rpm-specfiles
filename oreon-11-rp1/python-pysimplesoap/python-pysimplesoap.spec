%global source1_hash 7356e6cda1d7f2e62663e6749aeeb1a1b8e33553f96d6517bad7904bc3423e5a
%global source0_hash b1bbf4d0d0adff9b652197d61aa1b76731ad618849e27d28fe5cb250916d67e1
%global pypi_name PySimpleSOAP
%global rpmname pysimplesoap
Name:           python-%{rpmname}
Version:        1.16.2
Release:        1%{?dist}
Summary:        Python simple and lightweight SOAP Library
License:        LGPL-3.0-or-later
URL:            https://github.com/pysimplesoap/pysimplesoap
Source0:        https://files.pythonhosted.org/packages/source/p/python-pysimplesoap/python-pysimplesoap-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/pysimplesoap/pysimplesoap/master/license.txt
Patch0:         httplib2.patch 
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
Python simple and lightweight SOAP library for client and
server web services interfaces, aimed to be as small and easy
as possible, supporting most common functionality. 

%package -n     python3-%{rpmname}
Summary:        Python simple and lightweight SOAP Library
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{rpmname}
Python simple and lightweight SOAP library for client and 
server web services interfaces, aimed to be as small and easy 
as possible, supporting most common functionality. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
for lib in pysimplesoap/*.py; do
 sed -e '1{\@^#! /usr/bin/env python@d}' -e '1{\@^#!/usr/bin/env python@d}' \
     -e '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
cp -p %{SOURCE1} .

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pysimplesoap -f %{oreon_filedir}/python3-pysimplesoap.list

%changelog

%autochangelog
