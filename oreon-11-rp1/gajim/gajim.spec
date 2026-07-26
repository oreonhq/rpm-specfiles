%global source0_hash b7ccb359f76c63ca57c9eec39f984c1346ce1e07fe333bb2558de1c1e5dcd318

%global appid org.gajim.Gajim

Name:     gajim
Version:  1.7.3
Release:  14%{?dist}
Summary:  Jabber client written in PyGTK
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:  GPL-3.0-only
URL:      https://gajim.org/
Source0:  https://gajim.org/downloads/1.7/gajim-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

## Hard requirements
Requires:    python3-gobject >= 3.42
Requires:    cairo >= 1.16
Requires:    python3-pillow
Requires:    gtk3 >= 3.24.30
Requires:    glib2 >= 2.60
Requires:    gtksourceview4
Requires:    pango >= 1.50
Requires:    sqlite-libs >= 3.33
Requires:    hicolor-icon-theme
## Optional, but not too big and not worth exploding the test matrix for
# For gajim-remote, desktop notifications, logind, NetworkManager, ...
Requires:    python3-dbus
## Optional, roughly in the order listed in upstream README.md
# OpenPGP message encryption - Encrypting chat messages with OpenPGP keys
Recommends:  python3-gnupg
# Spell checker - Spellchecking of composed messages
Recommends:  gspell
# Password storage
Recommends:  libsecret
# UPnP-IGD - Ability to request your router to forward port for file transfer
Recommends:  gupnp-igd
# Sharing location
Recommends:  geoclue2-libs
# Sound
Recommends:  gsound
# Audio/Video - Ability to start audio and video chat
Recommends:  farstream02
Recommends:  gstreamer1
Recommends:  gstreamer1-plugins-base
Recommends:  gstreamer1-plugins-good-gtk
## Plugins
# OMEMO
Recommends:  python3-axolotl
Recommends:  python3-protobuf
Recommends:  python3-qrcode

%description
Gajim is a Jabber client written in PyGTK. The goal of Gajim's developers is
to provide a full featured and easy to use xmpp client for the GTK+ users.
Gajim does not require GNOME to run, even though it exists with it nicely.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
./pep517build/build_metadata.py --output-dir dist/metadata

%install
%pyproject_install
./pep517build/install_metadata.py dist/metadata --prefix %{buildroot}/%{_prefix}
%pyproject_save_files gajim

# RHEL <= 9 doesn't support .desktop files with version 1.5,
# see: https://bugzilla.redhat.com/show_bug.cgi?id=2107278
%if 0%{?rhel} && 0%{?rhel} <= 9
sed -e 's/^SingleMainWindow=/X-GNOME-SingleWindow=/' \
    -i %{buildroot}/%{_datadir}/applications/%{appid}.desktop
%endif

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{appid}.appdata.xml

%find_lang %{name}

%files -f %{pyproject_files} -f %{name}.lang
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/%{name}-remote.1*
%{_bindir}/%{name}
%{_bindir}/%{name}-remote
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{appid}-symbolic.svg

%changelog
%autochangelog
