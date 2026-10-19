%global source0_hash 583072b43939627b1b0f4492e8af2587092efc1fb5e9f0228fa2df9ea3b44873
Name:           python-rstcheck
Version:        6.3.0
Release:        1%{?dist}
Summary:        Checks syntax of reStructuredText and code blocks nested within it
License:        MIT
URL:            https://github.com/rstcheck/rstcheck
Source0:        https://files.pythonhosted.org/packages/source/r/rstcheck/rstcheck-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-rstcheck = %{version}-%{release}
# /oreon:deps
%package -n       python3-rstcheck+sphinx
Summary:        Metapackage for python3-rstcheck sphinx extras
Requires:       python3-rstcheck = %{version}-%{release}
Requires:       python3dist(sphinx) >= 6.0
Provides:       python3dist(rstcheck[sphinx]) = %{version}-%{release}

%description -n python3-rstcheck+sphinx
Metapackage for python3-rstcheck sphinx extras.

%package -n       python3-rstcheck+toml
Summary:        Metapackage for python3-rstcheck toml extras
Requires:       python3-rstcheck = %{version}-%{release}
Requires:       python3dist(tomli) >= 2.0
Provides:       python3dist(rstcheck[toml]) = %{version}-%{release}

%description -n python3-rstcheck+toml
Metapackage for python3-rstcheck toml extras.

%package -n       python3-rstcheck+testing
Summary:        Metapackage for python3-rstcheck testing extras
Requires:       python3-rstcheck = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.2
Requires:       python3dist(pytest-cov) >= 3.0
Requires:       python3dist(coverage[toml]) >= 6.0
Requires:       python3dist(coverage-conditional-plugin) >= 0.5
Requires:       python3dist(pytest-sugar) >= 0.9.5
Requires:       python3dist(pytest-randomly) >= 3.0
Provides:       python3dist(rstcheck[testing]) = %{version}-%{release}

%description -n python3-rstcheck+testing
Metapackage for python3-rstcheck testing extras.

%package -n       python3-rstcheck+docs
Summary:        Metapackage for python3-rstcheck docs extras
Requires:       python3-rstcheck = %{version}-%{release}
Requires:       python3dist(sphinx) >= 6.0
Requires:       python3dist(myst-parser) >= 3
Requires:       python3dist(sphinx-rtd-theme) >= 1.2
Requires:       python3dist(sphinxcontrib-spelling) >= 7.3
Requires:       python3dist(sphinxcontrib-typer) >= 0.9.1
Requires:       python3dist(sphinx-autobuild) >= 2021.3.14
Provides:       python3dist(rstcheck[docs]) = %{version}-%{release}

%description -n python3-rstcheck+docs
Metapackage for python3-rstcheck docs extras.

%package -n       python3-rstcheck+type-check
Summary:        Metapackage for python3-rstcheck type-check extras
Requires:       python3-rstcheck = %{version}-%{release}
Requires:       python3dist(mypy) >= 1.0
Provides:       python3dist(rstcheck[type-check]) = %{version}-%{release}

%description -n python3-rstcheck+type-check
Metapackage for python3-rstcheck type-check extras.

%package -n       python3-rstcheck+dev
Summary:        Metapackage for python3-rstcheck dev extras
Requires:       python3-rstcheck = %{version}-%{release}
Requires:       python3dist(tox) >= 3.15
Provides:       python3dist(rstcheck[dev]) = %{version}-%{release}

%description -n python3-rstcheck+dev
Metapackage for python3-rstcheck dev extras.

%description

%package -n     python3-rstcheck
Summary:        Checks syntax of reStructuredText and code blocks nested within it
# oreon:reqs
Requires:       python3dist(rstcheck-core) >= 1.3.1
Requires:       python3dist(typer) >= 0.12.0
# /oreon:reqs
%description -n python3-rstcheck

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rstcheck-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rstcheck usr/lib/python3*/site-packages/rstcheck* usr/lib64/python3*/site-packages/rstcheck* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rstcheck* usr/lib64/python3*/site-packages/rstcheck* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rstcheck -f %{oreon_filedir}/python3-rstcheck.list

%changelog

%autochangelog
