%global source0_hash f697dba9ef44c9c722aa81742c029df483fdabf8f32f711b342c708112143546
Name:		jgmenu
Version:	4.7.0
Release:        1%{?dist}
Summary:        Simple X11 application menu
License:	GPL-2.0-or-later
URL:		https://jgmenu.github.io
Source0:        https://github.com/johanmalm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:	hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxfce4panel-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(xrandr)
# /oreon:deps
%description
A simple, independent and contemporary-looking X11 menu, designed for scripting,
ricing and tweaking. Useful for tint2, polymenu, cairo-dock, plank, unity,
openbox, i3, dwm and other light environments.

%package	lx
Summary:	LXDE %{name} plugin
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
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires: make
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	xfce4
Xfce4 plugin for %{name} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{configure} -a
%{make_build}
%install
%{make_install}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n jgmenu-lx -f %{oreon_filedir}/jgmenu-lx.list
%files -n jgmenu-pmenu -f %{oreon_filedir}/jgmenu-pmenu.list
%files -n jgmenu-gtktheme -f %{oreon_filedir}/jgmenu-gtktheme.list
%files -n jgmenu-xfce4 -f %{oreon_filedir}/jgmenu-xfce4.list

%changelog

%autochangelog
