%global source0_hash 8de4a1330f55b3c9a1d50ab1b70a765f2f136d6399ae206411117ed98c3b8e2b
Name:           python-portalocker
Version:        4.3.2
Release:        1%{?dist}
Summary:        Cross-platform file locking, with Redis, PID-file and bounded-semaphore locks
License:        BSD-3-Clause
URL:            https://github.com/wolph/portalocker/
Source0:        https://files.pythonhosted.org/packages/source/p/portalocker/portalocker-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.13
BuildRequires:  python3dist(uv-build) >= 0.11
Requires:       python3-portalocker = %{version}-%{release}
# /oreon:deps
%package -n       python3-portalocker+redis
Summary:        Metapackage for python3-portalocker redis extras
Requires:       python3-portalocker = %{version}-%{release}
Requires:       python3dist(redis) >= 5.0
Provides:       python3dist(portalocker[redis]) = %{version}-%{release}

%description -n python3-portalocker+redis
Metapackage for python3-portalocker redis extras.

%package -n       python3-portalocker+win32
Summary:        Metapackage for python3-portalocker win32 extras
Requires:       python3-portalocker = %{version}-%{release}
Requires:       python3dist(pywin32) >= 226
Provides:       python3dist(portalocker[win32]) = %{version}-%{release}

%description -n python3-portalocker+win32
Metapackage for python3-portalocker win32 extras.

%package -n       python3-portalocker+tests
Summary:        Metapackage for python3-portalocker tests extras
Requires:       python3-portalocker = %{version}-%{release}
Requires:       python3dist(coverage-conditional-plugin) >= 0.9
Requires:       python3dist(fakeredis) >= 2.31.0
Requires:       python3dist(pytest-cov) >= 2.8.1
Requires:       python3dist(pytest-rerunfailures) >= 15.1
Requires:       python3dist(pytest-timeout) >= 2.1.0
Requires:       python3dist(pytest) >= 5.4.1
Requires:       python3dist(types-pywin32) >= 310.0.0.20250429
Requires:       python3dist(typing-extensions) >= 4.4
Provides:       python3dist(portalocker[tests]) = %{version}-%{release}

%description -n python3-portalocker+tests
Metapackage for python3-portalocker tests extras.

%package -n       python3-portalocker+docs
Summary:        Metapackage for python3-portalocker docs extras
Requires:       python3-portalocker = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7
Provides:       python3dist(portalocker[docs]) = %{version}-%{release}

%description -n python3-portalocker+docs
Metapackage for python3-portalocker docs extras.

%description

%package -n     python3-portalocker
Summary:        Cross-platform file locking, with Redis, PID-file and bounded-semaphore locks
%description -n python3-portalocker

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir portalocker-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-portalocker usr/lib/python3*/site-packages/portalocker* usr/lib64/python3*/site-packages/portalocker* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/portalocker* usr/lib64/python3*/site-packages/portalocker* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-portalocker -f %{oreon_filedir}/python3-portalocker.list

%changelog

%autochangelog
