%global source0_hash b9e949f0ec7101094c4b0f096fad80d0aa90818854fa69a9d750fa4fd1e7b4ba
Name:           python-port-for
Version:        1.1.0
Release:        1%{?dist}
Summary:        Utility that helps with local TCP ports management. It can find an unused TCP localhost port and remember the association.
License:        MIT
URL:            https://github.com/fizyk/port-for/
Source0:        https://files.pythonhosted.org/packages/source/p/port_for/port_for-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.13
BuildRequires:  python3dist(uv-build) >= 0.12
Requires:       python3-port-for = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-port-for
Summary:        Utility that helps with local TCP ports management. It can find an unused TCP localhost port and remember the association.
%description -n python3-port-for

%prep
%global oreon_srcdir port_for-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-port-for usr/lib/python3*/site-packages/port_for* usr/lib64/python3*/site-packages/port_for* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/port_for* usr/lib64/python3*/site-packages/port_for* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-port-for -f %{oreon_filedir}/python3-port-for.list

%changelog

%autochangelog
