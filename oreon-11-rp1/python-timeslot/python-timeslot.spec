%global source0_hash a2ac998657e3f3b9ca928757b4906add2c05390c5fc14ed792bb9028d08547b1
Name:           python-timeslot
Version:        0.1.2
Release:        1%{?dist}
Summary:        Data type for representing time slots with a start and end.
License:        MIT
URL:            https://github.com/ErikBjare/timeslot
Source0:        https://files.pythonhosted.org/packages/source/t/timeslot/timeslot-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-timeslot = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-timeslot
Summary:        Data type for representing time slots with a start and end.
%description -n python3-timeslot

%prep
%global oreon_srcdir timeslot-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-timeslot usr/lib/python3*/site-packages/timeslot* usr/lib64/python3*/site-packages/timeslot* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/timeslot* usr/lib64/python3*/site-packages/timeslot* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-timeslot -f %{oreon_filedir}/python3-timeslot.list

%changelog

%autochangelog
