%global source0_hash 8afed18aa189fd81e2e833b426bb4af485594921f0b1d36c2001fc5637a2f210
Name:           python-jsonpickle
Version:        4.1.2
Release:        1%{?dist}
Summary:        jsonpickle encodes/decodes any Python object to/from JSON
License:        BSD-3-Clause
URL:            https://jsonpickle.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/j/jsonpickle/jsonpickle-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.0
Requires:       python3-jsonpickle = %{version}-%{release}
# /oreon:deps
%package -n       python3-jsonpickle+cov
Summary:        Metapackage for python3-jsonpickle cov extras
Requires:       python3-jsonpickle = %{version}-%{release}
Provides:       python3dist(jsonpickle[cov]) = %{version}-%{release}

%description -n python3-jsonpickle+cov
Metapackage for python3-jsonpickle cov extras.

%package -n       python3-jsonpickle+dev
Summary:        Metapackage for python3-jsonpickle dev extras
Requires:       python3-jsonpickle = %{version}-%{release}
Provides:       python3dist(jsonpickle[dev]) = %{version}-%{release}

%description -n python3-jsonpickle+dev
Metapackage for python3-jsonpickle dev extras.

%package -n       python3-jsonpickle+testing
Summary:        Metapackage for python3-jsonpickle testing extras
Requires:       python3-jsonpickle = %{version}-%{release}
Requires:       python3dist(pytest) >= 6.0
Requires:       python3dist(pytest-checkdocs) >= 1.2.3
Requires:       python3dist(pytest-enabler) >= 1.0.1
Requires:       python3dist(pytest-ruff) >= 0.2.1
Requires:       python3dist(scipy) >= 1.9.3
Requires:       python3dist(atheris) >= 2.3.0
Provides:       python3dist(jsonpickle[testing]) = %{version}-%{release}

%description -n python3-jsonpickle+testing
Metapackage for python3-jsonpickle testing extras.

%package -n       python3-jsonpickle+docs
Summary:        Metapackage for python3-jsonpickle docs extras
Requires:       python3-jsonpickle = %{version}-%{release}
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(sphinx) >= 3.5
Provides:       python3dist(jsonpickle[docs]) = %{version}-%{release}

%description -n python3-jsonpickle+docs
Metapackage for python3-jsonpickle docs extras.

%package -n       python3-jsonpickle+packaging
Summary:        Metapackage for python3-jsonpickle packaging extras
Requires:       python3-jsonpickle = %{version}-%{release}
Requires:       python3dist(setuptools) >= 61.2
Requires:       python3dist(setuptools-scm[toml]) >= 6.0
Provides:       python3dist(jsonpickle[packaging]) = %{version}-%{release}

%description -n python3-jsonpickle+packaging
Metapackage for python3-jsonpickle packaging extras.

%description

%package -n     python3-jsonpickle
Summary:        jsonpickle encodes/decodes any Python object to/from JSON
%description -n python3-jsonpickle

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jsonpickle-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jsonpickle usr/lib/python3*/site-packages/jsonpickle* usr/lib64/python3*/site-packages/jsonpickle* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jsonpickle* usr/lib64/python3*/site-packages/jsonpickle* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jsonpickle -f %{oreon_filedir}/python3-jsonpickle.list

%changelog

%autochangelog
