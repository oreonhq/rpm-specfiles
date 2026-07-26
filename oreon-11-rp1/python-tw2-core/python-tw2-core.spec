%global source0_hash c321f410354005e33d11c3982ac532f763761d6a476386ec02cbdccd955e7e6c

%global modname tw2.core

Name:           python-tw2-core
Version:        2.3.0
Release:        25%{?dist}
Summary:        Web widget creation toolkit based on TurboGears widgets

License:        MIT
URL:            http://toscawidgets.org
Source0:        https://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz

# remove kajiki support because of broken dependencies on Fedora
#Patch1:         python-tw2-core-without-kajiki.patch

BuildArch:      noarch

# For building, generally
# General
BuildRequires:  python3-devel
BuildRequires:  python3-webob >= 0.9.7
BuildRequires:  python3-simplejson >= 2.0
BuildRequires:  python3-decorator
BuildRequires:  python3-markupsafe
BuildRequires:  python3-speaklater
#BuildRequires:  python3-paste-deploy
BuildRequires:  python3-six

# Specifically for the test suite
#BuildRequires:  python3-nose
BuildRequires:  python3-coverage
BuildRequires:  python3-formencode
BuildRequires:  python3-webtest
BuildRequires:  python3-sieve

# Templating languages for the test suite
BuildRequires:  python3-mako
BuildRequires:  python3-genshi
BuildRequires:  python3-chameleon
BuildRequires:  python3-kajiki
BuildRequires:  python3-jinja2

%description

ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the web.

The tw2.core package is lightweight and intended for run-time use only;
development tools are in tw2.devtools.

%package -n python3-tw2-core
Summary: Web widget creation toolkit based on TurboGears widgets
Requires: python3-webob >= 0.9.7
Requires: python3-simplejson >= 2.0
Requires: python3-decorator
Requires: python3-markupsafe
Requires: python3-speaklater
#Requires: python3-paste-deploy
Requires: python3-six

%description -n python3-tw2-core
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the web.

The tw2.core package is lightweight and intended for run-time use only;
development tools are in tw2.devtools.

This package contains the python3 version of the toolkit

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
# Fix shebang for python3
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' tw2/core/testbase/xhtmlify.py
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build \
    --install-data=%{_datadir} --root=%{buildroot}

%files -n python3-tw2-core
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/tw2
%{python3_sitelib}/%{modname}-%{version}*

%changelog
%autochangelog
