%global source0_hash aeb951964c2f7ecc08174cb5517962d157595e9e3f38fc4a130b91dc2f9fec18

%global tarball_name xkbcommon

Name:           libxkbcommon
Version:        1.13.1
Release:        2%{?gitdate:.%{gitdate}}%{?dist}
Summary:        X.Org X11 XKB parsing library
License:        MIT AND X11 AND MIT-CMU
URL:            http://www.x.org

Source0:        https://github.com/xkbcommon/libxkbcommon/archive/refs/tags/xkbcommon-1.13.1.tar.gz
BuildRequires:  gcc
BuildRequires:  git meson
BuildRequires:  byacc flex bison
BuildRequires:  xorg-x11-proto-devel libX11-devel
BuildRequires:  pkgconfig(wayland-client) pkgconfig(wayland-protocols)
BuildRequires:  xkeyboard-config-devel
BuildRequires:  pkgconfig(xcb-xkb) >= 1.10
BuildRequires:  libxml2-devel

Requires:       xkeyboard-config

%description
%{name} is the X.Org library for compiling XKB maps into formats usable by
the X Server or other display servers.

%package devel
Summary:        X.Org X11 XKB parsing development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
X.Org X11 XKB parsing development package

%package x11
Summary:        X.Org X11 XKB keymap creation library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description x11
%{name}-x11 is the X.Org library for creating keymaps by querying the X
server.

%package x11-devel
Summary:        X.Org X11 XKB keymap creation library
Requires:       %{name}-x11%{?_isa} = %{version}-%{release}

%description x11-devel
X.Org X11 XKB keymap creation library development package

%package utils
Summary:        X.Org X11 XKB parsing utilities
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
%{name}-utils is a set of utilities to analyze and test XKB parsing.

%package x11-utils
Summary:        X.Org X11 XKB parsing utilities
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-x11%{?_isa} = %{version}-%{release}
Requires:       %{name}-utils%{?_isa} = %{version}-%{release}

%description x11-utils
%{name}-x11-utils is a set of X11 utilities to analyze and test XKB parsing.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git -n %{name}-%{tarball_name}-%{version}

%build
%meson -Denable-docs=false \
       -Denable-x11=true \
       -Denable-wayland=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libxkbcommon.so.0*
%{_libdir}/libxkbregistry.so.0*

%files devel
%{_libdir}/libxkbcommon.so
%{_libdir}/libxkbregistry.so
%dir %{_includedir}/xkbcommon/
%{_includedir}/xkbcommon/xkbcommon.h
%{_includedir}/xkbcommon/xkbcommon-compat.h
%{_includedir}/xkbcommon/xkbcommon-compose.h
%{_includedir}/xkbcommon/xkbcommon-keysyms.h
%{_includedir}/xkbcommon/xkbcommon-names.h
%{_includedir}/xkbcommon/xkbregistry.h
%{_libdir}/pkgconfig/xkbcommon.pc
%{_libdir}/pkgconfig/xkbregistry.pc

%ldconfig_scriptlets x11

%files x11
%{_libdir}/libxkbcommon-x11.so.0*

%files x11-devel
%{_libdir}/libxkbcommon-x11.so
%{_includedir}/xkbcommon/xkbcommon-x11.h
%{_libdir}/pkgconfig/xkbcommon-x11.pc

%files utils
%{_bindir}/xkbcli
%{_libexecdir}/xkbcommon/xkbcli-compile-compose
%{_libexecdir}/xkbcommon/xkbcli-compile-keymap
%{_libexecdir}/xkbcommon/xkbcli-dump-keymap
%{_libexecdir}/xkbcommon/xkbcli-dump-keymap-wayland
%{_libexecdir}/xkbcommon/xkbcli-how-to-type
%{_libexecdir}/xkbcommon/xkbcli-interactive
%{_libexecdir}/xkbcommon/xkbcli-interactive-evdev
%{_libexecdir}/xkbcommon/xkbcli-interactive-wayland
%{_libexecdir}/xkbcommon/xkbcli-list
%{_mandir}/man1/xkbcli-compile-compose.1.gz
%{_mandir}/man1/xkbcli-compile-keymap.1.gz
%{_mandir}/man1/xkbcli-dump-keymap-wayland.1.gz
%{_mandir}/man1/xkbcli-how-to-type.1.gz
%{_mandir}/man1/xkbcli-interactive-evdev.1.gz
%{_mandir}/man1/xkbcli-interactive-wayland.1.gz
%{_mandir}/man1/xkbcli-list.1.gz
%{_mandir}/man1/xkbcli.1.gz
%{_datadir}/bash-completion/completions/xkbcli

%files x11-utils
%{_libexecdir}/xkbcommon/xkbcli-interactive-x11
%{_libexecdir}/xkbcommon/xkbcli-dump-keymap-x11
%{_mandir}/man1/xkbcli-interactive-x11.1.gz
%{_mandir}/man1/xkbcli-dump-keymap-x11.1.gz

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.13.1-2
- Prepare for Oreon 11 (RP1)
