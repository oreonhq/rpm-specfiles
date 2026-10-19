%global source0_hash 011e3cf1a68b31747cb762ba3d755ae1bdcc464c8fad0dc212a9adc550719552
Name:           python-pyshacl
Version:        0.40.1
Release:        1%{?dist}
Summary:        Python SHACL Validator
License:        ...
URL:            https://github.com/RDFLib/pySHACL
Source0:        https://files.pythonhosted.org/packages/source/p/pyshacl/pyshacl-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) < 3
BuildRequires:  python3dist(poetry-core) >= 2.0
Requires:       python3-pyshacl = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyshacl+js
Summary:        Metapackage for python3-pyshacl js extras
Requires:       python3-pyshacl = %{version}-%{release}
Requires:       python3dist(pyduktape2) < 1
Requires:       python3dist(pyduktape2) >= 0.4.6
Requires:       python3dist(pyduktape2) >= 0.5.0
Provides:       python3dist(pyshacl[js]) = %{version}-%{release}

%description -n python3-pyshacl+js
Metapackage for python3-pyshacl js extras.

%package -n       python3-pyshacl+oxigraph
Summary:        Metapackage for python3-pyshacl oxigraph extras
Requires:       python3-pyshacl = %{version}-%{release}
Requires:       python3dist(pyoxigraph) >= 0.5.6
Provides:       python3dist(pyshacl[oxigraph]) = %{version}-%{release}

%description -n python3-pyshacl+oxigraph
Metapackage for python3-pyshacl oxigraph extras.

%package -n       python3-pyshacl+http
Summary:        Metapackage for python3-pyshacl http extras
Requires:       python3-pyshacl = %{version}-%{release}
Requires:       python3dist(sanic) < 23
Requires:       python3dist(sanic) >= 22.12
Requires:       python3dist(sanic-ext) < 23.6
Requires:       python3dist(sanic-ext) >= 23.3
Requires:       python3dist(sanic-cors) == 2.2.0
Provides:       python3dist(pyshacl[http]) = %{version}-%{release}

%description -n python3-pyshacl+http
Metapackage for python3-pyshacl http extras.

%package -n       python3-pyshacl+dev-lint
Summary:        Metapackage for python3-pyshacl dev-lint extras
Requires:       python3-pyshacl = %{version}-%{release}
Requires:       python3dist(ruff) < 0.10
Requires:       python3dist(ruff) >= 0.9.3
Provides:       python3dist(pyshacl[dev-lint]) = %{version}-%{release}

%description -n python3-pyshacl+dev-lint
Metapackage for python3-pyshacl dev-lint extras.

%package -n       python3-pyshacl+dev-type-checking
Summary:        Metapackage for python3-pyshacl dev-type-checking extras
Requires:       python3-pyshacl = %{version}-%{release}
Requires:       python3dist(mypy) >= 1.13.0
Provides:       python3dist(pyshacl[dev-type-checking]) = %{version}-%{release}

%description -n python3-pyshacl+dev-type-checking
Metapackage for python3-pyshacl dev-type-checking extras.

%package -n       python3-pyshacl+dev-coverage
Summary:        Metapackage for python3-pyshacl dev-coverage extras
Requires:       python3-pyshacl = %{version}-%{release}
Requires:       python3dist(pytest-cov) < 3
Requires:       python3dist(pytest-cov) >= 2.8.1
Requires:       python3dist(coverage) > 6
Requires:       python3dist(coverage) < 7
Provides:       python3dist(pyshacl[dev-coverage]) = %{version}-%{release}

%description -n python3-pyshacl+dev-coverage
Metapackage for python3-pyshacl dev-coverage extras.

%description

%package -n     python3-pyshacl
Summary:        Python SHACL Validator
# oreon:reqs
Requires:       python3dist(importlib-metadata) > 6
Requires:       python3dist(owlrl) < 8
Requires:       python3dist(owlrl) >= 7.6.2
Requires:       python3dist(packaging) >= 21.3
Requires:       python3dist(prettytable) >= 3.5.0
Requires:       python3dist(prettytable) >= 3.7.0
Requires:       python3dist(rdflib[html]) < 8.0
Requires:       python3dist(rdflib[html]) >= 7.3.0
# /oreon:reqs
%description -n python3-pyshacl

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyshacl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyshacl usr/lib/python3*/site-packages/pyshacl* usr/lib64/python3*/site-packages/pyshacl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyshacl* usr/lib64/python3*/site-packages/pyshacl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyshacl -f %{oreon_filedir}/python3-pyshacl.list

%changelog

%autochangelog
