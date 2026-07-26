%global source0_hash 34f6fa63cece823e44410ae455230ace426ffb61bd5d259b8f243ac8cc03c94c

%global miral_ver 5.1
%global mirversion 2.18

%global miracle_configlib_somajor 0

Name:           miracle-wm
Version:        0.8.3
Release:        3%{?dist}
Summary:        A tiling Wayland compositor based on Mir

License:        GPL-3.0-or-later and MIT
URL:            https://github.com/miracle-window-manager/miracle-wm
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# bugfix: only install libmirrenderer-dev if it is available
# https://github.com/miracle-wm-org/miracle-wm/pull/734
Patch0:         734.patch
# already fixed upstream
Patch1:         miracle-wm-0.8.3-fix-for-gcc16.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pkgconfig(miral) >= %{miral_ver}
BuildRequires:  pkgconfig(mirplatform) >= %{mirversion}
BuildRequires:  pkgconfig(mircommon) >= %{mirversion}
BuildRequires:  pkgconfig(mirwayland) >= %{mirversion}
BuildRequires:  pkgconfig(mircommon-internal) >= %{mirversion}
BuildRequires:  pkgconfig(mirserver-internal) >= %{mirversion}
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  cmake(nlohmann_json) >= 3.2.0
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  cmake(gtest)
BuildRequires:  libxkbcommon-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pcre2
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(egl)
BuildRequires:  glm-devel
BuildRequires:  boost-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  systemd-rpm-macros

Recommends:     xorg-x11-server-Xwayland%{?_isa}

Requires:       %{name}-config-libs%{?_isa} = %{version}-%{release}

%description
miracle-wm is a Wayland compositor based on Mir. It features a tiling window
manager at its core, very much in the style of i3 and sway. The intention is
to build a compositor that is flashier and more feature-rich than either of
those compositors, like swayfx.

%package config-libs
Summary:        Libraries for %{name} configuration

%description config-libs
This package provides the libraries for manipulating the configuration
of %{name}.

%package config-devel
Summary:        Development files for %{name} configuration library
Requires:       %{name}-config-libs%{?_isa} = %{version}-%{release}

%description config-devel
This package provides the files to develop applications that use the
libraries for manipulating the configuration of %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%build
%cmake -DSYSTEMD_INTEGRATION=ON
%cmake_build

%install
%cmake_install

%check
%{_vpath_builddir}/tests/miracle-wm-tests

%files
%{_bindir}/miracle-wm
%{_bindir}/miracle-wm-sensible-terminal
%{_bindir}/miracle-wm-session
%{_bindir}/miraclemsg
%{_libexecdir}/miracle-wm-*
%{_datarootdir}/miracle-wm/
%{_datarootdir}/wayland-sessions/miracle-wm.desktop
%{_userunitdir}/miracle-wm*
%license LICENSE
%license miraclemsg/LICENSE.sway session/LICENSE.sway-systemd

%files config-libs
%license LICENSE
%{_libdir}/libmiracle-wm-config.so.%{miracle_configlib_somajor}{,.*}

%files config-devel
%{_includedir}/miracle/
%{_libdir}/libmiracle-wm-config.so
%{_libdir}/pkgconfig/miracle-wm-config.pc

%changelog
%autochangelog
