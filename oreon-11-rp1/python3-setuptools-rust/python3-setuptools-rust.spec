# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f2afcf4baeee689910ce49cfa8aad4e08cce72f417449bcc32891b8664fdc726
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-setuptools-rust
Version: 1.13.0
Release: 1%{?dist}
Summary: Setuptools plugin for Rust extensions
License: MIT
URL: https://pypi.org/project/setuptools-rust/
Source0: https://files.pythonhosted.org/packages/68/ba/b31781d61bf9ee3c232a1d1160db11c11cdeae1d44e06c90723b25a8279f/setuptools_rust-1.13.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-semantic-version
Requires: python3
Requires: python3-setuptools
Requires: python3-semantic-version

%description
Setuptools plugin for Rust extensions.

%prep
%oreon_sha256
%autosetup -n setuptools_rust-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import setuptools_rust'

%files -f %{_builddir}/%{name}.files
