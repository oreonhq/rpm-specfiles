%global source0_hash eb2c50404820fde8bfc6a0713b2a0b8eabececfecefde3a5847ae8006037829f
Name:           python-time-machine
Version:        3.5.1
Release:        1%{?dist}
Summary:        Travel through time in your tests.
License:        MIT
URL:            https://github.com/adamchainz/time-machine
Source0:        https://files.pythonhosted.org/packages/source/t/time_machine/time_machine-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-time-machine = %{version}-%{release}
# /oreon:deps
%package -n       python3-time-machine+cli
Summary:        Metapackage for python3-time-machine cli extras
Requires:       python3-time-machine = %{version}-%{release}
Provides:       python3dist(time-machine[cli]) = %{version}-%{release}

%description -n python3-time-machine+cli
Metapackage for python3-time-machine cli extras.

%package -n       python3-time-machine+dateutil
Summary:        Metapackage for python3-time-machine dateutil extras
Requires:       python3-time-machine = %{version}-%{release}
Requires:       python3dist(python-dateutil) >= 2.8.2
Provides:       python3dist(time-machine[dateutil]) = %{version}-%{release}

%description -n python3-time-machine+dateutil
Metapackage for python3-time-machine dateutil extras.

%description

%package -n     python3-time-machine
Summary:        Travel through time in your tests.
%description -n python3-time-machine

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir time_machine-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-time-machine usr/lib/python3*/site-packages/time_machine* usr/lib64/python3*/site-packages/time_machine* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/time_machine* usr/lib64/python3*/site-packages/time_machine* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-time-machine -f %{oreon_filedir}/python3-time-machine.list

%changelog

%autochangelog
