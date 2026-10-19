%global source0_hash 8d1db4e2e1132b9eac630ab6d050c45115aa7fbe0eb38f4f91563657a6348871
Name:           deepin-session-shell
Version:        6.0.68
Release:        1%{?dist}
Summary:        Deepin Desktop Environment - session-shell module
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-session-shell-snipe
Source0:        https://github.com/linuxdeepin/dde-session-shell-snipe/archive/%{version}/dde-session-shell-snipe-%{version}.tar.gz
Requires:       dbus-common
Requires:       %{_bindir}/qdbus-qt5
Requires:       %{_bindir}/xrandr
Requires:       %{_bindir}/xrdb
Requires:       lightdm
Provides:       lightdm-deepin-greeter%{?_isa} = %{version}-%{release}
Provides:       lightdm-greeter%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(liblightdm-qt6-3)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
# /oreon:deps
%description
DDE session shell provides two applications: dde-lock and lightdm-deepin-greeter.
dde-lock provides screen lock function, and lightdm-deepin-greeter provides
login function.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n dde-session-shell-snipe-%{version}

sed -i 's|/usr/lib|%{_libdir}|' CMakeLists.txt

%build

%cmake -GNinja -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build
%install
%cmake_install
chmod +x %{buildroot}%{_bindir}/deepin-greeter
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n deepin-session-shell-devel -f %{oreon_filedir}/deepin-session-shell-devel.list

%changelog

%autochangelog
