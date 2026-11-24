# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 267ac1ee1593c67884f3c9cb6566f72a92ca28353050fc9d087433c28c74a889
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pypi_name pyqt_builder

Name:           PyQt-builder
Version:        1.20.0
Release:        %{autorelease}
Summary:        The PEP 517 compliant PyQt build system

License:        BSD-2-Clause
URL:            https://www.riverbankcomputing.com/software/pyqt/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that
extend PyQt. It extends the sip build system and uses Qt's qmake to perform the
actual compilation and installation of extension modules.Projects that use
PyQt- builder provide an appropriate pyproject.toml file and an optional
project.py.

%prep
%oreon_sha256
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyqtbuild
rm -rf %{buildroot}/%{python3_sitelib}/pyqtbuild/bundle/dlls
sed -r -i '/\/pyqtbuild\/bundle\/dlls/d' %{pyproject_files}

%check
%py3_check_import pyqtbuild

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/pyqt-bundle
%{_bindir}/pyqt-qt-wheel

%changelog
%autochangelog
