%global source0_hash 717f9179a0dbed357012ddad50a5ad3d5e4d9a0b8712680d4e687f5e6e6ed9b3
%bcond tests 1
Name:           python-lazy-loader
Version:        0.5
Release:        1%{?dist}
Summary:        Populate library namespace without incurring immediate import costs
License:        BSD-3-Clause
URL:            https://github.com/scientific-python/lazy-loader
Source0:        https://files.pythonhosted.org/packages/source/l/lazy_loader/lazy_loader-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
lazy-loader makes it easy to load subpackages and functions on demand.
Motivation:
• Allow subpackages to be made visible to users without incurring import costs.
• Allow external libraries to be imported only when used, improving import
  times.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-lazy-loader = %{version}-%{release}
# /oreon:deps
%package -n       python3-lazy-loader+test
Summary:        Metapackage for python3-lazy-loader test extras
Requires:       python3-lazy-loader = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.0
Requires:       python3dist(pytest-cov) >= 5.0
Requires:       python3dist(coverage[toml]) >= 7.2
Provides:       python3dist(lazy-loader[test]) = %{version}-%{release}

%description -n python3-lazy-loader+test
Metapackage for python3-lazy-loader test extras.

%package -n       python3-lazy-loader+lint
Summary:        Metapackage for python3-lazy-loader lint extras
Requires:       python3-lazy-loader = %{version}-%{release}
Requires:       python3dist(pre-commit) == 4.3.0
Provides:       python3dist(lazy-loader[lint]) = %{version}-%{release}

%description -n python3-lazy-loader+lint
Metapackage for python3-lazy-loader lint extras.

%package -n       python3-lazy-loader+dev
Summary:        Metapackage for python3-lazy-loader dev extras
Requires:       python3-lazy-loader = %{version}-%{release}
Requires:       python3dist(changelist) == 0.5
Requires:       python3dist(spin) == 0.15
Provides:       python3dist(lazy-loader[dev]) = %{version}-%{release}

%description -n python3-lazy-loader+dev
Metapackage for python3-lazy-loader dev extras.

%description %{common_description}

%package -n python3-lazy-loader
Summary:        Populate library namespace without incurring immediate import costs
%description -n python3-lazy-loader %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lazy-loader usr/lib/python3*/site-packages/lazy_loader* usr/lib64/python3*/site-packages/lazy_loader* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lazy_loader* usr/lib64/python3*/site-packages/lazy_loader* usr/bin/*

%check

%if %{with tests}
%pytest
%endif
%files
%files -n python3-lazy-loader -f %{oreon_filedir}/python3-lazy-loader.list

%changelog

%autochangelog
