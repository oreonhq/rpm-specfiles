%global source0_hash b0f55d99498e791362a0f918f51d7f1b52c9f00ae38888470545729d6195ac78
Name:           python-envisage
Version:        8.0.1
Release:        1%{?dist}
Summary:        Extensible application framework
License:        BSD-3-Clause
URL:            https://github.com/enthought/envisage
Source0:        https://files.pythonhosted.org/packages/source/e/envisage/envisage-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.13
BuildRequires:  python3dist(uv-build) >= 0.12.2
Requires:       python3-envisage = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-envisage
Summary:        Extensible application framework
# oreon:reqs
Requires:       python3dist(apptools[preferences]) >= 5.3
Requires:       python3dist(traits) >= 6.2
# /oreon:reqs
%description -n python3-envisage

%prep
%global oreon_srcdir envisage-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-envisage usr/lib/python3*/site-packages/envisage* usr/lib64/python3*/site-packages/envisage* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/envisage* usr/lib64/python3*/site-packages/envisage* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-envisage -f %{oreon_filedir}/python3-envisage.list

%changelog

%autochangelog
