%global source0_hash f81659b175306ff487e35d88d6b36128e85a793bfb56b64fa22c62eb54c4abd0
Name:    rofi
Version: 2.0.0
Release:        1%{?dist}
Summary:        A window switcher, application launcher and dmenu replacement
License: MIT
URL:     https://github.com/davatorium/%{name}
Source0:        https://github.com/davatorium/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Provides: bundled(libgwater)
Provides: bundled(libnkutils)
Obsoletes:     rofi-wayland < 2
Provides:      rofi-wayland = %{version}-%{release}
Requires:      %{name}-themes = %{version}-%{release}
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-imdkit)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
# /oreon:deps
%description
Rofi is a dmenu replacement. Rofi, like dmenu, will provide the user with a
textual list of options where one or more can be selected. This can either be,
running an application, selecting a window or options provided by an external
script.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel-doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
%description    devel-doc
The %{name}-devel-doc package contains documentation files for developing
applications that use %{name}.

%package        themes
Summary:        Themes for %{name}
BuildArch:      noarch
%description    themes
The %{name}-themes package contains themes for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%meson_build doxy
find %{_vpath_builddir}/doc/html/html -name "*.map" -delete
find %{_vpath_builddir}/doc/html/html -name "*.md5" -delete
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/rofi*.desktop
%files -f %{oreon_filedir}/main.list
%files -n rofi-devel -f %{oreon_filedir}/rofi-devel.list
%files -n rofi-devel-doc -f %{oreon_filedir}/rofi-devel-doc.list
%files -n rofi-themes -f %{oreon_filedir}/rofi-themes.list

%changelog

%autochangelog
