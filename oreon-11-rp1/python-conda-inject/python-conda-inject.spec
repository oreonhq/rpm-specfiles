%global source0_hash 3259eeda320a65015ed9978adb54ab21dd831c03d0c08255c2e2fe068df204f0
Name:           python-conda-inject
Version:        1.3.2
Release:        1%{?dist}
Summary:        Inject a conda environment into the current python environment
License:        MIT
URL:            https://github.com/koesterlab/conda-inject
Source0:        https://github.com/koesterlab/conda-inject/archive/v%{version}/conda-inject-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
Helper functions for injecting a conda environment into the current python
environment. This happens by modifying sys.path, without actually changing the
current python environment.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-conda-inject = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-conda-inject
Summary:        Inject a conda environment into the current python environment
%description -n python3-conda-inject %{common_description}

# Currently, all tests require network access. Furthermore, of the three
# supported package managers (mamba, conda, and micromamba), the one used for
# the tests is mamba, and this is the only one that is not currently packaged.
# We therefore cannot even run the tests in a local mock build with
# --enable-network unless we patch them to use a different package manager.

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-conda-inject usr/lib/python3*/site-packages/conda_inject* usr/lib64/python3*/site-packages/conda_inject* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/conda_inject* usr/lib64/python3*/site-packages/conda_inject* usr/bin/*

%files
%files -n python3-conda-inject -f %{oreon_filedir}/python3-conda-inject.list

%changelog

%autochangelog
