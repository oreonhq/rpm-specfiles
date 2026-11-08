# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 155752ba6796aa294cde87c2bf0e771a5891eeeacb131345be0e080a3ec0ceea

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Summary: Localizations for Gnulib
Name:    gnulib-l10n
Version:        20241231
Release:        1%{?dist}
License: LGPL-2.1-or-later

Url:     https://www.gnu.org/software/gnulib
Source0:        https://mirror.cs.odu.edu/gnu/gnulib/gnulib-l10n-%{version}.tar.gz
Source1:        gnulib-l10n-20241231.tar.gz.sig

# From https://www.haible.de/bruno/gpgkeys.html
Source2: gnulib-l10n-keyring.gpg

# Machine objects (*.mo) are architecture independent.
BuildArch: noarch

BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: make

# For gpg verification of source tarball
BuildRequires: gnupg2
BuildRequires:  oreon-rpm-macros

%description
The localizations for the GNU portability library.

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup

%build
%configure
%make_build

%install
%make_install
%find_lang gnulib

%files -f gnulib.lang
%doc ABOUT-NLS README
%license COPYING

