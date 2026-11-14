# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ff56af8bfd0b50ebf10c81a07b8a5739787eb015d26b4ba162b6983d6e17c7c3
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-breathe
Version: 5.1.0
Release: 1%{?dist}
Summary: Sphinx Doxygen renderer
License: BSD License
URL: https://pypi.org/project/breathe/
Source0: https://files.pythonhosted.org/packages/7d/7f/c64ce129d35f05bac6b3d044ee2d3aea24b0c819f2f57cd34020b74d5efc/breathe-5.1.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
BuildRequires: python3-sphinx
BuildRequires: doxygen
Requires: python3
Requires: python3-sphinx
Requires: doxygen

%description
Sphinx Doxygen renderer

%prep
%oreon_sha256
%autosetup -n breathe-5.1.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import breathe'

%files -f %{_builddir}/%{name}.files
