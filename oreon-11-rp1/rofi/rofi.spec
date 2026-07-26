%global source0_hash f81659b175306ff487e35d88d6b36128e85a793bfb56b64fa22c62eb54c4abd0

Name:    rofi
Version: 2.0.0
Release: 2%{?dist}
Summary: A window switcher, application launcher and dmenu replacement

# lexer/theme-parser.[ch]:
# These files are generated from lexer/theme-parser.y and licensed with GPLv3+
# with Bison exception.
# As the source file is licensed with MIT, according to the Bison exception,
# the shipped files are considered to be MIT-licensed.
# See also
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/C4VVT54Z4WFGJPPD5X54ILKRF6X2IFLZ/
#
# protocols/wlr-layer-shell-unstable-v1.xml,
# protocols/wlr-foreign-toplevel-management-unstable-v1.xml:
# These files are licensed under HPND-sell-variant. The files are processed to
# C-compilable files by the `wayland-scanner` binary during build and don't
# alter the main license of the binaries.
License: MIT
URL:     https://github.com/davatorium/%{name}
Source:  %{URL}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires: gcc
BuildRequires: bison
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: graphviz
BuildRequires: meson
BuildRequires: pandoc
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-xcb)
BuildRequires: pkgconfig(check) >= 0.11.0
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-imdkit)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-xinerama)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)

# https://github.com/sardemff7/libgwater
Provides: bundled(libgwater)
# https://github.com/sardemff7/libnkutils
Provides: bundled(libnkutils)

Obsoletes:     rofi-wayland < 2
Provides:      rofi-wayland = %{version}-%{release}

Requires:      %{name}-themes = %{version}-%{release}
Requires:      hicolor-icon-theme

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

%autosetup -p1

%build
%meson
%meson_build

%meson_build doxy
find %{_vpath_builddir}/doc/html/html -name "*.map" -delete
find %{_vpath_builddir}/doc/html/html -name "*.md5" -delete

%install
%meson_install

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/rofi*.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%{_datadir}/applications/rofi.desktop
%{_datadir}/applications/rofi-theme-selector.desktop
%{_datadir}/icons/hicolor/scalable/apps/rofi.svg
%{_mandir}/man1/rofi*
%{_mandir}/man5/rofi*

%files themes
%license COPYING
%{_datarootdir}/rofi

%files devel
%{_includedir}/rofi
%{_libdir}/pkgconfig/rofi.pc

%files devel-doc
%license COPYING
%doc %{_vpath_builddir}/doc/html/html/*

%changelog
%autochangelog
