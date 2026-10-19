%global source0_hash 9c43d9f4bd30f4fea7f780d4e8b14f7589107c52e9cb6bd202bd0d1c2064de55
Name:           caribou
Version:        0.4.21
Release:        51%{?dist}
Summary:        A simplified in-place on-screen keyboard
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
Requires:       python3-%{name} = %{version}-%{release}
Requires:       gobject-introspection
Recommends:     (caribou-gtk2-module if gtk2)
Requires:       (caribou-gtk3-module if gtk3)
Obsoletes:      caribou < 0.4.1-3
Obsoletes:      gok < 2.30.1-6
# oreon:deps
BuildRequires:  at-spi2-core-devel
BuildRequires:  automake
BuildRequires:  clutter-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libXtst-devel
BuildRequires:  libgee-devel
BuildRequires:  libxklavier-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-devel
BuildRequires:  vala
# /oreon:deps
%description
Caribou is a text entry application that currently manifests itself as
a simplified in-place on-screen keyboard.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
%oreon_autofiles caribou-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-caribou usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles caribou-gtk2-module usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles caribou-gtk3-module usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles caribou-antler usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n caribou-devel -f %{oreon_filedir}/caribou-devel.list
%files -n python3-caribou -f %{oreon_filedir}/python3-caribou.list
%files -n caribou-gtk2-module -f %{oreon_filedir}/caribou-gtk2-module.list
%files -n caribou-gtk3-module -f %{oreon_filedir}/caribou-gtk3-module.list
%files -n caribou-antler -f %{oreon_filedir}/caribou-antler.list

%changelog

%autochangelog
