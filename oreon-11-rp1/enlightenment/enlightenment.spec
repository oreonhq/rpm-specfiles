%global source0_hash b41df8771f60e3b96a1973ae566d7425c53a8339f18e54e31230218781da2fa9
%global use_wayland 1
Name:		enlightenment
Version:	0.27.1
Release:        1%{?dist}
License:	LicenseRef-Callaway-BSD
Summary:        Enlightenment window manager
Url:		http://enlightenment.org
Source0:        http://download.enlightenment.org/rel/apps/enlightenment/%{name}-%{version}.tar.xz
Patch0:		enlightenment-0.25.0-fix-desktop-files.patch
Requires:	%{name}-data = %{version}-%{release}
Requires:	efl
Requires:	redhat-menus
Provides:	firstboot(windowmanager) = enlightenment
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  efl-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libXext-devel
BuildRequires:  libdrm-devel
BuildRequires:  libexif-devel
BuildRequires:  libuuid-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pam-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  systemd
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xkeyboard-config-devel
BuildRequires:  xorg-x11-server-Xwayland
# /oreon:deps
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
 -Dwl=true \
 -Dsystemdunitdir=%{_userunitdir}
%{meson_build}
%install
%{meson_install}
find %{buildroot} -name '*.la' -delete
%find_lang %{name}
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post enlightenment.service
%postun

%systemd_postun_with_restart enlightenment.service
%preun

%systemd_preun enlightenment.service
%files -f %{oreon_filedir}/main.list
%files -n enlightenment-data -f %{oreon_filedir}/enlightenment-data.list
%files -n enlightenment-devel -f %{oreon_filedir}/enlightenment-devel.list

%changelog

%autochangelog
