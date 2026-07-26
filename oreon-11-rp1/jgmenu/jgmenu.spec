%global source0_hash 523d7f7a2225f4d2cc9772c44bcc661518d99ccc478bd0d099b0b157917304b1

Name:		jgmenu
Version:	4.5.0
Release:	4%{?dist}
Summary:	Simple X11 application menu
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://jgmenu.github.io
Source0:	https://github.com/johanmalm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:	hicolor-icon-theme
BuildRequires:	gcc, desktop-file-utils
# libXrandr-devel
BuildRequires:	pkgconfig(xrandr)
# libxml2-devel
BuildRequires:	pkgconfig(libxml-2.0)
# cairo-devel
BuildRequires:	pkgconfig(cairo)
# pango-devel
BuildRequires:	pkgconfig(pango)
# librsvg2-devel
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.46

%description
A simple, independent and contemporary-looking X11 menu, designed for scripting,
ricing and tweaking. Useful for tint2, polymenu, cairo-dock, plank, unity,
openbox, i3, dwm and other light environments.

%package	lx
Summary:	LXDE %{name} plugin
# menu-cache-devel
BuildRequires:	pkgconfig(libmenu-cache)
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	lx
LXDE plugin for %{name} package.

%package	pmenu
Summary:	Pmenu %{name} plugin
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	pmenu
Pmenu plugin for %{name} package.

%package	gtktheme
Summary:	GTKtheme %{name} plugin
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	gtktheme
GTKtheme plugin for %{name} package.

%package	xfce4
Summary:	Xfce4 %{name} plugin
# xfce4-panel-devel
%if 0%{?fedora} > 33
BuildRequires:	pkgconfig(libxfce4panel-2.0)
%else
BuildRequires:	pkgconfig(libxfce4panel-1.0)
%endif
BuildRequires: make
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	xfce4
Xfce4 plugin for %{name} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# default: --with-lx --with-pmenu --with-gtktheme --with-xfce4-panel-applet
%{configure} -a
%{make_build}

%install
%{make_install}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
# TODO: make test (failed on aarch64: https://github.com/johanmalm/jgmenu/issues/123)

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}*
%{_libexecdir}/%{name}/%{name}-*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man?/%{name}*.*
%exclude %{_libexecdir}/%{name}/%{name}-{lx,pmenu.py,gtktheme.py}
%exclude %{_mandir}/man1/%{name}-{lx,pmenu}.1.*

%files	lx
%{_libexecdir}/%{name}/%{name}-lx
%{_mandir}/man1/%{name}-lx.1.*

%files	pmenu
%{_libexecdir}/%{name}/%{name}-pmenu.py
%{_mandir}/man1/%{name}-pmenu.1.*

%files	gtktheme
%{_libexecdir}/%{name}/%{name}-gtktheme.py

%files	xfce4
%{_libdir}/xfce4/panel/plugins/lib%{name}.so
%{_datadir}/xfce4/panel/plugins/%{name}-applet.desktop

%changelog
%autochangelog
