%global source0_hash 161907a8c132fcdf2ef47e612fee79dc70d232b88a4f4ba061966a4769906667
%global appstream_version 1.0.0~
%global bubblewrap_version 0.10.0
%global glib_version 2.46.0
%global gpgme_version 1.8.0
%global libcurl_version 7.29.0
%global ostree_version 2020.8
%global wayland_protocols_version 1.32
%global wayland_scanner_version 1.15
%global xdg_portal_version 1.7.0
%bcond malcontent %[!0%{?rhel}]
Name:           flatpak
Version:        1.19.2
Release:        1%{?dist}
Summary:        Application deployment framework for desktop apps
License:        LGPL-2.1-or-later
URL:            https://flatpak.org/
Source0:        https://github.com/flatpak/flatpak/releases/download/%{version}/%{name}-%{version}.tar.xz
%if 0%{?oreon}
Source1:        flatpak-add-flathub-repo.service
%endif
%if %{with malcontent}
%endif
Requires:       appstream%{?_isa} >= %{appstream_version}
Requires:       bubblewrap >= %{bubblewrap_version}
Requires:       glib2%{?_isa} >= %{glib_version}
Requires:       libcurl%{?_isa} >= %{libcurl_version}
Requires:       librsvg2%{?_isa}
Requires:       ostree-libs%{?_isa} >= %{ostree_version}
Requires:       /usr/bin/fusermount3
Requires:       /usr/bin/xdg-dbus-proxy
Requires:       (flatpak-selinux = %{?epoch:%{epoch}:}%{version}-%{release} if selinux-policy-targeted)
Requires:       %{name}-session-helper%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     p11-kit-server
%if 0%{?oreon} || 0%{?rhel} > 7
Recommends:     xdg-desktop-portal >= %{xdg_portal_version}
%else
Requires:       xdg-desktop-portal >= %{xdg_portal_version}
%endif
# oreon:deps
BuildRequires:  /usr/bin/fusermount3
BuildRequires:  /usr/bin/pkcheck
BuildRequires:  /usr/bin/socat
BuildRequires:  /usr/bin/xdg-dbus-proxy
BuildRequires:  /usr/bin/xmlto
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  bison
BuildRequires:  bubblewrap
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  libcap-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(ostree-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xau)
BuildRequires:  python3-pyparsing
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
flatpak is a system for building, distributing and running sandboxed desktop
applications on Linux. See https://wiki.gnome.org/Projects/SandboxedApps for
more information.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
This package contains the pkg-config file and development headers for %{name}.

%package libs
Summary:        Libraries for %{name}
Requires:       bubblewrap >= %{bubblewrap_version}
Requires:       ostree-libs%{?_isa} >= %{ostree_version}
%description libs
This package contains libflatpak.

%package selinux
Summary:        SELinux policy module for %{name}
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  make
BuildArch:      noarch
%{?selinux_requires}
%description selinux
This package contains the SELinux policy module for %{name}.

%package session-helper
Summary:        User D-Bus service used by %{name} and others
Conflicts:      flatpak < 1.4.1-2
Requires:       systemd
%description session-helper
This package contains the org.freedesktop.Flatpak user D-Bus service
that's used by %{name} and other packages.

%package tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-session-helper%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       bubblewrap >= %{bubblewrap_version}
Requires:       ostree%{?_isa} >= %{ostree_version}
%description tests
This package contains installed tests for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    -Dinstalled_tests=true \
    -Dsystem_bubblewrap=/usr/bin/bwrap \
    -Dsystem_dbus_proxy=/usr/bin/xdg-dbus-proxy \
    -Dtmpfilesdir=%{_tmpfilesdir} \
%if %{with malcontent}
    -Dmalcontent=enabled \
%else
    -Dmalcontent=disabled \
%endif
    -Dwayland_security_context=enabled \
    %{nil}
%meson_build
%install
%meson_install
install -pm 644 NEWS README.md %{buildroot}/%{_pkgdocdir}
install -d %{buildroot}%{_datadir}/%{name}/preinstall.d
install -d %{buildroot}%{_datadir}/%{name}/remotes.d
install -d %{buildroot}%{_localstatedir}/lib/flatpak
install -d %{buildroot}%{_sysconfdir}/%{name}/installations.d
install -d %{buildroot}%{_sysconfdir}/%{name}/preinstall.d
install -d %{buildroot}%{_sysconfdir}/flatpak/remotes.d
%if 0%{?oreon}
install -D -t %{buildroot}%{_unitdir} %{SOURCE1}
%endif
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?oreon}
%post

%systemd_post flatpak-add-flathub-repo.service
%endif
%post selinux

%selinux_modules_install %{_datadir}/selinux/packages/flatpak.pp.bz2
%if 0%{?oreon}
%preun

%systemd_preun flatpak-add-flathub-repo.service
%endif
%if 0%{?oreon}
%postun

%systemd_postun_with_restart flatpak-add-flathub-repo.service
%endif
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall %{_datadir}/selinux/packages/flatpak.pp.bz2
fi
%files -f %{oreon_filedir}/main.list
%files -n flatpak-devel -f %{oreon_filedir}/flatpak-devel.list
%files -n flatpak-libs -f %{oreon_filedir}/flatpak-libs.list
%files -n flatpak-selinux -f %{oreon_filedir}/flatpak-selinux.list
%files -n flatpak-session-helper -f %{oreon_filedir}/flatpak-session-helper.list
%files -n flatpak-tests -f %{oreon_filedir}/flatpak-tests.list

%changelog

%autochangelog
