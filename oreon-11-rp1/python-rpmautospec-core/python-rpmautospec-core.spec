%global source0_hash bb2f0e8c2cc9b9f8129399fca81abe361423111913b114b366286711a4787597
Name:           python-rpmautospec-core
Version:        0.2.0
Release:        1%{?dist}
Summary:        Core functionality for rpmautospec
License:        MIT
URL:            https://github.com/fedora-infra/rpmautospec-core
Source0:        https://files.pythonhosted.org/packages/source/r/rpmautospec_core/rpmautospec_core-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rpmautospec-core = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rpmautospec-core
Summary:        Core functionality for rpmautospec
%description -n python3-rpmautospec-core

%prep
%global oreon_srcdir rpmautospec_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rpmautospec-core usr/lib/python3*/site-packages/rpmautospec_core* usr/lib64/python3*/site-packages/rpmautospec_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rpmautospec_core* usr/lib64/python3*/site-packages/rpmautospec_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rpmautospec-core -f %{oreon_filedir}/python3-rpmautospec-core.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.5-1
- Prepare for Oreon 11 (RP1)
