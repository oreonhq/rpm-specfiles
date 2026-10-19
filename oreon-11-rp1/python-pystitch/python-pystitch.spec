%global source0_hash 4c067aeaf86e7489efdd8524b22beea089df66746b401a9efb34637ae1855e3b
Name:           python-pystitch
Version:        1.0.1
Release:        1%{?dist}
Summary:        Embroidery IO library
License:        MIT
URL:            https://github.com/inkstitch/pystitch.git
Source0:        https://files.pythonhosted.org/packages/source/p/pystitch/pystitch-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-pystitch = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pystitch
Summary:        Embroidery IO library
%description -n python3-pystitch

%prep
%global oreon_srcdir pystitch-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pystitch usr/lib/python3*/site-packages/pystitch* usr/lib64/python3*/site-packages/pystitch* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pystitch* usr/lib64/python3*/site-packages/pystitch* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pystitch -f %{oreon_filedir}/python3-pystitch.list

%changelog

%autochangelog
