# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b523afe23c4b5bb58261156564b7527a1f719bc9b9917f9c6bd3c763d823291c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: cosmic-sound-theme
Version: 1.11.0
Release: 1%{?dist}
Summary: COSMIC Sound Theme Source
License: CC-BY-SA-4.0
URL: https://github.com/pop-os/cosmic-sound-theme
Source0: https://github.com/pop-os/cosmic-sound-theme/archive/refs/tags/epoch-1.11.0.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
%endif

%description
COSMIC Sound Theme Source

%prep
%oreon_sha256
%autosetup -n cosmic-sound-theme-epoch-1.11.0 -p1

%build
%oreon_meson
%oreon_meson_build

%install
%oreon_meson_install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license LICENSE
