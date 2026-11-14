# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4401d4e231d842c2de8242395a74a395ca468cd96f5f610d822df33594898a70

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           desktop-file-utils
Version:        0.28
Release:        1%{?dist}
Summary:        Utilities for manipulating .desktop files
License:        GPL-2.0-or-later
URL:            https://www.freedesktop.org/software/desktop-file-utils
Source0:        https://www.freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.xz
Source1:        desktop-entry-mode-init.el
Patch0:         0001-validate-Add-Phosh-to-list-of-valid-OnlyShowIn-envir.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  meson

Provides:       %{_bindir}/update-desktop-database

%description
.desktop files are used to describe an application for inclusion in
GNOME or KDE menus.  This package contains desktop-file-validate which
checks whether a .desktop file complies with the specification at
http://www.freedesktop.org/standards/, and desktop-file-install
which installs a desktop file to the standard directory, optionally
fixing it up in the process.

%prep
%oreon_sha256
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/desktop-file-utils
mv %{buildroot}%{_datadir}/emacs/site-lisp/*.el* %{buildroot}%{_datadir}/emacs/site-lisp/desktop-file-utils/
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/emacs/site-lisp/site-start.d/desktop-entry-mode-init.el

%check
%meson_test
%{buildroot}%{_bindir}/desktop-file-validate --help >/dev/null
%{buildroot}%{_bindir}/update-desktop-database --help >/dev/null

%transfiletriggerin -- %{_datadir}/applications
update-desktop-database &> /dev/null || :

%transfiletriggerpostun -- %{_datadir}/applications
update-desktop-database &> /dev/null || :

%files
%doc AUTHORS README NEWS
%license COPYING
%{_bindir}/desktop-file-edit
%{_bindir}/desktop-file-install
%{_bindir}/desktop-file-validate
%{_bindir}/update-desktop-database
%{_mandir}/man1/desktop-file-install.1*
%{_mandir}/man1/desktop-file-validate.1*
%{_mandir}/man1/update-desktop-database.1*
%{_mandir}/man1/desktop-file-edit.1*
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%dir %{_datadir}/emacs/site-lisp/site-start.d
%{_datadir}/emacs/site-lisp/site-start.d/desktop-entry-mode-init.el
%{_datadir}/emacs/site-lisp/desktop-file-utils/

%changelog
%autochangelog
