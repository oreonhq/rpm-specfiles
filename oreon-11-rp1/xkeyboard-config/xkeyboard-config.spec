# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b77041324f0109f77161ee43743fe04baa485866af8460d31e476ad3f7648fd5

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           xkeyboard-config
Version:        2.48
Release:        1%{?dist}
Summary:        X Keyboard Extension configuration data
License:        MIT
URL:            https://www.freedesktop.org/wiki/Software/XKeyboardConfig/
Source0:        https://www.x.org/releases/individual/data/xkeyboard-config/xkeyboard-config-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  libxslt
BuildRequires:  python3

Provides:       xkeyboard-config-devel = %{version}-%{release}
Provides:       pkgconfig(xkeyboard-config) = %{version}
Provides:       pkgconfig(xkeyboard-config-2) = %{version}

%description
This package contains X Keyboard Extension (XKB) configuration data
including keymaps, rules, and symbols for many keyboards and layouts.

%prep
%oreon_sha256
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-man --all-name

%check
%meson_test

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_datadir}/X11/xkb/
%{_datadir}/xkeyboard-config-2/
%{_datadir}/pkgconfig/xkeyboard-config.pc
%{_datadir}/pkgconfig/xkeyboard-config-2.pc
%{_mandir}/man7/xkeyboard-config.7*
%{_mandir}/man7/xkeyboard-config-2.7*

%changelog
%autochangelog
