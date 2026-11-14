# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: MIT

%global source0_hash 52c88628b0e5671592dc2306613fb5f6f3615fd24def059b9894f143b7f9a139

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-meson-python
Version: 0.22.1
Release: 1%{?dist}
Summary: Meson Python build backend
License: MIT
URL: https://github.com/mesonbuild/meson-python
Source0: https://files.pythonhosted.org/packages/b4/40/343ae23722d5d66a7b94b752d1b194202640995296379333b274b1860871/meson_python-%{version}.tar.gz
BuildArch: noarch
Provides: python3dist(meson-python) = %{version}

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-packaging
BuildRequires: python3-pyproject-metadata
BuildRequires: meson
Requires: python3
Requires: python3-packaging
Requires: meson

%description
meson-python is a Python build backend using Meson.

%prep
%oreon_sha256
%autosetup -n meson_python-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import mesonpy'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
