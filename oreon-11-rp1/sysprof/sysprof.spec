# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ff04139637785c841948862087a4323b981680d942296409321b574fcb282878

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0

Name: sysprof
Version: 49.0
Release: 2%{?dist}
%oreon_bootstrap
%bcond tests %{without bootstrap}
Summary: Static library for capturing profiling data
License: GPL-3.0-or-later AND BSD-2-Clause
URL: https://gitlab.gnome.org/GNOME/sysprof
Source0: https://download.gnome.org/sources/sysprof/49/sysprof-%{version}.tar.xz
Patch0: sysprof-capture-tests.patch

BuildRequires: oreon-rpm-macros >= 1-14
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconf
%if %{with tests}
BuildRequires: glib2-devel
%endif

%description
libsysprof-capture is the static library other programs link when they
record sysprof capture data.

%prep
%oreon_sha256
%autosetup -p1

%build
%meson \
    -Dgtk=false \
    -Dsysprofd=none \
    -Dhelp=false \
    -Dlibsysprof=false \
    -Dtools=false \
    -Dexamples=false \
%if %{with tests}
    -Dtests=true \
%else
    -Dtests=false \
%endif
    -Dinstall-static=true \
    -Dpolkit-agent=disabled \
    -Ddebuginfod=disabled
%meson_build

%install
%meson_install

%check
%if %{with tests}
%meson_test
%endif

%files
%license COPYING
%license src/libsysprof-capture/COPYING
%{_libdir}/libsysprof-capture-4.a
%{_libdir}/pkgconfig/sysprof-capture-4.pc
%{_includedir}/sysprof-6/

%changelog
%autochangelog
