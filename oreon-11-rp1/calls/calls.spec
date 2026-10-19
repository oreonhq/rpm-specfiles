%global source1_hash fb1c6b3fcd66fdb267781ee65980bdf8d5d3ef0dca3361b07bdc6747225961d0
%global source0_hash 4a57cb65b6064c13e80e714b39dcf1dbdd90a7c6a6649f8544bc25d02b55734a
%global libcall_ui_commit f66056ace818ff19b507335634dd67138a92c77f
Name:       calls
Version:    50.0
Release:        1%{?dist}
Summary:        A phone dialer and call handler
License:    GPL-3.0-or-later AND LGPL-2.1-or-later
URL:        https://gitlab.gnome.org/GNOME/calls
Source0:        https://gitlab.gnome.org/GNOME/calls/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:    https://gitlab.gnome.org/World/Phosh/libcall-ui/-/archive/%{libcall_ui_commit}/libcall-ui-%{libcall_ui_commit}.tar.gz
Patch0:     807.patch
ExcludeArch:    %{ix86}
Requires:  hicolor-icon-theme
Recommends: feedbackd
Provides: gnome-calls = %{version}-%{release}
Provides: gnome-calls%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/xauth
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  cmake
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-plugins-good-gtk
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcallaudio-0.1)
BuildRequires:  pkgconfig(libebook-contacts-1.2)
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  python3-docutils
BuildRequires:  sofia-sip-glib-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A phone dialer and call handler.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -a1 -p1 -n %{name}-v%{version}

mv libcall-ui-%{libcall_ui_commit}/* subprojects/libcall-ui/

%conf
%meson

%build

%meson_build
%install
%meson_install
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/call-ui.mo
rm -rf %{buildroot}%{_libdir}/calls/plugins/provider/ofono/
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Calls.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Calls.desktop
LC_ALL=C.UTF-8 xvfb-run sh <<'SH'
%meson_test plugins
SH
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
