%global source0_hash 3d2de6650852fdf3da896917b2fe88550d854dda590de5f239c2899f7eaf20df
Name:           python-fuzzyfinder
Version:        2.3.0
Release:        1%{?dist}
Summary:        Fuzzy Finder implemented in Python.
License:        ...
URL:            https://github.com/amjith/fuzzyfinder
Source0:        https://files.pythonhosted.org/packages/source/f/fuzzyfinder/fuzzyfinder-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64.0
BuildRequires:  python3dist(setuptools-scm) < 8
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-fuzzyfinder = %{version}-%{release}
# /oreon:deps
%package -n       python3-fuzzyfinder+dev
Summary:        Metapackage for python3-fuzzyfinder dev extras
Requires:       python3-fuzzyfinder = %{version}-%{release}
Requires:       python3dist(coverage) >= 7.2.7
Requires:       python3dist(pytest) >= 7.4.4
Requires:       python3dist(pytest-cov) >= 4.1.0
Requires:       python3dist(pdbpp) >= 0.10.3
Requires:       python3dist(ruff) >= 0.11.1
Requires:       python3dist(sphinx) >= 8.1.3
Requires:       python3dist(sphinx-rtd-theme) >= 3.0.2
Requires:       python3dist(mypy) >= 1.15.0
Provides:       python3dist(fuzzyfinder[dev]) = %{version}-%{release}

%description -n python3-fuzzyfinder+dev
Metapackage for python3-fuzzyfinder dev extras.

%description

%package -n     python3-fuzzyfinder
Summary:        Fuzzy Finder implemented in Python.
%description -n python3-fuzzyfinder

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fuzzyfinder-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fuzzyfinder usr/lib/python3*/site-packages/fuzzyfinder* usr/lib64/python3*/site-packages/fuzzyfinder* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fuzzyfinder* usr/lib64/python3*/site-packages/fuzzyfinder* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fuzzyfinder -f %{oreon_filedir}/python3-fuzzyfinder.list

%changelog

%autochangelog
