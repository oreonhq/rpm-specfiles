%global source0_hash 97d01f6144bbe3abe1b2155cb2b42dab4ec33e09f4f7f7df7569f35d9a29aaf7
Name:           python-futurist
Version:        3.5.0
Release:        1%{?dist}
Summary:        Useful additions to futures, from the future.
License:        Apache-2.0
URL:            https://docs.openstack.org/futurist
Source0:        https://files.pythonhosted.org/packages/source/f/futurist/futurist-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-futurist = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-futurist
Summary:        Useful additions to futures, from the future.
%description -n python3-futurist

%prep
%global oreon_srcdir futurist-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-futurist usr/lib/python3*/site-packages/futurist* usr/lib64/python3*/site-packages/futurist* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/futurist* usr/lib64/python3*/site-packages/futurist* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-futurist -f %{oreon_filedir}/python3-futurist.list

%changelog

%autochangelog
