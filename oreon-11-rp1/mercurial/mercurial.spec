# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 85839e0f39e6cb893a88932aa36ef661759f3c5c5de4551ad26bd9df53cb71a2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: mercurial
Version: 7.2.4
Release: 1%{?dist}
Summary: Fast scalable distributed SCM
License: GPL-2.0-or-later
URL: https://www.mercurial-scm.org/
Source0: https://www.mercurial-scm.org/release/mercurial-%{version}.tar.gz
Patch0: mercurial-tls13-setup.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-wheel
BuildRequires: rust
BuildRequires: cargo
BuildRequires: openssl-devel

%description
Mercurial source control.

%prep
%oreon_sha256
%autosetup -n mercurial-%{version} -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
export CARGO_HOME=%{_builddir}/cargo-home
mkdir -p "$CARGO_HOME"
python3 setup.py build_ext -i
python3 setup.py bdist_wheel --dist-dir dist

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist
sed -i '\|/bin/hg$|d' %{_builddir}/%{name}.files

%check
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/hg version

%files -f %{_builddir}/%{name}.files
%{_bindir}/hg

%changelog
%autochangelog
