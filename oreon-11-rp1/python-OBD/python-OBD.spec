%global source0_hash 27b8f043376ca700edb98bf5216e2912295ecde0e735b260999f2d9ddf342522
Name:           python-obd
Version:        0.7.3
Release:        1%{?dist}
Summary:        Serial module for handling live sensor data from a vehicle_s OBD-II port
License:        GPL-2.0-only
URL:            https://github.com/brendan-w/python-OBD
Source0:        https://files.pythonhosted.org/packages/source/o/obd/obd-%{version}.tar.gz
BuildArch:      noarch
Patch0:        %{name}-dep-ver.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-obd = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-obd
Summary:        Serial module for handling live sensor data from a vehicle_s OBD-II port
# oreon:reqs
Requires:       python3dist(pint) == 0.24.*
Requires:       python3dist(pyserial) == 3.*
# /oreon:reqs
%description -n python3-obd

%prep
%global oreon_srcdir obd-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-obd usr/lib/python3*/site-packages/obd* usr/lib64/python3*/site-packages/obd* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/obd* usr/lib64/python3*/site-packages/obd* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-obd -f %{oreon_filedir}/python3-obd.list

%changelog

%autochangelog
