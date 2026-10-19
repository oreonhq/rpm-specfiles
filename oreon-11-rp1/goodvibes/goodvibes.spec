%global source0_hash b8d0f606debd2357f643e5da7fe6ca39c89dd055944f159100434f992475ce13
Name:           goodvibes
Version:        0.8.4
Release:        1%{?dist}
Summary:        Lightweight Radio Player
License:        GPL-3.0-or-later
URL:            https://goodvibes.readthedocs.io/en/stable/index.html
Source0:        https://gitlab.com/%{name}/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Requires:       dconf
Requires:       gstreamer1-plugins-ugly-free
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libgedit-amtk-5)
BuildRequires:  pkgconfig(libsoup-3.0)
# /oreon:deps
%description
Goodvibes is an Internet radio player for GNU/Linux. It aims to be light,
simple, straightforward.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

export CFLAGS="%build_cflags -fPIE"
%meson -Dc_args="%build_cflags -fPIE"
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
        %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate \
        %{buildroot}/%{_datadir}/applications/*.desktop
%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
