%global source0_hash dc27bed5ce6fe9eff5cfbbcb6583535d4ba4f3e7f5a993df8877a58b9504125d
%global commit 3792a0bedd6b807c7bc02f8055ee41389538417f
Name: remmina
Version: 1.4.43
Release:        1%{?dist}
Summary:        Remote Desktop Client
License: GPL-2.0-or-later and MIT
URL: https://remmina.org
Source0:        https://gitlab.com/Remmina/Remmina/-/archive/v%{version}/Remmina-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: pluginBuild-CMakeLists.txt
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%else
%endif
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%else
%endif
Obsoletes: %{name}-plugins-nx < %{version}-%{release}
Obsoletes: %{name}-plugins-st < %{version}-%{release}
Obsoletes: %{name}-plugins-xdmcp < %{version}-%{release}
Recommends: %{name}-plugins-exec
Recommends: %{name}-plugins-rdp
Recommends: %{name}-plugins-secret
Recommends: %{name}-plugins-vnc
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freerdp
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  harfbuzz-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libgcrypt-devel
BuildRequires:  libsodium-devel
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(freerdp3)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  python3-devel
BuildRequires:  xdg-utils
# /oreon:deps
%description
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

Remmina supports multiple network protocols in an integrated and consistent
user interface. Currently RDP, VNC and SSH are supported.

Please don't forget to install the plugins for the protocols you want to use.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
The %{name}-devel package contains header files for developing plugins for
%{name}.

%package plugins-exec
Summary: External execution plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-exec
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin to execute external processes (commands or
applications) from the Remmina window.

%package plugins-secret
Summary: Keyring integration for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-plugins-gnome < %{version}-%{release}
Provides: %{name}-plugins-gnome%{?_isa} = %{version}-%{release}
%description plugins-secret
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin with keyring support for the Remmina remote
desktop client.

%package plugins-rdp
Summary: RDP plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-rdp
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the Remote Desktop Protocol (RDP) plugin for the Remmina
remote desktop client.

%package plugins-vnc
Summary: VNC plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-vnc
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the VNC plugin for the Remmina remote desktop
client.

%package plugins-www
Summary: WWW plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-www
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the WWW plugin (web browser with authentication) for the
Remmina remote desktop client.

%package plugins-python
Summary: Python plugin for Remmina Remote Desktop Client
Requires: %{name}%{?_isa} = %{version}-%{release}
%description plugins-python
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the python plugin for the Remmina remote desktop client.

%package gnome-session
Summary: Gnome Shell session for Remmina kiosk mode
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnome-session
%description gnome-session
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains Remmina kiosk mode, including a Gnome Shell session
that shows up under the display manager session menu.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Remmina-v%{version}-%{commit}

%build

%cmake \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DHAVE_LIBAPPINDICATOR=ON \
    -DWITH_AVAHI=OFF \
    -DWITH_FREERDP3=ON \
    -DWITH_GCRYPT=ON \
    -DWITH_GETTEXT=ON \
    -DWITH_KF5WALLET=OFF \
    -DWITH_KIOSK_SESSION=ON \
    -DWITH_LIBSSH=ON \
    -DWITH_NEWS=OFF \
    -DWITH_PYTHONLIBS=ON \
    -DWITH_SPICE=OFF \
    -DWITH_VTE=ON \
    -DWITH_X2GO=OFF
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}/%{_libdir}/cmake/%{name}/
cp -pr cmake/*.cmake %{buildroot}/%{_libdir}/cmake/%{name}/
cp -pr config.h.in %{buildroot}/%{_includedir}/%{name}/
cp -p %{SOURCE1} %{buildroot}/%{_includedir}/%{name}/
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n remmina-devel -f %{oreon_filedir}/remmina-devel.list
%files -n remmina-plugins-exec -f %{oreon_filedir}/remmina-plugins-exec.list
%files -n remmina-plugins-secret -f %{oreon_filedir}/remmina-plugins-secret.list
%files -n remmina-plugins-rdp -f %{oreon_filedir}/remmina-plugins-rdp.list
%files -n remmina-plugins-vnc -f %{oreon_filedir}/remmina-plugins-vnc.list
%files -n remmina-plugins-www -f %{oreon_filedir}/remmina-plugins-www.list
%files -n remmina-plugins-python -f %{oreon_filedir}/remmina-plugins-python.list
%files -n remmina-gnome-session -f %{oreon_filedir}/remmina-gnome-session.list

%changelog

%autochangelog
