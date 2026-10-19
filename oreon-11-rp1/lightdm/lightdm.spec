%global source0_hash 6dbcd58332abdc113a7a345c22027c9e485ada802706c6b7fbf5f410464e53e3
%bcond_with tests
%global glib2_version	%(pkg-config --modversion glib-2.0 2>/dev/null || echo "2.44")
%global giturl		https://github.com/CanonicalLtd/lightdm
Name:		lightdm
Summary:        A cross-desktop Display Manager
Version:	1.33.1
Release:        1%{?dist}
License:	(LGPL-2.0-only OR LGPL-3.0-only) AND GPL-3.0-or-later
URL:		https://www.freedesktop.org/wiki/Software/LightDM/
Source0:        %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
Source10:	lightdm.pam
Source11:	lightdm-autologin.pam
Source12:	lightdm-tmpfiles.conf
Source13:	lightdm.service
Source14:	lightdm.logrotate
Source15:	lightdm.rules
Source16:	lightdm.sysusers
Source20:	50-backup-logs.conf
Source21:	50-minimum-vt.conf
Source22:	50-session-wrapper.conf
Source23:	50-user-authority-in-system-dir.conf
Source24:	50-xserver-command.conf
Source25:	50-disable-guest.conf
Source26:	50-run-directory.conf
Patch0:		gcc-10.patch
Patch1:		remove_bin_path.patch
Patch2:		%{giturl}/pull/5.patch#/lightdm-1.25.1-disable_dmrc.patch
Patch3:		lightdm-1.32.0-add-qt6-lib.patch
Requires:	%{name}-gobject%{?_isa} = %{version}-%{release}
Requires:	accountsservice
Requires:	dbus
Requires:	polkit-js-engine
Requires:	/sbin/nologin
Requires:	systemd
Requires:	xorg-x11-server-Xorg
Requires:	xorg-x11-xinit
Requires:   lightdm-greeter = 1.2
Suggests:   slick-greeter
%{?systemd_requires}
Obsoletes: lightdm-qt < %{version}-%{release}
Obsoletes: lightdm-qt-devel < %{version}-%{release}
Requires(post):	psmisc dbus-daemon
Provides:	service(graphical-login) = lightdm
# oreon:deps
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libgcrypt-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
# /oreon:deps
%description
Lightdm is a display manager that:
* Is cross-desktop - supports different desktops
* Supports different display technologies
* Is lightweight - low memory usage and fast performance

%package gobject
Summary:	LightDM GObject client library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	glib2%{?_isa} >= %{glib2_version}
%description gobject
This package contains a GObject based library for LightDM clients to use to
interface with LightDM.

%package gobject-devel
Summary:	Development files for %{name}-gobject
Requires:	%{name}-gobject%{?_isa} = %{version}-%{release}
%description gobject-devel
%{summary}.

%package qt5
Summary:	LightDM Qt5 client library
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description qt5
This package contains a Qt5-based library for LightDM clients to use to interface
with LightDM.

%package qt5-devel
Summary:	Development files for %{name}-qt5
Requires:	%{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.

%package qt6
Summary:	LightDM Qt6 client library
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description qt6
This package contains a Qt6-based library for LightDM clients to use to interface
with LightDM.

%package qt6-devel
Summary:	Development files for %{name}-qt6
Requires:	%{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%conf
# Make libtoolize happy.
%{__cat} %{_datadir}/aclocal/intltool.m4 > aclocal.m4
# gettext-0.25 fix
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
# Bootstrap
NOCONFIGURE=1 ./autogen.sh

%configure                      \
	--disable-dmrc              \
	--disable-silent-rules      \
	--disable-static			\
	--enable-gtk-doc			\
	--enable-libaudit			\
	--enable-liblightdm-qt5     \
	--enable-liblightdm-qt6		\
	--enable-introspection      \
%if %{with tests}
	--enable-tests				\
%else
	--disable-tests				\
%endif
	--enable-vala				\
	--with-greeter-user=lightdm \
	--with-greeter-session=lightdm-greeter

%build

%make_build
%install
%make_install
%{__mkdir_p} %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/		\
		%{buildroot}%{_datadir}/dbus-1/interfaces		\
		%{buildroot}%{_datadir}/dbus-1/system.d			\
		%{buildroot}%{_datadir}/lightdm/lightdm.conf.d/		\
		%{buildroot}%{_datadir}/lightdm/remote-sessions/	\
		%{buildroot}%{_datadir}/xgreeters/			\
		%{buildroot}%{_localstatedir}/cache/lightdm/		\
		%{buildroot}%{_rundir}/lightdm/		\
		%{buildroot}%{_localstatedir}/log/lightdm/		\
		%{buildroot}%{_localstatedir}/lib/lightdm/		\
		%{buildroot}%{_localstatedir}/lib/lightdm-data/
rm -fv %{buildroot}%{_libdir}/lib*.la
%{__rm} -rfv %{buildroot}%{_sysconfdir}/apparmor.d/
%{__rm} -rfv %{buildroot}%{_sysconfdir}/init
%{__install} -Dpm 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/lightdm
%{__install} -Dpm 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/pam.d/lightdm-autologin
%{__install} -Dpm 0644 %{SOURCE12} %{buildroot}%{_prefix}/lib/tmpfiles.d/lightdm.conf
%{__install} -Dpm 0644 %{SOURCE13} %{buildroot}%{_unitdir}/lightdm.service
%{__install} -Dpm 0644 %{SOURCE14} %{buildroot}%{_sysconfdir}/logrotate.d/lightdm
%{__install} -Dpm 0644 %{SOURCE15} %{buildroot}%{_datadir}/polkit-1/rules.d/lightdm.rules
%{__install} -Dpm 0644 %{SOURCE16} %{buildroot}%{_sysusersdir}/lightdm.conf
%{__install} -pm 0644 %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23}	\
	%{SOURCE24} %{SOURCE25} %{SOURCE26} %{buildroot}%{_datadir}/lightdm/lightdm.conf.d/
%find_lang lightdm --with-gnome
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

%make_build check ||:
%endif
%post

%systemd_post lightdm.service
%preun

%systemd_preun lightdm.service
%postun

%systemd_postun lightdm.service
%files -f %{oreon_filedir}/main.list
%files -n lightdm-gobject -f %{oreon_filedir}/lightdm-gobject.list
%files -n lightdm-gobject-devel -f %{oreon_filedir}/lightdm-gobject-devel.list
%files -n lightdm-qt5 -f %{oreon_filedir}/lightdm-qt5.list
%files -n lightdm-qt5-devel -f %{oreon_filedir}/lightdm-qt5-devel.list
%files -n lightdm-qt6 -f %{oreon_filedir}/lightdm-qt6.list
%files -n lightdm-qt6-devel -f %{oreon_filedir}/lightdm-qt6-devel.list

%changelog

%autochangelog
