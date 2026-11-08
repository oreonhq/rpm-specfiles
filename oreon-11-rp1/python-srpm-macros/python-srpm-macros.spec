# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6c690ae1b7b4c6f0036b759c3fdba8bcd42b1d7649409d8efa09f11f16528703
%global debug_package %{nil}

Name: python-srpm-macros
Version: 3.15
Release: 4%{?dist}
Summary: SRPM macros for Python packages
License: MIT
URL: https://www.python.org/
BuildArch: noarch
Source0: macros.python-srpm
Source1: compileall2.py
Source2: clamp_source_mtime.py
Source3: brp-python-bytecompile
Source4: brp-python-hardlink
Source5: brp-python-rpm-in-distinfo
Source6: brp-fix-pyc-reproducibility
Source7: python.lua
Requires: oreon-rpm-config
Provides: bundled(python3dist(compileall2)) = 0.8.0

BuildRequires: oreon-rpm-macros

%description
SRPM macros and the bytecompile scripts Python source packages use.

%prep
%oreon_sha256

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmconfigdir}/oreon
mkdir -p %{buildroot}%{_rpmluadir}/oreon/srpm
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.python-srpm
install -m 644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/oreon/compileall2.py
install -m 644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/oreon/clamp_source_mtime.py
install -m 755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/oreon/brp-python-bytecompile
install -m 755 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/oreon/brp-python-hardlink
install -m 755 %{SOURCE5} %{buildroot}%{_rpmconfigdir}/oreon/brp-python-rpm-in-distinfo
install -m 755 %{SOURCE6} %{buildroot}%{_rpmconfigdir}/oreon/brp-fix-pyc-reproducibility
install -m 644 %{SOURCE7} %{buildroot}%{_rpmluadir}/oreon/srpm/python.lua

%files
%{_rpmmacrodir}/macros.python-srpm
%{_rpmconfigdir}/oreon/compileall2.py
%{_rpmconfigdir}/oreon/clamp_source_mtime.py
%{_rpmconfigdir}/oreon/brp-python-bytecompile
%{_rpmconfigdir}/oreon/brp-python-hardlink
%{_rpmconfigdir}/oreon/brp-python-rpm-in-distinfo
%{_rpmconfigdir}/oreon/brp-fix-pyc-reproducibility
%{_rpmluadir}/oreon/srpm/python.lua
