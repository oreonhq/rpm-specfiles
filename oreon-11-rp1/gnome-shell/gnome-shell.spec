%global source0_hash 2179bab13af353427065096af8bf3d30da7b86e0c516e5ba86a14998af9575f6
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
%global portal_helper 1
Name:           gnome-shell
Version:        51.0
Release:        1%{?dist}
Summary:        Window management and application launching for GNOME
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/GnomeShell
Source0:        https://download.gnome.org/sources/%{name}/5%{portal_helper}/%{name}-%{version}.tar.xz
Patch: gnome-shell-favourite-apps-firefox.patch
%define eds_version 3.45.1
%define gnome_desktop_version 44.0-7
%define glib2_version 2.86.0
%define gjs_version 1.85.90
%define gtk4_version 4.0.0
%define adwaita_version 1.5.0
%define mutter_version 50~alpha
%define polkit_version 0.100
%define gsettings_desktop_schemas_version 50~alpha
%define ibus_version 1.5.2
%define gnome_bluetooth_version 1:42.3
%define gstreamer_version 1.4.5
%define pipewire_version 0.3.49
%define gnome_settings_daemon_version 3.37.1
%ifnarch s390 s390x ppc ppc64 ppc64p7
%endif
Conflicts: %{name} < 48~rc-5
%ifnarch s390 s390x
Recommends:     gnome-bluetooth%{?_isa} >= %{gnome_bluetooth_version}
%endif
Requires:       %{name}-common = %{version}-%{release}
Requires:       gcr%{?_isa}
Requires:       gjs%{?_isa} >= %{gjs_version}
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       libadwaita%{_isa} >= %{adwaita_version}
Requires:       libnma-gtk4%{?_isa}
Requires:       librsvg2%{?_isa}
Requires:       mutter%{?_isa} >= %{mutter_version}
Requires:       upower%{?_isa}
Requires:       polkit%{?_isa} >= %{polkit_version}
Requires:       gnome-desktop4%{?_isa} >= %{gnome_desktop_version}
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires:       gnome-settings-daemon%{?_isa} >= %{gnome_settings_daemon_version}
Requires:       gstreamer1%{?_isa} >= %{gstreamer_version}
Requires:       gstreamer1-plugins-good%{?_isa}
Requires:       pipewire-gstreamer%{?_isa}
Requires:       xdg-user-dirs-gtk
Requires:       at-spi2-atk%{?_isa}
Recommends:     ibus%{?_isa} >= %{ibus_version}
Requires:       ibus-libs%{?_isa} >= %{ibus_version}
Requires:       tecla
Requires:       accountsservice-libs%{?_isa}
Requires:       gdm-libs%{?_isa}
Requires:       gnome-control-center
Requires:       python3%{_isa}
Requires:       switcheroo-control
Requires:       geoclue2-libs%{?_isa}
Requires:       libgweather4%{?_isa}
Requires:  gettext
Recommends:     bolt%{?_isa}
Requires:       xdg-desktop-portal-gtk >= 1.8.0
Requires:       xdg-desktop-portal-gnome
Recommends:     gnome-tour
Requires:     webkitgtk6.0%{?_isa}
Provides:       gnome-shell(api) = %{major_version}
Provides:       desktop-notification-daemon = %{version}-%{release}
Provides:       PolicyKit-authentication-agent = %{version}-%{release}
Provides:       bundled(gvc)
Provides:       bundled(libcroco) = 0.6.13
Conflicts:      gnome-shell-extension-background-logo < 3.34.0
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gnome-bluetooth-libs-devel
BuildRequires:  gtk-doc
BuildRequires:  libXfixes-devel
BuildRequires:  librsvg2-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  mutter-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gnome-autoar-0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  python3
BuildRequires:  python3-docutils
# /oreon:deps
%description
GNOME Shell provides core user interface functions for the GNOME 3 desktop,
like switching to windows and launching applications. GNOME Shell takes
advantage of the capabilities of modern graphics hardware and introduces
innovative user interface concepts to provide a visually attractive and
easy to use experience.

%package common
Summary: Common files used by %{name}
Conflicts: %{name} < 48~rc-5
BuildArch: noarch
%description common
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -S git -n %{name}-%{tarball_version}

%build

%meson \
  -Dextensions_app=false \
  -Dportal_helper=true \
  %{nil}
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
mkdir -p %{buildroot}%{_datadir}/gnome-shell/search-providers
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Shell.Extensions.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Shell.PortalHelper.desktop
%files -f %{oreon_filedir}/main.list
%files -n gnome-shell-common -f %{oreon_filedir}/gnome-shell-common.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
