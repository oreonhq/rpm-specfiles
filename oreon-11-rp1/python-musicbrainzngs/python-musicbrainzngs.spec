%global source0_hash 93c3689e62215328588ec5b82715de7706b355927171a297bd1d56b7f34dcc62

%global module_name musicbrainzngs
%{!?python3_pkgversion: %global python3_pkgversion 3}

Name:           python-musicbrainzngs
Version:        0.7.1
Release:        20%{?dist}
Summary:        Python bindings for MusicBrainz NGS webservice

# Automatically converted from old format: BSD and ISC - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND ISC
URL:            https://github.com/alastair/python-musicbrainzngs
Source0:        https://github.com/alastair/python-musicbrainzngs#/python-%{module_name}-%{version}.tar.gz

BuildArch:      noarch

%description
This library implements webservice bindings for the MusicBrainz NGS site, also
known as /ws/2.

For more information on the MusicBrainz webservice see:
  https://wiki.musicbrainz.org/XML_Web_Service

%package     -n python%{python3_pkgversion}-%{module_name}
Summary:        Python %{python3_pkgversion} bindings for MusicBrainz NGS webservice
%{?python_provide:%python_provide python%{python3_pkgversion}-%{module_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{module_name}
This library implements Python %{python3_pkgversion} webservice bindings for the
MusicBrainz NGS site, also known as /ws/2.

For more information on the MusicBrainz webservice see:
  https://wiki.musicbrainz.org/XML_Web_Service

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
chmod a-x examples/*.py
sed -i '1{\@^#!/usr/bin/env python@d}' examples/*.py

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install

%check
rm -rf musicbrainzngs
%pytest
 
%files -n python%{python3_pkgversion}-%{module_name}
%license COPYING
%doc README.rst docs examples
%{python3_sitelib}/*

%changelog
%autochangelog
