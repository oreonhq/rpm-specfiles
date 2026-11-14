# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b44276f2c276e909239a4f6c955aa667aaafeb78597923b1c60babc76db78e4c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sphinx_rtd_theme
Version: 3.1.0
Release: 1%{?dist}
Summary: Read the Docs theme for Sphinx
License: MIT
URL: https://pypi.org/project/sphinx-rtd-theme/
Source0: https://files.pythonhosted.org/packages/84/68/a1bfbf38c0f7bccc9b10bbf76b94606f64acb1552ae394f0b8285bfaea25/sphinx_rtd_theme-3.1.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-docutils
BuildRequires: python3-sphinxcontrib-jquery
Requires: python3
Requires: python3-sphinx
Requires: python3-docutils
Requires: python3-sphinxcontrib-jquery

%description
Read the Docs theme for Sphinx

%prep
%oreon_sha256
%autosetup -n sphinx_rtd_theme-3.1.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import sphinx_rtd_theme'

%files -f %{_builddir}/%{name}.files
