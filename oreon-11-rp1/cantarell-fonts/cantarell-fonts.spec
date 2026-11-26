# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f9463a0659c63e57e381fdd753cf1929225395c5b49135989424761830530411
%global fontdir %{_fontbasedir}/cantarell

Name: cantarell-fonts
Version: 0.303.1
Release: 1%{?dist}
Summary: Default typeface of GNOME
License: OFL-1.1
URL: https://wiki.gnome.org/Projects/CantarellFonts
Source0: https://download.gnome.org/sources/cantarell-fonts/0.303/cantarell-fonts-%{version}.tar.xz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: fonts-srpm-macros
BuildRequires: meson
BuildRequires: pkgconfig
Requires: fontconfig

%description
Cantarell is the default typeface of GNOME. This package provides the
prebuilt variable OpenType font.

%prep
%oreon_sha256
%autosetup

%build
%meson \
  -Dfontsdir=%{fontdir} \
  -Duseprebuilt=true \
  -Dbuildappstream=false
%meson_build

%install
%meson_install

%check
test -f %{buildroot}%{fontdir}/Cantarell-VF.otf

%files
%license COPYING
%doc NEWS README.md
%dir %{fontdir}
%{fontdir}/*.otf

%changelog
%autochangelog
