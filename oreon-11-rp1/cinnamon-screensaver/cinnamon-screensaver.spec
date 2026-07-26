%global source0_hash d873cc22eb50db8b9339b546b9133945eee3a1458682136cb475a49252568fad

Summary: Cinnamon Screensaver
Name:    cinnamon-screensaver
Version: 6.6.1
Release: 4%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch: %{ix86}

BuildRequires: desktop-file-utils
BuildRequires: meson
BuildRequires: gcc
BuildRequires: intltool
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gdk-x11-3.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(libxdo)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(pam)
BuildRequires: python3-packaging

Recommends: caribou%{?_isa}
Requires: cinnamon-desktop%{?_isa} >= 6.6.0
Requires: cinnamon-translations >= 6.6.0
Requires: accountsservice-libs%{?_isa}
Requires: libgnomekbd%{?_isa}
Requires: python3-gobject%{?_isa}
Requires: python3-setproctitle%{?_isa}
Requires: python3-xapp
Requires: python3-xapps-overrides%{?_isa}
Requires: xapps%{?_isa}
Requires: xprop

# since we use it, and pam spams the log if a module is missing
Requires: gnome-keyring-pam%{?_isa}

%description
cinnamon-screensaver is a screen saver and locker.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install                                     \
  --delete-original                                      \
  --remove-only-show-in=Xfce                             \
  --dir %{buildroot}%{_datadir}/applications             \
  %{buildroot}%{_datadir}/applications/org.cinnamon.ScreenSaver.desktop

# Fix rpmlint errors
for file in %{buildroot}%{_datadir}/cinnamon-screensaver/{dbusdepot,util,widgets}/*.py; do
chmod a+x $file
done
for file in %{buildroot}%{_datadir}/cinnamon-screensaver/*.py; do
chmod a+x $file
done
chmod a-x %{buildroot}%{_datadir}/cinnamon-screensaver/{dbusdepot,util,widgets}/__init__.py
chmod a-x %{buildroot}%{_datadir}/cinnamon-screensaver/{__init__,config}.py
chmod a+x %{buildroot}%{_datadir}/cinnamon-screensaver/pamhelper/authClient.py

# Delete development files
rm %{buildroot}%{_datadir}/gir-1.0/CScreensaver-1.0.gir

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README.md
%license COPYING COPYING.LIB
%config(noreplace) %{_sysconfdir}/pam.d/cinnamon-screensaver
%{_bindir}/cinnamon-screensaver*
%{_bindir}/cinnamon-unlock-desktop
%{_datadir}/applications/org.cinnamon.ScreenSaver.desktop
%{_datadir}/cinnamon-screensaver/
%{_datadir}/dbus-1/services/org.cinnamon.ScreenSaver.service
%{_datadir}/icons/hicolor/scalable/*/*
%{_libexecdir}/cinnamon-screensaver/cinnamon-screensaver-pam-helper
%{_libexecdir}/cinnamon-screensaver/cs-backup-locker
%{_libexecdir}/cinnamon-screensaver/libcscreensaver.so
%{_libexecdir}/cinnamon-screensaver/girepository-1.0/CScreensaver-1.0.typelib

%changelog
%autochangelog
