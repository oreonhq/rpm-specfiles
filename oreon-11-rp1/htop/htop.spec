# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a8b164386494cb85bb255a415a3f5f80afe7a0c4491da5d113b3a0f951087e65

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:           htop
Version:        3.5.3
Release:        1%{?dist}
Summary:        Interactive process viewer
License:        GPL-2.0-or-later
URL:            https://htop.dev/
Source0:        https://github.com/htop-dev/htop/releases/download/%{version}/htop-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  hwloc-devel
BuildRequires:  libcap-devel
BuildRequires:  libnl3-devel
BuildRequires:  libtool
BuildRequires:  lm_sensors-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  oreon-rpm-macros

%description
htop is an interactive text-mode process viewer for Linux, similar to
top(1).

%prep
%oreon_sha256

%autosetup -p1

%build
autoreconf -vfi

%configure \
    --enable-capabilities \
    --enable-delayacct \
    --enable-hwloc \
    --enable-sensors \
    --enable-unicode

%make_build

%install
%make_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/htop
%{_datadir}/pixmaps/htop.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/htop.1*

