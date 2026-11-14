# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b75b420da9b0be9a3d99b1bee6ed87957b56ab54583ac1a97fbd0dc98ddddb25
%global xdgmime_commit a3d6162494270676fdfeb923cb0900517c4bd72f
%global xdgmime_hash aaaf788f5f91d4f02b065a6477e2132a7ffea20ca92026e0e0b01c73640517c4

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           shared-mime-info
Version:        2.5.1
Release:        1%{?dist}
Summary:        Shared MIME information database
License:        GPL-2.0-or-later
URL:            https://freedesktop.org/wiki/Software/shared-mime-info/
Source0:        https://gitlab.freedesktop.org/xdg/shared-mime-info/-/archive/%{version}/shared-mime-info-%{version}.tar.bz2
Source1:        https://gitlab.freedesktop.org/xdg/xdgmime/-/archive/%{xdgmime_commit}/xdgmime-%{xdgmime_commit}.tar.bz2

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libxml2
BuildRequires:  pkgconfig(glib-2.0) >= 2.6.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4
BuildRequires:  /usr/bin/xmllint
BuildRequires:  xmlto
BuildRequires:  docbook-style-xsl

Requires(post):   coreutils
Requires(postun): coreutils

%description
This is the freedesktop.org shared MIME type database. Many programs and
desktops use this database.

%prep
%oreon_sha256
echo '%{xdgmime_hash}  %{SOURCE1}' | sha256sum -c -
tar -xjf %{SOURCE1}
%autosetup -n shared-mime-info-%{version}
rm -rf subprojects/xdgmime
mv ../xdgmime-%{xdgmime_commit} subprojects/xdgmime

%build
%meson -Dbuild-tests=true -Dbuild-spec=true
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%post
/usr/bin/update-mime-database %{_datadir}/mime >/dev/null 2>&1 || :

%postun
if [ $1 -eq 0 ]; then
  /usr/bin/update-mime-database %{_datadir}/mime >/dev/null 2>&1 || :
fi

%files -f %{name}.lang
%license COPYING
%doc README.md NEWS
%{_bindir}/update-mime-database
%{_datadir}/mime/
%{_datadir}/pkgconfig/shared-mime-info.pc
%{_mandir}/man1/update-mime-database.1*

%changelog
%autochangelog
