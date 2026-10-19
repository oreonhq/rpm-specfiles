%global source0_hash e07dd38e6cf81275da213c02814c5352bbb5e8c0290bc3711abf098806293adb
Name:		imsettings
Version:	1.8.11
Release:        1%{?dist}
License:	LGPL-2.0-or-later
URL:		https://gitlab.com/tagoh/%{name}/
Source0:        https://gitlab.com/tagoh/%{name}/-/releases/%{version}/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-constraint-of-language.patch
Patch1:		%{name}-disable-xim.patch
Patch2:		%{name}-xinput-xcompose.patch
Summary:        Delivery framework for general Input Method configuration
Requires:	xorg-x11-xinit >= 1.0.2-22.fc8
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-desktop-module%{?_isa} = %{version}-%{release}
Requires(post):	systemd %{_sbindir}/alternatives
Requires(postun):	systemd %{_sbindir}/alternatives
Requires:	/bin/bash
Suggests:	%{name}-gsettings
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  libX11-devel
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the core DBus services and some utilities.

%package	libs
Summary:	Libraries for imsettings
%description	libs
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the shared library for imsettings.

%package	devel
Summary:	Development files for imsettings
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
Requires:	glib2-devel >= 2.32.0
%description	devel
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the development files to make any
applications with imsettings.

%package	gsettings
Summary:	GSettings support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	dconf
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}
Provides:	%{name}-gnome = %{version}-%{release}
Obsoletes:	%{name}-gnome < 1.5.1-3
Provides:	%{name}-systemd = %{version}-%{release}
Obsoletes:	%{name}-systemd < 1.8.3-6
Provides:	%{name}-cinnamon = %{version}-%{release}
Obsoletes:	%{name}-cinnamon < 1.8.10-4
%description	gsettings
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on
GNOME and Cinnamon which requires GSettings in their
own XSETTINGS daemons.

%package	qt
Summary:	Qt support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	im-chooser
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}
%description	qt
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on Qt
applications.

%package	plasma
Summary:	Plasma Workspace support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	im-chooser
Requires:	kf5-filesystem
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}
%description	plasma
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains Plasma Workspace support on
imsettings.

%package	mate
Summary:	MATE support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	mate-settings-daemon >= 1.5.0
Requires:	mate-session-manager
Requires:	im-chooser
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}
%description	mate
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on MATE.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
autoreconf -i

%build

%configure	\
	--with-xinputsh=50-xinput.sh \
	--disable-static \
	--disable-schemas-install
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"
chmod 0755 $RPM_BUILD_ROOT%{_libexecdir}/imsettings-target-checker.sh
chmod 0755 $RPM_BUILD_ROOT%{_libexecdir}/xinputinfo.sh
chmod 0755 $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/50-xinput.sh
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/plasma-workspace/env
ln -sf $(realpath --relative-to=$RPM_BUILD_ROOT%{_sysconfdir}/xdg/plasma-workspace/env/ $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/)/50-xinput.sh $RPM_BUILD_ROOT%{_sysconfdir}/xdg/plasma-workspace/env/xinput.sh
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/libimsettings-{cinnamon-gsettings,gconf,mateconf,systemd-gtk,systemd-qt}.so
desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/imsettings-start.desktop
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/none.conf 10
alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/xcompose.conf 20
alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/xim.conf 30
systemctl reload dbus.service 2>&1 || :
%postun

if [ "$1" = 0 ]; then
	alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/none.conf
	alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/xcompose.conf
	alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/xim.conf
	systemctl reload dbus.service 2>&1 || :
fi
%ldconfig_scriptlets	libs
%files -f %{oreon_filedir}/main.list
%files -n imsettings-libs -f %{oreon_filedir}/imsettings-libs.list
%files -n imsettings-devel -f %{oreon_filedir}/imsettings-devel.list
%files -n imsettings-gsettings -f %{oreon_filedir}/imsettings-gsettings.list
%files -n imsettings-qt -f %{oreon_filedir}/imsettings-qt.list
%files -n imsettings-plasma -f %{oreon_filedir}/imsettings-plasma.list
%files -n imsettings-mate -f %{oreon_filedir}/imsettings-mate.list

%changelog

%autochangelog
