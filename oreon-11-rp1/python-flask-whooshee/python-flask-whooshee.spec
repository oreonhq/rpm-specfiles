%global source0_hash 4770a4b8a0425ad39654a9ec62930fb94d4c4e600505cb589314c0ba35201ae2

%global mod_name flask-whooshee

Name:           python-flask-whooshee
Version:        0.9.1
Release:        8%{?dist}
Summary:        Whoosh integration

License:        BSD-3-Clause
URL:            https://github.com/fedora-copr/flask-whooshee
Source0:        https://pypi.python.org/packages/source/f/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:      noarch

%global _description \
Whoosh integration that allows to create and search custom indexes.

%description %{_description}

%package -n python3-%{mod_name}
Summary:        Whoosh integration
BuildRequires:  python3-devel
BuildRequires:  python3-whoosh
BuildRequires:  python3-flask
BuildRequires:  python3-flask-sqlalchemy
BuildRequires:  python3-flexmock
BuildRequires:  python3-blinker
BuildRequires:  python3-pytest

Requires:       python3-flask-sqlalchemy
Requires:       python3-whoosh
Requires:       python3-blinker
Requires:       python3-flask

%description -n python3-%{mod_name} %{_description}

Python 3 version.

%generate_buildrequires
%pyproject_buildrequires 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{mod_name}-%{version}

%build
%pyproject_wheel

%check
%{__python3} -m pytest -vv test.py

%install
%pyproject_install

%files -n python3-%{mod_name}
%doc LICENSE README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/flask_whooshee.py
%{python3_sitelib}/*.dist-info

%changelog
%autochangelog
