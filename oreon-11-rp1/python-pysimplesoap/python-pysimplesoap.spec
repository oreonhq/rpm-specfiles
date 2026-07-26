%global source0_hash b1bbf4d0d0adff9b652197d61aa1b76731ad618849e27d28fe5cb250916d67e1

%global pypi_name PySimpleSOAP
%global rpmname pysimplesoap

Name:           python-%{rpmname}
Version:        1.16.2
Release:        29%{?dist}
Summary:        Python simple and lightweight SOAP Library

License:        LGPL-3.0-or-later
URL:            https://github.com/pysimplesoap/pysimplesoap
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/pysimplesoap/pysimplesoap/master/license.txt
Patch0:         httplib2.patch 
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Python simple and lightweight SOAP library for client and
server web services interfaces, aimed to be as small and easy
as possible, supporting most common functionality. 

%package -n     python3-%{rpmname}
Summary:        %{summary}
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

%files -n python3-%{rpmname}
%license license.txt
%{python3_sitelib}/pysimplesoap
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
