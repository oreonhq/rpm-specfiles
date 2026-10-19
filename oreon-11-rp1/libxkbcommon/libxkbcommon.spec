%global source0_hash acc4d5f7c3cbba5f9f8d08d8bdbeede84ecede46792f47929aa9321873385528
%global tarball_name xkbcommon
Name:           libxkbcommon
Version:        1.13.2
Release:        1%{?dist}
Summary:        X.Org X11 XKB parsing library
License:        MIT AND X11 AND MIT-CMU
URL:            http://www.x.org
Source0:        https://github.com/%{tarball_name}/%{name}/archive/refs/tags/%{tarball_name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       xkeyboard-config
# oreon:deps
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  libX11-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  xkeyboard-config-devel
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n %{name}-%{tarball_name}-%{version}

%build

%meson -Denable-docs=false \
       -Denable-x11=true \
       -Denable-wayland=true
%meson_build
%install
%meson_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libxkbcommon-devel -f %{oreon_filedir}/libxkbcommon-devel.list
%files -n libxkbcommon-x11 -f %{oreon_filedir}/libxkbcommon-x11.list
%files -n libxkbcommon-x11-devel -f %{oreon_filedir}/libxkbcommon-x11-devel.list
%files -n libxkbcommon-utils -f %{oreon_filedir}/libxkbcommon-utils.list
%files -n libxkbcommon-x11-utils -f %{oreon_filedir}/libxkbcommon-x11-utils.list

%changelog

%autochangelog
