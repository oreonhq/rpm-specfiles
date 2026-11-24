# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ba561cf3c96305a47179fa5605856ad695c9238ea07f7093aebd9ba80c4e323b
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global adwlegacy_ver 46.2

%global tarball_version %(echo %{version} | tr '~' '.')

Name:           adwaita-icon-theme
Version:        51.0
Release:        1%{?dist}
Summary:        Adwaita icon theme

License:        LGPL-3.0-only OR CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/adwaita-icon-theme
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{tarball_version}.tar.xz
BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  meson
BuildRequires:  /usr/bin/gtk-update-icon-cache

%if 0%{?fedora} || (0%{?oreon} >= 11)
Requires:       %{name}-legacy >= %{adwlegacy_ver}
%endif
Requires:       adwaita-cursor-theme = %{version}-%{release}

%description
This package contains the Adwaita icon theme used by the GNOME desktop.

%package -n     adwaita-cursor-theme
Summary:        Adwaita cursor theme

%description -n adwaita-cursor-theme
The adwaita-cursor-theme package contains a modern set of cursors originally
designed for the GNOME desktop.

%package        devel
Summary:        Development files for %{name}
%if 0%{?fedora} || (0%{?oreon} >= 11)
Requires:       %{name}-legacy-devel >= %{adwlegacy_ver}
%endif
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains the pkgconfig file for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

touch $RPM_BUILD_ROOT%{_datadir}/icons/Adwaita/.icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/Adwaita
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/Adwaita
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :

%files
%license COPYING*
%dir %{_datadir}/icons/Adwaita/
%{_datadir}/icons/Adwaita/16x16/
%{_datadir}/icons/Adwaita/scalable/
%{_datadir}/icons/Adwaita/symbolic/
%{_datadir}/icons/Adwaita/index.theme
%ghost %{_datadir}/icons/Adwaita/.icon-theme.cache

%files -n adwaita-cursor-theme
%license COPYING*
%dir %{_datadir}/icons/Adwaita/
%{_datadir}/icons/Adwaita/cursors/

%files devel
%{_datadir}/pkgconfig/adwaita-icon-theme.pc

%changelog
%autochangelog
