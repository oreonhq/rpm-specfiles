%global source0_hash 622ee0f9a5dae946e635b7c6e0f6d65e1ed3c9ea0d20b89dab7f58d580e5126e

%global pypi_name npyscreen

Name:           python-%{pypi_name}
Version:        4.10.5
Release:        24%{?dist}
Summary:        Writing user interfaces without all that ugly mucking about in hyperspace

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.npcole.com/npyscreen/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This library provides a framework for developing console applications using
Python and curses. This framework should be powerful enough to create everything
from quick, simple programs to complex, multi-screen applications.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library provides a framework for developing console applications using
Python and curses. This framework should be powerful enough to create everything
from quick, simple programs to complex, multi-screen applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
for i in $(find . -name '*.py')
do
        sed -i -e"s|#\!/usr/bin/python||" $i
        sed -i -e"s|#\!/usr/bin/env python||" $i
        sed -i -e"s|#\!/usr/bin/env pyton||" $i
done

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENCE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
