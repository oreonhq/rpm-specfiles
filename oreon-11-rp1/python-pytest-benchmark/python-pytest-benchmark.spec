%global source0_hash 358444d4e89be901ee2b6404fb043ac3d7684002ad7f3563cc153fca6339c965
Name:           python-pytest-benchmark
Version:        5.3.0
Release:        1%{?dist}
Summary:        A __pytest__ fixture for benchmarking code. It will group the tests into rounds that are calibrated to the chosen timer.
License:        BSD-2-Clause
URL:            https://pytest-benchmark.readthedocs.io/en/latest/changelog.html
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_benchmark/pytest_benchmark-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
Requires:       python3-pytest-benchmark = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-benchmark+aspect
Summary:        Metapackage for python3-pytest-benchmark aspect extras
Requires:       python3-pytest-benchmark = %{version}-%{release}
Provides:       python3dist(pytest-benchmark[aspect]) = %{version}-%{release}

%description -n python3-pytest-benchmark+aspect
Metapackage for python3-pytest-benchmark aspect extras.

%package -n       python3-pytest-benchmark+elasticsearch
Summary:        Metapackage for python3-pytest-benchmark elasticsearch extras
Requires:       python3-pytest-benchmark = %{version}-%{release}
Provides:       python3dist(pytest-benchmark[elasticsearch]) = %{version}-%{release}

%description -n python3-pytest-benchmark+elasticsearch
Metapackage for python3-pytest-benchmark elasticsearch extras.

%package -n       python3-pytest-benchmark+histogram
Summary:        Metapackage for python3-pytest-benchmark histogram extras
Requires:       python3-pytest-benchmark = %{version}-%{release}
Provides:       python3dist(pytest-benchmark[histogram]) = %{version}-%{release}

%description -n python3-pytest-benchmark+histogram
Metapackage for python3-pytest-benchmark histogram extras.

%description

%package -n     python3-pytest-benchmark
Summary:        A __pytest__ fixture for benchmarking code. It will group the tests into rounds that are calibrated to the chosen timer.
# oreon:reqs
Requires:       python3dist(py-cpuinfo2) >= 10.1
Requires:       python3dist(pytest) >= 8.1
# /oreon:reqs
%description -n python3-pytest-benchmark

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_benchmark-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-benchmark usr/lib/python3*/site-packages/pytest_benchmark* usr/lib64/python3*/site-packages/pytest_benchmark* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_benchmark* usr/lib64/python3*/site-packages/pytest_benchmark* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-benchmark -f %{oreon_filedir}/python3-pytest-benchmark.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.0-5
- Prepare for Oreon 11 (RP1)
