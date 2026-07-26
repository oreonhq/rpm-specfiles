%global source0_hash none

%global use_wayland 1

Name:		enlightenment
Version:	0.27.1
Release:	3%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
Summary:	Enlightenment window manager
Url:		http://enlightenment.org
Source0:	http://download.enlightenment.org/rel/apps/enlightenment/%{name}-%{version}.tar.xz
Patch0:		enlightenment-0.25.0-fix-desktop-files.patch
BuildRequires:	gcc, gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	efl-devel >= 1.28.0
%if %{use_wayland}
BuildRequires:	wayland-protocols-devel
BuildRequires:	wayland-devel
BuildRequires:	xorg-x11-server-Xwayland
%endif
BuildRequires:	libdrm-devel
BuildRequires:	libexif-devel
BuildRequires:	libuuid-devel
BuildRequires:	libXext-devel
BuildRequires:	pam-devel
BuildRequires:	systemd
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	ninja-build, meson
BuildRequires:	xkeyboard-config-devel
Requires:	%{name}-data = %{version}-%{release}
Requires:	efl
Requires:	redhat-menus
Provides:	firstboot(windowmanager) = enlightenment
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
Enlightenment window manager is a lean, fast, modular and very extensible window
manager for X11 and Linux. It is classed as a "desktop shell" providing the
things you need to operate your desktop (or laptop), but is not a whole '
application suite. This covered launching applications, managing their windows
and doing other system tasks like suspending, reboots, managing files etc.

%package data
Summary:	Enlightenment data files
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description data
Contains data files for Enlightenment

%package devel
Summary:	Enlightenment headers, documentation and test programs
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Headers, test programs and documentation for enlightenment.

%prep
%setup -q
%patch -P0 -p1 -b .fixme

%build
%{meson} \
 -Dpam=true \
 -Dmount-eeze=true \
%if %{use_wayland}
 -Dwl=true \
%endif
 -Dsystemdunitdir=%{_userunitdir}
%{meson_build}

%install
%{meson_install}

find %{buildroot} -name '*.la' -delete

%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%post
%systemd_post enlightenment.service

%postun
%systemd_postun_with_restart enlightenment.service

%preun
%systemd_preun enlightenment.service

%files
%doc AUTHORS COPYING README.md TODO.md
%dir %{_sysconfdir}/enlightenment
%config %{_sysconfdir}/enlightenment/system.conf
%{_sysconfdir}/xdg/menus/e-applications.menu
%{_sysconfdir}/enlightenment/sysactions.conf
%{_bindir}/emixer
%{_bindir}/enlightenment
%{_bindir}/enlightenment_askpass
%{_bindir}/enlightenment_filemanager
%{_bindir}/enlightenment_fprint
%{_bindir}/enlightenment_imc
%{_bindir}/enlightenment_open
%{_bindir}/enlightenment_paledit
%{_bindir}/enlightenment_remote
%{_bindir}/enlightenment_start
%{_libdir}/enlightenment
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/pixmaps/enlightenment-askpass.png
%{_userunitdir}/enlightenment.service

%files data -f %{name}.lang
%if %{use_wayland}
%{_datadir}/wayland-sessions/enlightenment-wayland.desktop
%endif
%{_datadir}/xsessions/enlightenment.desktop
%{_datadir}/enlightenment
%{_datadir}/applications/*.desktop

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/enlightenment

%changelog
%autochangelog
