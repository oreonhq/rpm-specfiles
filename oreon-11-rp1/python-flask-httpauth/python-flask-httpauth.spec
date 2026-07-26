%global source0_hash 66568a05bc73942c65f1e2201ae746295816dc009edd84b482c44c758d75097a

%global pypi_name Flask-HTTPAuth
%global pkg_name flask-httpauth

Name:           python-%{pkg_name}
Version:        4.8.0
Release:        9%{?dist}
Summary:        Basic and Digest HTTP authentication for Flask routes

License:        MIT
URL:            http://github.com/miguelgrinberg/flask-httpauth/
Source0:        https://files.pythonhosted.org/packages/source/F/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# https://github.com/miguelgrinberg/Flask-HTTPAuth/commit/52a13b15b
Patch0:         python-flask-httpauth-toml.patch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-flask+async
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildArch:      noarch

%description
FlaskHTTPAuth Basic and Digest HTTP authentication for Flask routes.

%package -n     python-%{pkg_name}-doc
Summary:        Documentation for Flask-HTTPAuth

%description -n python-%{pkg_name}-doc
FlaskHTTPAuth Basic and Digest HTTP authentication for Flask routes.

This package provides the documentation.

%package -n     python3-%{pkg_name}
Summary:        Basic and Digest HTTP authentication for Flask routes
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
FlaskHTTPAuth Basic and Digest HTTP authentication for Flask routes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
 
# Build docs
pushd docs
make PYTHONPATH=%{buildroot}/%{python3_sitelib} SPHINXBUILD=sphinx-build-3 html
rm -v _build/html/.buildinfo
popd

%install
%pyproject_install
%pyproject_save_files flask_httpauth

%check
%pytest

%files -n python-%{pkg_name}-doc
%license LICENSE
%doc docs/_build/html

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
