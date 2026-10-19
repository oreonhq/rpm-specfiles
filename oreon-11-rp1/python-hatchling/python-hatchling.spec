%global source0_hash c4468f73144c054d2aab4ef0f0378c43b9878bf07f8ffd6b79690e970d375f07
Name:           python-hatchling
Version:        1.32.4
Release:        1%{?dist}
Summary:        Modern, extensible Python build backend
License:        MIT
URL:            https://hatch.pypa.io/latest/
Source0:        https://files.pythonhosted.org/packages/source/h/hatchling/hatchling-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-hatchling = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-hatchling
Summary:        Modern, extensible Python build backend
# oreon:reqs
Requires:       python3dist(configparser) < 5
Requires:       python3dist(requests) >= 2.6.0
# /oreon:reqs
%description -n python3-hatchling

%prep
%global oreon_srcdir hatchling-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hatchling usr/lib/python3*/site-packages/hatchling* usr/lib64/python3*/site-packages/hatchling* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hatchling* usr/lib64/python3*/site-packages/hatchling* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-hatchling -f %{oreon_filedir}/python3-hatchling.list

%changelog

%autochangelog
