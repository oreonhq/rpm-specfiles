%global source0_hash 4fcd00f23c542f3b79f35e10e322b67eacb399cac83f48db261cd8e8ea709478
Summary:        Application matching framework
Name:           bamf
Version:        0.5.6
Release:        1%{?dist}
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://launchpad.net/bamf
Source0:        http://launchpad.net/bamf/0.5/%{version}/+download/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  dbus-daemon
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
BAMF removes the headache of applications matching into a simple DBus
daemon and C wrapper library. Currently features application matching
at amazing levels of accuracy (covering nearly every corner case).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        daemon
Summary:        Application matching framework
License:        GPL-3.0-only
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}
%description    daemon
BAMF removes the headache of applications matching into a simple DBus
daemon and C wrapper library. Currently features application matching
at amazing levels of accuracy (covering nearly every corner case). This
package contains the bamf daemon and supporting data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
NOCONFIGURE=1 ./autogen.sh

%build

%configure --disable-static --disable-webapps --enable-gtk-doc
%make_build
%install
%make_install
find %{buildroot} -regex ".*\.la$" | xargs rm -f --
%oreon_autofiles bamf-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles bamf-daemon usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

dbus-run-session xvfb-run make check
%ldconfig_scriptlets
%post daemon

%systemd_user_post %{name}daemon.service
%preun daemon

%systemd_user_preun %{name}daemon.service
%files -f %{oreon_filedir}/main.list
%files -n bamf-devel -f %{oreon_filedir}/bamf-devel.list
%files -n bamf-daemon -f %{oreon_filedir}/bamf-daemon.list

%changelog

%autochangelog
