%global source0_hash 052c7fc3721d54c696e2dea019be67539d7b144e924f559f54beb3121831c364
Name:           python-installer
Version:        1.0.1
Release:        1%{?dist}
Summary:        A library for installing Python wheels.
License:        MIT
URL:            https://github.com/pypa/installer
Source0:        https://files.pythonhosted.org/packages/source/i/installer/installer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-installer = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-installer
Summary:        A library for installing Python wheels.
%description -n python3-installer

%prep
%global oreon_srcdir installer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-installer usr/lib/python3*/site-packages/installer* usr/lib64/python3*/site-packages/installer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/installer* usr/lib64/python3*/site-packages/installer* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-installer -f %{oreon_filedir}/python3-installer.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.7.0-14
- Prepare for Oreon 11 (RP1)
