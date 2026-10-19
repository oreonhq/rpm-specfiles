%global source0_hash 7979f7eaeac696cea51c25fe31e33a4bc06ec7952de0ecad593cfa8a7f38d783
Name:           python-gelidum
Version:        0.10.1
Release:        1%{?dist}
Summary:        Freeze your objects in python
License:        MIT
URL:            https://github.com/diegojromerolopez/gelidum
Source0:        https://files.pythonhosted.org/packages/source/g/gelidum/gelidum-%{version}.tar.gz
BuildArch:      noarch
Patch:          build-system.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gelidum = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-gelidum
Summary:        Freeze your objects in python
%description -n python3-gelidum

%prep
%global oreon_srcdir gelidum-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gelidum usr/lib/python3*/site-packages/gelidum* usr/lib64/python3*/site-packages/gelidum* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gelidum* usr/lib64/python3*/site-packages/gelidum* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gelidum -f %{oreon_filedir}/python3-gelidum.list

%changelog

%autochangelog
