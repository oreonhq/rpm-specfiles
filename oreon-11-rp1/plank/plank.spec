%global source0_hash 9120a2e7d3142b4202145b0e5e0d2ea49c1acad9508ca3d4d69b7cd12b9f1ebc
%global commit      013d0513bcf029426db19aea4d8b19c7b3b0077c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20210202
%global common_description %{expand:
Plank is meant to be the simplest dock on the planet. The goal is to
provide just what a dock needs and absolutely nothing more. It is,
however, a library which can be extended to create other dock programs
with more advanced features.
Thus, Plank is the underlying technology for Docky (starting in version
3.0.0) and aims to provide all the core features while Docky extends it
to add fancier things like Docklets, painters, settings dialogs, etc.}
Name:           plank
Summary:        Stupidly simple Dock
Version:        0.11.89
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://launchpad.net/%{name}
Source0:        https://github.com/elementary/dock/archive/%{commit}/dock-%{shortcommit}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       bamf-daemon
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  vala
# /oreon:deps
%description %{common_description}

%package        libs
Summary:        Shared libraries for %{name}
%description    libs %{common_description}
This package contains the shared libraries.

%package        docklets
Summary:        Docklets for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    docklets %{common_description}
This package contains the docklets for plank.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel %{common_description}
This package contains the files necessary to develop against plank.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dock-%{commit} -p1

%build

%meson -Denable-apport=false
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{name}.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n plank-libs -f %{oreon_filedir}/plank-libs.list
%files -n plank-docklets -f %{oreon_filedir}/plank-docklets.list
%files -n plank-devel -f %{oreon_filedir}/plank-devel.list

%changelog

%autochangelog
