%global source0_hash 9c43d9f4bd30f4fea7f780d4e8b14f7589107c52e9cb6bd202bd0d1c2064de55

Name:           caribou
Version:        0.4.21
Release:        51%{?dist}
Summary:        A simplified in-place on-screen keyboard
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Projects/Caribou
Source0:        http://download.gnome.org/sources/caribou/0.4/caribou-%{version}.tar.xz
Patch1:         caribou-0.4.20-fix-python-exec.patch
Patch2:         caribou-0.4.20-multilib.patch
Patch4:         fix-style-css.patch
Patch5:         Fix-compilation-error.patch
Patch6:         Fix-subkey-popmenu-not-showing-after-being-dismissed.patch
Patch7:         xadapter.vala-Remove-XkbKeyTypesMask-and-f.patch
Patch8:         drop_gir_patch.patch

BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  intltool
BuildRequires:  gnome-doc-utils
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  clutter-devel
BuildRequires:  vala
BuildRequires:  libXtst-devel
BuildRequires:  libxklavier-devel
BuildRequires:  libgee-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  at-spi2-core-devel

# Changed in F23 to pull python3-caribou default
Requires:       python3-%{name} = %{version}-%{release}
Requires:       gobject-introspection
Recommends:     (caribou-gtk2-module if gtk2)
Requires:       (caribou-gtk3-module if gtk3)

#Following is needed as package moved from noarch to arch
Obsoletes:      caribou < 0.4.1-3
# Obsolete retired 'gok' to make sure it gets removed with distro upgrade
Obsoletes:      gok < 2.30.1-6

%description
Caribou is a text entry application that currently manifests itself as
a simplified in-place on-screen keyboard.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Obsolete retired 'gok' to make sure it gets removed with distro upgrade
Obsoletes:      gok-devel < 2.30.1-6

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n python3-caribou
Summary:        Keyboard UI for %{name}
BuildRequires:  python3-devel
BuildRequires:  python3-gobject

Requires:       python3-gobject
Requires:       python3-pyatspi
Requires:       %{name} = %{version}-%{release}
Obsoletes:      caribou < 0.4.1-3
BuildArch:      noarch

%description  -n python3-caribou
This package contains caribou python3 GUI

%package        gtk2-module
Summary:        Gtk2 module for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      caribou < 0.4.1-3

%description    gtk2-module
This package contains caribou module for gtk2 applications.

%package        gtk3-module
Summary:        Gtk3 module for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      caribou < 0.4.1-3

%description    gtk3-module
This package contains caribou module for gtk3 applications.

%package        antler
Summary:        Keyboard implementation for %{name}
Requires:       python3-%{name} = %{version}-%{release}
Obsoletes:      caribou < 0.4.1-3

%description    antler
This package contains caribou keyboard implementation for
non-gnome-shell sessions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

gettextize --copy --force
aclocal --install -I m4
autoreconf --verbose --force --install

find -name '*.vala' -exec touch {} \;

%build
%configure --disable-static PYTHON=python3
make clean
%make_build

%install
%make_install autostart_DATA=

find %{buildroot} -name '*.la' -exec rm -f {} ';'

desktop-file-validate %{buildroot}%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/caribou-gtk-module.desktop || :

%find_lang caribou

%ldconfig_scriptlets

%files -f caribou.lang
%doc NEWS README
%license COPYING
%{_bindir}/caribou-preferences
%{_datadir}/caribou
%{_libdir}/girepository-1.0/Caribou-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.Caribou.Daemon.service
%{_datadir}/glib-2.0/schemas/org.gnome.caribou.gschema.xml
%{_libdir}/libcaribou.so.0*
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/caribou-gtk-module.desktop
%{_libexecdir}/caribou

%files -n python3-caribou
%{python3_sitelib}/caribou

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/caribou-1.0.pc
%{_datadir}/gir-1.0/Caribou-1.0.gir
%{_datadir}/vala

%files gtk2-module
%{_libdir}/gtk-2.0/modules/libcaribou-gtk-module.so

%files gtk3-module
%{_libdir}/gtk-3.0/modules/libcaribou-gtk-module.so

%files antler
%{_datadir}/antler
%{_datadir}/dbus-1/services/org.gnome.Caribou.Antler.service
%{_libexecdir}/antler-keyboard
%{_datadir}/glib-2.0/schemas/org.gnome.antler.gschema.xml

%changelog
%autochangelog
