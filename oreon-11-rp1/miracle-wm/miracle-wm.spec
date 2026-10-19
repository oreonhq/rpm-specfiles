%global source0_hash 5ea17cef4da2e89d8b27d4d00dabec4a924163b52b5a2ff47a02edf80be7ff26
%global miral_ver 5.1
%global mirversion 2.18
%global miracle_configlib_somajor 0
Name:           miracle-wm
Version:        0.11.0
Release:        1%{?dist}
Summary:        A tiling Wayland compositor based on Mir
License:        GPL-3.0-or-later and MIT
URL:            https://github.com/miracle-window-manager/miracle-wm
Source0:        https://github.com/miracle-window-manager/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         734.patch
Patch1:         miracle-wm-0.8.3-fix-for-gcc16.patch
Recommends:     xorg-x11-server-Xwayland%{?_isa}
Requires:       %{name}-config-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(gtest)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glm-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  pcre2
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(miral)
BuildRequires:  pkgconfig(mircommon)
BuildRequires:  pkgconfig(mircommon-internal)
BuildRequires:  pkgconfig(mirplatform)
BuildRequires:  pkgconfig(mirserver-internal)
BuildRequires:  pkgconfig(mirwayland)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
%oreon_prep
%build

%cmake -DSYSTEMD_INTEGRATION=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{_vpath_builddir}/tests/miracle-wm-tests
%files -f %{oreon_filedir}/main.list
%files -n miracle-wm-config-libs -f %{oreon_filedir}/miracle-wm-config-libs.list
%files -n miracle-wm-config-devel -f %{oreon_filedir}/miracle-wm-config-devel.list

%changelog

%autochangelog
