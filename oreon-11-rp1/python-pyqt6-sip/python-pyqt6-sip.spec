# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2cd55f575cde208c398d6cfdecc5a13394ed2afb54226210c50e3a6df7c3a997
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pkg_name pyqt6-sip
%global pypi_name pyqt6_sip
%global _sip_api_major 13
%global _sip_api_minor 13
%global _sip_api %{_sip_api_major}.%{_sip_api_minor}

Name:           python-%{pkg_name}
Version:        13.13.0
Release:        %{autorelease}
Summary:        The sip module support for PyQt6

License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.riverbankcomputing.com/software/sip/
Source0:        %{pypi_source}

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  python3-devel

%global _description %{expand:
The sip extension module provides support for the PyQt6 package.
}

%description %_description

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}
Provides: python3-pyqt6-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python3-pyqt6-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}

%description -n python3-%{pkg_name} %_description
%prep
%oreon_sha256
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l PyQt6

%check
%pyproject_check_import

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README

%changelog
%autochangelog
