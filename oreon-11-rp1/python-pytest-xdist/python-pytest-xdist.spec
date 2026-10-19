%global source0_hash 7e578125ec9bc6050861aa93f2d59f1d8d085595d6551c2c90b6f4fad8d3a9f1
Name:           python-pytest-xdist
Version:        3.8.0
Release:        1%{?dist}
Summary:        pytest xdist plugin for distributed testing, most importantly across multiple CPUs
License:        MIT
URL:            https://github.com/pytest-dev/pytest-xdist
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_xdist/pytest_xdist-%{version}.tar.gz
BuildArch:      noarch
Patch:          44f4bea.patch
Patch:          0c98447.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2.3
Requires:       python3-pytest-xdist = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-xdist+testing
Summary:        Metapackage for python3-pytest-xdist testing extras
Requires:       python3-pytest-xdist = %{version}-%{release}
Provides:       python3dist(pytest-xdist[testing]) = %{version}-%{release}

%description -n python3-pytest-xdist+testing
Metapackage for python3-pytest-xdist testing extras.

%package -n       python3-pytest-xdist+psutil
Summary:        Metapackage for python3-pytest-xdist psutil extras
Requires:       python3-pytest-xdist = %{version}-%{release}
Requires:       python3dist(psutil) >= 3.0
Provides:       python3dist(pytest-xdist[psutil]) = %{version}-%{release}

%description -n python3-pytest-xdist+psutil
Metapackage for python3-pytest-xdist psutil extras.

%package -n       python3-pytest-xdist+setproctitle
Summary:        Metapackage for python3-pytest-xdist setproctitle extras
Requires:       python3-pytest-xdist = %{version}-%{release}
Provides:       python3dist(pytest-xdist[setproctitle]) = %{version}-%{release}

%description -n python3-pytest-xdist+setproctitle
Metapackage for python3-pytest-xdist setproctitle extras.

%description

%package -n     python3-pytest-xdist
Summary:        pytest xdist plugin for distributed testing, most importantly across multiple CPUs
# oreon:reqs
Requires:       python3dist(execnet) >= 2.1
Requires:       python3dist(pytest) >= 7.0.0
# /oreon:reqs
%description -n python3-pytest-xdist

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pytest_xdist-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-xdist usr/lib/python3*/site-packages/pytest_xdist* usr/lib64/python3*/site-packages/pytest_xdist* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_xdist* usr/lib64/python3*/site-packages/pytest_xdist* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytest-xdist -f %{oreon_filedir}/python3-pytest-xdist.list

%changelog

%autochangelog
