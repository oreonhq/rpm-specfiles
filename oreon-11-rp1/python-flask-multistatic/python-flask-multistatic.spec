%global source0_hash f5e9c8e451dceb18dc6343a72021c93c5fc509fdf960fa41639c98cd33289b5c

%global modname flask-multistatic
%global sum A simple flask plugin to allow overriding static files

Name:               python-flask-multistatic
Version:            1.0
Release:            37%{?dist}
Summary:            %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:            LicenseRef-Callaway-BSD
URL:                https://pagure.io/flask-multistatic/
Source0:            https://pypi.python.org/packages/source/f/flask-multistatic/flask-multistatic-%{version}.tar.gz
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-flask
BuildRequires:      python3-setuptools

%description
Simple flask plugin allowing to override static files, making theming flask
applications really easy.

%package -n         python3-%{modname}
Summary:            %{sum}
Requires:           python3-flask

%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-flask-multistatic
Simple flask plugin allowing to override static files, making theming flask
applications really easy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

rm -rf %{modname}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/flask_multistatic.py*
%{python3_sitelib}/__pycache__/flask_multistatic*
%{python3_sitelib}/flask_multistatic-%{version}-*

%changelog
%autochangelog
