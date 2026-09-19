%global source0_hash 4fcd00f23c542f3b79f35e10e322b67eacb399cac83f48db261cd8e8ea709478

Summary:        Application matching framework
Name:           bamf
Version:        0.5.6
Release:        %autorelease
# Library bits are LGPLv2 or LGPLv3 (but not open-ended LGPLv2+);
# non-lib bits are GPLv3.
# pbrobinson points out that three files in the lib are actually
# marked GPL in headers, making library GPL, though we think this
# may not be upstream's intention. For now, marking library as
# GPL.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://launchpad.net/bamf
Source:         http://launchpad.net/bamf/0.5/%{version}/+download/%{name}-%{version}.tar.gz

BuildRequires:  vala
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  systemd-rpm-macros
# for tests
BuildRequires:  dbus-daemon
BuildRequires:  xorg-x11-server-Xvfb

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

%check
# tests currently do not 100% pass and are non-blocking
dbus-run-session xvfb-run make check

%ldconfig_scriptlets

%post daemon
%systemd_user_post %{name}daemon.service

%preun daemon
%systemd_user_preun %{name}daemon.service

%files
%license COPYING.LGPL COPYING
%{_libdir}/libbamf3.so.*
%{_libdir}/girepository-1.0/Bamf*.typelib

%files devel
%doc ChangeLog TODO
%{_includedir}/libbamf3
%{_libdir}/libbamf3.so
%{_libdir}/pkgconfig/libbamf3.pc
%{_datadir}/gtk-doc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Bamf*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libbamf3.vapi

%files daemon
%doc COPYING
%{_libexecdir}/bamf
%{_datadir}/dbus-1/services/*.service
%{_userunitdir}/bamfdaemon.service
%exclude %{_datadir}/upstart/sessions/bamfdaemon.conf

%changelog
%autochangelog
