%global source0_hash 2ccc96785b12046c08fd6d55839c12857831b54a3c1673ffadd2f04bfc4eda03
Name:           python-joblib
Version:        1.6.0
Release:        1%{?dist}
Summary:        Lightweight pipelining with Python functions
License:        BSD-3-Clause
URL:            https://joblib.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/j/joblib/joblib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-joblib = %{version}-%{release}
# /oreon:deps
%package -n       python3-joblib+test
Summary:        Metapackage for python3-joblib test extras
Requires:       python3-joblib = %{version}-%{release}
Provides:       python3dist(joblib[test]) = %{version}-%{release}

%description -n python3-joblib+test
Metapackage for python3-joblib test extras.

%package -n       python3-joblib+docs
Summary:        Metapackage for python3-joblib docs extras
Requires:       python3-joblib = %{version}-%{release}
Provides:       python3dist(joblib[docs]) = %{version}-%{release}

%description -n python3-joblib+docs
Metapackage for python3-joblib docs extras.

%description

%package -n     python3-joblib
Summary:        Lightweight pipelining with Python functions
# oreon:reqs
Requires:       python3dist(cloudpickle) >= 3.0
# /oreon:reqs
%description -n python3-joblib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir joblib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-joblib usr/lib/python3*/site-packages/joblib* usr/lib64/python3*/site-packages/joblib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/joblib* usr/lib64/python3*/site-packages/joblib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-joblib -f %{oreon_filedir}/python3-joblib.list

%changelog

%autochangelog
