%global source0_hash e38c9721cd5c835ec1d461ab55c9dabcacea8c42eb37aeb782be7b138c91c6eb
Name:           herbstluftwm
Version:        0.9.6
Release:        1%{?dist}
Summary:        A manual tiling window manager
License:        BSD-2-Clause
URL:            http://herbstluftwm.org
Source0:        http://herbstluftwm.org/tarballs/%{name}-%{version}.tar.gz
Patch0:         0.9.6-cstdint-gcc15.patch
Requires:       xsetroot
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
# /oreon:deps
%description
herbstluftwm is a manual tiling window manager for X11 using Xlib and Glib.
Its main features can be described with:

- The layout is based on splitting frames into subframes which can be split
again or can be filled with windows;
- Tags (or workspaces or virtual desktops or …) can be added/removed at
runtime. Each tag contains an own layout exactly one tag is viewed on each
monitor. The tags are monitor independent;
- It is configured at runtime via ipc calls from herbstclient. So the
configuration file is just a script which is run on startup.

%package        zsh
Summary:        Herbstluftwm zsh completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
%description    zsh
This package provides zsh completion script of %{name}.

%package        fish
Summary:        Herbstluftwm fish completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       fish
%description    fish
This package provides fish completion script of %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
for f in "%{buildroot}%{_pkgdocdir}/examples/*.sh"
do
    sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" $f
done
for f in "%{buildroot}%{_sysconfdir}/xdg/%{name}/*"
do
    sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" $f
done
rm %{buildroot}%{_pkgdocdir}/LICENSE
rm -r %{buildroot}%{_pkgdocdir}/html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n herbstluftwm-zsh -f %{oreon_filedir}/herbstluftwm-zsh.list
%files -n herbstluftwm-fish -f %{oreon_filedir}/herbstluftwm-fish.list

%changelog

%autochangelog
