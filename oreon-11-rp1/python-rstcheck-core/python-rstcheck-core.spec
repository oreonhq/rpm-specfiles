%global source0_hash 511ea4a39f88c5c01291689c7e2abd6c75c0d18492e1af722c7f2ac1fde34b97
Name:           python-rstcheck-core
Version:        1.3.2
Release:        1%{?dist}
Summary:        Checks syntax of reStructuredText and code blocks nested within it
License:        MIT
URL:            https://github.com/rstcheck/rstcheck-core
Source0:        https://files.pythonhosted.org/packages/source/r/rstcheck_core/rstcheck_core-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-rstcheck-core = %{version}-%{release}
# /oreon:deps
%package -n       python3-rstcheck-core+sphinx
Summary:        Metapackage for python3-rstcheck-core sphinx extras
Requires:       python3-rstcheck-core = %{version}-%{release}
Requires:       python3dist(sphinx) >= 6.0
Provides:       python3dist(rstcheck-core[sphinx]) = %{version}-%{release}

%description -n python3-rstcheck-core+sphinx
Metapackage for python3-rstcheck-core sphinx extras.

%package -n       python3-rstcheck-core+toml
Summary:        Metapackage for python3-rstcheck-core toml extras
Requires:       python3-rstcheck-core = %{version}-%{release}
Requires:       python3dist(tomli) >= 2.0
Provides:       python3dist(rstcheck-core[toml]) = %{version}-%{release}

%description -n python3-rstcheck-core+toml
Metapackage for python3-rstcheck-core toml extras.

%package -n       python3-rstcheck-core+yaml
Summary:        Metapackage for python3-rstcheck-core yaml extras
Requires:       python3-rstcheck-core = %{version}-%{release}
Requires:       python3dist(pyyaml) >= 6.0.0
Provides:       python3dist(rstcheck-core[yaml]) = %{version}-%{release}

%description -n python3-rstcheck-core+yaml
Metapackage for python3-rstcheck-core yaml extras.

%package -n       python3-rstcheck-core+testing
Summary:        Metapackage for python3-rstcheck-core testing extras
Requires:       python3-rstcheck-core = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.2
Requires:       python3dist(pytest-cov) >= 3.0
Requires:       python3dist(coverage[toml]) >= 6.0
Requires:       python3dist(coverage-conditional-plugin) >= 0.5
Requires:       python3dist(pytest-sugar) >= 0.9.5
Requires:       python3dist(pytest-randomly) >= 3.0
Requires:       python3dist(pytest-mock) >= 3.7
Provides:       python3dist(rstcheck-core[testing]) = %{version}-%{release}

%description -n python3-rstcheck-core+testing
Metapackage for python3-rstcheck-core testing extras.

%package -n       python3-rstcheck-core+docs
Summary:        Metapackage for python3-rstcheck-core docs extras
Requires:       python3-rstcheck-core = %{version}-%{release}
Requires:       python3dist(sphinx) >= 6.0
Requires:       python3dist(myst-parser) >= 3
Requires:       python3dist(sphinx-rtd-theme) >= 1.2
Requires:       python3dist(sphinx-autodoc-typehints) >= 1.15
Requires:       python3dist(sphinxcontrib-apidoc) >= 0.3
Requires:       python3dist(sphinxcontrib-spelling) >= 7.3
Requires:       python3dist(sphinx-autobuild) >= 2021.3.14
Provides:       python3dist(rstcheck-core[docs]) = %{version}-%{release}

%description -n python3-rstcheck-core+docs
Metapackage for python3-rstcheck-core docs extras.

%package -n       python3-rstcheck-core+type-check
Summary:        Metapackage for python3-rstcheck-core type-check extras
Requires:       python3-rstcheck-core = %{version}-%{release}
Requires:       python3dist(mypy) >= 1.0
Requires:       python3dist(types-docutils) >= 0.18
Requires:       python3dist(types-pyyaml) >= 6.0.0
Provides:       python3dist(rstcheck-core[type-check]) = %{version}-%{release}

%description -n python3-rstcheck-core+type-check
Metapackage for python3-rstcheck-core type-check extras.

%package -n       python3-rstcheck-core+dev
Summary:        Metapackage for python3-rstcheck-core dev extras
Requires:       python3-rstcheck-core = %{version}-%{release}
Requires:       python3dist(tox) >= 3.15
Provides:       python3dist(rstcheck-core[dev]) = %{version}-%{release}

%description -n python3-rstcheck-core+dev
Metapackage for python3-rstcheck-core dev extras.

%description

%package -n     python3-rstcheck-core
Summary:        Checks syntax of reStructuredText and code blocks nested within it
# oreon:reqs
Requires:       python3dist(docutils) >= 0.7
Requires:       python3dist(pydantic) >= 2
# /oreon:reqs
%description -n python3-rstcheck-core

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rstcheck_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rstcheck-core usr/lib/python3*/site-packages/rstcheck_core* usr/lib64/python3*/site-packages/rstcheck_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rstcheck_core* usr/lib64/python3*/site-packages/rstcheck_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rstcheck-core -f %{oreon_filedir}/python3-rstcheck-core.list

%changelog

%autochangelog
