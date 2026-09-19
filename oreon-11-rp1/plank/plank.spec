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
Release:        20.%{commitdate}.git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later

URL:            https://launchpad.net/%{name}
# use sources from elementary OS dock "fork" which is actually maintained
# * dropped patented zoom animation
# * fixed session integration
# * support for automatic dark theme
# * migrated from autotools to meson
Source0:        https://github.com/elementary/dock/archive/%{commit}/dock-%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(cairo) >= 1.13
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libbamf3) >= 0.4.0
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.6.99.1
BuildRequires:  pkgconfig(xfixes) >= 5.0

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Requires:       bamf-daemon
Requires:       hicolor-icon-theme

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

%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{name}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop

%{_bindir}/%{name}

%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/%{name}/

%{_mandir}/man1/%{name}.1*

%files libs
%license COPYING COPYRIGHT
%doc README.md AUTHORS NEWS

%{_libdir}/lib%{name}.so.1*
%dir %{_libdir}/%{name}

%files docklets
%dir %{_libdir}/%{name}/docklets
%{_libdir}/%{name}/docklets/*.so

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%{_includedir}/%{name}/

%{_datadir}/vala/vapi/%{name}.vapi
%{_datadir}/vala/vapi/%{name}.deps

%changelog
%autochangelog
