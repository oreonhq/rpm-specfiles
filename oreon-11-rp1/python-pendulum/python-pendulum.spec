%global source0_hash e80feda2d10fa3ff8b1526715f7d33dcb7e08494b3088f2c8a3ac92d4a4331ce
Name:           python-pendulum
Version:        3.2.0
Release:        1%{?dist}
Summary:        Python datetimes made easy
License:        MIT
URL:            https://pendulum.eustace.io
Source0:        https://files.pythonhosted.org/packages/source/p/pendulum/pendulum-%{version}.tar.gz
Patch:          0001-Allow-PyO3-0.26-until-we-have-0.27-RHBZ-2404994.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.0
Requires:       python3-pendulum = %{version}-%{release}
# /oreon:deps
%package -n       python3-pendulum+test
Summary:        Metapackage for python3-pendulum test extras
Requires:       python3-pendulum = %{version}-%{release}
Requires:       python3dist(time-machine) >= 2.6.0
Requires:       python3dist(time-machine) < 3.0.0
Provides:       python3dist(pendulum[test]) = %{version}-%{release}

%description -n python3-pendulum+test
Metapackage for python3-pendulum test extras.

%description

%package -n     python3-pendulum
Summary:        Python datetimes made easy
# oreon:reqs
Requires:       python3dist(python-dateutil) >= 2.6
Requires:       python3dist(tzdata) >= 2020.1
# /oreon:reqs
%description -n python3-pendulum

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pendulum-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pendulum usr/lib/python3*/site-packages/pendulum* usr/lib64/python3*/site-packages/pendulum* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pendulum* usr/lib64/python3*/site-packages/pendulum* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pendulum -f %{oreon_filedir}/python3-pendulum.list

%changelog

%autochangelog
