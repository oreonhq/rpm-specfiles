# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 37d0fa3d0a16fddc3d88099e147e164ddb3055e8bc3424506ef41dd80f723a73
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sbom
Version: 0.3.1
Release: 1%{?dist}
Summary: Software bill of materials helpers
License: MIT
URL: https://pypi.org/project/python-sbom/
Source0: https://files.pythonhosted.org/packages/e7/c8/433fce09ca6d9580e71b1bcde4db4da5c1f77039536deca9d373f1b7886e/python_sbom-0.3.1.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-hatchling
BuildRequires: python3-hatch-vcs
BuildRequires: python3-hatch-fancy-pypi-readme
BuildRequires: python3-setuptools
BuildRequires: python3-packageurl
BuildRequires: python3-packaging
BuildRequires: python3-zipremove
Requires: python3
Requires: python3-installer
Requires: python3-packageurl
Requires: python3-packaging
Requires: python3-zipremove

%description
Software bill of materials helpers

%prep
%oreon_sha256
%autosetup -n python_sbom-0.3.1

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
cd %{_builddir}
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -c 'import python_sbom'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
