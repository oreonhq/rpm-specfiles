# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9c58ed3dff90d51f43414ce37009ad1d5b0f08ffc9fc216998a06380f01c0045
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-hatch-fancy-pypi-readme
Version: 25.1.0
Release: 1%{?dist}
Summary: Fancy PyPI READMEs with Hatch
License: MIT
URL: https://pypi.org/project/hatch-fancy-pypi-readme/
Source0: https://files.pythonhosted.org/packages/f3/0f/aed57c301f339936eb91cb4d8c1e5088a101081854bd3ec18a889df32365/hatch_fancy_pypi_readme-25.1.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-hatchling
Requires: python3
Requires: python3-hatchling

%description
Fancy PyPI READMEs with Hatch

%prep
%oreon_sha256
%autosetup -n hatch_fancy_pypi_readme-25.1.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
cd %{_builddir}
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -c 'import hatch_fancy_pypi_readme'

%files -f %{_builddir}/%{name}.files
