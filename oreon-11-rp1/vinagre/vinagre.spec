%global source0_hash cd1cdbacca25c8d1debf847455155ee798c3e67a20903df8b228d4ece5505e82

%global _legacy_common_support 1
# old vala-generated code triggers -Werror=incompatible-pointer-type,
# but the code will not regenerate either due to changes in vala
%global build_type_safety_c 2

%ifarch %{ix86} x86_64
%define with_spice 1
%endif

Name:           vinagre
Version:        3.22.0
Release:        35%{?dist}
Summary:        VNC client for GNOME

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Vinagre
#VCS: git:git://git.gnome.org/vinagre
Source0:        https://download.gnome.org/sources/%{name}/3.22/%{name}-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/vinagre/merge_requests/3
Patch0:         fix-build-with-recent-freerdp-versions.patch

# Let the user cancel the rdp auth dialog instead of looping forever
# https://bugzilla.gnome.org/show_bug.cgi?id=780713
Patch1:         %{name}-rdp-let-cancel-auth-dialog.patch

# https://gitlab.gnome.org/GNOME/vinagre/merge_requests/7
Patch2:         fix-appstream-data.patch
Patch3: vinagre-c99.patch

%if 0%{?with_spice}
BuildRequires:  pkgconfig(spice-client-gtk-3.0)
%endif
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(avahi-ui-gtk3)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-vnc-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  desktop-file-utils
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  vala-devel
# For Patch0 gnome-autogen.sh
BuildRequires:  gnome-common
BuildRequires:  libappstream-glib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

# for /usr/share/dbus-1/services
Requires: dbus
Requires: telepathy-filesystem

# for file triggers
Requires: glib2 >= 2.45.4-2
Requires: desktop-file-utils >= 0.22-6
Requires: shared-mime-info >= 1.4-7

%description
Vinagre is a VNC client for the GNOME desktop.

With Vinagre you can have several connections open simultaneously, bookmark
your servers thanks to the Favorites support, store the passwords in the
GNOME keyring, and browse the network to look for VNC servers.

Apart from the VNC protocol, vinagre supports Spice and RDP.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
# copied from autogen.sh, needed for Patch0; drop when that is merged
ACLOCAL_FLAGS="$ACLOCAL_FLAGS" USE_GNOME2_MACROS=1 . gnome-autogen.sh
export CFLAGS="%{optflags} -Wno-deprecated-declarations -Wno-format-nonliteral"
%configure \
%if 0%{?with_spice}
           --enable-spice \
%endif
           --enable-rdp \
           --enable-ssh \
           --with-avahi
make V=1 %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

%find_lang vinagre --with-gnome


%check
make check

%files -f vinagre.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/vinagre
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/vinagre-mime.xml
%{_datadir}/vinagre/
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Vinagre.service
%{_datadir}/telepathy/clients/Vinagre.client
%{_datadir}/glib-2.0/schemas/org.gnome.Vinagre.gschema.xml
%dir %{_datadir}/GConf/
%dir %{_datadir}/GConf/gsettings/
%{_datadir}/GConf/gsettings/org.gnome.Vinagre.convert
%{_mandir}/man1/vinagre.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.22.0-35
- Prepare for Oreon 11 (RP1)
