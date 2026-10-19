%global source0_hash e141bae5f6572749dfbb283155743a068771a7cefbd02baf3952f90e64de88ce
Name:           python-sklearn-nature-inspired-algorithms
Version:        0.15.0
Release:        1%{?dist}
Summary:        Search using nature inspired algorithms over specified parameter values for an sklearn estimator.
License:        MIT
URL:            https://github.com/timzatko/Sklearn-Nature-Inspired-Algorithms
Source0:        https://files.pythonhosted.org/packages/source/s/sklearn_nature_inspired_algorithms/sklearn_nature_inspired_algorithms-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-sklearn-nature-inspired-algorithms = %{version}-%{release}
# /oreon:deps
%package -n       python3-sklearn-nature-inspired-algorithms+dev
Summary:        Metapackage for python3-sklearn-nature-inspired-algorithms dev extras
Requires:       python3-sklearn-nature-inspired-algorithms = %{version}-%{release}
Requires:       python3dist(flake8) >= 6.0
Requires:       python3dist(coverage) >= 7.0
Provides:       python3dist(sklearn-nature-inspired-algorithms[dev]) = %{version}-%{release}

%description -n python3-sklearn-nature-inspired-algorithms+dev
Metapackage for python3-sklearn-nature-inspired-algorithms dev extras.

%description

%package -n     python3-sklearn-nature-inspired-algorithms
Summary:        Search using nature inspired algorithms over specified parameter values for an sklearn estimator.
# oreon:reqs
Requires:       python3dist(matplotlib) >= 3.9
Requires:       python3dist(niapy) >= 2.7.0
Requires:       python3dist(numpy) >= 1.26
Requires:       python3dist(pandas) >= 2.2.2
Requires:       python3dist(scikit-learn) >= 1.4.2
Requires:       python3dist(scipy) >= 1.13
Requires:       python3dist(seaborn) >= 0.13
# /oreon:reqs
%description -n python3-sklearn-nature-inspired-algorithms

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sklearn_nature_inspired_algorithms-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sklearn-nature-inspired-algorithms usr/lib/python3*/site-packages/sklearn_nature_inspired_algorithms* usr/lib64/python3*/site-packages/sklearn_nature_inspired_algorithms* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sklearn_nature_inspired_algorithms* usr/lib64/python3*/site-packages/sklearn_nature_inspired_algorithms* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sklearn-nature-inspired-algorithms -f %{oreon_filedir}/python3-sklearn-nature-inspired-algorithms.list

%changelog

%autochangelog
