%global source0_hash 6f55008ecacf96ba945309fc12e680544764995e27bd63cc5e109afb97d7044d
Name:           python-distributed
Version:        2026.8.0
Release:        1%{?dist}
Summary:        Distributed scheduler for Dask
License:        BSD-3-Clause
URL:            https://distributed.dask.org
Source0:        https://files.pythonhosted.org/packages/source/d/distributed/distributed-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
BuildRequires:  python3dist(setuptools-scm) >= 9
Requires:       python3-distributed = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-distributed
Summary:        Distributed scheduler for Dask
# oreon:reqs
Requires:       python3dist(click) >= 8.0
Requires:       python3dist(cloudpickle) >= 3.0.0
Requires:       python3dist(dask) < 2026.8.1
Requires:       python3dist(dask) >= 2026.8.0
Requires:       python3dist(jinja2) >= 2.10.3
Requires:       python3dist(locket) >= 1.0.0
Requires:       python3dist(msgpack) >= 1.0.2
Requires:       python3dist(packaging) >= 20.0
Requires:       python3dist(psutil) >= 5.8.0
Requires:       python3dist(pyyaml) >= 5.4.1
Requires:       python3dist(sortedcontainers) >= 2.0.5
Requires:       python3dist(tblib) >= 1.6.0
Requires:       python3dist(toolz) >= 0.12.0
Requires:       python3dist(tornado) >= 6.2.0
Requires:       python3dist(zict) >= 3.0.0
# /oreon:reqs
%description -n python3-distributed

%prep
%global oreon_srcdir distributed-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-distributed usr/lib/python3*/site-packages/distributed* usr/lib64/python3*/site-packages/distributed* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/distributed* usr/lib64/python3*/site-packages/distributed* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-distributed -f %{oreon_filedir}/python3-distributed.list

%changelog

%autochangelog
