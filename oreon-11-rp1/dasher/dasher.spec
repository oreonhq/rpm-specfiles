%global source0_hash none

Summary: A predictive text input system
Name: dasher
Version: 5.0.0
Release: 0.28.beta%{?dist}
License: GPL-2.0-or-later
URL: http://www.inference.phy.cam.ac.uk/dasher/
Source0: https://github.com/ipomoena/dasher/archive/DASHER_5_0_0_beta.tar.gz

# https://github.com/ipomoena/dasher/pull/97
Patch0: dasher-5.0.0-sys-stat.patch

# https://github.com/dasher-project/dasher/pull/169
Patch1: gnome-doc-utils-depr.patch

# https://gitlab.gnome.org/GNOME/dasher/-/merge_requests/3
Patch2: 0001-Remove-extern-C-warpper-around-atspi-glib-headers-in.patch

BuildRequires: at-spi2-core-devel
BuildRequires: desktop-file-utils
BuildRequires: expat-devel
BuildRequires: gcc gcc-c++
BuildRequires: libXtst-devel
BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: yelp-tools

BuildRequires: gnome-common
BuildRequires: automake autoconf libtool
BuildRequires: make

%description
Dasher is an information-efficient text-entry interface, driven by natural
continuous pointing gestures. Dasher is a competitive text-entry system
wherever a full-size keyboard cannot be used, e.g. when operating a computer
one-handed, by joystick, touchscreen, trackball, or mouse, when operating
a computer without hands (i.e. by head-mouse or by eyetracker), or on
palmtops or wearable computers.

%prep
%setup -q -n dasher-DASHER_5_0_0_beta
%autopatch -p1
echo "5.0.0" > .tarball-version
rm  m4/glib-gettext.m4
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-japanese

make %{?_smp_mflags}

%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/dasher.desktop

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%doc AUTHORS README NEWS
%license COPYING
%{_bindir}/dasher
%{_datadir}/applications/dasher.desktop
%{_datadir}/dasher
%{_datadir}/icons/hicolor/*/apps/dasher.*

%{_mandir}/*/dasher.1.gz

%changelog
%autochangelog
