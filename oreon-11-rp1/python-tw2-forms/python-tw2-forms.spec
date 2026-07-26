%global source0_hash 8c4a7dcd8ab2706beaa4a4eee2a60d59be3afa82208078b99b186dd5c83a77d1

%global modname tw2.forms

Name:           python-tw2-forms
Version:        2.2.6
Release:        30%{?dist}
Summary:        Forms for ToscaWidgets2

License:        MIT
URL:            http://toscawidgets.org
Source0:        https://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

# For building, generally
BuildRequires:  python3-devel
BuildRequires:  python3-webob >= 0.9.7
BuildRequires:  python3-tw2-core >= 2.1.4
#BuildRequires:  python3-paste-deploy

# Specifically for the test suite
#BuildRequires:  python3-nose
BuildRequires:  python3-coverage
BuildRequires:  python3-formencode
BuildRequires:  python3-webtest
BuildRequires:  python3-sieve >= 0.1.9

# Templating languages for the test suite
BuildRequires:  python3-mako
BuildRequires:  python3-genshi
BuildRequires:  python3-chameleon
BuildRequires:  python3-kajiki
BuildRequires:  python3-jinja2

# Runtime requirements

%global _description\
ToscaWidgets is a web widget toolkit for Python to aid in the creation,\
packaging and distribution of common view elements normally used in the web.\
\
tw2.forms contains the basic form widgets.

%description %_description

%package -n python3-tw2-forms
Summary: Forms for ToscaWidgets2
Requires: python3-tw2-core >= 2.1.4

%description -n python3-tw2-forms
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the web.

This package contains the basic form widgets build for python3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%files -n python3-tw2-forms
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/tw2/forms
%{python3_sitelib}/%{modname}-%{version}*

%changelog
%autochangelog
